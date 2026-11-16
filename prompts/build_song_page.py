"""1화 노래 4곡의 Suno 프롬프트 복사 페이지와 md를 만든다.
사용법: python3 -I prompts/build_song_page.py episodes/ep01
"""
import html, json, re, sys
from pathlib import Path

ep = Path(sys.argv[1])
BASE = ("toddler sing-along nursery song, Korean lyrics, clear slow pronunciation, simple melody with small note range, "
        "warm female lead with kids choir, ukulele, marimba, glockenspiel, soft handclaps, gentle dinosaur stomp drum, "
        "major key, cheerful and cozy")

SONGS = [
    dict(id="op", short="오프닝", title="치키의 공룡 마을 (오프닝)", where="0:00–0:15 · 매회 같음", inst=False,
         style="short 20-second kids TV show theme jingle, bright and bouncy, 100 bpm, kids choir shouting the names back, " + BASE,
         lyrics="""[Intro]
쿵쿵 쾅! 쿵쿵 쾅!

[Verse]
뿔이 셋 치키 (치키!)
크앙 크앙 로로 (로로!)
목이 쭈욱 토롱 (토롱!)
하늘 슝슝 피오 (피오!)
안경 쓴 바우 할아버지 (허허!)
공룡 마을 친구들
치키치키 출발!

[End]"""),
    dict(id="egg", short="알 찾기", title="공룡알 어디 있니?", where="1:15–2:10 · 1화 노래 (후렴은 매회 같은 틀)", inst=False,
         style="call-and-response with short pauses for kids to echo, slow easy tempo 96 bpm, " + BASE,
         lyrics="""[Chorus]
쿵쿵 쾅! 쿵쿵 쾅!
공룡알 어디 있니? (어디 있니?)
친구들아 같이 가자
치키치키 출발!

[Verse 1]
바위 뒤에 동글동글
크앙! 로로가 찾았다
알이 하나, 알이 둘 (둘!)

[Verse 2]
나무 위에 동글동글
쭈욱~ 토롱이 찾았다
알이 둘, 알이 셋 (셋!)

[Verse 3]
언덕 위에 동글동글
슝~ 피오가 찾았다
알이 셋, 알이 넷 (넷!)

[Verse 4]
나뭇잎 밑 동글동글
짠! 치키가 찾았다
알이 넷, 알이 다섯 (다섯!)

[Chorus]
쿵쿵 쾅! 쿵쿵 쾅!
공룡알 다 찾았다 (찾았다!)
친구들아 고마워
치키치키 출발!

[End]"""),
    dict(id="ed", short="엔딩", title="내일 또 만나요 (엔딩)", where="2:45–3:00 · 매회 같음", inst=False,
         style="short 15-second goodbye jingle, gentle and warm, 92 bpm, " + BASE,
         lyrics="""[Verse]
오늘도 재밌었지? (응!)
바우 할아버지도 (허허!)
안녕! 바이바이! 아디오스!
내일 또 만나요, 크앙!

[End]"""),
    dict(id="bgm", short="배경음악", title="공룡 마을 배경음악", where="노래 사이 이야기 부분 · 가사 없음", inst=True,
         style=("gentle playful background music for a toddler cartoon, instrumental, no vocals, 92 bpm, ukulele, marimba, "
                "glockenspiel, soft pizzicato strings, light handclaps, major key, calm and cozy, steady and loopable"),
         lyrics=""),
]

PAGE = dict(note="오프닝은 바우 할아버지 줄을 넣은 새 가사예요 (2화부터 계속 쓰는 곡). 길게 나와도 괜찮아요. 받은 파일을 여기 채팅에 올려 주면 길이는 제가 맞춰 자를게요.", duration="<b>Custom</b> — 오프닝 25초, 엔딩 20초, 알 찾기 노래 60초, 배경음악 60초. 길이를 못 고르면 Auto로 두세요.", title="치키 노래 프롬프트", h1="1화 · 노래 만들기 (Suno)", lead="노래 3곡과 배경음악 1곡이에요. 칸마다 <b>복사</b>를 눌러 Suno에 그대로 붙여 넣으세요.")
cfg = ep / "songs.json"
if cfg.exists():
    c = json.loads(cfg.read_text(encoding="utf-8"))
    PAGE.update({k: c[k] for k in ("title", "h1", "lead", "note", "duration") if k in c})
    SONGS = [dict(s, style=s["style"].replace("{BASE}", BASE)) for s in c["songs"]]

e = html.escape
def box(kind, bid, text):
    return (f'<div class="prompt"><div class="prompt-head"><span class="kind">{e(kind)}</span>'
            f'<button type="button" class="copy" data-target="{bid}">복사</button></div><pre id="{bid}">{e(text)}</pre></div>')

cards = []
md = [f"# {PAGE['h1']}", "", "Suno → Create → Custom. 칸마다 그대로 붙여 넣는다.", "",
      "More Options: Vocal Gender Female / Duration Custom(오프닝·엔딩 20초, 알 찾기·배경음악 60초) / Max Mode Off / Weirdness 20% / Style Influence 80% / Variety Normal / Personalize Off", ""]
for s in SONGS:
    parts = [box("Title (제목)", s["id"] + "-t", s["title"])]
    if s["inst"]:
        parts.append('<p class="note">가사 칸은 비워 두고 <b>Instrumental</b>을 켠다.</p>')
    else:
        parts.append(box("Lyrics (가사)", s["id"] + "-l", s["lyrics"]))
    parts.append(box("Styles (스타일)", s["id"] + "-s", s["style"]))
    cards.append(f'<article class="scene" id="{s["id"]}"><header class="scene-head"><h2>{e(s["title"])}</h2>'
                 f'<span class="time">{e(s["where"])}</span></header>{"".join(parts)}</article>')
    md += [f"## {s['title']}", "", f"- 자리: {s['where']}", f"- Title: {s['title']}",
           "- Instrumental 켜기, 가사 없음" if s["inst"] else "", "", "Styles:", "```", s["style"], "```", ""]
    if not s["inst"]:
        md += ["Lyrics:", "```", s["lyrics"], "```", ""]

src = (Path(__file__).parent / "build_prompt_page.py").read_text(encoding="utf-8")
css = re.search(r"<style>\n(.*?)</style>", src, re.S).group(1).replace("{{", "{").replace("}}", "}")
css += "h1 { word-break: keep-all; }\n.note { margin: 0; font-size: .95rem; color: var(--muted); }\n.steps b { color: var(--ink); }\n"
css += ".opts { width: 100%; border-collapse: collapse; font-size: .92rem; }\n.opts th, .opts td { text-align: left; padding: 8px 6px; border-top: 1px solid var(--line); vertical-align: top; }\n.opts th { color: var(--muted); font-weight: 600; font-size: .8rem; }\n.opts td:first-child { white-space: nowrap; font-family: var(--mono); font-size: .85rem; }\n"
js = re.search(r"<script>\n(.*?)</script>", src, re.S).group(1).replace("{{", "{").replace("}}", "}")

page = f'''<title>{PAGE["title"]}</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Jua&family=Noto+Sans+KR:wght@400;600&family=IBM+Plex+Mono:wght@400&display=swap">
<style>
{css}</style>
<div class="wrap">
  <header style="display:grid;gap:8px">
    <h1>{PAGE["h1"]}</h1>
    <p class="lead">{PAGE["lead"]}</p>
  </header>
  <section class="fixed">
    <h2>쓰는 순서</h2>
    <ol class="steps">
      <li>Suno에서 <b>Create</b> → <b>Custom</b> 모드를 켠다.</li>
      <li>Lyrics 칸에 가사, Styles 칸에 스타일, Title 칸에 제목을 붙여 넣는다.</li>
      <li><b>More Options</b>는 아래 표처럼 맞춘다.</li>
      <li>한 번에 2곡씩 나와요. 발음이 또렷하고 밝은 쪽을 고른다.</li>
      <li>{PAGE["note"]}</li>
      <li>유튜브 수익 창출을 하려면 Suno <b>유료 플랜(Pro 이상)</b>으로 만든 곡이어야 해요. 무료 플랜 곡은 상업적으로 쓸 수 없어요.</li>
    </ol>
    <table class="opts"><thead><tr><th>설정</th><th>값</th></tr></thead><tbody>
      <tr><td>Vocal Gender</td><td><b>Female</b> (배경음악은 상관없음)</td></tr>
      <tr><td>Duration</td><td>{PAGE["duration"]}</td></tr>
      <tr><td>Max Mode</td><td><b>Off</b></td></tr>
      <tr><td>Weirdness</td><td><b>20%</b> (낮을수록 무난하고 동요다운 곡)</td></tr>
      <tr><td>Style Influence</td><td><b>80%</b> (스타일 문구를 잘 따르게)</td></tr>
      <tr><td>Variety</td><td><b>Normal</b> 그대로</td></tr>
      <tr><td>Personalize</td><td><b>Off</b> (4곡 소리를 똑같이 맞추려고)</td></tr>
    </tbody></table>
  </section>
  {"" if len(SONGS) < 2 else '<nav class="jump" aria-label="곡 바로가기">' + "".join(f'<a href="#{x["id"]}">{e(x.get("short", x["title"]))}</a>' for x in SONGS) + '</nav>'}
  {"".join(cards)}
</div>
<script>
{js}</script>
'''
(ep / "song_prompts_page.html").write_text(page, encoding="utf-8")
(ep / "song_prompts.md").write_text("\n".join(md) + "\n", encoding="utf-8")
print("ok")
