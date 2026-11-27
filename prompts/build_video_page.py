"""완성 영상 보기 페이지(화마다 탭)를 만든다.
사용법: python3 prompts/build_video_page.py <출력 폴더>
- episodes/videos.json 에 "file"이 있는 화만 영상이 들어가고, 없는 화는 '만드는 중' 탭.
- 미리보기 영상(640px, 약 10MB)과 썸네일을 출력 폴더의 v/, t/ 에 만든다(이미 있으면 건너뜀).
- 아티팩트 한 번 올릴 때 64MB 제한 → v/ 파일은 5개씩 나눠 올린다.
"""
import html, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
out = Path(sys.argv[1]); (out / "v").mkdir(parents=True, exist_ok=True); (out / "t").mkdir(exist_ok=True); (out / "th").mkdir(exist_ok=True); out_dir = out
eps = json.loads((ROOT / "episodes/videos.json").read_text(encoding="utf-8"))

def dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    s = round(float(r.stdout.strip() or 0)); return f"{s // 60}:{s % 60:02d}"

def status(ep):
    st = ROOT / f"episodes/ep{ep}/STATUS.md"
    if not st.exists(): return []
    rows = [l.strip("| \n").split(" | ") for l in st.read_text(encoding="utf-8").splitlines() if l.startswith("| ") and "---" not in l and "항목" not in l]
    return [(a, b.replace("**", "")) for a, b in (r[:2] for r in rows if len(r) >= 2)]

e = html.escape

def upload(ep):
    """upload_info.md에서 제목·설명·태그(복사 칸)와 설정(글)을 꺼낸다."""
    f = ROOT / f"episodes/ep{ep}/upload_info.md"
    if not f.exists(): return ""
    import re
    secs = re.split(r"^## ", f.read_text(encoding="utf-8"), flags=re.M)[1:]
    out = []
    for sec in secs:
        name, _, rest = sec.partition("\n")
        name = name.strip()
        m = re.search(r"```\n(.*?)\n```", rest, re.S)
        if m and name in ("제목", "설명", "태그"):
            bid = f"u{ep}-{len(out)}"
            out.append(f'<div class="copybox"><div class="cb-head"><span>{e(name)}</span>'
                       f'<button type="button" class="copy" data-target="{bid}">복사</button></div><pre id="{bid}">{e(m.group(1))}</pre></div>')
        elif name == "설정":
            txt = re.sub(r"`([^`]*)`", r"\1", rest.strip())
            out.append(f'<div class="setting"><span>설정</span><p>{e(txt).replace(chr(10), "<br>")}</p></div>')
    th = out_dir / f"th/ep{ep}.jpg"
    if (ROOT / f"episodes/ep{ep}/thumbnail.png").exists():
        if not th.exists():
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(ROOT / f"episodes/ep{ep}/thumbnail.png"), "-q:v", "2", str(th)], check=True)
        out.insert(0, f'<figure class="thumb"><figcaption><span>썸네일 (1280×720)</span><span>원본 <code>episodes/ep{ep}/thumbnail.png</code></span></figcaption>'
                      f'<img src="th/ep{ep}.jpg" alt="{int(ep)}화 썸네일" loading="lazy" width="1280" height="720">'
                      f'<p class="hint">사진을 길게 누르거나 오른쪽 클릭해서 저장할 수 있어요. 영어·스페인어 채널용은 같은 폴더의 thumbnail_en.png, thumbnail_es.png예요.</p></figure>')
    return f'<section class="yt"><h3>유튜브 올릴 정보</h3>{"".join(out)}</section>' if out else ""


# ---------- 진행 현황 탭 (파일 수를 세어 자동으로 만든다) ----------
import re as _re
PAGES = json.loads((ROOT / "episodes/pages.json").read_text(encoding="utf-8")) if (ROOT / "episodes/pages.json").exists() else {}
# (2026-11-26) 새 대화(빈 컨테이너)에서도 진행 현황이 맞게: 내려받지 않은 합격 파일은 tools/media_manifest.txt로 센다
_MAN = (ROOT / "tools/media_manifest.txt").read_text(encoding="utf-8").split() if (ROOT / "tools/media_manifest.txt").exists() else []
def _ids(d, ext):
    rel = str(d.relative_to(ROOT)) + "/"
    names = {f.name for f in d.glob(f"*.{ext}")} if d.exists() else set()
    names |= {m[len(rel):] for m in _MAN if m.startswith(rel) and m.endswith("." + ext)}
    return sorted({m.group(1) for n in names if (m := _re.match(r"(S\d\d)_", n))})
def _has_common(kind, c, ext):
    rel = f"episodes/common/{kind}/web/{c}_"
    return any((ROOT / f"episodes/common/{kind}/web").glob(f"{c}_*.{ext}")) or any(m.startswith(rel) for m in _MAN)
def progress(x):
    ep = x["ep"]; d = ROOT / f"episodes/ep{ep}"; n = x.get("no", int(ep))
    sc = d / "scenes.json"
    scs = json.loads(sc.read_text(encoding="utf-8")) if sc.exists() else []
    ids = [s["id"] for s in scs]
    img, vid = _ids(d / "images/web", "png"), _ids(d / "clips/web", "mp4")
    for s_ in scs:  # 공통 컷: episodes/common/ 에 있으면 이 화도 있는 것으로 센다
        c = s_.get("common")
        if c and _has_common("images", c, "png"): img.append(s_["id"])
        if c and _has_common("clips", c, "mp4"): vid.append(s_["id"])
    for s_ in scs:  # 같은 영상: 다른 장면(samevid)의 영상이 있으면 이 장면도 있는 것으로 센다
        if s_.get("samevid") and s_["samevid"] in vid: vid.append(s_["id"])
    song = any((d / "audio/songs").glob("*.wav")) or any((d / "audio/songs").glob("*.mp3"))
    voice = any((d / "audio/ko").glob("*.wav")) if (d / "audio/ko").exists() else False
    done = "file" in x
    T = len(ids) or 16
    ni = T if done else len([i for i in ids if i in img]); nv = T if done else len([i for i in ids if i in vid])
    mi = [i for i in ids if i not in img]; mv = [i for i in ids if i not in vid]
    if done: nxt, stage = "완성 · 올리기만 하면 돼요", 5
    elif ni < T: nxt, stage = ("그림 " + " ".join(mi) if ni else "그림 만들기 시작 전"), 1
    elif nv < T: nxt, stage = ("영상 " + " ".join(mv) if nv else "영상 만들기 시작 전"), 2
    elif not song: nxt, stage = "노래(Suno) 만들기", 3
    else: nxt, stage = "음성·조립", 4
    return dict(ep=ep, n=n, short=x["short"], T=T, ni=ni, nv=nv, song=song or done, voice=voice or done, done=done, nxt=nxt, stage=stage, page=PAGES.get(str(n), {}))
PR = sorted((progress(x) for x in eps), key=lambda r: r["n"])
def _bar(a, T): 
    pct = round(100 * a / T) if T else 0
    return f'<span class="bar" role="img" aria-label="{a}/{T}"><i style="width:{pct}%"></i></span><span class="num">{a}/{T}</span>'
def _ok(b): return '<span class="ok">✓</span>' if b else '<span class="no">–</span>'
_rows = "".join(
    f'<li class="pr s{r["stage"]}"><div class="pr-h"><span class="pn">{r["n"]}화</span><span class="pt">{e(r["short"])}</span>'
    f'{"<a href=" + chr(34) + r["page"]["scene"] + chr(34) + " target=_blank rel=noopener>장면</a>" if r["page"].get("scene") else ""}'
    f'{"<a href=" + chr(34) + r["page"]["song"] + chr(34) + " target=_blank rel=noopener>노래</a>" if r["page"].get("song") else ""}</div>'

    + ('<p class="nx done">✓ 완성 · 완성 영상은 이 화 탭에 있어요</p></li>' if r["done"] else
    f'<div class="pr-g"><span class="lb">그림</span>{_bar(r["ni"], r["T"])}<span class="lb">영상</span>{_bar(r["nv"], r["T"])}</div>'
    f'<div class="pr-c"><span>노래 {_ok(r["song"])}</span><span>음성 {_ok(r["voice"])}</span><span>완성 {_ok(r["done"])}</span></div>'
    f'<p class="nx">다음: {e(r["nxt"])}</p></li>') for r in PR)
_c = lambda k: sum(1 for r in PR if r["stage"] >= k)
import datetime as _dt
_now = _dt.datetime.now(_dt.timezone(_dt.timedelta(hours=9))).strftime("%m월 %d일 %H:%M")
PROG = (f'<section class="panel" id="prog" role="tabpanel" hidden><header class="ph"><h2>진행 현황</h2><span class="hint">{_now} 기준 · 파일 수를 세어 자동으로 만들어요</span></header>'
        f'<div class="sum"><div><b>{_c(5)}</b><span>완성</span></div><div><b>{_c(2)}</b><span>그림 끝</span></div><div><b>{_c(3)}</b><span>영상 끝</span></div><div><b>{len(PR)}</b><span>전체</span></div></div>'
        f'<ul class="prl">{_rows}</ul></section>')

tabs, panels = ['<a class="tab prog" href="#prog" data-ep="prog" role="tab"><span class="no">진행 현황</span></a>'], [PROG]
for x in eps:
    ep = x["ep"]; n = x.get("no", int(ep)); done = "file" in x
    tabs.append(f'<a class="tab{" soon" if not done else ""}" href="#ep{ep}" data-ep="ep{ep}" role="tab"><span class="no">{n}화</span></a>')
    if done:
        src = ROOT / f"output/{x['file']}.mp4"
        v, t = out / f"v/ep{ep}.mp4", out / f"t/ep{ep}.jpg"
        if not v.exists():
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", "scale=640:-2", "-c:v", "libx264", "-preset", "veryfast",
                            "-b:v", "400k", "-maxrate", "500k", "-bufsize", "1000k", "-c:a", "aac", "-b:a", "64k", "-movflags", "+faststart", str(v)], check=True)
        if not t.exists():
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(ROOT / f"episodes/ep{ep}/thumbnail.png"), "-vf", "scale=640:-2", "-q:v", "4", str(t)], check=True)
        body = (f'<video controls preload="none" playsinline poster="t/ep{ep}.jpg" src="v/ep{ep}.mp4"></video>'
                f'<dl class="facts"><div><dt>길이</dt><dd>{dur(src if src.exists() else v)}</dd></div><div><dt>주제</dt><dd>{e(x["theme"])}</dd></div>'
                f'<div class="wide"><dt>원본 파일</dt><dd><code>output/{e(x["file"])}.mp4</code>{" · 자막 없는 판 <code>output/" + e(x["file"]) + "_nosubs.mp4</code>" if (ROOT / f"output/{x['file']}_nosubs.mp4").exists() else " · 유튜브 자막 파일 <code>output/" + e(x["file"]) + ".srt</code>"}</dd></div></dl>'
                f'<p class="hint">여기 영상은 미리보기용(작은 화질)이에요. 유튜브에는 원본 파일을 올려요.</p>' + upload(ep))
    else:
        rows = "".join(f"<li><span>{e(a)}</span><b>{e(b)}</b></li>" for a, b in status(ep))
        body = (f'<div class="wait"><p class="wait-h">아직 만드는 중이에요</p><p>노래·음성까지 받아 완성되면 이 탭에 영상이 들어가요.</p>'
                f'<ul class="prog">{rows}</ul></div>')
    panels.append(f'<section class="panel" id="ep{ep}" role="tabpanel" hidden><header class="ph"><span class="badge">{n}화</span>'
                  f'<h2>{e(x["short"])}</h2></header>{body}</section>')

ndone = sum("file" in x for x in eps)
page = f"""<title>치키 타운 완성 영상</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;600&display=swap">
<style>
/* 레이아웃: 위에 화 번호 탭 띠(가로 스크롤), 아래에 고른 화 하나만 크게 */
:root {{
  --bg: #f4f7ef; --surface: #ffffff; --ink: #24301f; --muted: #66735e; --line: #dde5d3;
  --accent: #e8772e; --accent-ink: #ffffff; --soon: #b9c4ad;
  --display: "Jua", "Noto Sans KR", system-ui, sans-serif; --body: "Noto Sans KR", system-ui, sans-serif;
}}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{
  --bg: #151a13; --surface: #1e251b; --ink: #e8eee0; --muted: #a2ae97; --line: #2f3a2a;
  --accent: #f08a45; --accent-ink: #1a1006; --soon: #4c5844; color-scheme: dark }} }}
:root[data-theme="dark"] {{
  --bg: #151a13; --surface: #1e251b; --ink: #e8eee0; --muted: #a2ae97; --line: #2f3a2a;
  --accent: #f08a45; --accent-ink: #1a1006; --soon: #4c5844; color-scheme: dark }}
body {{ background: var(--bg); color: var(--ink); font-family: var(--body); font-size: 15px; line-height: 1.6;
  padding-left: max(16px, env(safe-area-inset-left, 0px)); padding-right: max(16px, env(safe-area-inset-right, 0px)); padding-block: 20px 40px; }}
.wrap {{ max-width: 860px; margin: 0 auto; display: grid; gap: 18px; }}
h1 {{ font-family: var(--display); font-weight: 400; font-size: 1.9rem; margin: 0; text-wrap: balance; }}
.sub {{ margin: 2px 0 0; color: var(--muted); }}
.tabs {{ display: flex; gap: 8px; overflow-x: auto; padding-bottom: 6px; scrollbar-width: thin; }}
.tab {{ flex: none; white-space: nowrap; text-decoration: none; color: var(--ink); background: var(--surface); border: 1.5px solid var(--line);
  border-radius: 999px; padding: 6px 14px; font-family: var(--display); font-size: 1.05rem; }}
.tab.soon {{ color: var(--muted); border-style: dashed; }}
.tab[aria-selected="true"] {{ background: var(--accent); border-color: var(--accent); color: var(--accent-ink); }}
.tab:focus-visible {{ outline: 3px solid var(--accent); outline-offset: 2px; }}
.panel {{ display: grid; gap: 14px; }} .panel[hidden] {{ display: none; }}
.ph {{ display: flex; align-items: baseline; gap: 10px; flex-wrap: wrap; }}
.badge {{ font-family: var(--display); color: var(--accent); font-size: 1.1rem; }}
h2 {{ font-family: var(--display); font-weight: 400; font-size: 1.6rem; margin: 0; text-wrap: balance; }}
video {{ width: 100%; max-width: 100%; aspect-ratio: 16 / 9; background: #000; border-radius: 14px; display: block; }}
.facts {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 10px 18px; margin: 0; }}
.facts div {{ min-width: 0; }} .facts .wide {{ grid-column: 1 / -1; }}
dt {{ font-size: 0.78rem; letter-spacing: 0.04em; color: var(--muted); }}
dd {{ margin: 0; font-variant-numeric: tabular-nums; overflow-wrap: anywhere; }}
code {{ font-size: 0.85rem; background: var(--surface); border: 1px solid var(--line); border-radius: 6px; padding: 1px 6px; }}
.hint {{ margin: 0; color: var(--muted); font-size: 0.85rem; }}
.wait {{ background: var(--surface); border: 1.5px dashed var(--soon); border-radius: 14px; padding: 18px; display: grid; gap: 6px; }}
.wait p {{ margin: 0; }} .wait-h {{ font-family: var(--display); font-size: 1.25rem; }}
.prog {{ list-style: none; margin: 6px 0 0; padding: 0; display: grid; gap: 4px; }}
.prog li {{ display: flex; justify-content: space-between; gap: 12px; border-top: 1px solid var(--line); padding-top: 4px; }}
.prog b {{ font-weight: 600; text-align: right; }}
.yt {{ display: grid; gap: 10px; border-top: 1.5px solid var(--line); padding-top: 14px; }}
.yt h3 {{ font-family: var(--display); font-weight: 400; font-size: 1.25rem; margin: 0; }}
.copybox {{ background: var(--surface); border: 1px solid var(--line); border-radius: 12px; overflow: hidden; min-width: 0; }}
.cb-head {{ display: flex; justify-content: space-between; align-items: center; padding: 6px 10px; border-bottom: 1px solid var(--line); font-size: 0.85rem; color: var(--muted); }}
.copybox pre {{ margin: 0; padding: 10px 12px; white-space: pre-wrap; overflow-wrap: anywhere; font-family: var(--body); font-size: 0.9rem; line-height: 1.55; max-height: 320px; overflow-y: auto; }}
.copy {{ font: inherit; font-size: 0.85rem; border: 1.5px solid var(--accent); background: transparent; color: var(--ink); border-radius: 999px; padding: 2px 12px; cursor: pointer; }}
.copy.done {{ background: var(--accent); color: var(--accent-ink); }}
.copy:focus-visible {{ outline: 3px solid var(--accent); outline-offset: 2px; }}
.setting {{ font-size: 0.88rem; color: var(--muted); }} .setting span {{ font-size: 0.78rem; letter-spacing: 0.04em; }} .setting p {{ margin: 2px 0 0; color: var(--ink); overflow-wrap: anywhere; }}
.thumb {{ margin: 0; display: grid; gap: 6px; min-width: 0; }} .thumb img {{ width: 100%; max-width: 100%; height: auto; border-radius: 12px; border: 1px solid var(--line); display: block; }} .thumb figcaption {{ display: flex; flex-wrap: wrap; justify-content: space-between; gap: 4px 12px; font-size: 0.85rem; color: var(--muted); }}
.sum {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px; }}
.sum div {{ background: var(--surface); border: 1px solid var(--line); border-radius: 12px; padding: 8px 10px; display: grid; }}
.sum b {{ font-family: var(--display); font-weight: 400; font-size: 1.6rem; font-variant-numeric: tabular-nums; }} .sum span {{ color: var(--muted); font-size: 0.82rem; }}
.prl {{ list-style: none; margin: 0; padding: 0; display: grid; gap: 8px; }}
.pr {{ background: var(--surface); border: 1px solid var(--line); border-left: 5px solid var(--soon); border-radius: 12px; padding: 8px 12px; display: grid; gap: 4px; min-width: 0; }}
.pr.s2 {{ border-left-color: #e9b949; }} .pr.s3, .pr.s4 {{ border-left-color: #6fb4e6; }} .pr.s5 {{ border-left-color: #5bb06a; }}
.pr-h {{ display: flex; align-items: baseline; gap: 8px; flex-wrap: wrap; }} .pn {{ font-family: var(--display); color: var(--accent); }} .pt {{ font-weight: 600; flex: 1; min-width: 0; }}
.pr-h a {{ font-size: 0.8rem; color: var(--ink); border: 1px solid var(--line); border-radius: 999px; padding: 0 9px; text-decoration: none; }}
.pr-g {{ display: grid; grid-template-columns: auto 1fr auto; align-items: center; gap: 2px 8px; font-size: 0.85rem; }}
.pr-c {{ display: flex; gap: 14px; flex-wrap: wrap; font-size: 0.85rem; color: var(--muted); }} .nx.done {{ color: #3f9a52; }}
.pr-g .lb {{ color: var(--muted); }}
.bar {{ height: 8px; background: var(--line); border-radius: 99px; overflow: hidden; display: block; min-width: 40px; }} .bar i {{ display: block; height: 100%; background: var(--accent); }}
.num {{ font-variant-numeric: tabular-nums; }} .ok {{ color: #3f9a52; font-weight: 600; }} .no {{ color: var(--muted); }}
.nx {{ margin: 0; font-size: 0.85rem; color: var(--muted); overflow-wrap: anywhere; }}
.tab.prog {{ border-color: var(--accent); }}
</style>
<div class="wrap">
  <header><h1>치키 타운 완성 영상</h1><p class="sub">완성 {ndone}편 · 탭을 눌러 화마다 볼 수 있어요</p></header>
  <nav class="tabs" role="tablist">{''.join(tabs)}</nav>
  {''.join(panels)}
</div>
<script>
const tabs = [...document.querySelectorAll('.tab')], panels = [...document.querySelectorAll('.panel')];
function show(id) {{
  if (!panels.some(p => p.id === id)) id = 'prog';
  panels.forEach(p => {{ if (p.id !== id) {{ const v = p.querySelector('video'); if (v) v.pause(); }} p.hidden = p.id !== id; }});
  tabs.forEach(t => {{ const on = t.dataset.ep === id; t.setAttribute('aria-selected', on); if (on) t.scrollIntoView({{block: 'nearest', inline: 'center'}}); }});
}}
document.addEventListener('click', ev => {{
  const b = ev.target.closest('.copy'); if (!b) return;
  const pre = document.getElementById(b.dataset.target);
  const ok = () => {{ b.textContent = '복사됨'; b.classList.add('done'); setTimeout(() => {{ b.textContent = '복사'; b.classList.remove('done'); }}, 1500); }};
  const sel = () => {{ const r = document.createRange(); r.selectNodeContents(pre); const s = getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = '선택됨 · 복사하세요'; }};
  try {{ navigator.clipboard.writeText(pre.textContent).then(ok, sel); }} catch (_) {{ sel(); }}
}});
addEventListener('hashchange', () => show(location.hash.slice(1)));
show(location.hash.slice(1));
</script>
"""
(out / "index.html").write_text(page, encoding="utf-8")
print("ok", ndone, "videos")
