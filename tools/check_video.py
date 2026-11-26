"""영상 링크 확인을 명령 하나로: 받기 → 장면 찾기 → 합격 그림 + 1초 간격 프레임 한 장.

  python3 -I tools/check_video.py CODE [CODE …]
  → <스크래치패드 또는 /tmp>/vcheck/<CODE>/sheet.jpg  (첫 칸 = 합격 그림)

합격 처리:
  python3 -I tools/check_video.py --accept epXX S## CODE "STATUS에 적을 말"
  → clips/web/S##_CODE.mp4 복사, media_manifest 추가, STATUS.md 한 줄, 장면 페이지 다시 만들기
"""
import glob, os, shutil, subprocess, sys
from pathlib import Path

ROOT = Path("/home/user/chiqui-channel")
SP = Path(os.environ.get("VCHECK_DIR", "/tmp/claude-0/-home-user-lkslangel7-cloud-chiqui-channel/d5207752-7fbe-54fd-9ea4-b464b28155b6/scratchpad/vcheck"))


def sheet(code):
    d = SP / code
    shutil.rmtree(d, ignore_errors=True); d.mkdir(parents=True)
    out = subprocess.run([sys.executable, "-I", str(ROOT / "tools/fetch_any.py"), str(d), "--", code], capture_output=True, text=True).stdout
    mp4 = sorted(d.glob("*.mp4"))
    if not mp4:
        print(code, "영상 없음", out.strip()); return
    f = mp4[0]; parts = f.stem.split("_")
    img = None
    if parts[0].startswith("ep") and len(parts) > 2:
        ep, sid = parts[0], parts[1]
        sc = {s["id"]: s for s in __import__("json").load(open(ROOT / f"episodes/{ep}/scenes.json", encoding="utf-8"))}
        com = sc.get(sid, {}).get("common")
        pat = ROOT / (f"episodes/common/images/web/{com}_*.png" if com else f"episodes/{ep}/images/web/{sid}_*.png")
        g = sorted(glob.glob(str(pat))); img = g[0] if g else None
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(f), "-vf", "fps=1,scale=400:-1", str(d / "f%02d.jpg")])
    from PIL import Image
    fs = ([img] if img else []) + sorted(glob.glob(str(d / "f*.jpg")))
    ims = [Image.open(x).convert("RGB").resize((400, 225)) for x in fs]
    c = Image.new("RGB", (400 * 6, 225 * ((len(ims) + 5) // 6)), "white")
    for i, im in enumerate(ims): c.paste(im, ((i % 6) * 400, (i // 6) * 225))
    c.save(d / "sheet.jpg")
    print(code, f.name, "그림:", img or "없음", "→", d / "sheet.jpg")


def accept(ep, sid, code, note):
    src = sorted((SP / code).glob("*.mp4"))[0]
    E = ROOT / "episodes" / ep
    sc = {s["id"]: s for s in __import__("json").load(open(E / "scenes.json", encoding="utf-8"))}
    com = sc.get(sid, {}).get("common")
    dst = (ROOT / f"episodes/common/clips/web/{com}_{code}.mp4") if com else (E / f"clips/web/{sid}_{code}.mp4")
    dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy(src, dst)
    man = ROOT / "tools/media_manifest.txt"
    lines = set(man.read_text().splitlines()) | {str(dst.relative_to(ROOT))}
    man.write_text("\n".join(sorted(lines)) + "\n")
    if note:
        with open(E / "STATUS.md", "a", encoding="utf-8") as fh: fh.write(note.rstrip() + "\n")
    print("저장:", dst)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--accept":
        accept(a[1], a[2], a[3], a[4] if len(a) > 4 else "")
    else:
        for c in a: sheet(c)
