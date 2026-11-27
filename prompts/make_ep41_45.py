"""41~45화 대본·가사·장면 프롬프트 (2026-11-26).
인기 유아 채널(핑크퐁·베베핀·뽀로로·코코멜론)에서 아이들이 좋아하는 '소재'만 참고했다
(소리 흉내 놀이, 감기 예절, 멈춤 춤, 나눠 먹기, 공룡 화석). 이야기·노래·그림은 모두 새로 만든다.
도우미(img·vid·scenes·write·CHEER·WAVE·BAU·MEADOW)는 make_ep26_40.py 것을 그대로 쓴다.
26~40화에서 배운 것: 반복 소품은 한 문장으로 고정(자리·색·개수), 토롱·바우는 물건을 들지 않는다,
땅에 선을 그리지 않는다, 탈것 없음, 카메라 고정, 동작은 결과까지 적는다, 바우는 손을 흔들지 않는다.
사용법: python3 -I prompts/make_ep41_45.py
"""
from pathlib import Path
import collections as _col, json as _json

_p = Path(__file__).resolve().parent / "make_ep26_40.py"
_src = _p.read_text(encoding="utf-8")
_ns = {"__file__": str(_p)}
exec(_src.split("\nEPS = {}")[0], _ns)
img, vid, scenes, write, D, HOME, NODOLL, NEAR, MEADOW, CHEER, WAVE, BAU = (
    _ns[k] for k in ("img", "vid", "scenes", "write", "D", "HOME", "NODOLL", "NEAR", "MEADOW", "CHEER", "WAVE", "BAU"))
BED26 = _src.split('BED26 = (')[1].split('\nEPS["ep26"]')[0]
BED26 = eval("(" + BED26)  # 26화와 같은 침실(밝은 아침)

EPS = {}

# ---------------- 41화 누구 소리일까? (소리 흉내 놀이) ----------------
BUSH = ("THE SAME one big round green bush in the MIDDLE of the meadow in every scene, as tall as Grandpa Bau, "
        "with small cream flowers on top; nothing is hidden in front of it")
EPS["ep41"] = dict(
 title="41화. 누구 소리일까? — 소리 흉내 놀이", short="누구 소리일까?", song_id="sound", song_short="소리 노래",
 theme="소리 듣고 누구인지 맞히기, 소리 흉내 내기(크앙·쿵쿵·슝·허허). 화면 밖 아이가 먼저 맞히게 쉬어 준다.",
 twist="덤불 뒤에서 \"크앙!\" 큰 소리… 무서운 공룡일까? 짠! 하나도 안 무서운 로로였어요. 마지막엔 \"치키치키!\" 소리, 누구게?",
 bau="공룡들도 소리로 친구를 불렀단다!",
 lines=[("치키","소리 놀이 하자!",""),("모두","좋아!","♻ 1화 07"),("내레이션","쉿, 잘 들어 봐요.",""),
        ("내레이션","누구 소리일까?","뒤에 3초 쉼"),("모두","로로다!",""),("내레이션","쿵쿵쿵, 누구일까?","뒤에 3초 쉼"),("모두","토롱이다!",""),
        ("내레이션","치키치키! 누구일까?","뒤에 3초 쉼"),("모두","치키다!",""),
        ("바우","공룡들도 소리로 친구를 불렀단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("덤불 뒤에 크앙 크앙","누구 소리일까? (누구?)","로로 소리 (크앙!)"),("땅이 쿵쿵 흔들흔들","누구 소리일까? (누구?)","토롱 소리 (쿵쿵!)"),
         ("바람이 슝슝 불어요","누구 소리일까? (누구?)","피오 소리 (슝슝!)"),("허허허 웃음소리","누구 소리일까? (누구?)","할아버지 (허허!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "귀를 쫑긋 (쫑긋!)", "누구 소리일까요?", "치키치키 맞혀 봐!"],
 scenes=scenes([
  ("소리 놀이 하자!", "C", MEADOW + f"{D['C']} stands next to {BUSH}, holding one front paw next to the ear, smiling excitedly.", "Exactly one bush.", False, "Chiqui cups one paw next to the ear and bounces once. The bush stays still."),
  CHEER(MEADOW),
  ("쉿, 잘 들어 봐요", "C", MEADOW + f"Close view of {D['C']} with eyes closed and one front paw next to the ear, listening carefully; {BUSH} behind.", "", True, "Chiqui listens with closed eyes, tilting the head slowly. The camera stays still."),
  ("덤불이 흔들흔들", "", MEADOW + f"{BUSH}; its leaves shake a little as if someone is hiding behind it. No characters are visible.", "Exactly one bush. Nobody is visible.", False, "The bush shakes gently two times; nobody comes out. No characters, animals or creatures appear."),
  ("누구 소리일까?", "CTP", MEADOW + f"Chiqui, Torong and Pio stand on the LEFT side of {BUSH}, all three with the heads turned toward the bush and curious wondering faces (faces turned to the bush, NOT looking at the viewer); Chiqui holds one front paw next to the ear; Torong stands on all four feet.", "", False, "The friends lean toward the bush and look at each other. Nobody else appears."),
  ("크앙!", "R", MEADOW + f"{D['R']} pops out from the RIGHT side of {BUSH} with both short arms up and a big friendly open-mouth roar face, not scary at all.", "Only one Roro appears.", False, "Roro jumps out from behind the bush, roars a friendly roar with both arms up, then laughs. Only one Roro appears."),
  ("하나도 안 무서워", "CRTP", MEADOW + f"Chiqui, Roro, Torong and Pio laugh together next to {BUSH}; Roro scratches the head shyly.", "", False, "Everyone laughs; Roro scratches the head once. The camera stays still."),
  ("쿵쿵쿵", "", MEADOW + f"{BUSH}; behind it the top of one long green neck and head are just visible above the leaves, the grass trembles a little. No other characters.", "Exactly one bush. Only the top of one long green neck is visible.", False,
   "The long green neck behind the bush bobs up and down two times; small leaves shake. Nothing else appears."),
  ("토롱이다!", "T", MEADOW + f"{D['T']} steps out from the RIGHT side of {BUSH} on all four feet with a big gentle smile.", "Only one Torong appears.", False, "Torong takes two slow steps forward and tilts the long neck with a smile; all four feet stay on the ground."),
  ("슝슝", "P", MEADOW + f"{D['P']} swoops over {BUSH} in the sky, wings wide open, a little wind bending the grass.", "", False, "Pio swoops once over the bush from LEFT to RIGHT and lands softly on the grass. The camera stays still."),
  ("허허허", "B", MEADOW + f"{D['B']} peeks out from the RIGHT side of {BUSH}, laughing warmly with eyes squeezed into happy curves; all four feet on the ground.", "Only one Grandpa Bau appears.", False,
   "Grandpa Bau laughs, nodding the head three times; all four feet stay on the ground."),
  ("치키치키! 누구?", "", MEADOW + f"{BUSH}; three small cream horns and the top of one ORANGE frill with yellow spots are just visible above the leaves. No other characters.", "Exactly one bush. Only the top of one orange frilled head is visible.", True,
   "The orange frill behind the bush wiggles left and right two times. Nothing else appears."),
  ("치키다!", "C", MEADOW + f"{D['C']} jumps out from the RIGHT side of {BUSH} with both front paws up, laughing.", "Only one Chiqui appears.", False, "Chiqui jumps out once with paws up and laughs. Only one Chiqui appears."),
  BAU(MEADOW, "소리로 친구를 불렀단다", f"stands next to {BUSH}, smiling wisely, one ear turned to listen."),
  ("다 같이 소리 내요", "BCRTP", MEADOW + f"All five friends stand in a row in front of {BUSH}, all with mouths open, making happy sounds together; Grandpa Bau and Torong stand on all four feet.", "", False,
   "Everyone opens the mouth and calls out happily two times; Pio flaps; Torong sways the neck; Grandpa Bau nods. The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 42화 콜록콜록 에취! (감기 예절) ----------------
SCARF42 = "Chiqui wears one soft ORANGE knitted scarf around the neck"
EPS["ep42"] = dict(
 title="42화. 콜록콜록 에취! — 감기 조심", short="콜록콜록 에취!", song_id="achoo", song_short="에취 노래",
 theme="기침·재채기는 팔꿈치로 가리기, 손 씻기, 따뜻한 물 마시기, 푹 자기. 아프면 쉬어도 괜찮아요.",
 twist="치키가 재채기를 손바닥에 \"에취!\" 하려는 순간, 친구들과 화면 밖 아이가 \"팔꿈치!\" 알려 주면 팔꿈치로 쏙!",
 bau="공룡도 푹 자고 나면 튼튼해졌단다!",
 lines=[("치키","콜록콜록…",""),("로로","치키야, 괜찮아?",""),("바우","감기에 걸렸구나.",""),("치키","에… 에…",""),
        ("내레이션","어디로 가려야 할까?","뒤에 3초 쉼"),("모두","팔꿈치!",""),("치키","에취!",""),("모두","손 씻기!",""),
        ("바우","공룡도 푹 자고 나면 튼튼해졌단다!","바우 할아버지 상식"),("치키","다 나았다!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("콜록콜록 기침이 나면","크앙! 로로처럼","팔꿈치로 쏙 (쏙!)"),("에취 에취 재채기 나면","슝~ 피오처럼","날개로 쏙 (쏙!)"),
         ("밖에 놀다 들어오면","보글보글 비누로","손을 싹싹 (싹싹!)"),("따뜻한 물 호록호록","이불 덮고 쿨쿨","푹 자요 (쿨쿨!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "콜록콜록 에취! (에취!)", "팔꿈치로 가려요", "치키치키 튼튼!"],
 scenes=scenes([
  ("콜록콜록", "C", MEADOW + f"{D['C']} stands on the meadow coughing into the bend of one front leg (the elbow), eyes squeezed, a little tired; {SCARF42}.", "", False,
   "Chiqui coughs two times into the bend of the front leg, then sniffles. The scarf stays on. The camera stays still."),
  ("치키야, 괜찮아?", "CRP", MEADOW + f"Roro and Pio stand next to {D['C']} with worried kind faces; {SCARF42}.", "", False, "Roro and Pio lean in gently toward Chiqui; Chiqui sniffles and nods. The camera stays still."),
  ("감기에 걸렸구나", "BC", MEADOW + f"{D['B']} stands on all four feet next to {D['C']}, looking kindly at Chiqui; {SCARF42}.", "", False,
   "Grandpa Bau nods slowly and smiles kindly; Chiqui sniffles once. Grandpa Bau's four feet stay on the ground."),
  ("에… 에…", "C", MEADOW + f"Close view of {D['C']} about to sneeze, head tilted back, eyes half closed, nose wrinkled, one open front paw raised in front of the mouth (palm toward the mouth); {SCARF42}.", "", True,
   "Chiqui tilts the head back two times, about to sneeze, but does not sneeze yet. The camera stays still."),
  ("팔꿈치!", "RTP", MEADOW + "Roro, Torong and Pio call out together; Roro bends one short arm and points at the own elbow, Pio folds one wing in front of the beak, Torong nods.", "", False,
   "Roro taps the own elbow two times; Pio folds one wing in front of the beak; Torong nods with all four feet on the ground. The camera stays still."),
  ("에취!", "C", MEADOW + f"{D['C']} sneezes into the bend of one front leg (the elbow covers the nose and mouth), eyes squeezed shut; {SCARF42}.", "", False,
   "Chiqui sneezes once into the elbow; the elbow stays in front of the nose and mouth during the sneeze; then Chiqui lowers the leg and smiles proudly."),
  ("로로는 팔이 짧아", "R", MEADOW + f"{D['R']} tries to cough into the bend of one SHORT arm, stretching the neck down to reach it, a funny face.", "", False,
   "Roro bends the head down to the short arm and coughs into the elbow once, then laughs. The camera stays still."),
  ("피오는 날개로", "P", MEADOW + f"{D['P']} folds one wing in front of the beak and coughs into it.", "", False, "Pio coughs once into the folded wing, then opens the wings and smiles."),
  ("손을 싹싹", "C", MEADOW + f"{D['C']} washes both front paws at one small round grey stone basin of clear water with ORANGE soap bubbles; {SCARF42}.", "Exactly one basin.", False,
   "Chiqui rubs the paws together three times; orange bubbles grow; then Chiqui rinses the paws in the water and smiles."),
  ("토롱도 싹싹", "T", MEADOW + f"{D['T']} bends the neck down and dips the nose into one small round grey stone basin of clear water right in front of the mouth, with soft GREEN soap bubbles on the water.", "Exactly one basin.", False,
   NEAR + "Torong dips the nose into the green bubbles two times and lifts the head with a smile; all four feet stay on the ground."),
  ("따뜻한 물 호록", "BC", HOME + BED26 + f"{D['C']} sits in the bed with the blanket on the lap and sips from one small ORANGE cup held in both front paws; {D['B']} stands on all four feet next to the bed; {SCARF42}.", "Exactly one cup.", False,
   "Chiqui sips from the orange cup two times and smiles; Grandpa Bau nods. Grandpa Bau's four feet stay on the floor. It stays a bright sunny day: the window stays bright."),
  ("이불 덮고 쿨쿨", "C", HOME + BED26 + f"{D['C']} sleeps peacefully in the bed under the blanket, eyes closed, smiling; the orange scarf is folded on the tree-stump side table.", "", False,
   "Chiqui sleeps, breathing slowly; the blanket rises and falls gently. It stays a bright sunny day: the window stays bright, the room never gets dark."),
  ("다 나았다!", "C", HOME + BED26 + f"{D['C']} sits up in the bed with both front paws raised high, full of energy, a big happy smile; no scarf.", "", False,
   "Chiqui throws both front paws up and bounces once in the bed, cheering. It stays a bright sunny morning: the window stays bright."),
  BAU(MEADOW, "푹 자고 나면", "stands on the meadow in the morning sun, smiling wisely, eyes closed for a moment as if remembering a good sleep."),
  ("다시 신나게!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio play tag together on the meadow, laughing; no scarf.", "", False, "The friends run around in a small circle and laugh. The camera stays still and everyone stays inside the frame."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 43화 멈춰라 얼음! (멈춤 춤 놀이) ----------------
DRUM43 = "one big round PURPLE drum standing on the grass in front of Grandpa Bau, right next to his tail club"
EPS["ep43"] = dict(
 title="43화. 멈춰라 얼음! — 멈춤 춤 놀이", short="멈춰라 얼음!", song_id="freeze", song_short="얼음 춤",
 theme="음악이 나오면 춤추고, 멈추면 '얼음!'. 듣고 몸을 멈추는 자기 조절 놀이. 화면 밖 아이도 같이 멈춰요.",
 twist="다들 얼음! 했는데 치키만 계속 빙글빙글… 다음엔 치키가 제일 먼저 꽁꽁 얼음! 화면 밖 친구도 얼음!",
 bau="공룡도 꼼짝 않고 숨어서 몸을 지켰단다!",
 lines=[("바우","얼음 춤 놀이 하자!",""),("모두","좋아!","♻ 1화 07"),("바우","음악이 멈추면?",""),("모두","얼음!",""),
        ("내레이션","치키는 왜 계속 춤출까?","뒤에 2초 쉼"),("모두","하하하!","♻ 3화 11"),("치키","이번엔 꽁꽁!",""),
        ("내레이션","우리 친구도 얼음!","뒤에 3초 쉼"),("바우","공룡도 꼼짝 않고 숨어서 몸을 지켰단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("둥둥 북이 울리면","크앙! 로로는 엉덩이","씰룩씰룩 (씰룩!)"),("둥둥 북이 울리면","쭈욱~ 토롱은 목을","흔들흔들 (흔들!)"),
         ("둥둥 북이 울리면","슝~ 피오는 날개","팔랑팔랑 (팔랑!)"),("북소리가 뚝 멈추면","모두 다 같이 (얼음!)","꼼짝 마 (꽁꽁!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "춤추다가 멈춰라 (얼음!)", "귀 기울여 들어요", "치키치키 얼음!"],
 scenes=scenes([
  ("얼음 춤 놀이", "B", MEADOW + f"{D['B']} stands on all four feet behind {DRUM43}, smiling playfully.", "Exactly one drum.", False,
   "Grandpa Bau taps the purple drum two times with the tail club; all four feet stay on the ground. The camera stays still."),
  CHEER(MEADOW),
  ("음악이 멈추면?", "B", MEADOW + f"Close view of {D['B']} behind {DRUM43}, raising the white eyebrows with a playful questioning look.", "", True, "Grandpa Bau raises the eyebrows and smiles; the tail club rests still on the drum."),
  ("둥둥 춤춰요", "BCRTP", MEADOW + f"Chiqui, Roro, Torong and Pio dance in a row on the meadow; {D['B']} stands on all four feet behind {DRUM43} on the far RIGHT, tapping it with the tail club.", "Exactly one drum.", False,
   "Chiqui, Roro and Pio dance and bounce; Torong sways the long neck; Grandpa Bau taps the drum with the tail club; Grandpa Bau's four feet stay on the ground. The camera stays still."),
  ("로로 씰룩씰룩", "R", MEADOW + f"{D['R']} wiggles the tail and bottom left and right in a funny dance.", "", False, "Roro wiggles the bottom left and right four times and laughs."),
  ("얼음!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio are frozen like statues in funny dance poses: Roro with one foot up, Pio with both wings wide, Torong with the neck tilted to one side (four feet on the ground), Chiqui with both front paws up; all eyes wide, holding still.", "", False,
   "Everyone stays completely still like statues for the whole clip; only their eyes blink once. Nobody moves. The camera stays still."),
  ("토롱 흔들흔들", "T", MEADOW + f"{D['T']} sways the long neck left and right in a happy dance, all four feet on the ground.", "", False, "Torong sways the neck left and right three times; all four feet stay on the ground."),
  ("피오 팔랑팔랑", "P", MEADOW + f"{D['P']} hops and flaps both wings in a happy dance.", "", False, "Pio hops three times flapping the wings and turns once."),
  ("또 얼음!", "RTP", MEADOW + "Roro, Torong and Pio are frozen like statues in funny poses (Roro on one foot, Pio with wings wide, Torong with the neck tilted, four feet on the ground), eyes wide, holding still.", "", False,
   "Roro, Torong and Pio stay completely still for the whole clip; only eyes blink once. The camera stays still."),
  ("치키만 빙글빙글", "CRTP", MEADOW + f"Roro, Torong and Pio stand frozen like statues in funny poses on the LEFT; {D['C']} on the RIGHT keeps spinning around happily with eyes closed, not noticing.", "", False,
   "Chiqui spins around two times with eyes closed; Roro, Torong and Pio stay frozen, then their eyes slide toward Chiqui. The camera stays still."),
  ("어? 나만?", "C", MEADOW + f"Close view of {D['C']} stopping mid-spin with one paw up, eyes wide open in surprise, looking at the viewer.", "", True, "Chiqui opens the eyes, stops, blinks two times at the viewer, then giggles."),
  ("하하하!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio laugh together on the meadow; Chiqui scratches the head.", "", False, "Everyone laughs; Chiqui scratches the head once. The camera stays still."),
  ("이번엔 꽁꽁!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio are all frozen like statues; Chiqui in front stands perfectly still in a proud pose with both paws on the hips and the eyes tightly shut.", "", False,
   "Everyone stays completely still for the whole clip; nobody moves at all. The camera stays still."),
  BAU(MEADOW, "꼼짝 않고 숨어서", f"stands perfectly still behind {DRUM43} like a statue, eyes peeking, a tiny playful smile."),
  ("다 같이 둥둥", "BCRTP", MEADOW + f"All five friends dance together on the meadow; {D['B']} stands on all four feet behind {DRUM43} and taps it with the tail club.", "Exactly one drum.", False,
   "Chiqui, Roro and Pio dance; Torong sways the neck; Grandpa Bau taps the drum with the tail club; all four of Grandpa Bau's feet stay on the ground. The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 44화 나눠 먹어요! (귤 나누기) ----------------
BASKET44 = "one round woven ORANGE basket"
TABLE44 = "one low round wooden table on the grass"
EPS["ep44"] = dict(
 title="44화. 나눠 먹어요! — 하나씩 나눠요", short="나눠 먹어요!", song_id="share", song_short="나눔 노래",
 theme="나눠 먹기, 하나씩 세며 건네기(1~5). 나누면 모두 웃어요. 바우·토롱은 탁자 위 귤을 입으로.",
 twist="귤 다섯 개를 혼자 다 먹으려던 치키… 친구들 얼굴을 보고 \"하나씩 나눠 먹자!\" 그런데 마지막 하나는 치키 거! 다 같이 \"냠!\"",
 bau="공룡들도 먹이를 나누며 함께 살았단다!",
 lines=[("치키","귤이다! 다 내 거!",""),("내레이션","친구들은 어떤 얼굴일까?","뒤에 3초 쉼"),("치키","하나씩 나눠 먹자!",""),
        ("치키","하나, 로로!",""),("치키","둘, 토롱!",""),("치키","셋, 피오!",""),("치키","넷, 할아버지!",""),("치키","다섯, 내 거!",""),
        ("모두","잘 먹겠습니다!",""),("모두","냠!",""),("바우","공룡들도 먹이를 나누며 함께 살았단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("주황 귤이 하나","크앙! 로로에게","하나 줄게 (하나!)"),("주황 귤이 둘","쭈욱~ 토롱에게","하나 줄게 (둘!)"),
         ("주황 귤이 셋","슝~ 피오에게","하나 줄게 (셋!)"),("넷은 할아버지","다섯은 치키","다 같이 냠 (냠!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "하나씩 나눠요 (나눠요!)", "나누면 더 맛있어", "치키치키 냠냠!"],
 scenes=scenes([
  ("귤이다!", "C", MEADOW + f"{D['C']} finds {BASKET44} on the grass with exactly FIVE small round orange tangerines with green leaves in it, eyes sparkling.", "Exactly one basket with exactly five tangerines.", False,
   "Chiqui gasps and bounces once next to the basket; the five tangerines stay in the basket. The camera stays still."),
  ("다 내 거!", "C", MEADOW + f"{D['C']} hugs {BASKET44} with five tangerines in both front paws, a funny greedy smile.", "Exactly five tangerines.", True,
   "Chiqui hugs the basket and wiggles happily; the five tangerines stay in the basket the whole time."),
  ("친구들 얼굴", "RTP", MEADOW + "Roro, Torong and Pio stand together looking toward the viewer side a little sadly, mouths small, Pio with drooping wings.", "", False,
   "Roro, Torong and Pio blink slowly and look down a little sad. The camera stays still."),
  ("음…", "C", MEADOW + f"Close view of {D['C']} holding {BASKET44}, thinking with the head tilted, looking at the viewer.", "", True, "Chiqui tilts the head two times, thinking, then smiles brightly."),
  ("하나씩 나눠 먹자!", "CRTP", MEADOW + f"{D['C']} sets {BASKET44} with five tangerines on {TABLE44}; Roro, Torong and Pio stand around the table smiling.", "Exactly one basket, exactly five tangerines, exactly one table.", False,
   "Chiqui puts the basket on the table and opens the paws wide; the friends cheer. The camera stays still."),
  ("하나, 로로!", "CR", MEADOW + f"{D['C']} hands one tangerine to {D['R']}; Roro takes it with both short arms, smiling; {BASKET44} on {TABLE44} now has four tangerines.", "Roro holds exactly one tangerine; the basket has exactly four.", False,
   "Chiqui gives one tangerine to Roro; Roro hugs it and says thank you with a nod."),
  ("둘, 토롱!", "CT", MEADOW + f"{D['C']} places one tangerine on {TABLE44} right in front of {D['T']}'s mouth; the basket now has three tangerines.", "Exactly one tangerine in front of Torong; the basket has exactly three.", False,
   NEAR + "Chiqui puts one tangerine on the table in front of Torong; Torong lowers the head and smiles; Torong never holds the tangerine."),
  ("셋, 피오!", "CP", MEADOW + f"{D['C']} hands one tangerine to {D['P']}; Pio holds it between both wing tips, happy; {BASKET44} on {TABLE44} now has two tangerines.", "Pio holds exactly one tangerine; the basket has exactly two.", False,
   "Chiqui gives one tangerine to Pio; Pio hugs it with the wing tips and hops once."),
  ("넷, 할아버지!", "BC", MEADOW + f"{D['C']} places one tangerine on {TABLE44} right in front of {D['B']}'s mouth; Grandpa Bau stands on all four feet; the basket now has one tangerine.", "Exactly one tangerine in front of Grandpa Bau; the basket has exactly one.", False,
   "Chiqui puts one tangerine on the table in front of Grandpa Bau; Grandpa Bau nods with a warm smile; Grandpa Bau never holds it and all four feet stay on the ground."),
  ("다섯, 내 거!", "C", MEADOW + f"{D['C']} holds up the last tangerine from the now EMPTY {BASKET44}, beaming.", "Chiqui holds exactly one tangerine; the basket is empty.", True, "Chiqui lifts the last tangerine high and cheers."),
  ("잘 먹겠습니다!", "BCRTP", MEADOW + f"All five friends stand around {TABLE44}; Chiqui, Roro and Pio each hold ONE tangerine, and one tangerine lies on the table in front of Torong's mouth and one in front of Grandpa Bau's mouth; the empty basket on the table.", "Exactly five tangerines in total, one for each friend.", False,
   "Everyone bows the head once together politely; nobody eats yet. Torong and Grandpa Bau keep all four feet on the ground. The camera stays still."),
  ("냠!", "BCRTP", MEADOW + f"All five friends around {TABLE44} each take a bite of their own tangerine at the same time: Chiqui, Roro and Pio bite the tangerine they hold; Torong and Grandpa Bau bite the tangerine on the table right in front of their mouths.", "Exactly five tangerines.", False,
   "Everyone takes one bite at the same time; a small bite mark shows on each tangerine; everyone smiles with full cheeks. Torong and Grandpa Bau keep all four feet on the ground and never hold the tangerine. The camera stays still."),
  ("맛있다!", "C", MEADOW + f"Close view of {D['C']} with full happy cheeks, holding a half-eaten tangerine (a bite mark shows), eyes closed in joy.", "", True, "Chiqui chews happily and rocks side to side."),
  BAU(MEADOW, "먹이를 나누며", f"stands next to {TABLE44}, smiling wisely; one tangerine with a bite mark lies on the table in front of his mouth."),
  ("나누면 다 같이 웃어요", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio hug each other and laugh together on the meadow.", "", False, "The friends lean together in a hug and laugh; Torong bends the neck around them gently, four feet on the ground. The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 45화 화석 도서관 탐험! (바우 할아버지 공룡 상식 특집) ----------------
LIB = ("INDOORS inside Grandpa Bau's fossil library: one big round cave room with soft cream walls, tall curved wooden bookshelves full of colorful books along the back wall, warm lamp light; "
       "NOT outdoors: no meadow, no open sky, no rainbow, no volcano. " + NODOLL)
FOS = ("THE SAME three cute cream-colored clay fossil displays in every scene, each on one low round grey stone stand, in this fixed order from LEFT to RIGHT: "
       "LEFT = one fossil skull with THREE horns and a round frill; MIDDLE = one big fossil skull with a big toothy smile and two tiny arms below it; "
       "RIGHT = one long curved fossil neck with a small head on top; the fossils are smooth, rounded and friendly, never scary, never broken")
EPS["ep45"] = dict(
 title="45화. 화석 도서관 탐험! — 공룡 상식 특집", short="화석 도서관 탐험!", song_id="fossil", song_short="화석 노래",
 theme="바우 할아버지의 화석 도서관. 화석 세 개를 보고 우리 친구들과 닮은 진짜 공룡 맞히기(트리케라톱스·티라노사우루스·브라키오사우루스).",
 twist="뿔 셋 화석은 치키, 이빨 화석은 로로, 긴 목 화석은 토롱을 닮았어요! 그럼 피오를 닮은 화석은? 하늘을 올려다보면… 천장에 날개 화석!",
 bau="트리케라톱스는 뿔이 세 개였단다!",
 lines=[("바우","화석 도서관에 온 걸 환영한다!",""),("모두","와아~","♻ 1화 15"),("바우","이 화석은 누구를 닮았을까?",""),
        ("내레이션","뿔이 세 개! 누구일까?","뒤에 3초 쉼"),("모두","치키!",""),("내레이션","이빨이 커다래! 누구일까?","뒤에 3초 쉼"),("모두","로로!",""),
        ("내레이션","목이 길쭉! 누구일까?","뒤에 3초 쉼"),("모두","토롱!",""),("피오","내 건 없어?",""),("바우","저기 위를 보렴!",""),
        ("바우","트리케라톱스는 뿔이 세 개였단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("뿔이 하나 둘 셋","누구를 닮았나? (누구?)","치키 닮았네 (치키!)"),("이빨이 커다래","누구를 닮았나? (누구?)","로로 닮았네 (로로!)"),
         ("목이 길쭉길쭉","누구를 닮았나? (누구?)","토롱 닮았네 (토롱!)"),("하늘 위 날개 화석","누구를 닮았나? (누구?)","피오 닮았네 (피오!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "화석 화석 누구일까? (누구?)", "할아버지 따라가요", "치키치키 탐험!"],
 scenes=scenes([
  ("화석 도서관", "", LIB + FOS + ". No characters.", "Exactly three fossil displays.", False, "Warm lamp light flickers softly; nothing moves."),
  ("환영한다!", "B", LIB + FOS + f". {D['B']} stands on all four feet in front of the bookshelves, smiling warmly, glasses shining.", "", False,
   "Grandpa Bau nods two times in welcome and wags the tail club; all four feet stay on the floor. The camera stays still."),
  ("와아~", "CRTP", LIB + FOS + ". Chiqui, Roro, Torong and Pio stand in the doorway area looking around with wide amazed eyes.", "", False, "The friends gasp and look around slowly. The camera stays still."),
  ("누구를 닮았을까?", "B", LIB + FOS + f". Close view of {D['B']} pointing with the nose toward the fossils, eyebrows raised playfully.", "", True, "Grandpa Bau turns the head toward the fossils and smiles."),
  ("뿔이 셋!", "", LIB + "Close view of the LEFT fossil display only: one cute cream clay fossil skull with THREE horns and a round frill on a low round grey stone stand. No characters.", "Exactly one fossil skull with exactly three horns.", True,
   "Soft light glows on the fossil; nothing moves."),
  ("치키다!", "C", LIB + FOS + f". {D['C']} stands next to the LEFT fossil with three horns, copying its pose proudly, the two heads side by side.", "", False,
   "Chiqui turns the head to the fossil, then to the viewer, and laughs. The fossil does not move."),
  ("이빨이 커다래!", "", LIB + "Close view of the MIDDLE fossil display only: one big cute cream clay fossil skull with a big toothy smile and two tiny arms, on a low round grey stone stand. No characters.", "Exactly one fossil skull.", True,
   "Soft light glows on the fossil; nothing moves."),
  ("로로다!", "R", LIB + FOS + f". {D['R']} stands next to the MIDDLE fossil, showing a big toothy grin and holding up two short arms, just like the fossil.", "", False,
   "Roro grins wide and wiggles the two short arms; the fossil does not move."),
  ("목이 길쭉!", "T", LIB + FOS + f". {D['T']} stands on all four feet next to the RIGHT fossil with the long curved neck, stretching the own long neck up the same way.", "", False,
   "Torong stretches the neck up slowly beside the fossil and smiles; all four feet stay on the floor."),
  ("내 건 없어?", "P", LIB + FOS + f". {D['P']} stands in front of the three fossils looking a little sad, wings drooping.", "", False, "Pio looks at each fossil, then droops the wings with a small sigh."),
  ("저기 위를 보렴!", "BP", LIB + FOS + f". {D['B']} on all four feet points the nose UP toward the ceiling; {D['P']} looks up.", "", False, "Grandpa Bau lifts the head up toward the ceiling; Pio follows the look up. The camera stays still."),
  ("날개 화석!", "", LIB + "Looking UP at the round cave ceiling: one big cute cream clay pteranodon fossil with wide wings and a pointed crest hangs from the ceiling on two thin ropes. No characters.", "Exactly one hanging wing fossil.", False,
   "The hanging fossil sways very gently; nothing else moves."),
  ("피오다!", "P", LIB + FOS + f". {D['P']} flies up near the ceiling with wings wide open, copying the hanging pteranodon fossil, a big happy smile.", "", False, "Pio flies one small circle under the hanging fossil and spreads the wings wide like it."),
  BAU(LIB + FOS + ". ", "뿔이 세 개였단다", "stands next to the LEFT fossil with three horns, smiling wisely, glasses shining."),
  ("다 같이 탐험!", "BCRTP", LIB + FOS + ". All five friends stand in front of the three fossils, each next to the fossil that looks like them, smiling proudly; Pio flies above.", "", False,
   "Everyone cheers; Pio flaps; Torong sways the neck; Grandpa Bau nods with all four feet on the floor. The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# (2026-11-27, 사용자: 영상을 여러 번 다시 만들지 않게) 합격 그림을 보고 동작을 그림 자세에 맞춤.
# 그림에서 이미 나와 있는 친구는 "튀어나온다" 대신 제자리 동작, 앞으로 걷기·내려앉기 금지.
_B4 = " Grandpa Bau keeps exactly 4 legs with all four feet flat on the ground; he never lifts a front foot."
_BUSHV = " The one round green bush with three cream flowers on top stays exactly the same, in the same place, the whole time."
VIDFIX = {"ep41": {
 "S02": "Chiqui cups one front paw next to the ear and bounces once on the same spot." + _BUSHV,
 "S04": "Chiqui listens with closed eyes, tilting the head slowly; the paw stays next to the ear." + _BUSHV,
 "S05": "The bush shakes gently two times; nobody comes out and nobody is visible." + _BUSHV,
 "S06": "Chiqui, Torong and Pio lean a little toward the bush, then look at each other, curious; they stay on the LEFT of the bush." + _BUSHV,
 "S07": "Roro, already standing at the RIGHT side of the bush as in the start image, hops once on the same spot, roars a friendly roar with both arms up, then laughs. Only one Roro appears." + _BUSHV,
 "S09": "Everyone laughs on the same spot; Roro scratches the head once." + _BUSHV,
 "S10": "Torong's small head above the bush bobs up and down two times; Torong's body stays hidden behind the bush; nothing else appears." + _BUSHV,
 "S11": "Torong, already standing at the RIGHT side of the bush, tilts the long neck to one side and smiles; all four feet stay on the ground; Torong does not walk." + _BUSHV,
 "S12": "Pio glides a little to the RIGHT above the bush, flapping the wings, and stays in the sky inside the frame at the same size; Pio does not land and does not fly toward the camera." + _BUSHV,
 "S13": "Grandpa Bau laughs with eyes squeezed shut, nodding the head three times." + _B4 + _BUSHV,
 "S14": "The orange frill with three cream horns behind the bush wiggles left and right two times; nothing else appears." + _BUSHV,
 "S15": "Chiqui, already beside the bush as in the start image, hops once on the same spot with both front paws up and laughs. Only one Chiqui appears." + _BUSHV,
 "S16": "Grandpa Bau nods once and smiles wisely." + _B4 + _BUSHV,
 "S17": "Everyone opens the mouth and calls out happily two times on the same spot; Pio flaps; Torong sways the neck; Grandpa Bau nods." + _B4 + _BUSHV,
}}
for _e, _fx in VIDFIX.items():
    if _e in EPS:
        EPS[_e]["scenes"] = [t[:6] + (vid(t[3], _fx[t[0]]),) if t[0] in _fx else t for t in EPS[_e]["scenes"]]

for ep, e in EPS.items():
    write(ep, e)

# ---------- 공통 컷: 26~45화 전체에서 그림 프롬프트가 같은 장면은 같은 그림·영상 하나를 쓴다 ----------
_ROOT = Path(__file__).resolve().parent.parent
_COMMON_NAME = {"안녕!": "ending_meadow", "좋아!": "cheer_meadow"}
_known = {}  # 26~40화에서 이미 정한 공통 컷 (프롬프트 → id)
for _n in range(26, 41):
    _f = _ROOT / f"episodes/ep{_n}/scenes.json"
    if _f.exists():
        for _s in _json.loads(_f.read_text(encoding="utf-8")):
            if _s.get("common"): _known[_s["img"]] = _s["common"]
_groups = _col.defaultdict(list)
for _ep in EPS:
    for _s in _json.loads((_ROOT / f"episodes/{_ep}/scenes.json").read_text(encoding="utf-8")):
        _groups[_s["img"]].append((_ep, _s["id"], _s["name"]))
for _ep in EPS:
    _f = _ROOT / f"episodes/{_ep}/scenes.json"
    _sc = _json.loads(_f.read_text(encoding="utf-8"))
    for _s in _sc:
        _v = _groups[_s["img"]]
        if _s["img"] in _known: _s["common"] = _known[_s["img"]]
        elif len(_v) > 1: _s["common"] = _COMMON_NAME.get(_v[0][2], f"common_{_v[0][0]}_{_v[0][1]}")
        else: _s.pop("common", None)
    _f.write_text(_json.dumps(_sc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(_ep, "common:", [(s["id"], s["common"]) for s in _sc if s.get("common")])
