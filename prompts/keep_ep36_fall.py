"""(2026-11-25, 사용자) 36화 「알록달록 가을 낙엽!」은 계절이 지나 내년 가을에 만들기로 킵.
내년에 쓸 때는 이 블록을 make_ep26_40.py(또는 새 생성기)에 붙여 새 화 번호로 쓰고, song_styles.json의 아래 KEEP_STYLE도 함께 넣는다.
"""
KEEP_STYLE = {"vocal": "Female", "style": "cozy indie-folk, 100 bpm, acoustic guitar, handclaps, crunchy leaf rustle percussion, warm autumn feeling, soft female lead, toddler sing-along kids song, Korean lyrics, clear slow pronunciation, simple catchy melody with small note range, kids choir echoes the short shouts in brackets, major key"}
KEEP_BLOCK = r'''
# ---------------- 36화 알록달록 가을 낙엽 ----------------
FALL = "In the volcano-island village in autumn: the meadow is golden, trees have orange and yellow leaves, a few leaves drift down. "
GINKGO = "THE SAME big ginkgo tree with fan-shaped bright YELLOW leaves"
EPS["ep36"] = dict(
 title="36화. 알록달록 가을 낙엽! — 가을 놀이", short="알록달록 가을 낙엽!", song_id="leaf", song_short="낙엽 노래",
 theme="가을 낙엽 줍기·세기·낙엽 더미 놀이, 까꿍.",
 twist="폭신폭신 낙엽 더미… 치키는 어디 있지? 까꿍! 낙엽 속에서 치키가 짠!",
 bau="은행나무는 공룡 시대에도 있었단다!",
 lines=[("내레이션","바스락바스락, 가을이에요.",""),("치키","낙엽 놀이 하자!",""),("모두","좋아!","♻ 1화 07"),("모두","하나, 둘, 셋!",""),
        ("내레이션","치키는 어디 있을까?","뒤에 3초 쉼"),("치키","까꿍!",""),("모두","하하하!","♻ 3화 11"),
        ("바우","은행나무는 공룡 시대에도 있었단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("노란 은행잎 팔랑","크앙! 로로가 줍고","하나 (팔랑!)"),("높은 데 초록 잎","쭈욱~ 토롱이 쏙","둘 (쏙!)"),
         ("바람에 휘리릭","슝~ 피오가 잡고","셋 (휘리릭!)"),("낙엽 더미 폭신폭신","치키는 어디 있지? (어디?)","까꿍! (까꿍!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "알록달록 낙엽 (팔랑!)", "바스락 바스락", "치키치키 가을!"],
 scenes=scenes([
  ("가을이에요", "", FALL + "Leaves drift down over the round cave houses. No characters.", "", False, "Leaves drift down slowly; nothing else moves."),
  ("낙엽 놀이 하자!", "C", FALL + f"{D['C']} catches one falling ORANGE leaf with both paws, delighted.", "", False, "Chiqui catches the leaf and smiles."),
  BAU(FALL, "은행나무 아래", f"stands under {GINKGO}, smiling."),
  CHEER(FALL),
  ("바스락", "", FALL + "Close view of colorful fallen leaves on the ground: orange, yellow and a few green ones. No characters.", "", True, "A leaf lands softly; nothing else moves."),
  ("작은 낙엽 더미", "C", FALL + f"{D['C']} jumps into a small pile of leaves, leaves flying up.", "", False, "Chiqui jumps once; leaves fly up and fall back."),
  ("로로가 줍고", "R", FALL + f"{D['R']} picks up one YELLOW ginkgo leaf from the ground and holds it up.", "", False, "Roro picks up the leaf and shows it, smiling."),
  ("토롱이 쏙", "T", FALL + f"{D['T']} takes one GREEN leaf from a low branch right in front of the mouth.", "", False, NEAR + "Torong gently takes the leaf with the mouth and lifts the head, smiling."),
  ("피오가 잡고", "P", FALL + f"{D['P']} flies and catches one falling ORANGE leaf in the beak.", "", False, "Pio glides and catches the leaf in the beak."),
  ("큰 낙엽 더미", "CRTP", FALL + "Chiqui, Roro, Torong and Pio push fallen leaves into one big round pile together.", "Exactly one big pile.", False, "They push leaves into the pile; it grows; Torong pushes leaves with the nose."),
  ("치키는?", "RTP", FALL + "Roro, Torong and Pio look around next to the big leaf pile; Chiqui is not there.", "", False, "They look left and right, puzzled."),
  ("어디 있을까?", "", FALL + "Close view of the big leaf pile; only the tip of one small ORANGE horn peeks out of the top. No other characters visible.", "", True, "The leaf pile wiggles a little."),
  ("까꿍!", "CRTP", FALL + f"{D['C']} pops out of the big leaf pile with leaves flying; Roro, Torong and Pio laugh.", "", False, "Chiqui pops up with a big smile; leaves fly; everyone laughs."),
  BAU(FALL, "공룡 시대에도", f"stands under {GINKGO} with yellow leaves drifting down, smiling wisely."),
  ("낙엽 비", "CRTP", FALL + "Chiqui, Roro, Torong and Pio toss leaves up into the air together.", "", False, "Leaves fly up and drift down; everyone laughs."),
  WAVE(FALL, "안녕!"),
 ]))

'''
