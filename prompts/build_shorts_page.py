"""숏폼 미리보기 페이지. 사용법: python3 prompts/build_shorts_page.py <출력 폴더>
출력 폴더의 v/epXX_kind.mp4(432px 미리보기)·p/epXX_kind.jpg(포스터)를 쓰고, 제목·설명은 output/shorts/shorts_info.md에서 읽는다.
"""
import html, re, sys
from pathlib import Path

R = Path(__file__).resolve().parent.parent
out = Path(sys.argv[1])
md = (R / "output/shorts/shorts_info.md").read_text(encoding="utf-8")
e = html.escape
eps = re.findall(r"^## (\d+)화 · (.+?)\n(.*?)(?=^## |\Z)", md, re.S | re.M)


def card(ep, kind, label, body):
    t = re.search(rf"`ep{ep}_{kind}\.mp4` — 제목: `([^`]+)`", body).group(1)
    d = re.search(rf"`ep{ep}_{kind}\.mp4`.*?\n  - 설명: `([^`]+)`", body, re.S).group(1)
    i = f"{ep}{kind}"
    box = lambda n, k, txt: (f'<div class="copybox"><div class="cb-head"><span>{n}</span><button type="button" class="copy" data-target="{i}{k}">복사</button></div>'
                             f'<pre id="{i}{k}">{e(txt)}</pre></div>')
    return (f'<article class="card"><span class="kind {kind}">{label}</span>'
            f'<video controls preload="none" playsinline poster="p/ep{ep}_{kind}.jpg" src="v/ep{ep}_{kind}.mp4"></video>'
            f'<p class="file"><code>output/shorts/ep{ep}_{kind}.mp4</code></p>{box("제목", "t", t)}{box("설명", "d", d)}</article>')


secs = "".join(f'<section class="ep" id="ep{int(n):02d}"><h2><span class="no">{int(n)}화</span> {e(name)}</h2><div class="pair">'
               f'{card(f"{int(n):02d}", "song", "노래 28초", body)}{card(f"{int(n):02d}", "quiz", "퀴즈", body)}</div></section>'
               for n, name, body in eps)
nav = "".join(f'<a href="#ep{int(n):02d}">{int(n)}화</a>' for n, _, _ in eps)
common = re.search(r"공통 해시태그: (.+)", md).group(1)
page = f"""<title>치키 타운 숏폼</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;600&display=swap">
<style>
/* 레이아웃: 위에 화 바로가기, 화마다 세로 영상 2개(노래·퀴즈)를 나란히, 아래에 제목·설명 복사 칸 */
:root {{ --bg:#f4f7ef; --surface:#fff; --ink:#24301f; --muted:#66735e; --line:#dde5d3; --accent:#e8772e; --accent-ink:#fff; --song:#e8772e; --quiz:#3f8fd0;
  --display:"Jua","Noto Sans KR",system-ui,sans-serif; --body:"Noto Sans KR",system-ui,sans-serif; }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#151a13; --surface:#1e251b; --ink:#e8eee0; --muted:#a2ae97; --line:#2f3a2a; --accent:#f08a45; --accent-ink:#1a1006; --song:#f08a45; --quiz:#5aa6e0; color-scheme:dark }} }}
:root[data-theme="dark"] {{ --bg:#151a13; --surface:#1e251b; --ink:#e8eee0; --muted:#a2ae97; --line:#2f3a2a; --accent:#f08a45; --accent-ink:#1a1006; --song:#f08a45; --quiz:#5aa6e0; color-scheme:dark }}
body {{ background:var(--bg); color:var(--ink); font-family:var(--body); font-size:15px; line-height:1.55;
  padding-left:max(16px,env(safe-area-inset-left,0px)); padding-right:max(16px,env(safe-area-inset-right,0px)); padding-block:20px 48px; }}
.wrap {{ max-width:900px; margin:0 auto; display:grid; gap:22px; }}
h1 {{ font-family:var(--display); font-weight:400; font-size:1.9rem; margin:0; }}
.sub {{ margin:2px 0 0; color:var(--muted); }}
nav {{ display:flex; gap:8px; overflow-x:auto; padding-bottom:4px; }}
nav a {{ flex:none; text-decoration:none; color:var(--ink); background:var(--surface); border:1.5px solid var(--line); border-radius:999px; padding:5px 13px; font-family:var(--display); }}
.ep {{ display:grid; gap:12px; scroll-margin-top:12px; }}
h2 {{ font-family:var(--display); font-weight:400; font-size:1.45rem; margin:0; }} h2 .no {{ color:var(--accent); }}
.pair {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:16px; }}
.card {{ background:var(--surface); border:1px solid var(--line); border-radius:16px; padding:12px; display:grid; gap:8px; min-width:0; align-content:start; }}
.kind {{ justify-self:start; font-family:var(--display); color:#fff; border-radius:999px; padding:2px 12px; }} .kind.song {{ background:var(--song); }} .kind.quiz {{ background:var(--quiz); }}
video {{ width:100%; max-width:300px; justify-self:center; aspect-ratio:9/16; background:#000; border-radius:12px; display:block; }}
.file {{ margin:0; font-size:.8rem; color:var(--muted); overflow-wrap:anywhere; }}
.copybox {{ border:1px solid var(--line); border-radius:10px; overflow:hidden; min-width:0; }}
.cb-head {{ display:flex; justify-content:space-between; align-items:center; padding:4px 10px; border-bottom:1px solid var(--line); font-size:.82rem; color:var(--muted); }}
.copybox pre {{ margin:0; padding:8px 10px; white-space:pre-wrap; overflow-wrap:anywhere; font-family:var(--body); font-size:.88rem; }}
.copy {{ font:inherit; font-size:.82rem; border:1.5px solid var(--accent); background:transparent; color:var(--ink); border-radius:999px; padding:1px 11px; cursor:pointer; }}
.copy.done {{ background:var(--accent); color:var(--accent-ink); }} .copy:focus-visible, nav a:focus-visible {{ outline:3px solid var(--accent); outline-offset:2px; }}
.tips {{ background:var(--surface); border:1px solid var(--line); border-radius:14px; padding:12px 16px; }} .tips p {{ margin:4px 0; }}
</style>
<div class="wrap">
  <header><h1>치키 타운 숏폼</h1><p class="sub">유튜브 쇼츠·인스타 릴스용 {len(eps) * 2}개 · 화마다 노래 1개, 퀴즈 1개 · 여기 영상은 미리보기(작은 화질)예요</p></header>
  <div class="tips"><p><b>공통 해시태그</b> {e(common)}</p><p>유튜브 쇼츠는 아동용 "예", 본편을 "관련 동영상"으로 연결하세요. 하루 1~2개씩 나눠 올리는 게 좋아요.</p></div>
  <nav>{nav}</nav>
  {secs}
</div>
<script>
document.addEventListener('click', ev => {{
  const b = ev.target.closest('.copy'); if (!b) return;
  const pre = document.getElementById(b.dataset.target);
  const ok = () => {{ b.textContent = '복사됨'; b.classList.add('done'); setTimeout(() => {{ b.textContent = '복사'; b.classList.remove('done'); }}, 1500); }};
  const sel = () => {{ const r = document.createRange(); r.selectNodeContents(pre); const s = getSelection(); s.removeAllRanges(); s.addRange(r); b.textContent = '선택됨'; }};
  try {{ navigator.clipboard.writeText(pre.textContent).then(ok, sel); }} catch (_) {{ sel(); }}
}});
document.addEventListener('play', ev => {{ document.querySelectorAll('video').forEach(v => {{ if (v !== ev.target) v.pause(); }}); }}, true);
</script>
"""
(out / "index.html").write_text(page, encoding="utf-8")
print("ok", len(eps))
