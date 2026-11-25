"""26~40화 대본·가사·장면 프롬프트 (2026-11-24, 무제한 끝나기 전 한꺼번에).
인기 유아 채널 소재만 참고, 이야기·노래는 새로. 11~25화에서 배운 것을 처음부터 넣었다:
- 반복 소품은 한 문장으로 고정(자리·색·개수), 장면마다 '아직 없는 것'도 적는다.
- 토롱·바우는 물건을 들지 않는다(바로 앞 땅·탁자 위 물건을 코·입으로), 다리 정확히 4개.
- 땅에 선·줄무늬를 그리지 않는다(횡단보도는 예외: 길을 건너는 장면만).
- 탈것 없음. 카메라 고정. 동작은 결과까지 적는다.
사용법: python3 -I prompts/make_ep26_40.py
"""
from pathlib import Path

_p = Path(__file__).resolve().parent / "make_ep11_15.py"
_src = _p.read_text(encoding="utf-8")
_ns = {"__file__": str(_p)}
exec(_src.split("\nEPS = {}")[0], _ns)
img, vid, scenes, write, D, HOME, NODOLL = (_ns[k] for k in ("img", "vid", "scenes", "write", "D", "HOME", "NODOLL"))

NEAR = "The thing Torong touches is right in front of Torong's mouth, so Torong's neck keeps its normal length and never stretches longer; all four feet stay on the ground. "
MEADOW = "On a sunny plain green meadow of the volcano-island village with palm trees, round cave houses and the far volcano; the grass is plain green with no lines or paths drawn on it. "
SCARF = ""


def CHEER(where, name="좋아!"):
    return (name, "CRTP", where + "Chiqui, Roro, Torong and Pio cheer and bounce happily.", "", False, "The friends cheer and bounce a little. The camera stays still.")


def WAVE(where, name, extra=""):
    return (name, "BCRTP", where + f"All five friends stand in a row facing the viewer with big smiles{extra}. Chiqui and Roro each wave ONE front paw, Pio waves one wing; Grandpa Bau does NOT wave: Grandpa Bau has exactly 4 legs with all four feet flat on the ground and says hi by nodding the head and wagging the tail club; Torong stands on all four feet and tilts the long neck and head to one side.", "", False,
            "Chiqui, Roro and Pio wave at the viewer; Grandpa Bau nods and wags the tail club with all four feet staying on the ground (exactly 4 legs); Torong sways the long neck side to side with all four feet on the ground. The camera stays still.")


def BAU(where, name, pose):
    return (name, "B", where + f"{D['B']} {pose}", "", False, "Grandpa Bau nods once and smiles warmly; all four feet stay on the ground. The camera stays still.")


EPS = {}
# ---------------- 26화 좋은 아침! (아침 습관) ----------------
BASIN = "one small round grey stone basin of clear water standing on the grass"
BED26 = ("THE SAME bedroom and bed in every scene: ONE round window with a wooden cross frame on the LEFT wall with green ivy leaves hanging around it, "
         "two chunky wooden shelves on the RIGHT wall (a potted green plant on the top shelf; blue, yellow and green books and a small cream jar on the lower shelf), "
         "a tree-stump side table with a glowing mushroom lamp on the LEFT of the bed, a round rug with cream and yellow rings on the floor on the right; "
         "Chiqui's bed is a round WOODEN bed with a big curved wooden headboard and a thick rounded wooden rim, an orange mattress and a cream pillow; "
         "the blanket is ORANGE with big YELLOW dots and a wide cream folded edge at the top. It is a BRIGHT MORNING: warm sunlight shines through the window, the window panes are bright pale yellow (never dark blue, never night), the room is light and warm. ")
EPS["ep26"] = dict(
 title="26화. 좋은 아침! — 아침 습관", short="좋은 아침!", song_id="morning", song_short="아침 노래",
 theme="아침에 일어나기, 기지개·세수·머리 빗기·아침밥, 아침 인사. 치키만 늦잠!",
 twist="다들 일어났는데 치키만 쿨쿨… 화면 밖 아이와 다 같이 \"치키야, 일어나!\" 외치면 눈이 번쩍!",
 bau="공룡도 해님이 뜨면 일어났단다!",
 lines=[("내레이션","해님이 떴어요.",""),("로로","좋은 아침!",""),("모두","좋은 아침!",""),("내레이션","치키는 어디 있을까?","뒤에 3초 쉼"),
        ("모두","치키야, 일어나!","아이도 같이 외치게 2초 쉼"),("치키","하암~ 좋은 아침!",""),("치키","세수 어푸어푸!",""),("모두","잘 먹겠습니다!",""),
        ("바우","공룡도 해님이 뜨면 일어났단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("해님이 방긋 떴어요","크앙! 로로가 기지개","쭉쭉 쭈욱 (쭈욱!)"),("찬물로 어푸어푸","쭈욱~ 토롱이 세수","반짝반짝 (반짝!)"),
         ("볏을 슥슥 빗어요","슝~ 피오가 슥슥","단정하게 (슥슥!)"),("치키는 아직 쿨쿨","다 같이 불러요 (치키야!)","눈을 번쩍 (번쩍!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "좋은 아침! (좋은 아침!)", "해님 보고 일어나요", "치키치키 일어나!"],
 scenes=scenes([
  ("해님이 떴어요", "", "Early morning in the volcano-island dinosaur village: the sun rises softly over the far volcano, soft pink-orange sky, quiet round cave houses on the meadow. No characters.", "", False,
   "The sun rises slowly and soft light spreads over the village; nothing else moves."),
  ("좋은 아침!", "R", MEADOW + f"{D['R']} steps out of a round cave-house door, stretching both arms up with a big happy smile.", "", False, "Roro stretches both arms up two times and smiles. The camera stays still."),
  ("다 같이 좋은 아침!", "RTP", MEADOW + "Roro, Torong and Pio stand together in the morning sun, greeting each other happily.", "", False, "Roro and Pio wave; Torong tilts the long neck; everyone smiles."),
  ("치키는 어디?", "RTP", MEADOW + "Roro, Torong and Pio look around the meadow, puzzled, searching for someone.", "", False, "The friends look left and right, puzzled. The camera stays still."),
  ("쿨쿨", "C", HOME + BED26 + f"{D['C']} sleeps in the bed under the blanket, eyes closed, smiling; morning light from the round window.", "", False,
   "Chiqui sleeps, breathing slowly; the blanket rises and falls gently. Chiqui stays asleep. It stays a bright sunny morning the whole time: the window stays bright pale yellow with sunlight, the room never gets dark and never turns into night."),
  ("치키야, 일어나!", "RTP", MEADOW + "Roro, Torong and Pio stand in front of the round door of Chiqui's cave house, calling with open mouths, Roro and Pio with a paw or wing next to the mouth.", "", False,
   "The friends call out two times toward the door. The camera stays still."),
  ("기지개 쭉쭉", "R", MEADOW + f"{D['R']} stretches both arms up high, standing on tiptoes in the morning sun.", "", False, "Roro stretches up three times, bouncing on the toes."),
  ("어푸어푸 세수", "T", MEADOW + f"{D['T']} bends the neck down to {BASIN} right in front of the mouth and splashes the face gently in the water.", "Exactly one basin.", False,
   NEAR + "Torong dips the face into the basin, splashes gently, then lifts the head and smiles; little water drops fly."),
  ("볏을 슥슥", "P", MEADOW + f"{D['P']} stands next to a small round pond and smooths the pointed crest with one wing tip, looking at the reflection.", "", False, "Pio smooths the crest two times with the wing tip and smiles."),
  ("눈을 번쩍!", "C", HOME + BED26 + f"{D['C']} sits up in the bed with wide-open surprised eyes, the blanket slipping down to the lap.", "", False, "Chiqui blinks two times and sits up straight, surprised. It stays a bright sunny morning the whole time: the window stays bright pale yellow with sunlight, the room never gets dark and never turns into night."),
  ("하암~", "C", HOME + BED26 + f"Close view of {D['C']} sitting in the bed with the blanket on the lap, stretching both front paws up with a big yawn.", "", True, "Chiqui yawns with a big open mouth and stretches, then smiles. It stays a bright sunny morning the whole time: the window stays bright pale yellow with sunlight, the room never gets dark and never turns into night."),
  ("어푸어푸!", "C", MEADOW + f"{D['C']} stands at {BASIN} and splashes the face with both front paws.", "Exactly one basin.", False, "Chiqui splashes water on the face two times; drops fly; Chiqui laughs."),
  ("잘 먹겠습니다!", "BCRTP", MEADOW + "All five friends around a low wooden table with five small bowls: Grandpa Bau PURPLE grapes, Chiqui ORANGE carrot sticks, Roro one YELLOW corn cob, Torong GREEN broccoli (Torong's bowl is right in front of Torong's mouth), Pio dark BLUE blueberries. Grandpa Bau stands on all four feet behind the table.", "Exactly five bowls.", False,
   "Chiqui, Roro and Pio each take one bite from their own bowl; Torong bends the neck to the green bowl right in front of the mouth and takes one bite; Grandpa Bau nods. A bite really happens."),
  BAU(MEADOW, "해님이 뜨면", "stands in the morning sun, smiling wisely and looking up at the sun."),
  ("오늘도 신나게!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio walk together across the sunny meadow, happy.", "", False, "The friends walk a few steps to the LEFT together, smiling. The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 27화 쉬~ 화장실 (배변 습관) ----------------
HUT = ("THE SAME little bathroom hut in every scene: one small round clay hut with a smooth cream wall and a roof of big green clay leaves, "
       "a round pale-blue wooden door with a yellow knob in the middle of the front, the door is hinged on its LEFT edge so it always swings open to the LEFT, "
       "and one tiny round window with a wooden frame on the RIGHT side of the door (never on the left); nothing written or drawn on it")
SINK = "a small round grey stone hand-wash basin with clear water and a little wooden spout, standing on the LEFT side of the hut (never on the right)"
EPS["ep27"] = dict(
 title="27화. 쉬~ 화장실! — 배변 습관", short="쉬~ 화장실!", song_id="potty", song_short="화장실 노래",
 theme="쉬가 마려우면 말하고 화장실 가기, 다녀와서 손 씻기. 비누 거품은 친구 몸 색.",
 twist="놀이에 푹 빠진 치키가 동동동… 화면 밖 아이와 친구들이 \"치키야, 화장실!\" 알려 주면 얼른 다녀와요.",
 bau="공룡도 날마다 응가를 했단다!",
 lines=[("모두","신나게 놀자!",""),("로로","쉬 마려워요!",""),("바우","얼른 다녀오렴!",""),("내레이션","다녀와서는?","뒤에 2초 쉼"),("모두","손 씻기!",""),
        ("내레이션","치키는 왜 동동거릴까?","뒤에 3초 쉼"),("모두","치키야, 화장실!",""),("치키","다녀왔어요!",""),
        ("바우","공룡도 날마다 응가를 했단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("쉬가 마려워 동동","크앙! 로로가 말해요","화장실 갈래요 (갈래요!)"),("쭈욱~ 토롱도 동동","천천히 다녀와요","손 씻고 와요 (싹싹!)"),
         ("슝~ 피오도 동동","쉬 마려워요 말해요","다녀왔어요 (짠!)"),("치키는 놀다가 동동","참으면 안 돼요 (안 돼!)","얼른 가요 (얼른!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "쉬 마려워요! (쉬~!)", "참지 말고 말해요", "치키치키 화장실!"],
 scenes=scenes([
  ("신나게 놀자!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio play tag on the meadow, laughing.", "", False, "The friends run around in a small circle and laugh. The camera stays still and everyone stays inside the frame."),
  ("쉬 마려워요!", "R", MEADOW + f"{D['R']} stops playing and wiggles from foot to foot with both paws on the tummy, a funny worried face.", "", False, "Roro wiggles from foot to foot three times, holding the tummy."),
  ("얼른 다녀오렴!", "BR", MEADOW + f"{D['R']} looks up at {D['B']}; Grandpa Bau smiles and points with the nose toward {HUT} a little way off.", "Exactly one hut.", False,
   "Grandpa Bau nods toward the hut; Roro nods back quickly. Grandpa Bau's four feet stay on the grass."),
  ("화장실이에요", "", MEADOW + f"{HUT}, standing alone on the meadow with {SINK}. No characters.", "Exactly one hut and one basin.", False, "Nothing moves except grass swaying a little; the door stays closed."),
  ("쏙 들어가요", "R", MEADOW + f"{D['R']} walks toward {HUT}, the round pale-blue door is open, Roro's back is to the viewer.", "", False, "Roro walks two steps into the hut and the door closes softly. Only one Roro."),
  ("손을 싹싹", "R", MEADOW + f"{D['R']} washes both paws at {SINK} with soft YELLOW soap bubbles, standing next to {HUT}.", "", False, "Roro rubs the paws together three times; yellow bubbles grow, then Roro rinses and smiles."),
  ("토롱도 동동", "T", MEADOW + f"{D['T']} shifts the weight from one side to the other with a funny worried face next to {HUT}.", "", False, "Torong shifts the weight left and right two times, then walks slowly toward the hut door; four legs only."),
  ("피오 다녀왔어요", "P", MEADOW + f"{D['P']} hops out of the open round pale-blue door of {HUT}, smiling.", "", False, "Pio hops out two times and flaps the wings happily."),
  ("치키는 놀다가", "C", MEADOW + f"{D['C']} plays alone with one ORANGE ball, wiggling the feet a little.", "Exactly one ball.", False, "Chiqui bounces the ball and wiggles from foot to foot, still playing."),
  ("동동동", "C", MEADOW + f"Close view of {D['C']} holding one ORANGE ball with crossed legs and a funny wiggly face.", "", True, "Chiqui keeps hugging the ORANGE ball in both front paws the WHOLE time (the ball never disappears, never drops and never rolls away) while wiggling and squeezing the legs together two times, looking left and right. The camera stays still."),
  ("치키야, 화장실!", "RTP", MEADOW + f"Roro, Torong and Pio point toward {HUT} and call out to Chiqui; Torong points with the nose.", "", False, "Roro and Pio point and call twice; Torong nods toward the hut."),
  ("얼른!", "C", MEADOW + f"{D['C']} runs quickly toward {HUT}, the round pale-blue door is open.", "", False, "Chiqui runs into the hut and the door closes softly. Only one Chiqui."),
  ("다녀왔어요!", "C", MEADOW + f"{D['C']} washes both paws at {SINK} with soft ORANGE soap bubbles next to {HUT}, smiling with relief.", "", False, "Chiqui rubs the paws with orange bubbles three times, rinses and smiles."),
  BAU(MEADOW, "공룡도 응가를", "stands on the meadow next to a small fern, smiling wisely, one eyebrow raised playfully."),
  ("다시 신나게!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio play tag again on the meadow, laughing.", "", False, "The friends run around in a small circle and laugh. The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 28화 우산 쓰고 첨벙첨벙 (비 오는 날) ----------------
RAIN = "On the meadow of the volcano-island village on a soft rainy day, gentle raindrops falling, a few small round puddles on the grass, grey-blue sky. "
UMB = "Chiqui holds one ORANGE umbrella, Roro holds one YELLOW umbrella, Pio holds one small SKY-BLUE umbrella with one wing"
BIGTREE = "THE SAME big round leafy green tree in every scene, with a wide umbrella-like crown of leaves"
EPS["ep28"] = dict(
 title="28화. 우산 쓰고 첨벙첨벙! — 비 오는 날", short="우산 쓰고 첨벙첨벙!", song_id="rain", song_short="첨벙 노래",
 theme="비 오는 날 놀이(우산·물웅덩이), 친구 몸 색 우산. 토롱은 우산 대신 큰 나무가 우산!",
 twist="토롱 우산은 어디 있지? 토롱이 큰 나무 아래 쏙 — 나뭇잎이 커다란 우산이 돼요.",
 bau="공룡들도 큰 나무 밑에서 비를 피했단다!",
 lines=[("내레이션","톡톡, 비가 와요.",""),("바우","우산 쓰고 놀자!",""),("모두","좋아!","♻ 1화 07"),("모두","첨벙첨벙!",""),
        ("내레이션","토롱 우산은 어디 있을까?","뒤에 3초 쉼"),("토롱","여기 있지!",""),("모두","나뭇잎 우산!",""),
        ("바우","공룡들도 큰 나무 밑에서 비를 피했단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("노란 우산 빙글빙글","크앙! 로로가 첨벙","물웅덩이 (첨벙!)"),("하늘색 우산 팔랑팔랑","슝~ 피오가 첨벙","물웅덩이 (첨벙!)"),
         ("주황 우산 동글동글","치키도 첨벙","물웅덩이 (첨벙!)"),("토롱 우산은 어디 있지?","큰 나무 아래 쏙 (쏙!)","나뭇잎 우산 (우산!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "우산 쓰고 첨벙첨벙 (첨벙!)", "비가 와도 신나요", "치키치키 첨벙!"],
 scenes=scenes([
  ("톡톡, 비가 와요", "", RAIN + "Raindrops fall on the round cave houses and puddles. No characters.", "", False, "Raindrops fall and make little rings in the puddles; nothing else moves."),
  ("비다!", "C", RAIN + f"{D['C']} stands at the round door of the cave house, looking up at the rain with sparkling eyes.", "", False, "Chiqui holds one paw out and catches raindrops, smiling."),
  ("우산 쓰고 놀자!", "B", RAIN + f"{D['B']} wears one small PURPLE rain hat and stands on all four feet in the rain, smiling.", "", False, "Grandpa Bau nods; raindrops roll off the purple hat."),
  ("좋아!", "CRP", RAIN + f"Chiqui, Roro and Pio cheer in the rain; {UMB}.", "Exactly three umbrellas.", False, "The friends twirl the umbrellas once and cheer."),
  ("물웅덩이", "", RAIN + "Close view of one round puddle on the grass with raindrop rings. No characters.", "", True, "Raindrops make rings in the puddle."),
  ("첨벙!", "C", RAIN + f"{D['C']} holding one ORANGE umbrella jumps into one round puddle; a splash of water flies up.", "", False, "Chiqui jumps into the puddle once; water splashes; Chiqui laughs."),
  ("로로 첨벙", "R", RAIN + f"{D['R']} holding one YELLOW umbrella twirls it and splashes in a puddle.", "", False, "Roro twirls the yellow umbrella and stamps in the puddle two times; water splashes."),
  ("피오 첨벙", "P", RAIN + f"{D['P']} holding one small SKY-BLUE umbrella with one wing hops in a small puddle.", "", False, "Pio hops in the puddle two times; little splashes."),
  ("치키 첨벙", "C", RAIN + f"{D['C']} holding one ORANGE umbrella splashes in a puddle with both feet, laughing.", "", False, "Chiqui stamps two times; water splashes."),
  ("토롱은?", "T", RAIN + f"{D['T']} stands in the rain with NO umbrella, raindrops on the head, a little sad face.", "", False, "Torong blinks at the raindrops and looks a little sad; four legs on the grass."),
  ("토롱 우산은?", "CRTP", RAIN + f"Chiqui, Roro and Pio with their umbrellas ({UMB}) look at Torong, who has no umbrella, worried.", "", False, "The friends look at Torong and tilt their heads."),
  ("어디 있을까?", "C", RAIN + f"Close view of {D['C']} holding one ORANGE umbrella, looking at the viewer, thinking.", "", True, "Chiqui looks at the viewer and tilts the head."),
  ("나뭇잎 우산!", "CRTP", RAIN + f"{D['T']} stands under {BIGTREE}; the leaves cover Torong's head like a big umbrella and Torong smiles; Chiqui, Roro and Pio cheer next to the tree with their umbrellas ({UMB}).", "Exactly one big tree.", False,
   "Torong smiles under the leaves; raindrops fall around the tree but not on Torong; the friends cheer."),
  BAU(RAIN, "큰 나무 밑에서", f"wears the small PURPLE rain hat and stands under {BIGTREE}, smiling wisely."),
  ("비가 그쳤어요", "CRTP", MEADOW + "The rain has stopped; Chiqui, Roro, Torong and Pio play happily on the wet shiny meadow. Exactly THREE closed umbrellas lie on the grass: one ORANGE, one YELLOW and one small SKY-BLUE. There is NO green umbrella and no fourth umbrella (Torong never had an umbrella).", "Exactly three umbrellas.", False, "The friends jump in the sunshine; drops sparkle. The three closed umbrellas (orange, yellow, sky-blue) stay lying on the grass; no new umbrella appears."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 29화 쑥쑥 자라라 (씨앗 심기) ----------------
POTS = ("THE SAME four small round clay flower pots in every scene, standing in ONE row on the grass, left to right as seen by the viewer: ORANGE pot, YELLOW pot, GREEN pot, SKY-BLUE pot, "
        "each filled with dark brown soil; every pot has the same one decoration in the middle of its front: one small cream-white five-petal flower with a round yellow center (no leaves, nothing else)")
EPS["ep29"] = dict(
 title="29화. 쑥쑥 자라라! — 씨앗 심기", short="쑥쑥 자라라!", song_id="seed", song_short="씨앗 노래",
 theme="씨앗 심기(흙 파기·덮기·물 주기·햇빛), 기다림. 화분은 친구 몸 색.",
 twist="친구들 화분엔 싹이 쏙! 그런데 치키 화분만 그대로… 물을 안 줬구나! 물을 주니 쑥!",
 bau="공룡들도 초록 잎을 냠냠 먹었단다!",
 lines=[("바우","씨앗을 심어 볼까?",""),("모두","좋아!","♻ 1화 07"),("치키","콕! 다 심었다!",""),("모두","쑥쑥 자라라!",""),
        ("내레이션","치키 화분은 왜 싹이 안 날까?","뒤에 3초 쉼"),("치키","아! 물을 안 줬어!",""),("모두","와아~","♻ 1화 15"),
        ("바우","공룡들도 초록 잎을 냠냠 먹었단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("콕콕 흙을 파고","크앙! 로로가 콕","씨앗 하나 (콕!)"),("토닥토닥 흙 덮고","쭈욱~ 토롱이 토닥","잘 자라라 (토닥!)"),
         ("쪼르르 물을 주고","슝~ 피오가 쪼르르","해님 방긋 (방긋!)"),("치키 화분은 왜 그럴까?","싹이 안 나요 (왜?)","물을 줘요 (쪼르르!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "쑥쑥 자라라 (쑥쑥!)", "씨앗 콕 물 주고", "치키치키 쑥쑥!"],
 scenes=scenes([
  BAU(MEADOW, "씨앗을 심어 볼까?", "stands next to one small cloth bag of seeds lying on the grass, smiling."),
  CHEER(MEADOW),
  ("빈 화분", "", MEADOW + f"Use the reference image ONLY for the flower pots: draw the four pots EXACTLY like the pots in the reference image (same shape, size, color, rim, soil and spacing), but leave out the character, so the picture shows only the pots on the grass. Close view of {POTS}; all four pots have only soil, no plants, no seeds visible. No characters.", "Exactly four pots, no sprouts.", True, "Nothing moves; the pots stay the same."),
  ("콕! 다 심었다!", "C", MEADOW + f"{D['C']} pokes one seed into the soil of the ORANGE pot of {POTS}, then claps.", "No sprouts anywhere.", False, "Chiqui pokes the seed in, pats the soil once and claps."),
  ("놀러 가요", "C", MEADOW + f"{D['C']} runs off happily across the meadow after one rolling ORANGE ball, leaving the pots behind.", "", False, "Chiqui runs a few steps to the LEFT after the ball. Chiqui does not water the pot."),
  ("로로가 콕", "R", MEADOW + f"{D['R']} digs a little hole in the YELLOW pot of {POTS} and drops in one seed.", "No sprouts anywhere.", False, "Roro digs, drops the seed and pats the soil."),
  ("토롱이 토닥", "T", MEADOW + f"{D['T']} bends the neck down to the GREEN pot of {POTS}, which is right in front of Torong's mouth, and pats the soil gently with the nose.", "No sprouts anywhere.", False, NEAR + "Torong pats the soil two times with the nose and lifts the head, smiling."),
  ("피오가 쪼르르", "P", MEADOW + f"{D['P']} stands next to the SKY-BLUE pot of {POTS} with a tiny SKY-BLUE watering can in the beak, pouring water on the soil.", "No sprouts anywhere.", False, "Pio pours a thin stream of water on the soil, then sets the can down and flaps once."),
  ("해님 방긋", "", MEADOW + f"{POTS} in bright sunshine: the YELLOW, GREEN and SKY-BLUE pots each have one small green sprout with two leaves; the ORANGE pot has only bare soil. No characters.", "Exactly three sprouts.", False, "Sunlight glows; the three sprouts sway a little; the orange pot stays bare."),
  ("싹이 났다!", "RTP", MEADOW + f"Roro, Torong and Pio cheer behind {POTS}; the yellow, green and sky-blue pots have small sprouts, the ORANGE pot is bare.", "", False, "The friends cheer and point at their sprouts."),
  ("치키 화분은?", "C", MEADOW + f"{D['C']} looks sadly at the bare ORANGE pot of {POTS}; the other three pots have sprouts.", "", False, "Chiqui looks at the bare pot, then tilts the head, sad."),
  ("왜 싹이 안 날까?", "C", MEADOW + f"Close view of {D['C']} looking at the viewer, thinking hard.", "", True, "Chiqui looks at the viewer and tilts the head."),
  ("물을 줘요!", "C", MEADOW + f"{D['C']} pours water from one small ORANGE watering can onto the ORANGE pot of {POTS}; one tiny green sprout pops up from the soil.", "", False,
   "Chiqui pours the water; then one tiny sprout pops up out of the soil in the orange pot and stays. Chiqui jumps with joy."),
  ("초록 잎 냠냠", "B", MEADOW + f"{D['B']} stands on all four feet next to one low round leafy green plant on the grass, smiling wisely.", "", False,
   "Grandpa Bau bends the head down to the green plant and takes ONE bite of one leaf with the mouth, chews happily and smiles; afterwards that leaf has a small round bite missing. Grandpa Bau keeps exactly 4 legs with all four feet on the ground and never uses the front feet. The camera stays still."),
  ("모두 쑥쑥!", "CRTP", MEADOW + f"Chiqui, Roro, Torong and Pio cheer behind {POTS}; now all four pots have one small green sprout.", "Exactly four sprouts.", False, "The friends cheer; all four sprouts stay."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 30화 치키가 말했어요! (따라 하기 놀이) ----------------
EPS["ep30"] = dict(
 title="30화. 치키가 말했어요! — 따라 하기 놀이", short="치키가 말했어요!", song_id="copy", song_short="따라 하기",
 theme="보고 따라 하기 몸 놀이(손 들기·꼬리 흔들기·빙글·쿵쿵), 화면 밖 아이도 같이.",
 twist="마지막 \"쉿! 잠자는 척!\" 다 같이 쿨쿨… 할아버지가 \"일어나라!\" 하자 모두 벌떡!",
 bau="공룡도 엄마 따라 걸음마를 배웠단다!",
 lines=[("치키","치키가 말했어요!",""),("모두","좋아!","♻ 1화 07"),("치키","손을 위로!",""),("치키","꼬리를 살랑!",""),("치키","빙글 돌아요!",""),
        ("치키","쉿! 잠자는 척!",""),("내레이션","다 같이 쿨쿨…","뒤에 2초 쉼"),("바우","일어나라!",""),("모두","와아~","♻ 1화 15"),
        ("바우","공룡도 엄마 따라 걸음마를 배웠단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("손을 위로 쭈욱","크앙! 로로도 쭈욱","따라 해요 (쭈욱!)"),("꼬리를 살랑살랑","쭈욱~ 토롱 살랑","따라 해요 (살랑!)"),
         ("빙글빙글 돌아요","슝~ 피오가 빙글","따라 해요 (빙글!)"),("쿵쿵 발을 굴러요","다 같이 쿵쿵 (쿵쿵!)","따라 해요 (쿵!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "치키가 말했어요 (말했어요!)", "보고 보고 따라 해", "치키치키 따라 해!"],
 scenes=scenes([
  ("치키가 말했어요!", "C", MEADOW + f"{D['C']} stands in front, facing the viewer, one front paw raised like a little leader.", "", False, "Chiqui raises the paw and smiles. The camera stays still."),
  ("좋아!", "RTP", MEADOW + "Roro, Torong and Pio stand in a row facing Chiqui and the viewer, ready to play.", "", False, "The friends nod and bounce once."),
  BAU(MEADOW, "지켜봐요", "sits on the grass to one side, watching happily."),
  ("손을 위로!", "C", MEADOW + f"{D['C']} stretches both front paws up high.", "", False, "Chiqui stretches both paws up two times."),
  ("다 같이 위로!", "RTP", MEADOW + "Roro and Pio stretch arms and wings up high; Torong stretches the long neck straight up; all four of Torong's feet stay on the ground.", "", False, "They stretch up two times; Torong lifts only the neck."),
  ("꼬리를 살랑!", "C", MEADOW + f"{D['C']} wags the tail with a cheeky smile.", "", False, "Chiqui wags the tail left and right three times."),
  ("로로도 쭈욱", "R", MEADOW + f"{D['R']} stretches both arms up high on tiptoes.", "", False, "Roro stretches up three times."),
  ("토롱 살랑", "T", MEADOW + f"{D['T']} wags the long tail, smiling.", "", False, "Torong wags the tail left and right three times; four feet stay on the ground."),
  ("피오 빙글", "P", MEADOW + f"ONE single picture (NOT a grid, NOT a comic strip, NOT several panels or frames, NOT a step-by-step sequence): {D['P']} stands on the grass in the middle of the meadow, turned a little to the side as if starting to spin, with both wings open wide; Pio appears only ONCE in the picture.", "", False, "Pio turns around in one full circle on the spot and stops facing the viewer."),
  ("다 같이 쿵쿵", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio stomp their feet together happily.", "", False, "Everyone stomps two times in place; the camera stays still."),
  ("쉿!", "C", MEADOW + f"Close view of {D['C']} holding one paw in front of the mouth, eyes sparkling, whispering.", "", True, "Chiqui whispers 'shh' and winks."),
  ("잠자는 척", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio lie down on the grass with eyes closed, pretending to sleep, little smiles.", "", False, "They breathe slowly with eyes closed; nobody moves much."),
  ("일어나라!", "BCRTP", MEADOW + "Grandpa Bau calls out with a big smile; Chiqui, Roro, Torong and Pio jump up from the grass, laughing.", "", False, "The friends spring up from lying down and laugh; Grandpa Bau's four feet stay on the grass."),
  BAU(MEADOW, "걸음마를 배웠단다", "stands on the meadow smiling wisely."),
  ("다 같이 춤!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio dance together, bouncing.", "", False, "Everyone bounces and sways; Torong sways the neck. The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 31화 퐁퐁 비눗방울 ----------------
BOWL = "one big round PURPLE bowl of bubble soap on the grass"
WAND31 = "each bubble wand is a simple short stick with ONE plain round ring loop at the top (no flower, star or heart shapes)"
RING31 = "one big plain GREEN bubble ring on a short wooden stick stuck upright in the grass (the ring never floats in the air)"
EPS["ep31"] = dict(
 title="31화. 퐁퐁 비눗방울! — 비눗방울 놀이", short="퐁퐁 비눗방울!", song_id="bubble", song_short="비눗방울",
 theme="비눗방울 불기·잡기·세기. 막대는 친구 몸 색. 토롱은 바닥에 세운 커다란 고리에 후~.",
 twist="하늘에 둥실 엄청 큰 비눗방울! 누가 만들었을까? 토롱이 목이 길어서 숨을 길~게 후~!",
 bau="공룡 알도 비눗방울처럼 동글동글했단다!",
 lines=[("바우","비눗방울 놀이 하자!",""),("모두","좋아!","♻ 1화 07"),("치키","후~",""),("모두","퐁퐁!",""),
        ("내레이션","커다란 비눗방울은 누가 만들었을까?","뒤에 3초 쉼"),("토롱","내가 했지!",""),("모두","와아~","♻ 1화 15"),
        ("바우","공룡 알도 비눗방울처럼 동글동글했단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("후~ 불면 퐁퐁","크앙! 로로가 후~","노란 막대 (퐁!)"),("후~ 길게 불면","쭈욱~ 토롱이 후~","커다란 방울 (우와!)"),
         ("팡팡 터뜨려요","슝~ 피오가 콕","하나 둘 셋 (팡!)"),("치키도 후~","방울방울 (퐁퐁!)","하늘 높이 (둥실!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "퐁퐁 비눗방울 (퐁퐁!)", "후~ 불면 둥실둥실", "치키치키 퐁퐁!"],
 scenes=scenes([
  BAU(MEADOW, "비눗방울 놀이 하자!", f"stands next to {BOWL}, smiling."),
  CHEER(MEADOW),
  ("비눗방울 준비", "", MEADOW + f"Close view of {BOWL} with three small bubble wands lying next to it on the grass (ORANGE, YELLOW, SKY-BLUE); {WAND31}; and {RING31}. No characters.", "Exactly three wands and one ring.", True, "Nothing moves except the soap shining."),
  ("후~", "C", MEADOW + f"{D['C']} holds one ORANGE bubble wand and blows clear shiny soap bubbles.", "", False, "Chiqui blows; five clear bubbles float up and drift. The camera stays still."),
  ("둥실둥실", "", MEADOW + "Clear shiny rainbow-sheen soap bubbles float above the meadow in the sunshine. No characters.", "", False, "Bubbles float up slowly; one pops."),
  ("방울 잡기", "CRP", MEADOW + "Chiqui, Roro and Pio jump to catch floating soap bubbles, laughing.", "", False, "They jump and pop a few bubbles with paws and beak."),
  ("로로가 후~", "R", MEADOW + f"{D['R']} holds one YELLOW bubble wand and blows bubbles.", "", False, "Roro blows; bubbles float up."),
  ("토롱이 후~", "T", MEADOW + f"{D['T']} stands right in front of one big GREEN bubble ring on a short stick stuck in the grass; the ring is right in front of Torong's mouth; Torong blows gently.", "Exactly one ring.", False,
   NEAR + "Torong blows a long breath; one very big shiny bubble grows out of the ring and floats away."),
  ("피오가 콕", "P", MEADOW + f"{D['P']} flies low and pops floating bubbles with the beak.", "", False, "Pio pops three bubbles one by one: pop, pop, pop."),
  ("방울방울", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio play among many floating soap bubbles.", "", False, "Bubbles float everywhere; the friends laugh. The camera stays still."),
  ("엄청 큰 방울!", "CRTP", MEADOW + "One very big shiny soap bubble floats above the meadow; Chiqui, Roro, Torong and Pio look up at it with open mouths.", "Exactly one giant bubble.", False, "The giant bubble floats slowly; the friends gasp."),
  ("누가 만들었을까?", "C", MEADOW + f"Close view of {D['C']} looking at the viewer, curious.", "", True, "Chiqui looks at the viewer and tilts the head."),
  ("토롱이 했지!", "CRTP", MEADOW + f"Torong smiles proudly standing next to {RING31}, with four feet on the ground; Chiqui, Roro and Pio cheer.", "", False, "The friends cheer; Torong nods proudly with four feet on the ground."),
  BAU(MEADOW, "공룡 알도 동글동글", "smiles wisely; a few round soap bubbles float around."),
  ("다 같이 퐁퐁", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio play with bubbles together.", "", False, "Bubbles float and the friends laugh."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 32화 둥둥 공룡 음악대 (악기) ----------------
INSTR = ("Roro's YELLOW hand drum, Torong's big GREEN floor drum standing on the grass, Pio's small SKY-BLUE recorder flute, Chiqui's pair of ORANGE maracas, "
         "and Grandpa Bau's big PURPLE floor drum standing on the grass")
EPS["ep32"] = dict(
 title="32화. 둥둥 공룡 음악대! — 악기 놀이", short="둥둥 공룡 음악대!", song_id="band", song_short="음악대",
 theme="악기 소리(북·큰북·피리·마라카스), 함께 연주. 악기는 친구 몸 색. 토롱은 꼬리로, 할아버지는 꼬리 곤봉으로 큰북!",
 twist="마지막에 \"쾅!\" 커다란 소리, 누구지? 할아버지 꼬리 곤봉이 보라 큰북을 쾅!",
 bau="안킬로사우루스 꼬리는 곤봉처럼 단단했단다!",
 lines=[("치키","음악대 하자!",""),("모두","좋아!","♻ 1화 07"),("모두","둥둥 쿵쿵 삐리리 찰찰!",""),("내레이션","쾅! 누구 소리일까?","뒤에 3초 쉼"),
        ("모두","할아버지다!",""),("바우","허허, 쾅!",""),("바우","안킬로사우루스 꼬리는 곤봉처럼 단단했단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("둥둥둥 노란 북","크앙! 로로가 둥둥","신나요 (둥둥!)"),("쿵쿵쿵 초록 큰북","쭈욱~ 토롱 꼬리로 쿵","신나요 (쿵쿵!)"),
         ("삐리리 하늘색 피리","슝~ 피오가 삐리리","신나요 (삐리리!)"),("찰찰찰 주황 마라카스","치키가 찰찰","신나요 (찰찰!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "둥둥 공룡 음악대 (둥둥!)", "다 같이 연주해요", "치키치키 음악대!"],
 scenes=scenes([
  ("악기가 가득", "", MEADOW + f"Close view of the instruments lying and standing on the grass: {INSTR}. No characters.", "Exactly these five instruments.", True, "Nothing moves; the instruments shine in the sun."),
  ("음악대 하자!", "C", MEADOW + f"{D['C']} holds the pair of ORANGE maracas up high, excited.", "", False, "Chiqui shakes the maracas once and cheers."),
  CHEER(MEADOW),
  BAU(MEADOW, "할아버지도", "stands next to the big PURPLE floor drum standing on the grass, smiling."),
  ("찰찰", "C", MEADOW + f"{D['C']} shakes the pair of ORANGE maracas, dancing.", "", False, "Chiqui shakes the maracas three times, bouncing."),
  ("음악대 출발", "CRTP", MEADOW + "Chiqui with ORANGE maracas, Roro with a YELLOW hand drum, Pio with a SKY-BLUE recorder in the beak, and Torong next to a big GREEN floor drum standing on the grass, all smiling.", "", False, "Everyone bobs to the beat. The camera stays still."),
  ("로로가 둥둥", "R", MEADOW + f"{D['R']} taps the YELLOW hand drum with both paws.", "", False, "Roro taps the drum four times, bouncing."),
  ("토롱 꼬리로 쿵", "T", MEADOW + f"{D['T']} stands next to the big GREEN floor drum on the grass and thumps it with the tip of the tail.", "Exactly one green drum.", False, "Torong swings the tail and taps the drum two times; four feet stay on the ground."),
  ("피오가 삐리리", "P", MEADOW + f"{D['P']} plays the small SKY-BLUE recorder held in the beak.", "", False, "Pio blows the recorder and sways; little music notes are NOT drawn."),
  ("다 같이 연주", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio play together, happy, each with ONLY their OWN instrument in their OWN body color (never swapped, never shared): Chiqui (orange) shakes the pair of ORANGE maracas, Roro (yellow) taps the YELLOW hand drum, Pio (sky-blue) plays the SKY-BLUE recorder in the beak, Torong (green) thumps the big GREEN floor drum standing on the grass with the tip of the tail. Exactly one of each instrument; no extra drums.", "", False, "Everyone plays and sways; the camera stays still."),
  ("쾅!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio jump a little, surprised with round open mouths, looking around; they still hold their OWN instruments in their OWN body color: Chiqui the pair of ORANGE maracas, Roro the YELLOW hand drum, Pio the SKY-BLUE recorder; the big GREEN floor drum stands on the grass next to Torong.", "", False, "The friends jump once, surprised, and look left and right."),
  ("누구 소리일까?", "C", MEADOW + f"Close view of {D['C']} holding the ORANGE maracas, looking at the viewer, curious.", "", True, "Chiqui looks at the viewer and tilts the head."),
  ("할아버지다!", "BCRTP", MEADOW + "Grandpa Bau swings the round tail club onto the big PURPLE floor drum standing on the grass; Chiqui, Roro, Torong and Pio cheer.", "", False,
   "Grandpa Bau swings the tail club and taps the purple drum once; all four of Grandpa Bau's feet stay on the grass; the friends cheer."),
  ("꼬리 곤봉", "B", MEADOW + f"Close view of {D['B']} proudly lifting the round tail club, smiling wisely.", "", True, "Grandpa Bau wiggles the tail club once and smiles."),
  ("음악대 행진", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio march in a line to the right, each with ONLY their OWN instrument in their OWN body color (never swapped): Chiqui (orange) shakes the pair of ORANGE maracas, Roro (yellow) taps the YELLOW hand drum, Pio (sky-blue) plays the SKY-BLUE recorder in the beak, and Torong (green) walks at the back carrying THE SAME GREEN drum (green with a cream zigzag rope and light-green leaf pattern, exactly like before, only Torong has a green drum) hanging on a soft strap on the chest, thumping it with the tip of the tail as it walks; all four of Torong's feet stay on the ground and Torong never uses the front legs on the drum.", "", False, "They march a few steps to the LEFT, playing. The camera stays still."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 33화 미안해, 괜찮아 (사과·화해) ----------------
FALLEN33 = "exactly THREE same-size YELLOW cube toy blocks (the same three cubes from the tower, no other blocks, no rectangles, no smaller pieces) lying scattered on the grass"
TOWER4 = "the block tower: exactly three same-size YELLOW cube blocks stacked straight up with exactly one same-size ORANGE cube block on top (four cubes in total, no other blocks, no other colors, no arch or triangle)"
TOWER = "one small tower of exactly three YELLOW square toy blocks stacked on the grass"
EPS["ep33"] = dict(
 title="33화. 미안해, 괜찮아! — 사과와 화해", short="미안해, 괜찮아!", song_id="sorry", song_short="미안해 노래",
 theme="실수했을 때 \"미안해\", 받아 주는 \"괜찮아\", 함께 다시 하기.",
 twist="치키가 공을 쫓다 로로 블록 탑을 와르르… \"미안해!\" \"괜찮아!\" 둘이 같이 더 높이 쌓아요.",
 bau="공룡 친구들도 서로 도왔단다!",
 lines=[("로로","높이 높이 쌓자!",""),("모두","와르르!",""),("내레이션","치키는 뭐라고 말할까?","뒤에 3초 쉼"),("치키","로로야, 미안해.",""),
        ("로로","괜찮아!",""),("모두","같이 쌓자!",""),("바우","공룡 친구들도 서로 도왔단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("앗! 와르르 무너졌어","치키가 툭 쳤어요","어떡하지? (어떡해!)"),("눈물이 글썽글썽","로로가 속상해요","훌쩍훌쩍 (훌쩍!)"),
         ("미안해 말해요","치키가 꼬옥","미안해 (미안해!)"),("괜찮아 웃어요","다시 쌓아요","같이 하자 (같이!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "미안해 괜찮아 (괜찮아!)", "손잡고 웃어요", "치키치키 친구!"],
 scenes=scenes([
  ("높이 쌓자!", "R", MEADOW + f"{D['R']} carefully builds {TOWER}, smiling proudly.", "Exactly three blocks.", False, "Roro places the top block gently and claps."),
  ("공놀이", "C", MEADOW + f"{D['C']} chases one rolling ORANGE ball across the meadow, not looking ahead.", "Exactly one ball.", False, "Chiqui runs after the ball, laughing."),
  ("와르르!", "CR", MEADOW + f"{D['C']} bumps into {TOWER} by accident; the blocks tumble down; {D['R']} gasps.", "", False, "The three yellow blocks fall onto the grass; Chiqui and Roro freeze, surprised."),
  ("무너졌어", "", MEADOW + "Close view of three YELLOW square toy blocks lying scattered on the grass. No characters.", "Exactly three blocks.", True, "Nothing moves."),
  ("훌쩍", "R", MEADOW + f"Close view of {D['R']} with teary eyes, sad, next to {FALLEN33}.", "", True, "Roro sniffles once; a small tear."),
  ("어떡하지?", "C", MEADOW + f"Close view of {D['C']} worried, paws near the mouth.", "", True, "Chiqui looks worried and blinks."),
  ("토롱·피오도 걱정", "TP", MEADOW + "Torong and Pio watch from a little way off with worried faces.", "", False, "They look at each other, worried."),
  ("다가가요", "CR", MEADOW + f"{D['C']} walks slowly to {D['R']}, who sits next to {FALLEN33} with a sad face and teary eyes (not smiling yet); Chiqui looks sorry.", "", False, "Chiqui takes two slow steps toward Roro."),
  ("미안해", "CR", MEADOW + f"Chiqui hugs Roro gently with a sorry face (eyebrows down, small apologetic smile, not laughing); Roro still has teary eyes and looks up; next to them lie {FALLEN33}.", "", False, "Chiqui hugs Roro; Roro looks up."),
  ("괜찮아!", "CR", MEADOW + "Roro smiles at Chiqui and holds Chiqui's paw.", "", False, "Roro smiles and nods; they hold paws."),
  ("같이 쌓자!", "CR", MEADOW + f"Chiqui and Roro stack the three YELLOW blocks together into a tower, smiling.", "Exactly three blocks.", False, "They stack the blocks one by one; the tower stands."),
  ("더 높이!", "CR", MEADOW + "Chiqui puts one ORANGE block on top of the three YELLOW blocks; the tower now has four blocks.", "Exactly four blocks.", False, "Chiqui sets the orange block on top; it stays; they cheer."),
  ("친구 최고", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio cheer around the tower of three yellow blocks and one orange block on top.", "", False, "The friends cheer; the tower stays standing."),
  BAU(MEADOW, "서로 도왔단다", f"stands smiling wisely next to {TOWER4}."),
  ("다시 공놀이", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio play gently with one ORANGE ball, far from the block tower.", "", False, "Chiqui rolls the ball to Roro, Roro rolls it to Pio; Torong watches with four feet on the grass."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 34화 나 혼자 입을래! (모자 쓰기) ----------------
BENCH = ("one low light-wood bench by the door with five knitted pompom hats on it, left to right: a small ORANGE hat, a YELLOW hat, a GREEN hat, a tiny SKY-BLUE hat and one big PURPLE hat")
EPS["ep34"] = dict(
 title="34화. 나 혼자 할래! — 모자 쓰기", short="나 혼자 할래!", song_id="myself", song_short="혼자서 노래",
 theme="스스로 하기(모자 쓰기), 내 물건 알기. 모자는 친구 몸 색.",
 twist="치키가 혼자 쓴 모자가 너무 커서 앞이 깜깜! 할아버지 보라 모자였어요. 할아버지는 작은 주황 모자를 쓰고… 바꿔 써요!",
 bau="아기 공룡도 알에서 나와 혼자 걸었단다!",
 lines=[("바우","밖에 나가자, 모자 쓰고!",""),("치키","나 혼자 할래!",""),("모두","혼자서 쏙!",""),("치키","어? 깜깜해!",""),
        ("내레이션","이건 누구 모자일까?","뒤에 3초 쉼"),("모두","할아버지 모자!",""),("모두","하하하!","♻ 3화 11"),
        ("바우","아기 공룡도 알에서 나와 혼자 걸었단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("노란 모자 쏙","크앙! 로로 혼자서","잘했어요 (쏙!)"),("초록 모자 쏙","쭈욱~ 토롱 고개 숙여","잘했어요 (쏙!)"),
         ("하늘색 모자 쏙","슝~ 피오 혼자서","잘했어요 (쏙!)"),("치키 모자는 너무 커","앞이 안 보여요 (깜깜!)","누구 모자? (누구?)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "나 혼자 할래요 (혼자서!)", "모자 쓰고 나가요", "치키치키 혼자서!"],
 scenes=scenes([
  ("모자가 가득", "", HOME + f"Close view of {BENCH}. No characters.", "Exactly five hats.", True, "Nothing moves."),
  BAU(HOME, "모자 쓰고 나가자", f"stands on all four feet next to {BENCH}, smiling."),
  ("나 혼자 할래!", "C", HOME + f"Close view of {D['C']} with a proud determined face, one paw on the chest.", "", True, "Chiqui nods proudly."),
  ("좋아!", "CRTP", HOME + f"Chiqui, Roro, Torong and Pio gather happily near {BENCH}.", "", False, "The friends bounce once, happy."),
  ("큰 모자 꼬옥", "C", HOME + f"{D['C']} hugs the big PURPLE pompom hat happily, not noticing it is too big.", "", False, "Chiqui hugs the purple hat and smiles."),
  ("로로 쏙", "R", HOME + f"{D['R']} puts the YELLOW pompom hat on the head by itself.", "", False, "Roro pulls the yellow hat on and claps; the hat stays on."),
  ("토롱 쏙", "T", HOME + f"{D['T']} bends the neck down and pushes the head into the GREEN pompom hat lying on the bench right in front of the mouth; the hat ends up on Torong's head.", "", False, NEAR + "Torong pushes the head into the hat and lifts the head; the green hat stays on."),
  ("피오 쏙", "P", HOME + f"{D['P']} puts the tiny SKY-BLUE pompom hat on the head with one wing.", "", False, "Pio tugs the hat on and flaps once; it stays on."),
  ("깜깜해!", "C", HOME + f"{D['C']} wears the big PURPLE pompom hat that slides down over the eyes and frill; Chiqui wobbles with paws out.", "", False, "Chiqui wobbles left and right, unable to see. Only one Chiqui."),
  ("하하하", "RTP", HOME + "Roro in a YELLOW hat, Torong in a GREEN hat and Pio in a SKY-BLUE hat laugh kindly.", "", False, "The friends laugh."),
  ("누구 모자일까?", "C", HOME + f"Close view of {D['C']} pushing the big PURPLE hat up from the eyes, looking at the viewer.", "", True, "Chiqui peeks out from under the hat and tilts the head."),
  ("바꿔 써요", "BC", HOME + "Grandpa Bau wears the small ORANGE pompom hat perched on top of the head; Chiqui wears the big PURPLE hat; they laugh.", "", False, "They laugh; Grandpa Bau's four feet stay on the floor."),
  ("딱 맞아!", "BC", HOME + "Now Chiqui wears the small ORANGE pompom hat and Grandpa Bau wears the big PURPLE pompom hat; both smile.", "", False, "Both nod happily; the hats stay on."),
  BAU(HOME, "혼자 걸었단다", "wears the big PURPLE pompom hat and smiles wisely."),
  ("밖으로!", "CRTP", MEADOW + "Chiqui in an ORANGE hat, Roro in a YELLOW hat, Torong in a GREEN hat and Pio in a SKY-BLUE hat walk out onto the meadow.", "", False, "They walk a few steps to the LEFT, happy."),
  WAVE(MEADOW, "안녕!", ", each wearing a pompom hat in their own body color (Grandpa Bau PURPLE)"),
 ]))

# ---------------- 35화 빨간불 멈춰요 (교통안전) ----------------
ROAD = ("THE SAME crossing in every scene, always seen from the same camera: one straight smooth sandy road runs from the BOTTOM of the picture straight up into the distance in the MIDDLE of the frame, "
        "dividing the meadow into a LEFT grass side and a RIGHT grass side; a white-striped crosswalk goes across the road from the LEFT side to the RIGHT side in the front; "
        "TWO identical toy-like traffic lights on short wooden posts, one at EACH end of the crosswalk: one on the LEFT grass side and one on the RIGHT grass side, each with two round lights, RED on top and GREEN below; both lights always show the SAME color at the same time. "
        "LEFT side = the waiting side (this side), RIGHT side = the other side. No cars. ")
LEFTW = "standing on the LEFT grass side next to the left traffic light, facing the road, clearly NOT on the road and NOT on the right side"
def ALL5(where_side, focus=""):
    side = "LEFT" if where_side == "L" else "RIGHT"
    empty = "RIGHT" if where_side == "L" else "LEFT"
    return (f"ALL FIVE friends are in this picture, together in one group on the {side} grass side: Grandpa Bau, Chiqui, Roro, Torong and Pio "
            f"(draw exactly one of each, nobody missing); the {empty} grass side and the road are empty of characters. {focus} ")
EPS["ep35"] = dict(
 title="35화. 빨간불 멈춰요! — 길 건너기", short="빨간불 멈춰요!", song_id="traffic", song_short="신호등 노래",
 theme="신호등(빨간불 멈춤·초록불 건넘), 좌우 살피기, 손잡고 건너기.",
 twist="치키가 공을 쫓아 길로 뛰어가려는데 빨간불! 친구들이 \"멈춰!\" 외치고 치키가 딱 멈춰요.",
 bau="공룡들도 무리 지어 천천히 함께 걸었단다!",
 lines=[("바우","빨간불은?",""),("모두","멈춰요!",""),("바우","초록불은?",""),("모두","건너요!",""),
        ("내레이션","치키는 어떻게 해야 할까?","뒤에 3초 쉼"),("모두","치키야, 멈춰!",""),("치키","휴~ 기다릴게요.",""),
        ("바우","공룡들도 무리 지어 천천히 함께 걸었단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("빨간불 반짝","크앙! 로로도 멈춰","기다려요 (멈춰!)"),("초록불 반짝","쭈욱~ 토롱 천천히","건너가요 (건너!)"),
         ("오른쪽 왼쪽","슝~ 피오가 살펴","잘 보고요 (살펴!)"),("치키가 공을 따라","빨간불인데 (멈춰!)","휴~ 기다려요 (휴~)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "빨간불 멈춰요 (멈춰!)", "초록불 건너요", "치키치키 안전!"],
 scenes=scenes([
  ("마을 길", "", ROAD + "Only the RED light is on. No characters, no cars.", "", False, "Nothing moves; the red light glows."),
  ("빨간불은?", "BCRTP", ROAD + ALL5("L", "Grandpa Bau stands in front next to the left traffic light, smiling and looking at the RED light; the others stand behind him and look at the light too.") + "Only the RED lights are on.", "", False, "Grandpa Bau nods toward the red light; the friends look and nod; nobody steps onto the road. Grandpa Bau keeps four feet on the ground. The camera stays still."),
  ("길가에 모여요", "BCRTP", ROAD + ALL5("L", "They all face the road and look at the left traffic light.") + "Only the RED lights are on.", "", False, "The friends wait and look at the light."),
  ("빨간불", "BCRTP", ROAD + ALL5("L", "Closer view: the LEFT traffic light stands big in the front on one side of the picture, only the top RED light is on, the green light is off; right next to it the five friends stand together on the LEFT grass and look up at the glowing RED light; the road and the right traffic light are still visible behind them.") + "Both traffic lights show only RED.", "", True, "The red light glows; the friends look up at it and nod once; nobody steps onto the road; four feet on the ground for Torong and Grandpa Bau. The camera stays still."),
  ("기다려요", "BCRTP", ROAD + ALL5("L", "They all wait calmly at the edge of the road.") + "Only the RED lights are on.", "", False, "They wait still and nod; nobody steps onto the road."),
  ("초록불", "BCRTP", ROAD + ALL5("L", "Closer view: the LEFT traffic light stands big in the front on one side of the picture, only the bottom GREEN light is on, the red light is off; right next to it the five friends stand together on the LEFT grass and look up at the glowing GREEN light; the road and the right traffic light are still visible behind them.") + "Both traffic lights show only GREEN.", "", True, "The green light glows; the friends look up at it and smile; nobody moves onto the road yet; four feet on the ground for Torong and Grandpa Bau. The camera stays still."),
  ("로로도 멈춰", "BCRTP", ROAD + ALL5("L", "Roro stands in FRONT of the group at the edge of the road with both paws at the sides, waiting; the others stand just behind Roro.") + "Only the RED lights are on.", "", False, "Roro waits and nods; Roro does not step onto the road."),
  ("토롱 천천히", "BCRTP", ROAD + ALL5("L", "Torong stands in FRONT of the group and slowly puts the front feet onto the first stripe of the crosswalk, starting to cross; the others still stand on the LEFT grass side just behind Torong.").replace("the LEFT grass side and the road are empty of characters", "x").replace("the RIGHT grass side and the road are empty of characters", "the RIGHT grass side is empty") + "Only the GREEN lights are on.", "", False, "Torong takes one slow step onto the crosswalk and waits there for the friends; the others stay on the left grass; four legs only. The camera stays still."),
  ("오른쪽 왼쪽", "BCRTP", ROAD + ALL5("L", "Pio stands in FRONT of the group at the edge of the crosswalk and looks to one side; the others stand just behind Pio."), "", False, "Pio turns the head right, then left, then nods."),
  ("공을 따라", "BCRTP", ROAD + ALL5("L", "Chiqui runs out of the group after one rolling ORANGE ball toward the road (the ball is about to roll onto the road), still on the LEFT grass; Grandpa Bau, Roro, Torong and Pio stay behind on the LEFT grass and look surprised.") + "Only the RED lights are on.", "Exactly one ball.", False, "Chiqui runs toward the road after the ball, not looking."),
  ("멈춰!", "BCRTP", ROAD + ALL5("L", "Chiqui is near the edge of the road with the ORANGE ball; Grandpa Bau, Roro, Torong and Pio, a little behind on the LEFT grass, call out STOP with worried faces toward Chiqui;")+" Roro and Pio hold up a paw and a wing; only the RED light is on.", "", False, "They call out once; Torong lifts the neck; four feet on the ground."),
  ("딱 멈춰요", "BCRTP", ROAD + ALL5("L", "Chiqui stops right at the edge of the road holding the ORANGE ball, not on the road, with a relieved face; Grandpa Bau, Roro, Torong and Pio stand just behind Chiqui, relieved.") + "Only the RED lights are on.", "", False, "Chiqui stops, sighs with relief and waits. Chiqui does not step onto the road."),
  ("다 같이 건너요", "BCRTP", ROAD + "Only the GREEN light is on; all five walk together on the crosswalk across the road from the LEFT side toward the RIGHT side, now in the middle of the road: Grandpa Bau leads in front (on the right), Chiqui and Roro hold paws, Pio walks next to them, Torong walks beside them.", "", False,
   "Everyone walks slowly to the RIGHT along the crosswalk toward the right grass side. The camera stays still."),
  ("함께 걸었단다", "BCRTP", ROAD + ALL5("R", "They have just crossed; Grandpa Bau stands in front, smiling wisely; the friends stand around him, happy.") + "Only the GREEN lights are on.", "", False, "Grandpa Bau nods once and smiles; four feet stay on the ground. The camera stays still."),
  ("안전하게 건넜어요", "BCRTP", ROAD + ALL5("R", "Chiqui, Roro, Torong and Pio cheer and jump; Grandpa Bau smiles next to them with four feet on the ground.") + "Only the GREEN lights are on.", "", False, "The friends cheer."),
  WAVE(MEADOW, "안녕!"),
 ]))

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

# ---------------- 37화 구름 모양 찾기 ----------------
SKYM = "On the soft green hill of the village under a bright blue sky with big fluffy white clouds. "
EPS["ep37"] = dict(
 title="37화. 구름 모양 찾기! — 상상 놀이", short="구름 모양 찾기!", song_id="cloud", song_short="구름 노래",
 theme="하늘 보기, 구름 모양 상상(알·긴 목·하트), 말로 표현하기.",
 twist="뿔이 세 개 달린 구름이 둥실! 누구 같아요? 치키 구름!",
 bau="구름이 비를 내려 공룡 숲을 키웠단다!",
 lines=[("치키","구름 좀 봐!",""),("모두","와아~","♻ 1화 15"),("로로","공룡알 같아!",""),("토롱","내 목 같아!",""),("피오","하트다!",""),
        ("내레이션","저 구름은 누구 같을까?","뒤에 3초 쉼"),("모두","치키 구름!",""),
        ("바우","구름이 비를 내려 공룡 숲을 키웠단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("동글동글 구름","크앙! 로로가 보니","공룡알 같아 (알!)"),("길쭉길쭉 구름","쭈욱~ 토롱이 보니","내 목 같아 (쭈욱!)"),
         ("폭신폭신 구름","슝~ 피오가 날아","하트 모양 (하트!)"),("뿔 세 개 구름","누구 같아요? (누구?)","치키 구름! (치키!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "구름 구름 무슨 모양? (모양?)", "하늘 보고 찾아요", "치키치키 구름!"],
 scenes=scenes([
  ("구름 좀 봐!", "", SKYM + "Big fluffy white clouds drift in the blue sky. No characters.", "", False, "Clouds drift slowly; nothing else moves."),
  ("누워서 봐요", "C", SKYM + f"{D['C']} lies on the back on the grass, looking up at the sky with a big smile.", "", False, "Chiqui points up and kicks the feet happily."),
  ("다 같이 누워요", "CRTP", SKYM + "Chiqui, Roro and Pio lie on their backs on the grass; Torong lies on the belly with legs folded under and the long neck up; all look at the sky.", "", False, "They look up and smile; nobody gets up."),
  BAU(SKYM, "할아버지도", "sits on the grass nearby looking up at the clouds, smiling."),
  ("동그란 구름", "", SKYM + "One big round egg-shaped white cloud in the blue sky. No characters.", "Exactly one egg-shaped cloud in focus.", True, "The cloud drifts slowly."),
  ("손가락으로 콕", "C", SKYM + f"{D['C']} lying on the grass points up at the sky.", "", False, "Chiqui points up two times and giggles."),
  ("공룡알 같아", "R", SKYM + f"{D['R']} lying on the grass points at one big round egg-shaped cloud.", "", False, "Roro points and laughs."),
  ("내 목 같아", "T", SKYM + f"{D['T']} lies on the belly on the grass, looking up at one long thin curved cloud shaped like a long neck.", "", False, "Torong lifts the head a little and smiles; legs stay folded."),
  ("하트다!", "P", SKYM + f"{D['P']} flies up near one heart-shaped white cloud.", "", False, "Pio circles once near the heart cloud and flaps happily."),
  ("하늘 구경", "CRTP", SKYM + "Chiqui, Roro, Torong and Pio lie on the grass watching the clouds together.", "", False, "Clouds drift; the friends smile."),
  ("뿔 세 개 구름", "RTP", SKYM + "Roro, Torong and Pio point up at one white cloud that has three little horn-shaped bumps and a round frill shape, like Chiqui's head.", "", False, "They point and gasp."),
  ("누구 같을까?", "C", SKYM + f"Close view of {D['C']} lying on the grass, looking at the viewer, curious.", "", True, "Chiqui looks at the viewer and tilts the head."),
  ("치키 구름!", "CRTP", SKYM + "Chiqui laughs and points at the cloud with three horn bumps; Roro, Torong and Pio cheer.", "", False, "Everyone laughs and cheers."),
  BAU(SKYM, "구름이 비를 내려", "sits on the grass looking up at a soft grey rain cloud far away over green forests, smiling wisely."),
  ("해 질 녘 하늘", "CRTP", SKYM.replace("bright blue sky", "soft pink sunset sky") + "Chiqui, Roro, Torong and Pio sit together on the hill watching pink clouds.", "", False, "They sway gently, happy."),
  WAVE(SKYM, "안녕!"),
 ]))

# ---------------- 38화 할아버지, 사랑해요 (카드 만들기) ----------------
CARD = ("one big cream-white paper card lying flat on a low wooden table; the four drawing spots on it are fixed: top-left, top-right, bottom-left, bottom-right")
EPS["ep38"] = dict(
 title="38화. 할아버지, 사랑해요! — 마음 전하기", short="할아버지, 사랑해요!", song_id="love", song_short="사랑해요",
 theme="고마운 사람에게 마음 전하기, 카드 만들기. 친구마다 몸 색 하트.",
 twist="쿨쿨 자는 할아버지 몰래 만든 카드! 할아버지가 깨어나 카드를 보고 눈물 글썽… 다 같이 꼬옥!",
 bau="공룡 할아버지 할머니도 아기 공룡을 지켜 줬단다!",
 lines=[("치키","쉿! 할아버지 주무셔.",""),("모두","카드 만들자!",""),("모두","사랑해요!",""),("내레이션","할아버지는 뭐라고 할까?","뒤에 3초 쉼"),
        ("바우","고맙구나, 얘들아!",""),("모두","사랑해요, 할아버지!",""),
        ("바우","공룡 할아버지 할머니도 아기 공룡을 지켜 줬단다!","바우 할아버지 상식"),("치키","안녕!","♻ 1화 18")],
 verses=[("노란 하트 쓱쓱","크앙! 로로가 그려요","사랑해요 (사랑해!)"),("초록 하트 콩","쭈욱~ 토롱 코로 콩","사랑해요 (사랑해!)"),
         ("하늘색 발자국 콩콩","슝~ 피오가 콩콩","사랑해요 (사랑해!)"),("주황 하트 크게","치키가 쓱쓱","할아버지께 (짠!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "사랑해요 할아버지 (사랑해요!)", "마음 담아 그려요", "치키치키 사랑해!"],
 scenes=scenes([
  ("쿨쿨", "B", MEADOW + f"{D['B']} dozes on the warm grass with eyes closed, lying on the belly with legs folded, smiling.", "", False, "Grandpa Bau breathes slowly, asleep."),
  ("쉿!", "C", MEADOW + f"Close view of {D['C']} with one paw in front of the mouth, whispering an idea.", "", True, "Chiqui whispers 'shh' and winks."),
  ("카드 만들자!", "CRTP", MEADOW + "Chiqui, Roro, Torong and Pio huddle together quietly, smiling.", "", False, "They nod quietly and tiptoe in place."),
  ("하얀 카드", "", MEADOW + f"Close view of {CARD}, completely blank, with one ORANGE crayon, one YELLOW crayon, one small cup of GREEN paint and one small cup of SKY-BLUE paint next to it. No characters.", "", True, "Nothing moves."),
  ("탁자에 모여요", "CRTP", MEADOW + f"Chiqui, Roro, Torong and Pio gather around {CARD}; the card is still blank.", "", False, "They look at the blank card, excited."),
  BAU(MEADOW, "아직 쿨쿨", "is still asleep on the grass, lying on the belly with legs folded, smiling in the sleep."),
  ("노란 하트", "R", MEADOW + f"{D['R']} draws one YELLOW heart with a YELLOW crayon in the top-right spot of {CARD}; the other spots are still blank.", "", False, "Roro draws the heart; it stays on the card."),
  ("초록 하트 콩", "T", MEADOW + f"{D['T']} dips the nose in the small cup of GREEN paint and boops one GREEN heart-shaped nose print in the bottom-left spot of {CARD}, which is right in front of Torong's mouth; a YELLOW heart is already top-right.", "", False,
   NEAR + "Torong boops the card once and lifts the head with a green nose tip, giggling; the green print stays."),
  ("하늘색 발자국", "P", MEADOW + f"{D['P']} dips the feet in SKY-BLUE paint and stamps two tiny SKY-BLUE footprints in the bottom-right spot of {CARD}; a YELLOW heart (top-right) and a GREEN nose heart (bottom-left) are already there.", "", False, "Pio hops on the card spot two times; two footprints stay."),
  ("주황 하트 크게", "C", MEADOW + f"{D['C']} draws one big ORANGE heart with an ORANGE crayon in the top-left spot of {CARD}; now the card has an ORANGE heart top-left, a YELLOW heart top-right, a GREEN nose heart bottom-left and two SKY-BLUE footprints bottom-right.", "", False, "Chiqui finishes the heart and claps; the card is complete."),
  ("살금살금", "CRTP", MEADOW + "Chiqui and Roro carry the finished card together, tiptoeing; Torong and Pio tiptoe behind toward sleeping Grandpa Bau (not shown).", "", False, "They tiptoe two steps to the LEFT, giggling quietly."),
  ("할아버지 깼다!", "B", MEADOW + f"Close view of {D['B']} waking up, blinking, surprised.", "", True, "Grandpa Bau opens the eyes and blinks two times."),
  ("고맙구나", "BCRTP", MEADOW + "The finished card stands on the grass in front of Grandpa Bau; Grandpa Bau, on all four feet, looks at it with happy teary eyes; Chiqui, Roro, Torong and Pio hug Grandpa Bau from the sides.", "", False,
   "The friends hug Grandpa Bau; Grandpa Bau smiles with happy tears; all four of Grandpa Bau's feet stay on the grass."),
  BAU(MEADOW, "지켜 줬단다", "stands next to the card on the grass, smiling wisely."),
  ("다 같이 꼬옥", "BCRTP", MEADOW + "All five friends sit close together on the grass, smiling, the card in front of them.", "", False, "They lean together happily."),
  WAVE(MEADOW, "안녕!"),
 ]))

# ---------------- 39화 별 하나 나 하나 (밤하늘·세기) ----------------
NIGHT = "On the soft hill of the village at night, deep blue sky, a calm glow over the far volcano, round cave houses with warm windows. "
EPS["ep39"] = dict(
 title="39화. 별 하나 나 하나! — 별 세기", short="별 하나 나 하나!", song_id="star", song_short="별 노래",
 theme="밤하늘 별 하나~다섯 세기, 별똥별 소원 빌기, 잠자리 인사.",
 twist="별을 다 세었는데 슝~ 별똥별! 다 같이 눈 감고 소원: \"계속 계속 친구 해 주세요!\"",
 bau="공룡들도 이 별을 올려다봤단다!",
 lines=[("내레이션","밤이 되었어요.",""),("치키","별이다!",""),("모두","하나, 둘, 셋, 넷, 다섯!",""),("모두","별똥별이다!",""),
        ("내레이션","무슨 소원을 빌까?","뒤에 3초 쉼"),("치키","계속 친구 해 주세요!",""),
        ("바우","공룡들도 이 별을 올려다봤단다!","바우 할아버지 상식"),("모두","잘 자!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("별 하나 반짝","크앙! 로로가 찾고","하나 (반짝!)"),("별 둘 반짝","쭈욱~ 토롱이 찾고","둘 (반짝!)"),
         ("별 셋 반짝","슝~ 피오가 찾고","셋 (반짝!)"),("별 넷 다섯 반짝","치키도 찾고","넷, 다섯! (반짝!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "별 하나 나 하나 (반짝!)", "하늘 보고 세어요", "치키치키 반짝!"],
 scenes=scenes([
  ("밤이 되었어요", "", NIGHT + "Exactly ONE bright star twinkles in the sky. No characters.", "Exactly one star.", False, "The star twinkles; nothing else moves."),
  ("별이다!", "C", NIGHT + f"{D['C']} points up at exactly ONE bright star.", "Exactly one star.", False, "Chiqui points and smiles."),
  BAU(NIGHT, "별 보러 가자", "sits on the hill, smiling, looking up."),
  ("다 같이 언덕에", "CRTP", NIGHT + "Chiqui, Roro, Torong and Pio sit together on a soft blanket on the hill, looking up.", "", False, "They look up quietly."),
  ("하늘", "", NIGHT + "Close view of the deep blue night sky with exactly ONE bright star. No characters.", "Exactly one star.", True, "The star twinkles."),
  ("담요 위에", "CRTP", NIGHT + "Chiqui, Roro and Pio lie on a soft blanket; Torong lies on the belly with legs folded; all looking up.", "", False, "They smile and point up."),
  ("별 하나", "R", NIGHT + f"{D['R']} points up at exactly ONE bright star.", "Exactly one star.", False, "Roro points and counts one."),
  ("별 둘", "T", NIGHT + f"{D['T']} lifts the head toward exactly TWO bright stars.", "Exactly two stars.", False, "Torong nods two times toward the stars; legs stay folded."),
  ("별 셋", "P", NIGHT + f"{D['P']} flies low near exactly THREE bright stars.", "Exactly three stars.", False, "Pio glides once and flaps happily."),
  ("넷, 다섯!", "C", NIGHT + f"{D['C']} points up at exactly FIVE bright stars.", "Exactly five stars.", False, "Chiqui points at the stars one by one and claps."),
  ("별똥별!", "CRTP", NIGHT + "One shooting star streaks across the sky; Chiqui, Roro, Torong and Pio gasp and point.", "Exactly one shooting star.", False, "The shooting star streaks across once; the friends gasp."),
  ("소원을 빌어요", "C", NIGHT + f"Close view of {D['C']} with eyes closed and paws together, making a wish.", "", True, "Chiqui closes the eyes and smiles, wishing."),
  ("다 같이 소원", "BCRTP", NIGHT + "All five friends sit together with eyes closed, making a wish; stars twinkle above.", "", False, "They sit quietly with eyes closed, smiling."),
  BAU(NIGHT, "공룡들도 이 별을", "looks up at the stars, smiling wisely."),
  ("하암~", "CRTP", NIGHT + "Chiqui, Roro, Torong and Pio yawn sleepily on the blanket.", "", False, "They yawn one by one and rub their eyes."),
  WAVE(NIGHT, "잘 자!"),
 ]))

# ---------------- 40화 치키 타운 대축제 (40화 특집) ----------------
LANT = ("THE SAME string of exactly five round paper lanterns hanging between two wooden posts across the village square, left to right as seen by the viewer: "
        "ORANGE, YELLOW, GREEN, SKY-BLUE, PURPLE")
SQUARE = "In the village square in the evening, soft purple-orange sky, round cave houses around. "
EPS["ep40"] = dict(
 title="40화. 치키 타운 대축제! — 40화 특집", short="치키 타운 대축제!", song_id="festival", song_short="축제 노래",
 theme="40화 기념 축제: 등불 켜기, 친구마다 장기자랑(춤·흔들흔들·빙글·노래), 다 함께.",
 twist="등불이 하나씩 켜지는데 보라 등불만 깜깜… 다 같이 \"하나 둘 셋!\" 외치면 할아버지 보라 등불도 반짝!",
 bau="공룡들도 함께 모여 살았단다!",
 lines=[("치키","오늘은 대축제!",""),("모두","좋아!","♻ 1화 07"),("바우","등불을 켜자!",""),("모두","와아~","♻ 1화 15"),
        ("내레이션","보라 등불은 왜 깜깜할까?","뒤에 3초 쉼"),("모두","하나, 둘, 셋!",""),("바우","고맙구나!",""),
        ("바우","공룡들도 함께 모여 살았단다!","바우 할아버지 상식"),("모두","치키치키 출발!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("노란 등불 반짝","크앙! 로로 춤추고","축제다 (와!)"),("초록 등불 반짝","쭈욱~ 토롱 흔들흔들","축제다 (와!)"),
         ("하늘색 등불 반짝","슝~ 피오 빙글빙글","축제다 (와!)"),("주황 등불 반짝","치키가 노래해요","다 같이 (와아!)")],
 chorus_lines=["쿵쿵 쾅! 쿵쿵 쾅!", "치키 타운 대축제 (축제!)", "다 같이 춤춰요", "치키치키 출발!"],
 scenes=scenes([
  ("축제 날", "", SQUARE + f"{LANT}; none of the lanterns are lit yet. No characters.", "Exactly five lanterns, all dark.", False, "Nothing moves except the lanterns swaying a little."),
  ("오늘은 대축제!", "C", SQUARE + f"{D['C']} jumps with joy under {LANT}; all lanterns still dark.", "", False, "Chiqui jumps once and cheers."),
  BAU(SQUARE, "등불을 켜자!", f"stands under {LANT}, smiling; all lanterns still dark."),
  CHEER(SQUARE),
  ("등불이 반짝", "", SQUARE + f"{LANT}: the ORANGE, YELLOW, GREEN and SKY-BLUE lanterns glow warmly; the PURPLE lantern on the far right stays dark. No characters.", "", False,
   "The four lanterns glow; the purple lantern stays dark the whole time."),
  ("치키 춤", "C", SQUARE + f"{D['C']} dances under {LANT}; four lanterns glow, the PURPLE one is dark.", "", False, "Chiqui hops and twirls once."),
  ("로로 춤", "R", SQUARE + f"{D['R']} dances happily under the glowing lanterns; the PURPLE lantern is dark.", "", False, "Roro wiggles and hops three times."),
  ("토롱 흔들흔들", "T", SQUARE + f"{D['T']} sways the long neck left and right under the glowing lanterns; the PURPLE lantern is dark.", "", False, "Torong sways the neck three times; four feet on the ground."),
  ("피오 빙글빙글", "P", SQUARE + f"{D['P']} flies in one loop under the glowing lanterns; the PURPLE lantern is dark.", "", False, "Pio flies one small circle and lands."),
  ("치키 노래", "C", SQUARE + f"{D['C']} sings happily with arms open under the glowing lanterns; the PURPLE lantern is dark.", "", False, "Chiqui sings and sways."),
  ("보라 등불은?", "CRTP", SQUARE + f"Chiqui, Roro, Torong and Pio look up at the dark PURPLE lantern at the far right of {LANT}; the other four glow.", "", False, "They look up and tilt their heads."),
  ("왜 깜깜할까?", "C", SQUARE + f"Close view of {D['C']} looking at the viewer, curious, warm lantern glow on the face.", "", True, "Chiqui looks at the viewer and tilts the head."),
  ("하나 둘 셋!", "BCRTP", SQUARE + f"All five friends call out together under {LANT}; now the PURPLE lantern glows too, all five glow.", "", False,
   "They call out; the purple lantern lights up and glows; everyone cheers."),
  BAU(SQUARE, "함께 모여 살았단다", f"stands under {LANT}, all five glowing, smiling wisely."),
  ("다 같이 춤", "BCRTP", SQUARE + f"All five friends dance together under {LANT}, all glowing.", "", False, "Everyone dances; Torong sways the neck; Grandpa Bau's four feet stay on the ground."),
  WAVE(SQUARE, "치키치키 출발!", f" under {LANT}, all glowing"),
 ]))

for ep, e in EPS.items():
    write(ep, e)

# ---------- 공통 컷 (2026-11-24, 사용자: 같은 배경·같은 장면은 여러 번 만들지 않기) ----------
# 26~40화에서 그림 프롬프트가 똑같은 장면은 한 번만 만들고 episodes/common/의 그림·영상을 같이 쓴다.
import collections as _col, json as _json
_COMMON_NAME = {"안녕!": "ending_meadow", "좋아!": "cheer_meadow"}
_groups = _col.defaultdict(list)
for _ep in EPS:
    _f = Path(__file__).resolve().parent.parent / f"episodes/{_ep}/scenes.json"
    for _s in _json.loads(_f.read_text(encoding="utf-8")):
        _groups[_s["img"]].append((_ep, _s["id"], _s["name"]))
_mark = {}
for _img, _v in _groups.items():
    if len(_v) > 1:
        _cid = _COMMON_NAME.get(_v[0][2], f"common_{_v[0][0]}_{_v[0][1]}")
        for _ep, _sid, _ in _v: _mark[(_ep, _sid)] = _cid
for _ep in EPS:
    _f = Path(__file__).resolve().parent.parent / f"episodes/{_ep}/scenes.json"
    _sc = _json.loads(_f.read_text(encoding="utf-8"))
    for _s in _sc:
        if (_ep, _s["id"]) in _mark: _s["common"] = _mark[(_ep, _s["id"])]
        else: _s.pop("common", None)
    _f.write_text(_json.dumps(_sc, ensure_ascii=False, indent=1), encoding="utf-8")
