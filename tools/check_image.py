"""그림 링크 확인을 명령 하나로 (허락을 묻지 않게, 셸 변수·for·;·&& 없이 한 줄로 쓴다).

  python3 -I tools/check_image.py --ep ep43 CODE [CODE …]
  → /tmp/chiqui_check/<CODE>/S##_CODE.png (원본), view.jpg (1400px, 이것을 Read로 본다)
    /tmp/chiqui_check/<ep>_all.jpg  (그 화 합격 그림 + 이번 그림을 한 장에, 반복 소품·배치 대조용)
  --ep 없으면 26~45화 전체에서 프롬프트가 가장 비슷한 장면을 찾는다.

소품 크게 잘라 나란히 보기 (좌표는 view.jpg 기준, 1400×792):
  python3 -I tools/check_image.py --crop ep43:S05 1100 490 1300 640 CODE 1090 520 1290 670
  → /tmp/chiqui_check/crop.jpg   (ep43:S05 = 합격 그림, CODE = 이번에 받은 그림)

합격 처리:
  python3 -I tools/check_image.py --accept ep43 S17 CODE "STATUS에 적을 한 줄"
  → images/web/S##_CODE.png 복사(공통 컷이면 episodes/common), media_manifest 추가, STATUS.md 한 줄, 장면 페이지 다시 만들기
"""
import difflib, glob, html, json, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SP = Path("/tmp/chiqui_check")


def scenes(ep):
    return json.loads((ROOT / f"episodes/{ep}/scenes.json").read_text(encoding="utf-8"))


def prompt_and_url(code):
    page = subprocess.run(["curl", "-sSL", "-m", "40", f"https://higgsfield.ai/s/{code}"], capture_output=True, text=True).stdout
    t = html.unescape(page)
    m = re.search(r'line-clamp-2">([^<]+)<', t)
    og = re.search(r'og:image" content="([^"]+)"', page)
    return (m.group(1).strip() if m else ""), (html.unescape(og.group(1)) if og else None)


def view(src, dst, size=(1400, 800)):
    from PIL import Image
    im = Image.open(src).convert("RGB"); im.thumbnail(size); im.save(dst, quality=88)


def accepted(ep):
    """그 화의 합격 그림 {장면: 파일} (공통 컷 포함)"""
    out = {}
    for s in scenes(ep):
        pat = (ROOT / f"episodes/common/images/web/{s['common']}_*.png") if s.get("common") else (ROOT / f"episodes/{ep}/images/web/{s['id']}_*.png")
        g = sorted(glob.glob(str(pat)))
        if g: out[s["id"]] = g[-1]
    return out


def check(ep, codes):
    eps = [ep] if ep else [f"ep{n}" for n in range(26, 46) if (ROOT / f"episodes/ep{n}/scenes.json").exists()]
    pool = [(e, s) for e in eps for s in scenes(e)]
    new = {}
    for code in codes:
        d = SP / code
        shutil.rmtree(d, ignore_errors=True); d.mkdir(parents=True)
        p, url = prompt_and_url(code)
        if not url:
            print(code, "그림 없음"); continue
        r = sorted(((difflib.SequenceMatcher(None, p, s["img"]).ratio(), e, s["id"], s["name"]) for e, s in pool), reverse=True)
        sc, e, sid, name = r[0]
        f = d / f"{sid}_{code}.png"
        subprocess.run(["curl", "-sSf", "-m", "180", "-o", str(f), url])
        view(f, d / "view.jpg")
        (d / "match.txt").write_text(f"{e} {sid}\n", encoding="utf-8")
        new.setdefault(e, {})[sid] = str(f)
        nxt = f"{r[1][1]} {r[1][2]} {r[1][0]:.3f}" if len(r) > 1 else "-"
        print(f"{code} → {e} {sid} {name} ({sc:.3f}; 다음 {nxt})  {d / 'view.jpg'}")
    # 화마다 합격 그림 + 이번 그림 한 장
    from PIL import Image, ImageDraw
    for e, got in new.items():
        acc = accepted(e)
        items = [(sid, acc[sid], False) for sid in sorted(acc)] + [(sid, f, True) for sid, f in sorted(got.items())]
        W, H = 467, 264
        c = Image.new("RGB", (W * 3, H * ((len(items) + 2) // 3)), "white")
        for i, (sid, f, isnew) in enumerate(items):
            im = Image.open(f).convert("RGB").resize((W - 4, H - 4))
            dr = ImageDraw.Draw(im); dr.rectangle([0, 0, 120, 22], fill="red" if isnew else "black")
            dr.text((4, 4), sid + (" NEW" if isnew else " ok"), fill="white")
            c.paste(im, ((i % 3) * W + 2, (i // 3) * H + 2))
        out = SP / f"{e}_all.jpg"; c.save(out, quality=85)
        print("한 장:", out)


def crop(args):
    from PIL import Image, ImageDraw
    parts = []
    while args:
        key, box, args = args[0], [int(v) for v in args[1:5]], args[5:]
        if ":" in key:
            e, sid = key.split(":"); src = accepted(e)[sid]
        else:
            src = sorted((SP / key).glob("*.png"))[0]
        im = Image.open(src).convert("RGB")
        s = im.width / 1400
        im = im.crop(tuple(int(v * s) for v in box)); im.thumbnail((440, 330))
        ImageDraw.Draw(im).text((5, 5), key, fill="red")
        parts.append(im)
    c = Image.new("RGB", (450 * len(parts), 340), "white")
    for i, im in enumerate(parts): c.paste(im, (i * 450 + 5, 5))
    out = SP / "crop.jpg"; c.save(out, quality=90)
    print("잘라 보기:", out)


def accept(ep, sid, code, note):
    src = sorted((SP / code).glob("*.png"))[0]
    E = ROOT / "episodes" / ep
    sc = {s["id"]: s for s in scenes(ep)}
    com = sc.get(sid, {}).get("common")
    dst = (ROOT / f"episodes/common/images/web/{com}_{code}.png") if com else (E / f"images/web/{sid}_{code}.png")
    dst.parent.mkdir(parents=True, exist_ok=True); shutil.copy(src, dst)
    man = ROOT / "tools/media_manifest.txt"
    lines = set(man.read_text(encoding="utf-8").splitlines()) | {str(dst.relative_to(ROOT))}
    man.write_text("\n".join(sorted(l for l in lines if l)) + "\n", encoding="utf-8")
    if note:
        with open(E / "STATUS.md", "a", encoding="utf-8") as fh: fh.write(note.rstrip() + "\n")
    print("저장:", dst)
    t = re.search(r"<title>([^<]+)</title>", (E / "scene_prompts_page.html").read_text(encoding="utf-8"))
    title = t.group(1).replace(" 장면", "").strip() if t else ep
    subprocess.run([sys.executable, "-I", str(ROOT / "prompts/build_scene_page.py"), str(E), title])
    left = [s for s in sc if s not in accepted(ep)]
    print(f"{ep} 그림 {len(sc) - len(left)}/{len(sc)}, 남음 {' '.join(left) or '없음'}")


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--accept":
        accept(a[1], a[2], a[3], a[4] if len(a) > 4 else "")
    elif a and a[0] == "--crop":
        crop(a[1:])
    else:
        ep = None
        if a and a[0] == "--ep":
            ep, a = a[1], a[2:]
        check(ep, a)
