"""edit_order.json으로 에피소드 영상을 자동 편집한다 (영상 + 대사 + 배경음악 + 자막).

사용법: python3 scripts/assemble_episode.py episodes/ep01 output/ep01_ko.mp4
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


def main(ep_dir: str, out: str) -> None:
    ep = Path(ep_dir)
    spec = json.loads((ep / "edit_order.json").read_text(encoding="utf-8"))
    args, fc = [], []
    for i, v in enumerate(spec["video"]):
        args += ["-ss", str(v["from"]), "-t", str(v["dur"]), "-i", str(ep / v["file"])]
        fc.append(f"[{i}:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1,format=yuv420p[v{i}]")
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
    fc.append("[vcat]" + ",".join(subs) + "[vout]")

    # 소리: 배경음악 + 대사
    ai = n
    mus = spec["music"]
    args += ["-i", str(ep / mus["file"])]
    fc.append(f"[{ai}:a]atrim=0:{spec['length']},volume={mus['volume']},afade=t=out:st={spec['length'] - 3}:d=3[bgm]")
    mix = ["[bgm]"]
    for j, ln in enumerate(spec["lines"]):
        args += ["-i", str(ep / ln["audio"])]
        ms = int(ln["at"] * 1000)
        fc.append(f"[{ai + 1 + j}:a]aresample=44100,aformat=channel_layouts=stereo,adelay={ms}|{ms}[l{j}]")
        mix.append(f"[l{j}]")
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
    md += ["", "## 음악", "", f"- `{mus['file']}` 볼륨 {mus['volume']} — {mus['note']}", "", "## 효과음 (캡컷 무료 효과음에서 검색)", ""]
    md += [f"- {mmss(s['at'])} {s['what']}" for s in spec.get("sfx_suggestions", [])]
    (ep / "edit_order.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("done", out)


if __name__ == "__main__":
    main(*sys.argv[1:3])
