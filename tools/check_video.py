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
    f = mp4[0]
    if f.name.startswith("multi_") and EP:
        # 여러 화에 같은 프롬프트 → --ep 로 받은 화의 장면으로 정한다
        hits = [h for tok in out.split() for h in tok.split(",") if h.startswith(EP + "_S")]
        if len(hits) == 1:
            nf = d / f"{hits[0]}_{code}.mp4"; f.rename(nf); f = nf
    parts = f.stem.split("_")
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
    # 장면 페이지 다시 만들기 (제목은 기존 페이지 <title>에서)
    import re, json
    t = re.search(r"<title>([^<]+)</title>", (E / "scene_prompts_page.html").read_text(encoding="utf-8"))
    title = t.group(1).replace(" 장면", "").strip() if t else ep
    subprocess.run([sys.executable, "-I", str(ROOT / "prompts/build_scene_page.py"), str(E), title])
    # 진행 현황 줄: 영상 수 세어 고치기
    n_ep = len(sc)
    done = [s for s in sc.values() if (glob.glob(str(ROOT / f"episodes/common/clips/web/{s['common']}_*.mp4")) if s.get("common") else glob.glob(str(E / f"clips/web/{s['id']}_*.mp4")))]
    left = [s["id"] for s in sc.values() if s not in done]
    page = Path(os.environ.get("VIDEOPAGE", "/tmp/claude-0/-home-user/d5207752-7fbe-54fd-9ea4-b464b28155b6/scratchpad/videopage/index.html"))
    if page.exists():
        s = page.read_text(encoding="utf-8"); no = int(ep[2:])
        m = re.search(r'<li class="pr s\d"><div class="pr-h"><span class="pn">%d화</span>.*?</li>' % no, s)
        if m:
            li = m.group(0); k = len(done); pct = round(100 * k / n_ep)
            new = re.sub(r'(<span class="lb">영상</span><span class="bar" role="img" aria-label=")\d+/\d+("><i style="width:)\d+(%"></i></span><span class="num">)\d+/\d+',
                         lambda mm: f"{mm.group(1)}{k}/{n_ep}{mm.group(2)}{pct}{mm.group(3)}{k}/{n_ep}", li)
            nx = ("다음: 영상 다시 " + " ".join(left)) if left else "다음: 노래 받기"
            new = re.sub(r'<p class="nx">[^<]*</p>', f'<p class="nx">{nx}</p>', new)
            if not left: new = new.replace('class="pr s2"', 'class="pr s3"')
            page.write_text(s.replace(li, new), encoding="utf-8")
            print(f"진행 현황: {ep} 영상 {k}/{n_ep}, 남음 {' '.join(left) or '없음'} → {page}")


if __name__ == "__main__":
    a = sys.argv[1:]
    EP = None
    if a and a[0] == "--ep":
        EP, a = a[1], a[2:]
    if a and a[0] == "--accept":
        accept(a[1], a[2], a[3], a[4] if len(a) > 4 else "")
    else:
        for c in a: sheet(c)
