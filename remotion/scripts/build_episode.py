"""에피소드 스펙(JSON)과 실제 음성 길이로 장면 타이밍을 계산해 src/episodes/<id>.ts를 만든다.

사용법: python3 scripts/build_episode.py episodes-src/ep01_ko_3min.json src/episodes/ep01_ko_3min.ts
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"

LEAD, GAP, TAIL = 0.5, 0.6, 0.9  # 장면 시작 여백, 대사 사이, 장면 끝 여백(초)
MIN_STILL = 4.0
CLIP_LEN = 5.04
CLIP_MIN = CLIP_LEN * 0.75  # 1.33배속보다 빠르게는 돌리지 않는다
MAX_EXTRA_PER_STILL = 2.0


def duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    )
    return float(out.stdout.strip())


def main(spec_path: str, out_path: str) -> None:
    spec = json.loads(Path(spec_path).read_text(encoding="utf-8"))
    scenes = []
    for sc in spec["scenes"]:
        t = LEAD
        lines = []
        for i, (aid, speaker, text) in enumerate(sc["lines"]):
            if i:
                t += GAP
            audio = f"audio/{aid}.wav"
            lines.append({"at": round(t, 2), "audio": audio, "speaker": speaker, "text": text})
            t += duration(PUBLIC / audio)
        d = t + sc.get("tail", TAIL)
        if sc["kind"] == "image":
            d = max(d, sc.get("min", MIN_STILL))
        else:
            # CLIP_MAX보다 길면 Episode.tsx가 0.75배속으로 재생한 뒤 마지막 프레임을 잡아 둔다.
            d = max(d, CLIP_MIN)
        scenes.append({"kind": sc["kind"], "src": sc["src"], "duration": d, "lines": lines, "tail": "tail" in sc})

    # 목표 길이에 모자라면 그림 장면(엔딩 제외)에 여백을 고르게 나눠 준다.
    total = sum(s["duration"] for s in scenes)
    stills = [s for s in scenes if s["kind"] == "image" and not s["tail"]]
    extra = max(0.0, spec["target"] - total)
    if stills and extra:
        per = min(extra / len(stills), MAX_EXTRA_PER_STILL)
        for s in stills:
            s["duration"] += per
    total = sum(s["duration"] for s in scenes)

    def fmt_line(l):
        return (f'{{ at: {l["at"]}, audio: "{l["audio"]}", speaker: "{l["speaker"]}", '
                f'text: {json.dumps(l["text"], ensure_ascii=False)} }}')

    body = []
    for s in scenes:
        lines = ",\n        ".join(fmt_line(l) for l in s["lines"])
        body.append(
            f'    {{\n      kind: "{s["kind"]}",\n      src: "{s["src"]}",\n'
            f'      duration: {s["duration"]:.2f},\n      lines: [\n        {lines}\n      ],\n    }},'
        )
    ts = (
        'import type { Episode } from "../types";\n\n'
        f"// scripts/build_episode.py가 {Path(spec_path).name}에서 생성한 파일. 직접 고치지 말고 스펙을 고친 뒤 다시 생성한다.\n"
        f"// 전체 길이 {total:.1f}초\n"
        f'export const {spec["id"]}: Episode = {{\n'
        f'  title: {json.dumps(spec["title"], ensure_ascii=False)},\n'
        + (f'  series: {json.dumps(spec["series"], ensure_ascii=False)},\n' if "series" in spec else "")
        + '  bgm: "audio/bgm_3min.wav",\n'
        "  scenes: [\n" + "\n".join(body) + "\n  ],\n};\n"
    )
    Path(out_path).write_text(ts, encoding="utf-8")
    print(f"{len(scenes)}개 장면, 전체 {total:.1f}초")


if __name__ == "__main__":
    main(*sys.argv[1:3])
