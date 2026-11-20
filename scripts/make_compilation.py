"""여러 화를 이어 붙여 모음집을 만든다 (재인코딩 1회, 크레딧 0).

사용법: python3 -I scripts/make_compilation.py <spec.json> <out.mp4>
spec.json: {"segments": [{"file": "output/ep01_ko_v5.mp4", "srt": "output/ep01_ko_nosubs.srt",
                          "from": 0, "to": 160.4, "label": "1화 · 공룡알 하나 둘 셋"}, ...]}
- 각 구간 시작 4초 동안 왼쪽 위에 화 이름 배지를 띄운다 (label이 비어 있으면 생략).
- 구간 경계마다 소리를 0.3초 페이드해 툭 끊기지 않게 한다.
- srt가 있으면 시간을 옮겨 하나의 SRT로 합친다 (out과 같은 이름 .srt).
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "remotion/public/fonts/Jua.ttf"


def esc(t: str) -> str:
    return t.replace("\\", "\\\\").replace(":", "\\:").replace("'", "’").replace(",", "\\,").replace("%", "\\%")


def ts(sec: float) -> str:
    ms = int(round(sec * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def parse_srt(path: Path):
    out = []
    for block in re.split(r"\n\s*\n", path.read_text(encoding="utf-8").strip()):
        lines = block.strip().splitlines()
        if len(lines) < 3:
            continue
        m = re.match(r"(\d+):(\d+):(\d+),(\d+) --> (\d+):(\d+):(\d+),(\d+)", lines[1])
        if not m:
            continue
        g = [int(x) for x in m.groups()]
        a = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000
        b = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000
        out.append((a, b, "\n".join(lines[2:])))
    return out


def main(spec_path: str, out: str) -> None:
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    segs = spec["segments"]
    args, fc, cues, t0 = [], [], [], 0.0
    for i, s in enumerate(segs):
        dur = round(s["to"] - s["from"], 3)
        args += ["-ss", str(s["from"]), "-t", str(dur), "-i", str(ROOT / s["file"])]
        badge = ""
        if s.get("label"):
            badge = (f",drawbox=x=40:y=36:w={60 + 46 * len(s['label'])}:h=96:color=0xfff3c4@0.92:t=fill:enable='lt(t,4)'"
                     f",drawtext=fontfile={FONT}:text='{esc(s['label'])}':fontsize=56:fontcolor=0x5a3d1e:x=70:y=56:enable='lt(t,4)'")
        fc.append(f"[{i}:v]setpts=PTS-STARTPTS,fps=30,format=yuv420p{badge}[v{i}]")
        fc.append(f"[{i}:a]asetpts=PTS-STARTPTS,afade=t=in:d=0.3,afade=t=out:st={dur - 0.3}:d=0.3[a{i}]")
        if s.get("srt"):
            for a, b, text in parse_srt(ROOT / s["srt"]):
                if b <= s["from"] or a >= s["to"]:
                    continue
                cues.append((max(a, s["from"]) - s["from"] + t0, min(b, s["to"]) - s["from"] + t0, text))
        t0 += dur
    fc.append("".join(f"[v{i}][a{i}]" for i in range(len(segs))) + f"concat=n={len(segs)}:v=1:a=1[vout][aout]")
    cmd = ["ffmpeg", "-v", "error", "-y", *args, "-filter_complex", ";".join(fc), "-map", "[vout]", "-map", "[aout]",
           "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-c:a", "aac", "-b:a", "192k", "-ar", "44100",
           "-movflags", "+faststart", out]
    subprocess.run(cmd, check=True)
    if cues:
        srt = "\n".join(f"{n}\n{ts(a)} --> {ts(b)}\n{t}\n" for n, (a, b, t) in enumerate(cues, 1))
        Path(out).with_suffix(".srt").write_text(srt, encoding="utf-8")
    print("done", out, f"{t0:.1f}s")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
