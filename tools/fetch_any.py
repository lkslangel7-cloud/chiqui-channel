import json, re, subprocess, sys, html, glob
from pathlib import Path
out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
SC = []
for f in sorted(glob.glob("/home/user/chiqui-channel/episodes/ep*/scenes.json")):
    ep = f.split("/")[-2]
    for s in json.load(open(f, encoding="utf-8")):
        SC.append((ep, s["id"], s.get("vid", ""), s.get("img", "")))
for code in sys.argv[2:]:
    page = subprocess.run(["curl", "-sSL", "-m", "40", f"https://higgsfield.ai/s/{code}"], capture_output=True, text=True).stdout
    t = html.unescape(page)
    m = re.search(r'line-clamp-2">([^<]+)<', t)
    prompt = m.group(1).strip() if m else ""
    vid = re.findall(r'https://d8j0ntlcm91z4\.cloudfront\.net/[^"\\]+\.mp4', page)
    og = re.search(r'og:image" content="([^"]+)"', page)
    media = vid[0] if vid else (html.unescape(og.group(1)) if og else None)
    hits = [f"{e}_{i}" for e, i, v, im in SC if prompt and (prompt[:150] == v[:150] or prompt[:150] == im[:150])]
    name = (hits[0] if len(hits) == 1 else ("multi" if hits else "unknown")) + "_" + code + (".mp4" if vid else ".png")
    if media: subprocess.run(["curl", "-sSf", "-m", "120", "-o", str(out / name), media])
    print(code, ",".join(hits) or "-", prompt[:70])
