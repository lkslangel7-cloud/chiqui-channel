"""7~9화 edit_order.json을 노래 박자(받아쓰기 시간)에 맞춰 만든다."""
import json
from pathlib import Path
R = Path(__file__).resolve().parent.parent / "episodes"
d3 = json.loads((R / "ep03/edit_order.json").read_text(encoding="utf-8"))
OPEN = d3["video"][:4]; OPENCAP = [c for c in d3["captions"] if c["at"] < 20]; ENDCAP = [c for c in d3["captions"] if c["at"] >= 160]

def lyr(ep):
    t = (R / ep / "lyrics_ko.md").read_text(encoding="utf-8").split("```")[1]
    return [l for l in t.splitlines() if l.strip() and not l.startswith("[")]

def build(ep, title, song, songlen, sec, intro, intro_lines, post, post_lines, own_end=None, o=54.0, bye_at=17.6):
    c = lambda n: f"clips/{ep}_s{n}.mp4"
    V = list(OPEN)
    def v(st, du, f, note, frm=0, **k): V.append(dict(start=round(st, 2), file=f, **{"from": frm}, dur=round(du, 2), note=note, **k))
    t0 = 20
    for n, du, kw in intro:
        v(t0, du, c(n), f"S{n}", **kw); t0 += du
    assert abs(t0 - o) < 0.01, (ep, t0)
    starts = [s[0] for s in sec] + [songlen]
    v(o, starts[0], "../ep01/clips/ep01_v05.mp4", "치키 달리기 (1화, 노래 후렴)", speed=round(min(1, 10 / starts[0]), 2))
    for i, n in enumerate(["09", "10", "11", "12", "13"]):
        du = starts[i + 1] - starts[i]; kw = dict(sec[i][1])
        if "keep" in kw:
            kw = dict(speed=round(min(1, kw["keep"] / du), 2))
        elif du > 10 and "speed" not in kw:
            kw = dict(speed=round(10 / du, 2))
        v(o + starts[i], du, c(n), f"S{n} (노래 {['1절','2절','3절','4절','후렴'][i]})", **kw)
    t = o + songlen
    tt = t
    for n, du, kw in post:
        v(tt, du, c(n), f"S{n}", **kw); tt += du
    e = tt
    if own_end:
        for n, du in own_end:
            v(e + (0 if n == own_end[0][0] else own_end[0][1]), du, c(n), f"S{n} 엔딩")
    else:
        v(e, 10, "../ep04/clips/ep04_s20.mp4", "엔딩 춤 (4화)")
        v(e + 10, 10, "../ep04/clips/ep04_s21.mp4", "엔딩 노을 인사 (4화)", speed=0.9, pingpong=True)
    L = [dict(at=round(a, 2), audio=f"audio/ko/{f}", who=w, text=tx) for a, f, w, tx in intro_lines]
    L += [dict(at=round(t + a, 2), audio=f"audio/ko/{f}", who=w, text=tx) for a, f, w, tx in post_lines]
    if not own_end:
        L.append(dict(at=round(e + bye_at, 2), audio=f"audio/ko/{sorted(p.name for p in (R / ep / 'audio/ko').glob('*_chiqui.wav'))[-1]}", who="치키", text="안녕!"))
    ly = lyr(ep); C = list(OPENCAP); k = 0
    k = 0
    for si, (s0, kw, marks) in enumerate(sec):
        end = starts[si + 1] - 0.3
        for j, m in enumerate(marks):
            nxt = marks[j + 1] if j + 1 < len(marks) else end
            C.append(dict(at=round(o + m, 1), end=round(o + nxt, 1), text=ly[k])); k += 1
    C = [x for x in C] + [dict(at=round(x["at"] - 160 + e, 1), end=round(x["end"] - 160 + e, 1), text=x["text"]) for x in ENDCAP]
    M = [d3["music"][0], dict(file="../ep01/audio/songs/bgm.wav", at=20, **{"from": 0}, dur=o - 20 + 0.6, volume=0.3, fade_in=1, fade_out=1.5, note="배경음악"),
         dict(file=f"audio/songs/{song}", at=o, **{"from": 0}, dur=songlen, volume=0.9, fade_out=1, note="노래"),
         dict(file="../ep01/audio/songs/bgm.wav", at=t, **{"from": 0}, dur=round(e - t + 0.4, 2), volume=0.25 if own_end else 0.3, fade_in=1.5, fade_out=1.5, note="배경음악"),
         dict(d3["music"][-1], at=round(e + 0.4, 2), volume=0.6 if own_end else 0.9)]
    total = round(e + 20, 2)
    (R / ep / "edit_order.json").write_text(json.dumps(dict(title=title, length=total, draft="완성", video=V, lines=L, music=M, captions=C, sfx_suggestions=[]), ensure_ascii=False, indent=2), encoding="utf-8")
    print(ep, total, len(C) - len(OPENCAP) - len(ENDCAP), "lyric captions of", len(ly))

# 7화 사과 (노래 53.6초)
build("ep07", "7화 사과야 어디 있니?", "apple_song.wav", 53.6,
      [(12.6, {}, [2.5, 5.1, 7.9, 10.1, 12.6, 15.3, 17.4]), (20.1, {}, [20.1, 22.8, 25.2]), (27.8, {"keep": 6.5}, [27.8, 30.3, 32.4]), (35.3, {}, [35.3, 37.8, 40.0]), (42.6, {}, [42.6, 45.3, 47.8, 50.2])],
      [("02", 10, {}), ("03", 10, {}), ("04", 5, {}), ("05", 5, {}), ("06", 4, {})],
      [(21, "01_bau.wav", "바우 할아버지", "사과 열 개 따러 가자!"), (31.5, "02_chiqui.wav", "치키", "와, 사과 나무다!"), (45.8, "03_chiqui.wav", "치키", "친구들아, 같이 따자!"), (50.8, "04_all.wav", "모두", "좋아!")],
      [("14", 5, {}), ("15", 10, {}), ("16", 10, {}), ("17", 10, {"speed": 0.6}), ("18", 10, {})],
      [(0.5, "05_narr.wav", "내레이션", "몇 개 남았을까?"), (7.5, "06_bau.wav", "바우 할아버지", "아홉, 열!"), (15.3, "07_narr.wav", "내레이션", "다 같이 세어 볼까?"),
       (17.0, "08_all.wav", "모두", "하나, 둘, 셋, 넷, 다섯, 여섯, 일곱, 여덟, 아홉, 열!"), (27.0, "09_bau.wav", "바우 할아버지", "다 같이 모으니 열 개!"), (30.3, "10_all.wav", "모두", "와아~"), (36.0, "11_all.wav", "모두", "냠냠, 맛있다!")])

# 8화 발자국 (노래 61.9초)
build("ep08", "8화 발자국 누구 거니?", "foot_song.wav", 61.9,
      [(12.3, {}, [1.9, 4.3, 7.5, 8.9, 12.3, 14.4, 16.8]), (21.3, {}, [21.3, 23.9, 26.3]), (30.3, {"keep": 7}, [30.3, 33.3, 35.7]), (40.0, {}, [40.0, 43.5, 45.6]), (50.5, {}, [50.5, 53.1, 55.7, 58.0])],
      [("02", 10, {}), ("03", 5, {}), ("04", 5, {}), ("05", 5, {}), ("06", 5, {}), ("07", 4, {})],
      [(21.5, "01_chiqui.wav", "치키", "어? 발자국이다!"), (36.0, "02_bau.wav", "바우 할아버지", "누구 발자국일까?"), (41.0, "03_chiqui.wav", "치키", "친구들아, 같이 찾자!"), (46.0, "04_all.wav", "모두", "좋아!")],
      [("14", 5, {}), ("15", 10, {}), ("16", 10, {}), ("17", 10, {}), ("18", 10, {})],
      [(0.5, "05_narr.wav", "내레이션", "치키 발자국은 어디 있을까?"), (6.0, "06_chiqui.wav", "치키", "내 발자국이다!"), (9.0, "07_all.wav", "모두", "하하하!"),
       (16.0, "08_bau.wav", "바우 할아버지", "발자국 화석으로 공룡을 알 수 있단다."), (19.6, "09_all.wav", "모두", "와아~"),
       (25.3, "10_narr.wav", "내레이션", "누구 발이 제일 클까?"), (29.0, "11_all.wav", "모두", "토롱!"), (30.6, "12_narr.wav", "내레이션", "누구 발이 제일 작을까?"), (34.4, "13_all.wav", "모두", "피오!")])
# 9화 달님 (노래 62.2초, 잠자는 엔딩은 이 화 영상)
build("ep09", "9화 달님 어디 있니?", "moon_song.wav", 62.2,
      [(12.4, {}, [2.1, 4.8, 7.9, 9.8, 12.4, 14.8, 17.2]), (22.2, {"keep": 5}, [22.2, 24.8, 27.1]), (32.2, {"keep": 5.5}, [32.2, 34.6, 37.0]), (42.1, {}, [42.1, 44.7, 47.2]), (52.0, {}, [52.0, 54.3, 56.6, 59.3])],
      [("02", 10, {}), ("03", 5, {}), ("04", 5, {}), ("05", 5, {}), ("06", 5, {}), ("07", 4, {})],
      [(21.0, "01_chiqui.wav", "치키", "더 놀고 싶어!"), (31.0, "02_bau.wav", "바우 할아버지", "해님도 코~ 자러 가네."), (36.0, "03_chiqui.wav", "치키", "어? 달님이 없다!"),
       (41.0, "04_chiqui.wav", "치키", "친구들아, 같이 찾자!"), (46.0, "05_all.wav", "모두", "좋아!")],
      [("14", 5, {}), ("15", 10, {}), ("16", 10, {}), ("17", 10, {}), ("18", 10, {})],
      [(0.5, "06_narr.wav", "내레이션", "달님은 어디 있을까?"), (9.3, "07_chiqui.wav", "치키", "달님이다! 구름 뒤에 숨어 있었네!"), (12.6, "08_all.wav", "모두", "와아~"),
       (16.0, "09_bau.wav", "바우 할아버지", "구름에 가려도, 달님은 늘 있단다."), (26.0, "10_all.wav", "모두", "달님, 잘 자!"), (36.5, "11_narr.wav", "내레이션", "쉿, 잘 자요.")],
      own_end=[("19", 10), ("20", 10)])

# 10화 정리 (노래 62.0초, "상자에 쏙")
if __name__ == "__main__" or True:
    build("ep10", "10화 장난감은 제자리!", "box_song.wav", 62.0,
      [(12.4, {}, [2.0, 5.1, 7.8, 9.8, 12.4, 14.9, 16.4]), (21.6, {}, [21.6, 24.6, 26.5]), (31.6, {"frm": 5, "speed": 0.49}, [31.6, 35.2, 37.0]), (41.8, {}, [41.8, 44.3, 47.1]), (51.7, {}, [51.7, 54.2, 56.6, 59.0])],
      [("02", 10, {}), ("03", 5, {}), ("04", 5, {}), ("05", 5, {}), ("06", 5, {}), ("07", 4, {})],
      [(21.0, "01_chiqui.wav", "치키", "실컷 놀았다!"), (30.6, "02_bau.wav", "바우 할아버지", "어이쿠, 장난감이 가득하네."), (35.4, "03_bau.wav", "바우 할아버지", "다 놀면 제자리! 각자 자기 상자에 쏙!"),
       (40.8, "04_chiqui.wav", "치키", "어? 내 상자는?"), (45.5, "05_chiqui.wav", "치키", "친구들아, 같이 정리하자!"), (50.6, "06_all.wav", "모두", "좋아!")],
      [("14", 5, {}), ("15", 10, {}), ("16", 10, {}), ("17", 10, {}), ("18", 10, {})],
      [(0.5, "07_narr.wav", "내레이션", "치키 상자는 어디 있을까?"), (7.0, "08_chiqui.wav", "치키", "내가 앉아 있었네!"), (9.6, "09_all.wav", "모두", "하하하!"),
       (16.5, "03_bau.wav", "바우 할아버지", "다 놀면 제자리! 각자 자기 상자에 쏙!"), (26.0, "10_all.wav", "모두", "영차, 영차! 제자리!"),
       (35.3, "11_narr.wav", "내레이션", "방이 어떻게 됐을까?"), (38.4, "12_all.wav", "모두", "깨끗해!")])
