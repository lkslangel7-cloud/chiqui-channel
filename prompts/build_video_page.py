"""완성 영상 보기 페이지(화마다 탭)를 만든다.
사용법: python3 prompts/build_video_page.py <출력 폴더>
- episodes/videos.json 에 "file"이 있는 화만 영상이 들어가고, 없는 화는 '만드는 중' 탭.
- 미리보기 영상(640px, 약 10MB)과 썸네일을 출력 폴더의 v/, t/ 에 만든다(이미 있으면 건너뜀).
- 아티팩트 한 번 올릴 때 64MB 제한 → v/ 파일은 5개씩 나눠 올린다.
"""
import html, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
out = Path(sys.argv[1]); (out / "v").mkdir(parents=True, exist_ok=True); (out / "t").mkdir(exist_ok=True)
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
tabs, panels = [], []
for x in eps:
    ep = x["ep"]; n = int(ep); done = "file" in x
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
                f'<dl class="facts"><div><dt>길이</dt><dd>{dur(src)}</dd></div><div><dt>주제</dt><dd>{e(x["theme"])}</dd></div>'
                f'<div class="wide"><dt>원본 파일</dt><dd><code>output/{e(x["file"])}.mp4</code> · 자막 없는 판 <code>output/{e(x["file"])}_nosubs.mp4</code></dd></div></dl>'
                f'<p class="hint">여기 영상은 미리보기용(작은 화질)이에요. 유튜브에는 원본 파일을 올려요.</p>')
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
.tab {{ flex: none; text-decoration: none; color: var(--ink); background: var(--surface); border: 1.5px solid var(--line);
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
</style>
<div class="wrap">
  <header><h1>치키 타운 완성 영상</h1><p class="sub">완성 {ndone}편 · 탭을 눌러 화마다 볼 수 있어요</p></header>
  <nav class="tabs" role="tablist">{''.join(tabs)}</nav>
  {''.join(panels)}
</div>
<script>
const tabs = [...document.querySelectorAll('.tab')], panels = [...document.querySelectorAll('.panel')];
function show(id) {{
  if (!panels.some(p => p.id === id)) id = '{'ep%s' % [x for x in eps if 'file' in x][-1]['ep']}';
  panels.forEach(p => {{ if (p.id !== id) {{ const v = p.querySelector('video'); if (v) v.pause(); }} p.hidden = p.id !== id; }});
  tabs.forEach(t => {{ const on = t.dataset.ep === id; t.setAttribute('aria-selected', on); if (on) t.scrollIntoView({{block: 'nearest', inline: 'center'}}); }});
}}
addEventListener('hashchange', () => show(location.hash.slice(1)));
show(location.hash.slice(1));
</script>
"""
(out / "index.html").write_text(page, encoding="utf-8")
print("ok", ndone, "videos")
