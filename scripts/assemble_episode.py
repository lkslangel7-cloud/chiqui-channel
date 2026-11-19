"""edit_order.json으로 에피소드 영상을 자동 편집한다 (영상 + 대사 + 배경음악 + 자막).

사용법: python3 scripts/assemble_episode.py episodes/ep01 output/ep01_ko.mp4 [--no-subs]
- --no-subs: 화면에 자막을 넣지 않는다 (유튜브 자막 파일 ep01_ko.srt를 따로 만든다).
- 영상 클립은 소리를 빼고 1920x1080, 30fps로 맞춘다.
- 자막은 Jua 글꼴로 화면 아래에 띄운다.
- 함께 캡컷용 순서표 edit_order.md를 만든다.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "remotion/public/fonts/Jua.ttf"
W, H, FPS = 1920, 1080, 30


def dur(p: Path) -> float:
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def esc(t: str) -> str:
    return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’").replace(",", "\\,").replace("%", "\\%")


def mmss(t: float) -> str:
    return f"{int(t // 60)}:{t % 60:04.1f}"


def main(ep_dir: str, out: str, no_subs: bool = False) -> None:
    ep = Path(ep_dir)
    spec = json.loads((ep / "edit_order.json").read_text(encoding="utf-8"))
    args, fc = [], []
    missing = []
    for i, v in enumerate(spec["video"]):
        src = ep / v["file"]
        if not src.exists() and v.get("fallback") and (ep / v["fallback"]).exists():
            # 영상이 아직 없으면 같은 장면 그림을 천천히 확대해 미리보기로 쓴다
            missing.append(v["file"])
            args += ["-loop", "1", "-framerate", str(FPS), "-t", str(v["dur"]), "-i", str(ep / v["fallback"])]
            z = f"(1+0.06*t/{v['dur']})"
            fc.append(f"[{i}:v]scale=w='trunc({W}*{z}/2)*2':h='trunc({H}*{z}/2)*2':eval=frame,crop={W}:{H},fps={FPS},setsar=1,format=yuv420p[v{i}]")
            continue
        sp = v.get("speed", 1)  # 0.5면 반 속도로 늘려 쓴다 (짧게 나온 클립)
        args += ["-ss", str(v["from"]), "-t", str(round(v["dur"] * sp, 3)), "-i", str(src)]
        slow = f"setpts=PTS/{sp}," if sp != 1 else ""
        if v.get("pingpong"):  # 앞으로 갔다가 거꾸로 돌아와 길이를 두 배로 (끝이 처음 장면으로 돌아옴)
            half = round(v["dur"] / 2 * sp, 3)  # speed와 같이 쓰면 앞부분만 느리게
            args[-3] = str(half)  # 입력 길이를 절반만
            fc.append(f"[{i}:v]{slow}scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1,format=yuv420p,split[pa{i}][pb{i}];[pb{i}]reverse[pr{i}];[pa{i}][pr{i}]concat=n=2:v=1:a=0[v{i}]")
            continue
        fc.append(f"[{i}:v]{slow}scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1,format=yuv420p[v{i}]")
    if missing:
        print("그림으로 대신한 장면:", len(missing), "개")
    n = len(spec["video"])
    fc.append("".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[vcat]")

    # 자막: 대사가 나오는 동안 + 0.6초
    subs = []
    for ln in spec["lines"]:
        end = ln["at"] + dur(ep / ln["audio"]) + 0.6
        subs.append(
            f"drawtext=fontfile={FONT}:text='{esc(ln['text'])}':fontsize=64:fontcolor=white:borderw=6:bordercolor=0x5a3d1e"
            f":x=(w-text_w)/2:y=h-150:enable='between(t,{ln['at']:.2f},{end:.2f})'"
        )
    for c in spec.get("captions", []):  # 노래 가사 자막 (소리 파일 없이 시간만)
        subs.append(
            f"drawtext=fontfile={FONT}:text='{esc(c['text'])}':fontsize=60:fontcolor=0xfff3c4:borderw=6:bordercolor=0x5a3d1e"
            f":x=(w-text_w)/2:y=h-150:enable='between(t,{c['at']:.2f},{c['end']:.2f})'"
        )
    if no_subs:
        fc.append("[vcat]null[vout]")
    else:
        fc.append("[vcat]" + ",".join(subs) + "[vout]")

    # 유튜브용 자막 파일 (대사 + 노래 가사)
    def ts(t):
        ms = int(round(t * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); sec, ms = divmod(ms, 1000)
        return f"{h:02}:{m:02}:{sec:02},{ms:03}"
    cues = [(ln["at"], ln["at"] + dur(ep / ln["audio"]) + 0.6, ln["text"]) for ln in spec["lines"]]
    cues += [(c["at"], c["end"], c["text"]) for c in spec.get("captions", [])]
    cues.sort()
    srt = [f"{i}\n{ts(a)} --> {ts(min(b, cues[i][0] - 0.05) if i < len(cues) else b)}\n{t}\n" for i, (a, b, t) in enumerate(cues, 1)]
    (Path(out).with_suffix(".srt")).write_text("\n".join(srt), encoding="utf-8")

    # 소리: 배경음악 + 대사
    # 바닥 무음 트랙 (전체 길이 고정용)
    fc.append(f"anullsrc=r=44100:cl=stereo,atrim=0:{spec['length']}[base]")
    mix = ["[base]"]
    musics = spec["music"] if isinstance(spec["music"], list) else [
        dict(spec["music"], at=0, **{"from": 0}, dur=spec["length"], fade_in=0, fade_out=3)]
    k = n
    for m_i, m in enumerate(musics):
        args += ["-i", str(ep / m["file"])]
        d, fi, fo = m["dur"], m.get("fade_in", 0), m.get("fade_out", 0)
        ms = int(m["at"] * 1000)
        chain = f"[{k}:a]atrim={m.get('from', 0)}:{m.get('from', 0) + d},asetpts=PTS-STARTPTS,aresample=44100,aformat=channel_layouts=stereo,volume={m['volume']}"
        if fi: chain += f",afade=t=in:st=0:d={fi}"
        if fo: chain += f",afade=t=out:st={max(0, d - fo)}:d={fo}"
        fc.append(chain + f",adelay={ms}|{ms}[m{m_i}]")
        mix.append(f"[m{m_i}]")
        k += 1
    for j, ln in enumerate(spec["lines"]):
        args += ["-i", str(ep / ln["audio"])]
        ms = int(ln["at"] * 1000)
        fc.append(f"[{k}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={ms}|{ms}[l{j}]")
        mix.append(f"[l{j}]")
        k += 1
    fc.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0:duration=first,alimiter=limit=0.95[aout]")

    cmd = ["ffmpeg", "-loglevel", "error", "-y", *args, "-filter_complex", ";".join(fc),
           "-map", "[vout]", "-map", "[aout]", "-c:v", "libx264", "-preset", "medium", "-crf", "20",
           "-c:a", "aac", "-b:a", "192k", "-t", str(spec["length"]), out]
    subprocess.run(cmd, check=True)

    # 캡컷용 순서표
    md = [f"# {spec['title']} — 캡컷 순서표", "", "자동 편집본과 같은 순서. 캡컷에서 손볼 때 이 표대로 올린다.", "",
          "## 영상 트랙", "", "| 시작 | 파일 | 길이 | 내용 |", "| --- | --- | --- | --- |"]
    md += [f"| {mmss(v['start'])} | `{v['file']}` ({v['from']}초부터) | {v['dur']}초 | {v['note']} |" for v in spec["video"]]
    md += ["", "## 대사 트랙", "", "| 시작 | 파일 | 누가 | 대사 |", "| --- | --- | --- | --- |"]
    md += [f"| {mmss(l['at'])} | `{l['audio']}` | {l['who']} | {l['text']} |" for l in spec["lines"]]
    md += ["", "## 음악", ""]
    md += [f"- {mmss(m['at'])} `{m['file']}` ({m.get('from', 0)}초부터 {m['dur']}초, 볼륨 {m['volume']}) — {m.get('note', '')}" for m in musics]
    md += ["", "## 효과음 (캡컷 무료 효과음에서 검색)", ""]
    md += [f"- {mmss(s['at'])} {s['what']}" for s in spec.get("sfx_suggestions", [])]
    (ep / "edit_order.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("done", out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], "--no-subs" in sys.argv[3:])
