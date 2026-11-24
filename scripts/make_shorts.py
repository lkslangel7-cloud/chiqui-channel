"""완성 영상에서 세로 숏폼(1080x1920)을 잘라 만든다. 크레딧 0.
사용법: python3 -I scripts/make_shorts.py 01 02 ...   (화 번호 = 폴더 번호)
화마다 2개: song(에피소드 노래 시작부터 약 28초) · quiz(내레이션 질문 앞뒤, 아이가 맞히는 부분).
레이아웃: 흐린 배경 + 가운데 16:9 영상(자막 없는 판) + 위 제목 + 영상 아래 큰 자막 + 맨 아래 채널 이름.
"""
import json, re, subprocess, sys
from pathlib import Path

R = Path(__file__).resolve().parent.parent
FONT = R / "remotion/public/fonts/Jua.ttf"
OUT = R / "output/shorts"; OUT.mkdir(parents=True, exist_ok=True)
QUIZ_PICK = {"04": "누가 클까?", "05": "치키는 어떻게 볼 수 있을까?", "07": "몇 개 남았을까?"}  # 나머지는 '어디 있을까?' 질문


def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                                capture_output=True, text=True).stdout.strip())


def srt_cut(src, start, end, dst):
    """SRT에서 [start,end] 구간만 0초 기준으로 옮긴다."""
    def t(s):
        h, m, x = s.replace(",", ".").split(":"); return int(h) * 3600 + int(m) * 60 + float(x)
    def f(x):
        x = max(0, x); return f"{int(x // 3600):02d}:{int(x % 3600 // 60):02d}:{x % 60:06.3f}".replace(".", ",")
    out, n = [], 0
    for b in re.split(r"\n\s*\n", Path(src).read_text(encoding="utf-8").strip()):
        ls = b.strip().splitlines()
        if len(ls) < 3: continue
        a, c = [t(x.strip()) for x in ls[1].split("-->")]
        if c <= start or a >= end: continue
        n += 1; out.append(f"{n}\n{f(a - start)} --> {f(min(c, end) - start)}\n" + "\n".join(ls[2:]))
    Path(dst).write_text("\n\n".join(out) + "\n", encoding="utf-8")


def make(ep, kind, start, length, title):
    v = json.loads((R / "episodes/videos.json").read_text(encoding="utf-8"))
    base = next(x["file"] for x in v if x["ep"] == ep)
    src = R / f"output/{base}_nosubs.mp4"
    if not src.exists(): src = R / f"output/{base.rsplit('_v', 1)[0]}_nosubs.mp4"
    srt = R / f"output/{base}.srt"
    if not srt.exists(): srt = R / f"episodes/ep{ep}/subtitles_ko.srt"
    tmp = OUT / f"_{ep}_{kind}.srt"; srt_cut(srt, start, start + length, tmp)
    ttl = OUT / f"_{ep}_{kind}.txt"; ttl.write_text(title, encoding="utf-8")
    dst = OUT / f"ep{ep}_{kind}.mp4"
    fd = str(FONT.parent)
    vf = (f"[0:v]split[a][b];[a]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=30:3,eq=brightness=-0.05[bg];"
          f"[b]scale=1080:-2[fg];[bg][fg]overlay=0:560[c];"
          f"[c]drawtext=fontfile='{FONT}':textfile='{ttl}':fontsize=84:fontcolor=white:borderw=8:bordercolor=0xE8772E:x=(w-tw)/2:y=300,"
          f"drawtext=fontfile='{FONT}':text='치키 타운':fontsize=56:fontcolor=white:borderw=6:bordercolor=0x4A7A2A:x=(w-tw)/2:y=1640,"
          f"subtitles='{tmp}':fontsdir='{fd}':original_size=1080x1920:force_style='FontName=Jua,FontSize=11,PrimaryColour=&H00FFFFFF,OutlineColour=&H00202020,BorderStyle=1,Outline=3,Shadow=0,Alignment=2,MarginV=88'[out]")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{start:.2f}", "-t", f"{length:.2f}", "-i", str(src),
                    "-filter_complex", vf, "-map", "[out]", "-map", "0:a", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                    "-c:a", "aac", "-b:a", "160k", "-af", f"afade=t=out:st={length - 0.8:.2f}:d=0.8", "-movflags", "+faststart", str(dst)], check=True)
    tmp.unlink(); ttl.unlink()
    return dst


def plan(ep):
    d = json.loads((R / f"episodes/ep{ep}/edit_order.json").read_text(encoding="utf-8"))
    song = next(m for m in d["music"] if "songs/" in m["file"] and not any(k in m["file"] for k in ("opening", "ending", "bgm")))
    lines = d["lines"]
    want = QUIZ_PICK.get(ep)
    qi = next(i for i, l in enumerate(lines) if (l["text"] == want if want else ("어디 있을까?" in l["text"])))
    q, ans = lines[qi], lines[qi + 1]
    a_end = ans["at"] + dur(R / f"episodes/ep{ep}" / ans["audio"]) + 2.0
    qs = max(0, q["at"] - 6.0)
    short = json.loads((R / "episodes/videos.json").read_text(encoding="utf-8"))
    name = next(x["short"] for x in short if x["ep"] == ep)
    return [("song", song["at"] + 0.3, min(28.0, song["dur"] - 0.5), name), ("quiz", qs, min(30.0, a_end - qs), q["text"])]


if __name__ == "__main__":
    for ep in sys.argv[1:]:
        for kind, s, L, title in plan(ep):
            print(make(ep, kind, s, L, title), f"{s:.1f}s +{L:.1f}s", title)
