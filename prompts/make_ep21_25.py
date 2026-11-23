"""21~25화 대본·가사·장면 프롬프트. 인기 유아 채널에서 반응이 좋은 '소재'만 참고하고 이야기·노래는 새로 만든다.
21 구조대 자동차(탈것) · 22 바닷가 모래성 · 23 운동회 · 24 모양 블록 집 짓기 · 25 크리스마스 트리
도우미(img, vid, scenes, write)와 안전 문장은 make_ep11_15.py → make_ep06_10.py 것을 그대로 쓴다.
11~20화에서 배운 것을 처음부터 넣었다: 반복 소품은 한 문장으로 고정(CARS·CASTLE·FIELD·BLOCKS·XTREE),
탈것은 왼쪽으로만, 동작은 결과까지(붙인 조개가 남는다 등), 토롱은 가까이 있는 것만 입으로(목이 늘어나지 않게).
사용법: python3 -I prompts/make_ep21_25.py
"""
from pathlib import Path

_p = Path(__file__).resolve().parent / "make_ep11_15.py"
_src = _p.read_text(encoding="utf-8")
_ns = {"__file__": str(_p)}
exec(_src.split("\nEPS = {}")[0], _ns)
img, vid, scenes, write, D, HOME, NODOLL = (_ns[k] for k in ("img", "vid", "scenes", "write", "D", "HOME", "NODOLL"))

LEFT = "Every car faces LEFT and only ever moves to the LEFT, front first; no car rolls backward. "
NEAR = "The thing Torong touches is right in front of Torong's mouth, so Torong's neck keeps its normal length and never stretches longer. "

EPS = {}
# ---------------- 21화 삐뽀삐뽀 공룡 구조대 (탈것) ----------------
FIRE = "Chiqui's small ORANGE ride-on toy fire truck (just big enough for one friend sitting inside, a short white ladder on top, one round warm-YELLOW light on top (never red), chunky round wheels, no letters or logos)"
AMBU = "Roro's small YELLOW ride-on toy ambulance (just big enough for one friend sitting inside, a white heart sign on the side, one round warm-YELLOW light on top (never red), chunky round wheels, no letters, no cross sign)"
KITE = "one SKY-BLUE diamond-shaped kite with a short tail of exactly three little SKY-BLUE bows (no streamers, no other colors)"
KTREE = ("THE SAME kite tree in every scene: one big round leafy green tree on the sunny meadow, only a little taller than Torong's head, "
         "with " + KITE + " stuck in its top branches. ")
EPS["ep21"] = dict(
 title="21화. 삐뽀삐뽀 공룡 구조대! — 구조대 자동차", short="삐뽀삐뽀 공룡 구조대!", song_id="rescue", song_short="공룡 구조대",
 theme="탈것(소방차·구급차)과 돕는 마음. 피오 연이 나무에 걸려 구조대가 출동하지만 안 닿는다 → 키 큰 토롱이 입으로 쏙. 자동차는 친구 몸 색.",
 twist="사다리도, 점프도, 날갯짓도 안 닿았는데… 목이 긴 토롱이 살금살금 다가가 연을 쏙!",
 bau="목이 긴 공룡은 높은 잎도 냠냠!",
 lines=[("내레이션","슝슝, 연이 날아요.",""),("내레이션","앗! 연이 걸렸어요.",""),("치키","구조대 출동!",""),("모두","삐뽀삐뽀!",""),
        ("바우","조심조심 출발!",""),("내레이션","누가 연에 닿을까?","뒤에 3초 쉼"),("토롱","내가 해 볼게!",""),("모두","와아~","♻ 1화 15"),
        ("바우","목이 긴 공룡은 높은 잎도 냠냠!","바우 할아버지 상식"),("모두","구조대 최고!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("소방차 사다리 쭈욱","치키가 올려 봐도","안 닿아요 (어떡해!)"),("구급차 삐뽀삐뽀","크앙! 로로 폴짝","안 닿아요 (어떡해!)"),
         ("하늘 높이 슝슝","슝~ 피오가 당겨도","꼼짝 않아요 (어떡해!)"),("목이 쭈욱 토롱이","살금살금 다가가","연을 쏙! (쏙!)")],
 chorus="삐뽀삐뽀 공룡 구조대",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "삐뽀삐뽀 공룡 구조대 (출동!)", "친구가 부르면 달려가요", "치키치키 출동!"],
 scenes=scenes([
  ("연 날리기", "P", f"On a sunny meadow, {D['P']} flies happily, holding the string of {KITE} with the beak; the kite flies above.", "Exactly one kite.", False,
   "Pio flies in one slow circle holding the kite string; the kite flutters in the wind. The camera stays still."),
  ("앗! 연이 걸렸어요", "P", f"{KTREE}{D['P']} hovers below the tree looking up at the stuck kite with a worried face.", "Exactly one kite and one tree.", False,
   "Pio flaps gently in place and looks up, worried; the kite stays stuck in the branches the whole time."),
  ("구조대 출동!", "C", f"On a sunny meadow, {D['C']} sits inside {FIRE}, facing LEFT, raising one front paw high.", "", False,
   "Chiqui raises the paw and cheers; the round light on top blinks. The fire truck does not move."),
  ("삐뽀삐뽀!", "R", f"On a sunny meadow, {D['R']} sits inside {AMBU}, facing LEFT, smiling and cheering.", "", False,
   "Roro cheers; the round light on top blinks. The ambulance does not move."),
  ("조심조심 출발!", "B", f"On a sunny meadow, {D['B']} stands and waves one small PURPLE flag with a warm smile.", "Exactly one purple flag.", False,
   "Grandpa Bau waves the purple flag two times and nods. The camera stays still."),
  ("구조대가 간다", "CR", f"On a sunny meadow, {D['C']} drives {FIRE} and {D['R']} drives {AMBU} right behind it; both cars face LEFT on a little dirt path.", "Exactly two cars.", False,
   LEFT + "Both cars roll slowly to the LEFT along the path; the round lights blink. The camera stays still and both cars stay inside the frame."),
  ("소방차 사다리 쭈욱", "C", f"{KTREE}{D['C']} sits in {FIRE} parked under the tree; the short white ladder is raised up but its tip is still far below the kite.", "", False,
   "The ladder rises a little more but still does not reach the kite; Chiqui looks up and shakes the head. The kite stays stuck the whole time."),
  ("로로 폴짝", "R", f"{KTREE}{D['R']} stands next to {AMBU} under the tree and jumps up with both arms up; the kite is far above.", "", False,
   "Keep the whole start image exactly: the big leafy tree with the sky-blue kite STUCK in its top branches, and the yellow ambulance parked under the tree, stay visible in the same place for the whole video; the kite never floats free in the sky and has no long string. Roro stands next to the tree and hops three times reaching up toward the kite, but cannot reach it. The camera stays still: no zoom, no pan, no new background."),
  ("피오가 당겨도", "P", f"{KTREE}{D['P']} flies next to the stuck kite and holds its tail in the beak, pulling.", "", False,
   "Pio pulls the kite tail two times; the kite stays stuck in the branches and does not move."),
  ("누가 닿을까?", "CRP", f"{KTREE}Chiqui, Roro and Pio stand under the tree, looking up at the stuck kite, thinking with paws on their chins.", "", False,
   "The friends look up, then at each other, thinking. The kite stays stuck."),
  ("토롱이 왔다!", "CRTP", f"{KTREE}{D['T']} walks up to the tree; Torong's head is right next to the stuck kite. Chiqui, Roro and Pio look up at Torong, hopeful.", "", False,
   "Torong walks two slow steps closer to the tree and stops, looking at the kite next to the head; the friends look hopeful."),
  ("어떻게 할까?", "T", f"Close view of {D['T']} next to the leafy tree top, looking at the viewer with a gentle smile; the sky-blue kite is still STUCK in the leafy branches of the tree right next to Torong's head (it is not flying in the sky).", "", True,
   "Torong looks at the viewer and tilts the head once, smiling. The kite stays in the branches."),
  ("연을 쏙!", "TP", f"{KTREE}{D['T']} holds the kite gently in the mouth, taken from the branch right next to the head, and lowers the head toward {D['P']} hovering below.", "Exactly one kite.", False,
   NEAR + "Torong lowers the head slowly with the kite in the mouth; Pio takes the kite string with the beak and flaps happily. Now the kite is with Pio."),
  ("목이 긴 공룡은", "B", f"On a sunny meadow next to the big leafy tree, {D['B']} points up at the high leaves with one front paw, smiling wisely.", "", False,
   "Grandpa Bau points up at the leaves and nods. The camera stays still."),
  ("다시 연 날리기", "CRTP", f"On a sunny meadow, {D['P']} flies with the sky-blue kite again; Chiqui, Roro and Torong cheer below.", "Exactly one kite.", False,
   "Pio flies holding the kite string; the friends clap and cheer."),
  ("구조대 최고!", "BCRTP", f"All five friends stand in a row on the sunny meadow in front of {FIRE} and {AMBU} (both cars the same size as before, big enough for a friend to sit inside, both facing LEFT), facing the viewer with big smiles. Grandpa Bau, Chiqui and Roro each wave ONE front paw, Pio waves one wing, Torong tilts the long neck and head to one side.", "Exactly two cars.", False,
   "Grandpa Bau, Chiqui, Roro and Pio wave at the viewer; Torong sways the long neck side to side with all four feet on the ground; the round lights on the cars blink."),
 ]))

# ---------------- 22화 토닥토닥 모래성 (바닷가) ----------------
BEACH = "On a sunny sandy beach of the volcano island with soft turquoise waves, a few palm trees and the far volcano. "
SHELLS = "Chiqui's ORANGE shell, Roro's YELLOW shell, Torong's GREEN shell, Pio's SKY-BLUE shell"
BIG = ("one big sandcastle (THE SAME in S17 and S18): a wide sand wall with little square bumps on top, two round towers each with ONE small flag (left flag ORANGE, right flag YELLOW), "
       "a round arch door in the middle, and EXACTLY four shells in one row on the front: ORANGE, YELLOW, GREEN, SKY-BLUE (no pink, no purple, no white shells, no other shells)")
CASTLE = "one small round sandcastle (a big round sand mound with one round tower on top, smooth clay-like sand, no flags)"
CALM = "The sea is calm with only small low ripples at the shore; there is NO big wave anywhere in the picture. "
ROW = ("The shell windows sit in ONE straight horizontal row across the middle of the mound's FRONT face (the side facing the viewer), evenly spaced, never on the tower and never on the back or sides. "
       "The row order is fixed, left to right as seen by the viewer: 1st spot YELLOW, 2nd spot GREEN, 3rd spot SKY-BLUE, 4th spot ORANGE. Spots without a shell yet are plain smooth sand (no holes, no dents). Each shell is small (about the size of a friend\'s paw) with a little sand between shells. There is only ONE shell of each color in the whole picture. ")
EPS["ep22"] = dict(
 title="22화. 토닥토닥 모래성! — 바닷가 모래 놀이", short="토닥토닥 모래성!", song_id="sand", song_short="모래성 노래",
 theme="바닷가 모래 놀이, 하나~넷 세기, 무너져도 다시 하기. 조개는 친구 몸 색.",
 twist="조개 창문 넷까지 다 붙였는데 파도가 쏴아~ 모래성이 무너졌다! 괜찮아, 다시 더 크게!",
 bau="공룡 시대에도 조개가 살았단다!",
 lines=[("모두","바다다!",""),("바우","모래 놀이 하자!",""),("모두","좋아!","♻ 1화 07"),("치키","토닥토닥!",""),
        ("모두","모래성 완성!",""),("모두","앗! 파도다!",""),("내레이션","모래성은 어떻게 됐을까?","뒤에 3초 쉼"),("치키","괜찮아, 다시 하자!",""),
        ("바우","공룡 시대에도 조개가 살았단다!","바우 할아버지 상식"),("모두","모래성 최고!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("노란 조개 콕","크앙! 로로가 콕","창문 하나 (하나!)"),("초록 조개 콕","쭈욱~ 토롱이 콕","창문 둘 (둘!)"),
         ("하늘색 조개 콕","슝~ 피오가 콕","창문 셋 (셋!)"),("주황 조개 콕","치키도 콕","창문 넷 (넷!)")],
 chorus="토닥토닥 모래성",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "토닥토닥 모래성 (토닥토닥!)", "조개 콕콕 붙이고", "치키치키 완성!"],
 scenes=scenes([
  ("바다다!", "CRTP", BEACH + "Chiqui, Roro, Torong and Pio arrive on the sand and cheer at the sea.", "", False,
   "The friends cheer and bounce on the sand; small gentle waves roll in the background."),
  ("모래 놀이 하자!", "B", BEACH + f"{D['B']} stands on the sand holding one small PURPLE bucket, smiling.", "Exactly one purple bucket.", False,
   "Grandpa Bau lifts the purple bucket a little and nods. The camera stays still."),
  ("좋아!", "CRTP", BEACH + "Chiqui, Roro, Torong and Pio cheer on the sand.", "", False, "The friends cheer and nod happily."),
  ("토닥토닥", "C", BEACH + f"{D['C']} sits on the sand and pats a round sand mound with both front paws.", "", False,
   "Chiqui pats the sand mound three times; the mound grows a little rounder and stays."),
  ("영차 영차", "R", BEACH + f"{D['R']} pours sand from one small YELLOW bucket onto a round sand mound.", "", False,
   "Roro tips the yellow bucket; sand pours onto the mound and the mound gets a little taller and stays."),
  ("모래성 완성!", "CRTP", BEACH + f"Chiqui, Roro, Torong and Pio stand behind {CASTLE} on the sand, cheering. The castle is plain sand with no shells yet.", "Exactly one sandcastle.", False,
   "The friends cheer behind the sandcastle; the sandcastle stays the same."),
  ("노란 조개 창문", "R", BEACH + CALM + f"{D['R']} presses one YELLOW shell onto {CASTLE} like a little window. " + ROW + "Only the 1st spot (far left) has the YELLOW shell.", "Exactly one shell on the castle.", False,
   "Roro presses the yellow shell onto the castle; the shell stays stuck there. Roro claps."),
  ("초록 조개 창문", "T", BEACH + CALM + f"{D['T']} stands right next to {CASTLE} and bends the neck down to press one GREEN shell onto it with the mouth. " + ROW + "The 1st spot has the YELLOW shell and Torong is pressing the GREEN shell into the 2nd spot right next to it with the mouth; Torong holds nothing else (no leaf, no second shell).", "Exactly two shells on the castle.", False,
   NEAR + "Torong gently presses the green shell onto the castle with the mouth and lifts the head; the green shell stays there."),
  ("하늘색 조개 창문", "P", BEACH + CALM + f"{D['P']} presses one SKY-BLUE shell onto {CASTLE} with the beak. " + ROW + "YELLOW (1st) and GREEN (2nd) are already there. Pio stands on the RIGHT side of the sandcastle and presses the SKY-BLUE shell into the 3rd spot with the tip of the beak; the 4th spot (far right) is still plain sand.", "Exactly three shells on the castle.", False,
   "Pio presses the sky-blue shell onto the castle; it stays there. Pio flaps once happily."),
  ("주황 조개 창문", "C", BEACH + CALM + f"{D['C']} presses one ORANGE shell onto {CASTLE}. " + ROW + "YELLOW, GREEN and SKY-BLUE are already there; Chiqui stands on the RIGHT side of the sandcastle and presses the ORANGE shell with one front paw into the 4th spot on the far right, right next to Chiqui's paw, so the row is complete.", "Exactly four shells on the castle.", False,
   "Chiqui presses the orange shell on; all four shells stay on the castle. Chiqui cheers."),
  ("앗! 파도다!", "CRTP", BEACH + f"Chiqui, Roro, Torong and Pio stand next to {CASTLE} with four shell windows and look surprised at one big gentle wave rolling toward it. " + ROW + "All four spots are filled: YELLOW, GREEN, SKY-BLUE, ORANGE; no pink, purple or white shells.", "Exactly four shells on the castle.", False,
   "One big gentle wave rolls in toward the sandcastle; the friends step back, surprised."),
  ("모래성은 어떻게 됐을까?", "C", BEACH + f"Close view of {D['C']} looking at the viewer with a worried face, wet sand behind.", "", True,
   "Chiqui looks at the viewer and tilts the head. The camera stays still."),
  ("괜찮아, 다시 하자!", "CRTP", BEACH + f"Where the sandcastle was, there is now only a low flat wet sand bump with the four shells ({SHELLS}) lying on it. The friends look at it, then smile at each other.", "Exactly four shells.", False,
   "The friends sigh, then smile and nod to each other. The flat wet sand stays flat."),
  ("공룡 시대에도", "B", BEACH + f"{D['B']} holds one big PURPLE spiral shell and smiles wisely.", "Exactly one shell.", False,
   "Grandpa Bau holds up the purple shell and nods. The camera stays still."),
  ("다시 더 크게!", "CRTP", BEACH + f"Further up the beach, away from the waves, Chiqui, Roro, Torong and Pio build {BIG} together.", "Exactly one sandcastle and four shells.", False,
   "The friends pat the big sandcastle together; it stays standing with all four shells."),
  ("모래성 최고!", "BCRTP", BEACH + "All five friends stand behind " + BIG + ", facing the viewer and cheering. Grandpa Bau, Chiqui and Roro each wave ONE front paw, Pio waves one wing, Torong tilts the long neck and head to one side.", "Exactly one sandcastle.", False,
   "Grandpa Bau, Chiqui, Roro and Pio wave at the viewer; Torong sways the long neck side to side with all four feet on the sand; the sandcastle stays."),
 ]))

# ---------------- 23화 공룡 마을 운동회 ----------------
FIELD = ("On THE SAME sunny flat grass field in every scene, with one straight white chalk running track going from right to left, palm trees and the far volcano. ")
FINISH = "one finish line on the LEFT side of the track: two short light-wood posts with ONE cream-white ribbon stretched between them"
MEDALS = "Chiqui wears an ORANGE ribbon medal, Roro a YELLOW ribbon medal, Torong a GREEN ribbon medal, Pio a SKY-BLUE ribbon medal (each a simple round medal on a ribbon around the neck)"
EPS["ep23"] = dict(
 title="23화. 공룡 마을 운동회! — 같이 달려요", short="공룡 마을 운동회!", song_id="sports", song_short="운동회 노래",
 theme="운동회(달리기·공 굴리기·응원), 넘어진 친구 기다려 주기, 다 같이 결승선. 메달은 친구 몸 색.",
 twist="치키가 넘어질 뻔! 친구들이 멈춰서 기다려 주고 다 같이 결승선 통과 — 모두 1등!",
 bau="공룡도 친구랑 같이 다녔단다!",
 lines=[("모두","오늘은 운동회!",""),("바우","준비~ 출발!",""),("모두","영차 영차!",""),("치키","어이쿠!",""),
        ("내레이션","친구들은 어떻게 할까?","뒤에 3초 쉼"),("로로","같이 가자!",""),("모두","하나 둘, 하나 둘!",""),("모두","와아~","♻ 1화 15"),
        ("바우","공룡도 친구랑 같이 다녔단다!","바우 할아버지 상식"),("모두","모두 1등!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("깡총깡총 달리기","크앙! 로로가 쌩","영차 영차 (영차!)"),("데굴데굴 큰 공","쭈욱~ 토롱이 콩","영차 영차 (영차!)"),
         ("하늘 위로 휘익","슝~ 피오가 쌩","영차 영차 (영차!)"),("치키도 달려요","어이쿠 넘어질라 (괜찮아?)","같이 가자 (같이!)")],
 chorus="공룡 마을 운동회",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "공룡 마을 운동회 (운동회!)", "하나 둘 하나 둘", "치키치키 달려!"],
 scenes=scenes([
  ("오늘은 운동회!", "CRTP", FIELD + "Chiqui, Roro, Torong and Pio stand on the grass next to the track and cheer.", "", False, "The friends cheer and bounce on the spot."),
  ("준비~", "B", FIELD + f"{D['B']} stands next to the track holding up one small PURPLE flag, smiling.", "Exactly one purple flag.", False,
   "Grandpa Bau raises the purple flag high once and smiles. The camera stays still."),
  ("출발선", "CRTP", FIELD + "Chiqui, Roro, Torong and Pio stand in a row at the start line on the RIGHT side of the track, all facing LEFT, ready to go.", "", False,
   "The friends crouch a little, ready, and wiggle with excitement. They do not run yet."),
  ("출발!", "CRTP", FIELD + "Chiqui, Roro, Torong and Pio run along the track toward the LEFT, happy.", "", False,
   "Everyone runs a few steps to the LEFT and stays inside the frame. The camera stays still."),
  ("응원해요", "B", FIELD + f"{D['B']} cheers next to the track, waving the small PURPLE flag.", "", False,
   "Grandpa Bau waves the purple flag left and right and cheers."),
  ("열심히!", "C", FIELD + f"Side view of {D['C']} running along the track toward the LEFT with a determined smile.", "", True,
   "Chiqui runs in place toward the LEFT with quick little steps; the camera stays still."),
  ("로로 달리기", "R", FIELD + f"{D['R']} runs fast along the track toward the LEFT, smiling.", "", False,
   "Roro runs quickly toward the LEFT, hops once and roars happily; stays inside the frame."),
  ("토롱 큰 공 굴리기", "T", FIELD + f"{D['T']} walks along the track toward the LEFT, gently pushing one big GREEN ball with the nose; the ball is right in front of Torong's nose on the grass.", "Exactly one green ball.", False,
   NEAR + "Torong nudges the green ball with the nose; the ball rolls slowly to the LEFT and Torong follows with two slow steps."),
  ("피오 하늘 달리기", "P", FIELD + f"{D['P']} flies low above the track toward the LEFT with wings wide open.", "", False,
   "Pio flaps and glides to the LEFT, staying inside the frame. The camera stays still."),
  ("어이쿠!", "C", FIELD + f"{D['C']} has just tripped and sits softly on the grass of the track, surprised but not hurt, no tears.", "", False,
   "Chiqui wobbles and sits down softly on the grass, then blinks, surprised. Chiqui is not hurt."),
  ("기다려 줄게", "RTP", FIELD + "Roro, Torong and Pio have stopped on the track and turned back toward the RIGHT, smiling kindly and waiting.", "", False,
   "The friends turn around and wave gently to come along. Torong sways the neck; all four feet stay on the ground."),
  ("친구들은 어떻게 할까?", "C", FIELD + f"Close view of {D['C']} sitting on the grass, looking at the viewer hopefully.", "", True,
   "Chiqui looks at the viewer and tilts the head. The camera stays still."),
  ("다 같이 결승선", "CRTP", FIELD + f"Chiqui and Roro walk side by side holding paws, Pio flies next to them and Torong walks beside them, all toward {FINISH}, which is right in front of them.", "Exactly one ribbon.", False,
   "The friends walk together to the LEFT through the finish line; the cream-white ribbon breaks and falls down softly. Everyone cheers."),
  ("공룡도 친구랑", "B", FIELD + f"{D['B']} holds up four ribbon medals (ORANGE, YELLOW, GREEN, SKY-BLUE), smiling warmly.", "Exactly four medals.", False,
   "Grandpa Bau lifts the medals a little and nods warmly. The medals keep their colors."),
  ("모두 1등!", "CRTP", FIELD + f"Chiqui, Roro, Torong and Pio stand together at the finish line, cheering; {MEDALS}.", "Exactly four medals.", False,
   "The friends cheer and jump a little; each medal stays around its owner's neck."),
  ("운동회 최고!", "BCRTP", FIELD + f"All five friends stand in a row facing the viewer with big smiles; {MEDALS}. Grandpa Bau, Chiqui and Roro each wave ONE front paw, Pio waves one wing, Torong tilts the long neck and head to one side.", "", False,
   "Grandpa Bau, Chiqui, Roro and Pio wave at the viewer; Torong sways the long neck side to side with all four feet on the ground."),
 ]))

# ---------------- 24화 동글 네모 세모 (모양 블록) ----------------
MAT = ("On THE SAME play mat in every scene: one ROUND plain soft cream play mat with a thin pale-yellow rim and NO dots or patterns, on the sunny meadow. "
       "The ONLY toy blocks in the whole episode are these four, always exactly this shape and color: one YELLOW square block (a chunky flat-faced cube), "
       "one tall GREEN rectangle block (a plain smooth upright box twice as tall as the yellow square, with NO door lines, NO knob and NO rounded top), "
       "one SKY-BLUE circle block (a flat round disc, solid, not a ring), and one ORANGE triangle block (a flat triangle prism). "
       "NO other blocks anywhere: no blue cube, no yellow cylinder, no green arch, no red ball, no other toys. ")
BLK = "smooth chunky clay toy blocks with no letters, no numbers and no pictures"
HOUSE = ("a little block house on the mat: the YELLOW square block as the wall, the tall plain GREEN rectangle block (no knob, no door lines, twice as tall as the yellow square) standing right next to it SIDE BY SIDE on the same line (not behind it) as the door, "
         "and one SKY-BLUE circle block as a round window on the yellow wall")
DONE = ("the finished block house exactly like this: the YELLOW square block stands on the mat with the SKY-BLUE circle pressed flat onto its FRONT face as a round window (the circle is NOT on top), "
        "the tall GREEN rectangle stands on the mat right next to it as the door, and the ORANGE triangle lies on top across both as the roof")
HAT = ("Chiqui wears the ORANGE triangle block on top of the head like a little hat: a small FLAT triangle toy block with straight sharp edges, "
       "about as wide as the yellow square block, sitting ABOVE the frill on top of the head; it is clearly a separate toy block, not part of the frill or a horn, and it is not tall or cone-shaped")
EPS["ep24"] = dict(
 title="24화. 동글 네모 세모! — 모양 블록 집 짓기", short="동글 네모 세모!", song_id="shape", song_short="모양 노래",
 theme="모양(동그라미·네모·세모) 이름, 블록 쌓기. 블록은 친구 몸 색.",
 twist="지붕이 될 세모가 없다! 어디 있을까? …치키 머리 위에 모자처럼 쏙 (처음부터 쓰고 있었어요).",
 bau="치키 뿔은 세 개! 하나 둘 셋!",
 lines=[("치키","세모 모자!",""),("바우","블록 놀이 하자!",""),("모두","좋아!","♻ 1화 07"),("치키","집을 짓자!",""),
        ("모두","어? 세모가 없다!",""),("내레이션","세모는 어디 있을까?","뒤에 3초 쉼"),("모두","치키 머리 위에!",""),("모두","하하하!","♻ 3화 11"),
        ("바우","치키 뿔은 세 개! 하나 둘 셋!","바우 할아버지 상식"),("모두","우리 집 완성!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("네모 네모 벽","크앙! 로로가 쿵","노란 네모 (네모!)"),("길쭉 네모 문","쭈욱~ 토롱이 쏙","초록 네모 (네모!)"),
         ("동글동글 창문","슝~ 피오가 콕","하늘색 동그라미 (동그라미!)"),("뾰족 세모 지붕","어디 있을까? (어디 있지?)","세모 세모 (세모!)")],
 chorus="동글 네모 세모",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "동글 네모 세모 (모양!)", "모양 블록 쌓아요", "치키치키 뚝딱!"],
 scenes=scenes([
  ("세모 모자!", "C", MAT + f"{D['C']} holds one ORANGE triangle block ({BLK}) on top of the head like a little hat and giggles.", "Exactly one triangle block.", False,
   "Chiqui puts the orange triangle on the head and giggles; the triangle stays on the head."),
  ("블록 놀이 하자!", "B", MAT + f"{D['B']} sits on the mat next to three {BLK}: one YELLOW square, one tall GREEN rectangle, one SKY-BLUE circle. No triangle.", "Exactly three blocks.", False,
   "Grandpa Bau points at the blocks and smiles. The blocks do not move."),
  ("좋아!", "CRTP", MAT + f"Chiqui, Roro, Torong and Pio cheer on the mat; {HAT}.", "", False, "The friends cheer; the triangle stays on Chiqui's head."),
  ("블록이 가득", "", MAT + f"Close view of three {BLK} on the mat: one YELLOW square, one tall GREEN rectangle, one SKY-BLUE circle. No triangle anywhere.", "Exactly three blocks.", True,
   "Soft light on the blocks; nothing moves."),
  ("무엇을 지을까?", "CRTP", MAT + f"Chiqui, Roro, Torong and Pio sit around the three blocks, thinking with paws on their chins; {HAT}.", "", False,
   "The friends look at the blocks, thinking; the triangle stays on Chiqui's head."),
  ("집을 짓자!", "C", MAT + f"{D['C']} raises one front paw high, excited; {HAT}.", "", False, "Chiqui raises the paw and cheers; the triangle stays on the head."),
  ("노란 네모 벽", "R", MAT + f"{D['R']} sets one YELLOW square block upright on the mat like a little wall.", "Exactly one block on the mat.", False,
   "Roro sets the yellow square down with a little 'thump' and claps; the square stays standing."),
  ("초록 네모 문", "T", MAT + f"{D['T']} stands right next to the yellow square block and bends the neck down to set one tall GREEN rectangle block next to it with the mouth, like a door.", "Exactly two blocks.", False,
   NEAR + "Torong gently sets the green rectangle next to the yellow square and lifts the head; both blocks stay standing."),
  ("하늘색 동그라미 창문", "P", MAT + f"{D['P']} presses one SKY-BLUE circle block onto the yellow square with the beak, like a round window; the tall green door stands next to it.", "Exactly three blocks.", False,
   "Pio presses the sky-blue circle on; it stays there. Pio flaps once happily."),
  ("지붕이 없네?", "CRTP", MAT + f"Chiqui, Roro, Torong and Pio look at {HOUSE}; the block house has NO roof yet, puzzled; {HAT}.", "", False,
   "The friends tilt their heads at the house; the triangle stays on Chiqui's head."),
  ("세모가 없다!", "CRTP", MAT + f"Chiqui, Roro, Torong and Pio look around the mat, searching left and right; {HAT}; {HOUSE} with no roof is next to them.", "", False,
   "The friends look left and right, searching. Nobody looks at Chiqui's head yet."),
  ("세모는 어디 있을까?", "C", MAT + f"Close view of {D['C']} looking at the viewer innocently; {HAT}. Behind Chiqui, a little out of focus, stands {HOUSE}, built but with NO roof yet; no loose blocks on the mat.", "", True,
   "Chiqui looks at the viewer and tilts the head; the triangle stays on the head."),
  ("치키 머리 위에!", "CRTP", MAT + f"Roro, Torong and Pio point at Chiqui's head and laugh; Chiqui touches the ORANGE triangle block on top of the head, surprised and laughing. Next to them stands {HOUSE}, built but with NO roof yet; no loose blocks on the mat.", "", False,
   "Everyone laughs; Chiqui touches the triangle and laughs too. The triangle stays on the head."),
  ("치키 뿔은 세 개", "B", MAT + f"{D['B']} sits on the mat and smiles wisely, holding up one front paw.", "", False,
   "Grandpa Bau nods and chuckles. The camera stays still."),
  ("지붕 쏙!", "C", MAT + f"{D['C']} puts the ORANGE triangle block on top of {HOUSE}; now the house has an orange triangle roof.", "Exactly four blocks.", False,
   "Chiqui sets the orange triangle on top as the roof; it stays there. Chiqui claps."),
  ("우리 집 완성!", "BCRTP", MAT + f"All five friends sit around {DONE}, facing the viewer and cheering. Grandpa Bau, Chiqui and Roro each wave ONE front paw, Pio waves one wing, Torong tilts the long neck and head to one side.", "Exactly four blocks.", False,
   "Grandpa Bau, Chiqui, Roro and Pio wave at the viewer; Torong sways the long neck side to side with all four feet on the ground; the block house stays standing."),
 ]))

# ---------------- 25화 반짝반짝 크리스마스 ----------------
SNOWV = ("In the snowy volcano-island village with soft white snow on the ground and palm trees, gently falling snowflakes. "
         "The palm trees are plain with only snow on them: NO string lights, NO hanging stars, NO ornaments on any palm tree or house; the only Christmas decorations are the ones named in this scene. ")
XTREE = ("THE SAME Christmas tree in every scene: one small smooth cone-shaped green clay pine tree standing alone on the snow, "
         "a little shorter than Torong's head" + ". It is always a green PINE (fir) tree, NEVER a palm tree. The tree has three rounded tiers and NO snow on its branches. The ornament spots NEVER change (as seen by the viewer): the ORANGE ball always hangs on the RIGHT side of the MIDDLE tier, the YELLOW ball always hangs on the LEFT side of the BOTTOM tier, the SKY-BLUE ball always hangs on the LEFT side of the TOP tier, and the white star goes on the very top only after Torong puts it there. Only the ornaments named in this scene are on the tree: a ball or star that is not named is NOT on the tree")
DECO = ("THE SAME small green PINE Christmas tree (never a palm tree, no palm tree has lights), decorated with EXACTLY three round balls (one ORANGE, one YELLOW, one SKY-BLUE), "
        "one small WHITE star on the very top (white, not yellow) and tiny warm little lights; no other balls, ornaments, ribbons or garlands. The tree has three rounded tiers and NO snow on its branches. The ornament spots NEVER change (as seen by the viewer): the ORANGE ball always hangs on the RIGHT side of the MIDDLE tier, the YELLOW ball always hangs on the LEFT side of the BOTTOM tier, the SKY-BLUE ball always hangs on the LEFT side of the TOP tier, and the white star sits on the very top. The three balls are big and clearly visible.")
SCARF = "Chiqui wears an ORANGE scarf, Roro a YELLOW scarf, Torong a GREEN scarf, Pio a SKY-BLUE scarf"
GIFTS = "five small wrapped gift boxes under the tree: ORANGE, YELLOW, GREEN, SKY-BLUE and PURPLE, each with a white ribbon"
EPS["ep25"] = dict(
 title="25화. 반짝반짝 크리스마스! — 트리 꾸미기", short="반짝반짝 크리스마스!", song_id="xmas", song_short="크리스마스 노래",
 theme="크리스마스 트리 꾸미기, 고마운 마음 나누기. 방울·선물은 친구 몸 색, 별은 하얀 별.",
 twist="트리 밑 선물 다섯 개, 그런데 보라 선물은 누구 거지? …친구들이 준비한 할아버지 선물!",
 bau="공룡 시대에도 소나무가 있었단다!",
 lines=[("치키","와, 트리다!",""),("바우","다 같이 꾸미자!",""),("모두","좋아!","♻ 1화 07"),("내레이션","반짝반짝 방울.",""),
        ("모두","불을 켜요, 하나 둘 셋!",""),("모두","와아~","♻ 1화 15"),("치키","선물이다!",""),("내레이션","보라 선물은 누구 거지?","뒤에 3초 쉼"),
        ("모두","할아버지 거예요!",""),("바우","고맙구나, 허허!",""),("바우","공룡 시대에도 소나무가 있었단다!","바우 할아버지 상식"),
        ("모두","메리 크리스마스!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("노란 방울 달랑","크앙! 로로가 달랑","반짝반짝 (반짝!)"),("하얀 별은 맨 위에","쭈욱~ 토롱이 쏙","반짝반짝 (반짝!)"),
         ("하늘색 방울 대롱","슝~ 피오가 대롱","반짝반짝 (반짝!)"),("다 같이 불을 켜요","하나 둘 셋! (셋!)","반짝반짝 (반짝!)")],
 chorus="반짝반짝 크리스마스",
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "반짝반짝 크리스마스 (반짝!)", "다 같이 트리 꾸며요", "치키치키 메리!"],
 scenes=scenes([
  ("와, 트리다!", "C", SNOWV + f"{D['C']} wearing an ORANGE scarf looks at {XTREE}, with no decorations yet, amazed.", "", False,
   "Chiqui looks up at the tree and claps; snowflakes fall gently."),
  ("다 같이 꾸미자!", "B", SNOWV + f"{D['B']} (no scarf yet: Grandpa Bau's purple scarf is the gift later) holds one small PURPLE basket with round ornament balls (ORANGE, YELLOW, SKY-BLUE) and one small white star.", "", False,
   "Grandpa Bau lifts the basket a little and smiles. The camera stays still."),
  ("좋아!", "CRTP", SNOWV + f"Chiqui, Roro, Torong and Pio cheer in the snow; {SCARF}.", "", False, "The friends cheer and bounce in the snow."),
  ("반짝반짝 방울", "", SNOWV + "Close view of a small PURPLE basket on the snow holding three shiny round ornament balls (ORANGE, YELLOW, SKY-BLUE) and one small white star.", "Exactly three balls and one star.", True,
   "The ornaments shine softly; snowflakes fall; nothing else moves."),
  ("트리 앞에 모여요", "CRTP", SNOWV + f"Chiqui, Roro, Torong and Pio stand around {XTREE}, which has no decorations yet; {SCARF}.", "", False,
   "The friends look at the tree and smile at each other."),
  ("주황 방울 먼저", "C", SNOWV + f"{D['C']} wearing an ORANGE scarf stands on the RIGHT side of {XTREE} and hangs one shiny ORANGE ball on the RIGHT side of the middle tier; it is the first and only ornament on the tree: NO other balls yet. The very top of the tree is EMPTY (just a bare green tip): there is NO star on the tree and NO star anywhere in the picture.", "Exactly one ball on the tree.", False,
   "Chiqui hangs the orange ball on the branch; it stays there and swings a little. Chiqui cheers."),
  ("노란 방울", "R", SNOWV + f"{D['R']} wearing a YELLOW scarf hangs one shiny YELLOW ball on {XTREE}; one ORANGE ball already hangs on the tree. The very top of the tree is EMPTY (just a bare green tip): NO star on the tree and NO star anywhere in the picture.", "Exactly two balls and NO star on the tree.", False,
   "Roro hangs the yellow ball on the branch; it stays there and swings a little. Roro claps."),
  ("하얀 별은 맨 위에", "T", SNOWV + f"{D['T']} wearing a GREEN scarf stands right next to {XTREE} and gently sets one small white star on the very top with the mouth; only TWO balls hang on the tree: the ORANGE ball (right side of the middle tier) and the YELLOW ball (left side of the bottom tier). There is NO sky-blue ball yet: the left side of the top tier is empty.", "Exactly two balls and one star on the tree; no sky-blue ball.", False,
   NEAR + "Torong sets the white star on the treetop and lifts the head; the star stays on the top."),
  ("하늘색 방울", "P", SNOWV + f"{D['P']} wearing a SKY-BLUE scarf flies next to {XTREE} and hangs one shiny SKY-BLUE ball on a branch with the beak; now the tree has an ORANGE ball, a YELLOW ball, a SKY-BLUE ball and a white star on top.", "Exactly three balls and one star.", False,
   "Pio hangs the sky-blue ball; it stays there. Pio flaps happily."),
  ("불을 켜요!", "CRTP", SNOWV + f"Chiqui, Roro, Torong and Pio stand around {DECO}; the tiny lights glow; {SCARF}.", "", False,
   "The tiny lights on the tree turn on and twinkle; the friends cheer."),
  ("선물이다!", "CRTP", SNOWV + f"Chiqui, Roro, Torong and Pio look at {GIFTS} of {DECO}, surprised and happy; {SCARF}.", "Exactly five gift boxes.", False,
   "The friends gasp happily and point at the gifts. The boxes stay closed."),
  ("보라 선물은 누구 거지?", "C", SNOWV + f"Close view of {D['C']} wearing an ORANGE scarf, holding one small wrapped PURPLE gift box with a white ribbon, looking at the viewer curiously.", "Exactly one purple box.", True,
   "Chiqui looks at the box, then at the viewer, and tilts the head."),
  ("할아버지 거예요!", "BCRTP", SNOWV + f"Chiqui pushes the PURPLE gift box across the snow to {D['B']}; the box sits on the snow right in front of Grandpa Bau's face. Grandpa Bau stands low on EXACTLY FOUR short legs (two front legs, two back legs), all four feet flat on the snow, and looks down at the box with a big warm smile; Grandpa Bau does NOT hold the box and does NOT lift any leg. Roro, Torong and Pio cheer next to them; {SCARF}; Grandpa Bau has NO scarf yet; {DECO} is behind.", "Exactly one purple box. Grandpa Bau has exactly four legs.", False,
   "Grandpa Bau bends the head down and gently nuzzles the purple box on the snow with the nose, smiling warmly with closed eyes; all four of Grandpa Bau's feet stay flat on the snow and Grandpa Bau never grows an extra leg; the friends clap."),
  ("공룡 시대에도", "B", SNOWV + f"{D['B']} stands next to {DECO}, with a soft new PURPLE knitted scarf from the gift around the neck, smiling wisely.", "", False,
   "Grandpa Bau touches the new purple scarf and nods. The camera stays still."),
  ("우리 선물도!", "CRTP", SNOWV + f"{SCARF}. Chiqui, Roro, Torong and Pio each open their own small gift box (ORANGE, YELLOW, GREEN, SKY-BLUE); inside each is one small jingle bell of the same color. Torong's GREEN box lies open on the snow right in front of Torong's mouth.", "Exactly four open boxes and four bells.", False,
   "Chiqui, Roro and Pio lift their bells and ring them; Torong nudges the green bell gently with the nose so it rings (front legs on the ground). Everyone smiles."),
  ("메리 크리스마스!", "BCRTP", SNOWV + f"All five friends stand around {DECO}, facing the viewer with big smiles; {SCARF}, Grandpa Bau a PURPLE scarf. Grandpa Bau, Chiqui and Roro each wave ONE front paw, Pio waves one wing, Torong tilts the long neck and head to one side.", "", False,
   "Grandpa Bau, Chiqui, Roro and Pio wave at the viewer; Torong sways the long neck side to side with all four feet on the snow; the tree lights twinkle."),
 ]))

for ep, e in EPS.items():
    write(ep, e)
