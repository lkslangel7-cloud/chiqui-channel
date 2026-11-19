"""6~10화 대본·가사·장면 프롬프트를 한 번에 만든다. (규칙: CLAUDE.md 3장 안전 문장)
사용법: python3 -I prompts/make_ep06_10.py
"""
import json
from pathlib import Path
R = Path(__file__).resolve().parent.parent
STYLE = "Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text."
D = {"C": "Chiqui, the orange baby triceratops with a yellow-spotted frill", "R": "Roro, the yellow baby T-rex with orange spots on the back (round head, no frill, no horns)",
     "T": "Torong, the green baby brachiosaurus with light-green spots", "P": "Pio, the little sky-blue pteranodon with a yellow beak",
     "B": "Grandpa Bau, the purple ankylosaurus with round glasses and white eyebrows"}
AT = {"C": "@chiqui", "R": "@roro", "T": "@torong", "P": "@pio", "B": "@bau"}
NM = {"C": "Chiqui", "R": "Roro", "T": "Torong", "P": "Pio", "B": "Grandpa Bau"}
COL = {"C": "ORANGE", "R": "YELLOW", "T": "GREEN", "P": "SKY-BLUE", "B": "PURPLE"}
TALL = " SIZE RULE: Torong is MUCH TALLER than everyone else, with a very long neck, and Torong's head is high above all the other friends' heads; Pio is the smallest."
NOHANDS = " Torong never touches the face with front legs."
NOCOPY = "Do NOT add any baby, child, twin, copy, parent, or smaller or bigger version of any character. "
END = "One continuous shot with no cuts and no scene changes. Keep every character exactly as in the start image and keep the soft 3D clay style unchanged. No new characters appear. Gentle, smooth motion."
FULL = "Show every character's full body from head to feet, with empty space around them; nothing is cut off at the edges. Keep the characters in the middle of the frame. "

def img(refs, scene, extra="", close=False):
    if "night" in scene.lower() or "dusk" in scene.lower() or "sunset" in scene.lower(): scene += " NO rainbow anywhere."
    head = ("Characters: " + "; ".join(f"{AT[c]} is {D[c]}" for c in refs) + ". Draw them exactly like their element images. ") if refs else ""
    cnt = (f" Draw exactly one of each character, never duplicated ({len(refs)} character{'s' if len(refs) > 1 else ''} in total).") if refs else " No characters in this scene."
    size = TALL if ("T" in refs and len(refs) > 1) else ""
    nh = NOHANDS if "T" in refs else ""
    return (f"Wide horizontal 16:9 landscape image, like a TV screen (1920x1080), not square. {head}{scene}{size}{nh}{cnt}"
            f"{(' ' + extra) if extra else ''} {'' if close else FULL}Match the art style, colors, textures and lighting of @village (style only, do not copy its layout). {STYLE}")

def vid(refs, action):
    if len(refs) == 1:
        only = f"The camera stays still. {NM[refs]} is the only creature in the frame. ONLY {NM[refs]} is in this scene from start to end; no other character, animal or creature appears at any time. "
    elif refs:
        only = f"ONLY these {len(refs)} characters are in this scene: {', '.join(NM[r] for r in refs)}; no other character, animal or creature appears at any time. "
    else:
        only = "No characters, animals or creatures appear at any time. "
    size = "Torong stays much taller than everyone with a long neck the whole time. " if ("T" in refs and len(refs) > 1) else ""
    look = ""  # 4화에서 배운 것: 피오가 동그란 새로, 로로가 트리케라톱스로 바뀜
    if "P" in refs: look += "Pio always keeps wide thin sky-blue pteranodon wings, a pointed crest on the head and a long yellow beak; Pio never turns into a round bird or a chick. "
    if "R" in refs: look += "Roro always keeps a round head with no frill and no horns. "
    cam = "" if len(refs) == 1 else ("The camera stays still: no zoom and no camera move; every character stays fully inside the frame from start to end. " if len(refs) > 1 else "")
    return f"{action} {only}{size}{look}{cam}{NOCOPY}{END}"

def items(word, refs):  # 친구 몸 색 물건 못박기
    return " ".join(f"{NM[r]} holds a {COL[r]} {word};" for r in refs) + f" Each {word} matches its owner's body color; no other colors."

EPS = {}
# ---------------- 6화 손 씻기 ----------------
SOAP = "small round bar of soap"
EPS["ep06"] = dict(
 title="6화. 비누야 어디 있니? — 손 씻기", short="비누야 어디 있니?", song_id="soap", song_short="비누 찾기",
 theme="손 씻기 습관 (거품 뽀글뽀글, 손을 싹싹), 친구와 함께 찾기. 친구마다 자기 몸 색 비누.",
 twist="치키 주황 비누는 진흙 웅덩이 속에 있었다.",
 bau="거품 뽀글뽀글, 손을 싹싹!",
 lines=[("치키","흙놀이 하자!",""),("치키","손이 지저분해!",""),("바우","이리 와서 손 씻자!",""),("치키","어? 비누가 없다!",""),
        ("치키","친구들아, 같이 찾자!","♻ 1화 06"),("모두","좋아!","♻ 1화 07"),("내레이션","치키 비누는 어디 있을까?","뒤에 3초 쉼"),
        ("치키","진흙 속에 있었네!",""),("모두","하하하!","♻ 3화 11"),("바우","거품 뽀글뽀글!",""),("바우","손을 싹싹!",""),("모두","싹싹싹!",""),
        ("내레이션","손이 어떻게 됐을까?","뒤에 2초 쉼"),("모두","깨끗해!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("바위 뒤에 몽글몽글","크앙! 로로가 찾았다","노란 비누 찾았다 (비누!)"),("나무 위에 몽글몽글","쭈욱~ 토롱이 찾았다","초록 비누 찾았다 (비누!)"),
         ("구름 위에 몽글몽글","슝~ 피오가 찾았다","파란 비누 찾았다 (비누!)"),("치키 비누 어디 있니?","두리번 두리번 (어디 있지?)","주황 주황 내 비누 (어디?)")],
 chorus="비누야 어디 있니?",
 scenes=[
  ("S02","흙놀이 하자!","0:20–0:30","BCRTP",10,img("BCRTP","On a sunny meadow, Chiqui, Roro, Torong and Pio happily play in a big soft brown mud puddle, their paws and feet covered in mud, while Grandpa Bau watches smiling from the side.","Only paws, feet and legs are muddy; faces stay clean."),vid("BCRTP","The friends stomp and splash in the mud puddle, laughing; Grandpa Bau chuckles.")),
  ("S03","손이 지저분해!","0:30–0:35","C",5,img("C",f"Close view of {D['C']} holding up both front paws covered in brown mud, looking at them with a surprised, funny face.","",True),vid("C","Chiqui looks at the muddy paws, wiggles the fingers and makes a funny surprised face.")),
  ("S04","이리 와서 손 씻자!","0:35–0:40","B",5,img("B",f"{D['B']} stands next to a round stone wash basin with clear water and an empty little wooden soap dish, waving one front paw kindly.","No soap anywhere."),vid("B","Grandpa Bau waves kindly and points at the wash basin with a warm smile.")),
  ("S05","어? 비누가 없다!","0:40–0:45","C",5,img("C",f"{D['C']} with muddy paws stands at the round stone wash basin, looking at the EMPTY wooden soap dish with big surprised eyes and an open mouth.","No soap anywhere in this scene."),vid("C","Chiqui looks at the empty soap dish, jumps a little in surprise and looks left and right.")),
  ("S06","친구들아, 같이 찾자!","0:45–0:50","C",5,img("C",f"{D['C']} stands in a sunny meadow, waving both arms high, calling out to friends far away.",""),vid("C","Chiqui waves both arms and calls out happily toward the distance.")),
  ("S07","좋아!","0:50–0:55","CRTP",5,img("CRTP","Roro, Torong and Pio (flying low) gather around Chiqui on a sunny meadow, all nodding and smiling eagerly.","No soap in this scene."),vid("CRTP","The friends nod together and cheer, bouncing a little with excitement.")),
  ("S09","로로 · 노란 비누","1:05–1:15","R",10,img("R",f"{D['R']} peeks behind a big round play rock and finds one YELLOW {SOAP} with a few soft bubbles, lying in the grass.","Exactly one yellow soap."),vid("R","Roro picks up the yellow soap, holds it up high and does a cute happy roar, wiggling with joy; a few bubbles float up.")),
  ("S10","토롱 · 초록 비누","1:15–1:25","T",10,img("T",f"{D['T']} stretches the very long neck up toward a high branch of a big leafy tree where one GREEN {SOAP} is resting.","Exactly one green soap."),vid("T","Torong stretches the neck up slowly, gently takes the green soap in the mouth, brings it down and smiles proudly. The soap stays green.")),
  ("S11","피오 · 파란 비누","1:25–1:35","P",10,img("P",f"{D['P']} flies above soft fluffy cloud hills holding one SKY-BLUE {SOAP} in the beak.","Exactly one sky-blue soap."),vid("P","Pio flies across the cloud hills with the sky-blue soap, doing one gentle swoop; a few bubbles trail behind.")),
  ("S12","치키 비누는?","1:35–1:45","C",10,img("C",f"Front view of {D['C']} with muddy paws standing alone near the mud puddle, looking around with a puzzled, slightly sad face.","No soap visible anywhere."),vid("C","Chiqui looks left, then right, then down, searching; the shoulders droop a little.")),
  ("S13","같이 찾아 줄게","1:45–1:55","CRTP",10,img("CRTP","Roro, Torong and Pio come to Chiqui, who has no soap. "+items("soap",["R","T","P"]).replace("holds a","holds one")+" They look around kindly together.","Exactly three soaps: yellow, green, sky-blue. No orange soap."),vid("CRTP","The friends gather around Chiqui, give a gentle pat, and all look around together. The soaps keep their colors: yellow, green, sky-blue.")),
  ("S14","치키 비누는 어디 있을까?","1:55–2:00","C",5,img("C",f"Close-up of {D['C']} facing the viewer with a curious face, head tilted, as if asking a question.","",True),vid("C","Chiqui tilts the head, blinks and looks at the viewer as if asking 'Where is it?'.")),
  ("S15","진흙 속에 있었네!","2:00–2:10","C",10,img("C",f"{D['C']} kneels at the mud puddle and pulls one ORANGE {SOAP} out of the brown mud, laughing with surprise.","Exactly one orange soap."),vid("C","Chiqui lifts the orange soap out of the mud, looks at it and laughs happily; the soap stays orange.")),
  ("S16","거품 뽀글뽀글, 손을 싹싹!","2:10–2:20","B",10,img("B",f"Close view of {D['B']} at the stone wash basin rubbing both front paws together with one PURPLE {SOAP}, making lots of soft white bubbles.","Exactly one purple soap.",True),vid("B","Grandpa Bau rubs the paws together with the soap, round and round; soft white bubbles grow, then he rinses the paws in the water and smiles.")),
  ("S17","싹싹싹!","2:20–2:30","BCRTP",10,img("BCRTP","All five friends stand at a long round stone wash basin washing their front paws with soft white bubbles. "+items(SOAP,list("CRTPB")),"Exactly five soaps: orange, yellow, green, sky-blue, purple."),vid("BCRTP","All five friends wash their front paws at the same time with big, clear, bouncy movements. First they lift both front paws up above the basin and rub them together quickly, round and round, six times, so big fluffy piles of white bubbles grow on their paws. Then they dip their paws into the water with a splash and lift them up again, showing shiny clean paws and giggling. The washing motion is large and easy to see. Each soap keeps its color: Chiqui orange, Roro yellow, Torong green, Pio sky-blue, Grandpa Bau purple. Torong washes with the front paws at the basin and never touches the face.")),
  ("S18","깨끗해!","2:30–2:40","BCRTP",10,img("BCRTP","All five friends stand in a row facing the viewer, holding up clean shiny front paws with big happy smiles, next to the stone wash basin.","No mud on anyone."),vid("BCRTP","Everyone shows their clean paws to the viewer, then cheers and bounces happily together.")),
 ])
# ---------------- 7화 숫자 1~10 ----------------
AP = "round shiny red apple"
EPS["ep07"] = dict(
 title="7화. 사과야 어디 있니? — 하나부터 열까지", short="사과야 어디 있니?", song_id="apple", song_short="사과 따기",
 theme="1~10 세기, 친구와 함께 모으기. 친구마다 자기 몸 색 바구니(사과는 빨강).",
 twist="네 친구가 2개씩 8개 → 할아버지가 나무를 흔들어 아홉, 열!",
 bau="다 같이 모으니 열 개!",
 lines=[("바우","사과 열 개 따러 가자!",""),("치키","와, 사과 나무다!",""),("치키","친구들아, 같이 따자!",""),("모두","좋아!","♻ 1화 07"),
        ("내레이션","몇 개 남았을까?","뒤에 2초 쉼"),("바우","아홉, 열!",""),("내레이션","다 같이 세어 볼까?",""),
        ("모두","하나, 둘, 셋, 넷, 다섯, 여섯, 일곱, 여덟, 아홉, 열!","천천히"),("바우","다 같이 모으니 열 개!",""),("모두","와아~","♻ 1화 15"),("모두","냠냠, 맛있다!",""),("치키","안녕!","♻ 1화 18")],
 verses=[("낮은 가지 동글동글","크앙! 로로가 땄어요","하나, 둘 (둘!)"),("높은 가지 동글동글","쭈욱~ 토롱이 땄어요","셋, 넷 (넷!)"),
         ("꼭대기에 동글동글","슝~ 피오가 땄어요","다섯, 여섯 (여섯!)"),("폴짝 뛰어 동글동글","짠! 치키가 땄어요","일곱, 여덟 (여덟!)")],
 chorus="사과야 어디 있니?",
 scenes=[
  ("S02","사과 열 개 따러 가자!","0:20–0:30","BCRTP",10,img("BCRTP","On a sunny meadow, Grandpa Bau holds one big empty PURPLE basket and smiles at Chiqui, Roro, Torong and Pio, who cheer excitedly.","Exactly one basket. No apples yet."),vid("BCRTP","Grandpa Bau lifts the empty basket and nods; the friends cheer and bounce.")),
  ("S03","와, 사과 나무다!","0:30–0:40","C",10,img("C",f"{D['C']} stands in front of a big round apple tree full of {AP}s, looking up with wide happy eyes and an open mouth.",""),vid("C","Chiqui looks up at the apple tree, gasps happily and claps.")),
  ("S04","바구니 하나씩","0:40–0:45","CRTP",5,img("CRTP","Chiqui, Roro, Torong and Pio stand under the apple tree, each holding a small empty basket. "+items("basket",list("CRTP")),"Exactly four empty baskets: orange, yellow, green, sky-blue."),vid("CRTP","The friends lift their baskets and smile; each basket keeps its color.")),
  ("S05","친구들아, 같이 따자!","0:45–0:50","C",5,img("C",f"{D['C']} holds a small ORANGE basket and waves the other arm, calling friends happily under the apple tree.","Exactly one orange basket."),vid("C","Chiqui waves and calls out happily, swinging the orange basket.")),
  ("S06","좋아!","0:50–0:55","CRTP",5,img("CRTP","Roro, Torong and Pio nod eagerly around Chiqui under the apple tree, each holding their own empty basket. "+items("basket",list("CRTP")),""),vid("CRTP","The friends nod together and cheer.")),
  ("S09","로로 · 하나, 둘","1:05–1:15","R",10,img("R",f"{D['R']} stands under a low branch of the apple tree, holding a small YELLOW basket, reaching for two {AP}s on the low branch.","Exactly one yellow basket."),vid("R","Roro picks two red apples one by one and puts them into the yellow basket, doing a cute happy roar.")),
  ("S10","토롱 · 셋, 넷","1:15–1:25","T",10,img("T",f"{D['T']} stretches the very long neck up to a high branch of the apple tree with two {AP}s; a small GREEN basket sits on the grass at Torong's feet.","Exactly one green basket."),vid("T","Torong picks two red apples from the high branch with the mouth, one by one, and gently drops them into the green basket.")),
  ("S11","피오 · 다섯, 여섯","1:25–1:35","P",10,img("P",f"{D['P']} flies at the very top of the apple tree next to two {AP}s; a small SKY-BLUE basket hangs from Pio's feet.","Exactly one sky-blue basket."),vid("P","Pio picks two red apples from the treetop one by one and drops them into the sky-blue basket, then does one happy loop.")),
  ("S12","치키 · 일곱, 여덟","1:35–1:45","C",10,img("C",f"{D['C']} jumps up toward a middle branch with two {AP}s, holding a small ORANGE basket.","Exactly one orange basket."),vid("C","Chiqui jumps, grabs two red apples one by one, puts them into the orange basket and cheers.")),
  ("S13","할아버지에게","1:45–1:55","BCRTP",10,img("BCRTP","Chiqui, Roro, Torong and Pio bring their baskets, each with two red apples, to Grandpa Bau, who holds a big empty PURPLE basket. "+items("basket",list("CRTP")),"Exactly eight apples in the four small baskets."),vid("BCRTP","The friends pour their apples into Grandpa Bau's big purple basket one by one; everyone smiles.")),
  ("S14","몇 개 남았을까?","1:55–2:00","C",5,img("C",f"Close-up of {D['C']} facing the viewer with a curious face, head tilted, holding up two paws as if counting.","",True),vid("C","Chiqui tilts the head and looks at the viewer, thinking.")),
  ("S15","아홉, 열!","2:00–2:10","B",10,img("B",f"{D['B']} gently bumps the apple tree trunk with the round tail club; two {AP}s are falling toward a big PURPLE basket on the grass.","Exactly two falling apples and one purple basket."),vid("B","The tree shakes gently; two red apples fall one after another into the purple basket; Grandpa Bau chuckles.")),
  ("S16","다 같이 세어 볼까?","2:10–2:20","BCRTP",10,img("BCRTP","All five friends sit around a big PURPLE basket full of exactly ten round shiny red apples, pointing at the apples and smiling.","Exactly ten apples, set in two neat rows of five on top of the basket, every apple fully visible and none hidden behind another, so a child can count all ten."),vid("BCRTP","The friends point at the apples one by one, nodding as if counting together. The ten apples stay still in two rows of five; no apple appears or disappears.")),
  ("S17","다 같이 모으니 열 개!","2:20–2:30","BCRTP",10,img("BCRTP","Grandpa Bau smiles warmly beside the big purple basket of red apples; Chiqui, Roro, Torong and Pio cheer around him.",""),vid("BCRTP","Grandpa Bau nods proudly; the friends cheer and clap.")),
  ("S18","냠냠, 맛있다!","2:30–2:40","BCRTP",10,img("BCRTP","All five friends sit together on a picnic blanket under the apple tree, each happily holding one red apple, smiling.","Exactly five apples, one per friend."),vid("BCRTP","Everyone takes a little bite of the apple and smiles happily, rocking side to side.")),
 ])
# ---------------- 8화 발자국 ----------------
EPS["ep08"] = dict(
 title="8화. 발자국 누구 거니? — 공룡 발자국", short="발자국 누구 거니?", song_id="foot", song_short="발자국 찾기",
 theme="공룡 상식(발자국 화석), 크다/작다 비교. 물건 없음.",
 twist="치키는 자기 발자국을 찾는데, 뒤를 돌아보니 내 발자국이 졸졸!",
 bau="발자국 화석으로 공룡을 알 수 있단다.",
 lines=[("치키","어? 발자국이다!",""),("바우","누구 발자국일까?",""),("치키","친구들아, 같이 찾자!","♻ 1화 06"),("모두","좋아!","♻ 1화 07"),
        ("내레이션","치키 발자국은 어디 있을까?","뒤에 3초 쉼"),("치키","내 발자국이다!",""),("모두","하하하!","♻ 3화 11"),
        ("바우","발자국 화석으로 공룡을 알 수 있단다.",""),("모두","와아~","♻ 1화 15"),("내레이션","누구 발이 제일 클까?","뒤에 2초 쉼"),("모두","토롱!","♻ 4화"),
        ("내레이션","누구 발이 제일 작을까?","뒤에 2초 쉼"),("모두","피오!","♻ 4화"),("치키","안녕!","♻ 1화 18")],
 verses=[("콩콩 콩콩 세 발가락","크앙! 로로 발자국","딱 맞았다 (맞았다!)"),("쿵쿵 쿵쿵 커다란 발","쭈욱~ 토롱 발자국","딱 맞았다 (맞았다!)"),
         ("총총 총총 조그만 발","슝~ 피오 발자국","딱 맞았다 (맞았다!)"),("치키 발자국 어디 있니?","두리번 두리번 (어디 있지?)","내 발자국 (어디?)")],
 chorus="발자국 누구 거니?",
 scenes=[
  ("S02","어? 발자국이다!","0:20–0:30","C",10,img("C",f"On a soft sandy beach by the sea, {D['C']} walks along and stops, looking down with surprise at a trail of different footprints in the sand.",""),vid("C","Chiqui walks, stops, points down at the footprints and gasps with excitement.")),
  ("S03","여러 가지 발자국","0:30–0:35","",5,img("",f"Close view from above of footprints pressed into smooth sand: small three-toed prints, very big round prints, tiny bird-like prints, and wide round prints, in a winding trail.","",True),vid("","The camera slowly glides along the trail of footprints in the sand; small waves sparkle at the edge.")),
  ("S04","누구 발자국일까?","0:35–0:40","B",5,img("B",f"{D['B']} stands on the sandy beach adjusting the round glasses, looking curiously at the footprints.",""),vid("B","Grandpa Bau pushes up the glasses and tilts the head curiously, smiling.")),
  ("S05","친구들아, 같이 찾자!","0:40–0:45","C",5,img("C",f"{D['C']} stands on the sandy beach waving both arms high, calling out to friends.",""),vid("C","Chiqui waves both arms and calls out happily.")),
  ("S06","좋아!","0:45–0:50","CRTP",5,img("CRTP","Roro, Torong and Pio (flying low) gather around Chiqui on the sandy beach, nodding and smiling eagerly.",""),vid("CRTP","The friends nod together and cheer.")),
  ("S07","따라가 보자","0:50–0:55","CRTP",5,img("CRTP","Chiqui, Roro, Torong and Pio walk in a line along the sandy beach following the trail of footprints, seen from the side.",""),vid("CRTP","The friends walk along the footprint trail with bouncy steps; Pio glides just above.")),
  ("S09","로로 발자국","1:05–1:15","R",10,img("R",f"{D['R']} on the sandy beach places one foot into a matching small three-toed footprint, looking delighted.",""),vid("R","Roro steps into the three-toed footprints one by one, matching them perfectly, and does a cute happy roar.")),
  ("S10","토롱 발자국","1:15–1:25","T",10,img("T",f"{D['T']} on the sandy beach places one big front foot into a matching very big round footprint, smiling proudly.",""),vid("T","Torong steps slowly into the big round footprints, they match perfectly, and Torong nods happily.")),
  ("S11","피오 발자국","1:25–1:35","P",10,img("P",f"{D['P']} hops on the sandy beach next to a line of tiny bird-like footprints, one tiny foot placed in a matching print.",""),vid("P","Pio hops along the tiny footprints, matching them one by one, then flaps both wings twice happily.")),
  ("S12","치키 발자국은?","1:35–1:45","C",10,img("C",f"Front view of {D['C']} standing alone on the sandy beach, looking around at the sand with a puzzled face, searching.","Only smooth sand in front of Chiqui."),vid("C","Chiqui looks left, then right, searching the sand, and scratches the head, puzzled.")),
  ("S13","같이 찾아 줄게","1:45–1:55","CRTP",10,img("CRTP","Roro, Torong and Pio come to Chiqui on the sandy beach and look around the sand together kindly.",""),vid("CRTP","The friends gather around Chiqui and look around together, turning their heads.")),
  ("S14","치키 발자국은 어디 있을까?","1:55–2:00","C",5,img("C",f"Medium close-up of {D['C']} sitting on the sandy beach, seen from the front from the belly up, facing the viewer with big round curious eyes and a small open mouth, one front paw raised beside the cheek as if wondering. The head is only slightly tilted; the face, the yellow-spotted orange frill and both horns are fully inside the frame with space above the frill. Behind Chiqui: soft golden sand, gentle blue sea and a clear sky. No footprints are visible anywhere in this picture.","Exactly one Chiqui with one round head, three horns and one frill; normal body proportions.",True),vid("C","Chiqui tilts the head and looks at the viewer as if asking 'Where is it?'.")),
  ("S15","내 발자국이다!","2:00–2:10","C",10,img("C",f"{D['C']} on the sandy beach turns around and looks behind, where a line of Chiqui's own round footprints follows right behind, and laughs with surprise.",""),vid("C","Chiqui turns around, sees the own footprints behind, points at them and laughs happily, then hops and makes one more footprint.")),
  ("S16","발자국 화석","2:10–2:20","B",10,img("B",f"Inside a cozy round fossil library with wooden shelves, {D['B']} shows a big flat stone with a fossil dinosaur footprint pressed into it, smiling warmly.","Exactly one fossil stone."),vid("B","Grandpa Bau gently pats the fossil footprint stone and nods with a warm smile.")),
  ("S17","누구 발이 제일 클까?","2:20–2:30","BCRTP",10,img("BCRTP","On the sandy beach, all five friends stand in a row behind their own fresh footprints: Torong's footprints are the biggest, Pio's are the tiniest.","Clear size difference of footprints."),vid("BCRTP","Everyone looks down at the footprints, then Torong lifts one big foot proudly and Pio hops on tiny feet; everyone laughs.")),
  ("S18","다 같이 콩콩","2:30–2:40","BCRTP",10,img("BCRTP","All five friends march happily together along the sandy beach, leaving a trail of different footprints behind them, facing the viewer.",""),vid("BCRTP","Everyone marches forward happily in a line, stomping footprints into the sand.")),
 ])
# ---------------- 9화 잠자기 ----------------
EPS["ep09"] = dict(
 title="9화. 달님 어디 있니? — 잘 자요", short="달님 어디 있니?", song_id="moon", song_short="달님 찾기",
 theme="잠자기 습관(놀다가도 잘 시간), 밤하늘. 친구마다 자기 몸 색 이불. 엔딩은 이 화만 잠자는 장면으로 따로 만든다(춤 재사용 안 함).",
 twist="달님은 구름 뒤에 숨어 있다가 치키 머리 위로 쏙!",
 bau="달님도 잘 자래.",
 lines=[("치키","더 놀고 싶어!",""),("바우","이제 잘 시간이란다.",""),("치키","어? 달님이 없다!",""),("치키","친구들아, 같이 찾자!","♻ 1화 06"),("모두","좋아!","♻ 1화 07"),
        ("내레이션","달님은 어디 있을까?","뒤에 3초 쉼"),("치키","달님이다!",""),("모두","와아~","♻ 1화 15"),("바우","달님도 잘 자래.",""),
        ("모두","잘 자!",""),("내레이션","쉿, 잘 자요.","속삭이듯")],
 verses=[("바위 뒤에 반짝반짝","크앙! 로로가 찾았다","반딧불이 (반짝!)"),("나무 위에 반짝반짝","쭈욱~ 토롱이 찾았다","작은 별님 (반짝!)"),
         ("구름 위에 반짝반짝","슝~ 피오가 찾았다","별님 하나 더 (반짝!)"),("달님 달님 어디 있니?","두리번 두리번 (어디 있지?)","동글동글 달님 (어디?)")],
 chorus="달님 어디 있니?",
 scenes=[
  ("S02","더 놀고 싶어!","0:20–0:30","C",10,img("C",f"At soft pink sunset in the dinosaur village, {D['C']} hops around playfully with a little yawn, not wanting to stop playing.",""),vid("C","Chiqui hops and plays, gives a small yawn, then shakes the head and keeps playing.")),
  ("S03","이제 잘 시간이란다","0:30–0:35","B",5,img("B",f"At dusk, {D['B']} stands by the round cave house with a warm glowing lantern, smiling gently.",""),vid("B","Grandpa Bau nods gently with a warm smile; the lantern glows softly.")),
  ("S04","어? 달님이 없다!","0:35–0:40","C",5,img("C",f"Night sky with soft clouds and no moon. {D['C']} looks up at the dark blue sky with a surprised face.","No moon anywhere in the sky."),vid("C","Chiqui looks up at the sky, searching, and makes a surprised face.")),
  ("S05","친구들아, 같이 찾자!","0:40–0:45","C",5,img("C",f"At night under soft blue sky, {D['C']} waves both arms, calling out to friends.","No moon visible."),vid("C","Chiqui waves both arms and calls out softly.")),
  ("S06","좋아!","0:45–0:50","CRTP",5,img("CRTP","At night, Roro, Torong and Pio (flying low) gather around Chiqui and nod eagerly, lit softly by a few glowing fireflies.","No moon visible."),vid("CRTP","The friends nod together and smile; fireflies twinkle around them.")),
  ("S07","밤길을 살금살금","0:50–0:55","CRTP",5,img("CRTP","At night, Chiqui, Roro, Torong and Pio walk in a line along a soft path with little glowing fireflies, seen from the side.","No moon visible."),vid("CRTP","The friends tiptoe forward along the path; fireflies float and twinkle.")),
  ("S09","로로 · 반딧불이","1:05–1:15","R",10,img("R",f"At night, {D['R']} peeks behind a big round rock and finds a few cute glowing yellow fireflies.","No moon visible."),vid("R","The fireflies float up around Roro; Roro giggles and does a tiny happy roar, watching them glow.")),
  ("S10","토롱 · 작은 별님","1:15–1:25","T",10,img("T",f"At night, {D['T']} stretches the very long neck up toward the top of a tall tree where one small glowing yellow clay star rests on the branches.","Exactly one star on the tree. No moon visible."),vid("T","Torong stretches the neck up and gently nudges the little star; it twinkles and floats up into the sky.")),
  ("S11","피오 · 별님 하나 더","1:25–1:35","P",10,img("P",f"At night, {D['P']} flies above soft cloud hills toward one small glowing yellow clay star in the sky.","No moon visible."),vid("P","Pio flies to the little star; it twinkles brightly; Pio does one gentle happy loop.")),
  ("S12","달님은?","1:35–1:45","C",10,img("C",f"Front view of {D['C']} standing alone on a hill at night, looking up at a sky with stars and soft clouds, with a puzzled face.","No moon visible."),vid("C","Chiqui looks up and around, searching the sky, then tilts the head, puzzled.")),
  ("S13","같이 찾아 줄게","1:45–1:55","CRTP",10,img("CRTP","At night on a hill, Roro, Torong and Pio come close to Chiqui and look up at the starry sky together kindly.","No moon visible."),vid("CRTP","The friends gather around Chiqui and all look up at the sky together.")),
  ("S14","달님은 어디 있을까?","1:55–2:00","C",5,img("C",f"Close-up of {D['C']} facing the viewer at night with a curious face, head tilted.","",True),vid("C","Chiqui tilts the head and looks at the viewer as if asking 'Where is it?'.")),
  ("S15","달님이다!","2:00–2:10","C",10,img("C",f"At night on a hill, a soft cloud is moving away and a big round smiling yellow moon appears right above {D['C']}, who looks up with a huge happy face.","Exactly one moon."),vid("C","The cloud slides away and the smiling moon glows; Chiqui throws both arms up with joy.")),
  ("S16","달님도 잘 자래","2:10–2:20","BCRTP",10,img("BCRTP","Under a big smiling moon, Grandpa Bau smiles gently at Chiqui, Roro, Torong and Pio, who yawn sleepily.","Exactly one moon."),vid("BCRTP","Everyone yawns slowly and rubs their eyes sleepily; Grandpa Bau nods with a warm smile. Torong only yawns and does not rub the eyes.")),
  ("S17","잘 자!","2:20–2:30","BCRTP",10,img("BCRTP","Inside a cozy round cave house at night, the five friends lie side by side under their own blankets: Chiqui under an ORANGE blanket, Roro under a YELLOW blanket, Torong under a GREEN blanket, Pio under a SKY-BLUE blanket, Grandpa Bau under a PURPLE blanket. Moonlight comes through a round window.","Each blanket matches its owner's body color."),vid("BCRTP","Everyone snuggles into the blankets and waves a sleepy goodnight; each blanket keeps its color.")),
  ("S18","쉿, 잘 자요","2:30–2:40","BCRTP",10,img("BCRTP","Inside the cozy cave house, all five friends sleep peacefully under their own color blankets (orange, yellow, green, sky-blue, purple), eyes closed, smiling; soft moonlight.","",),vid("BCRTP","Everyone sleeps peacefully, breathing slowly; a few tiny stars twinkle outside the window.")),
  ("S19","별님이 반짝 (엔딩)","2:40–2:50","",10,img("","Night view of the colorful volcanic-island dinosaur village asleep under a big smiling moon and many twinkling clay stars; round cave houses with softly glowing windows.","",True),vid("","The camera slowly glides over the sleeping village; stars twinkle and the moon smiles.")),
  ("S20","잘 자요 마을 (엔딩)","2:50–3:00","",10,img("","Close view of a round cave house window at night with a soft glowing light, a big smiling moon and stars above, very peaceful.","",True),vid("","The window light slowly dims and the moon gently smiles; stars twinkle softly.")),
 ])
# ---------------- 10화 정리정돈 ----------------
EPS["ep10"] = dict(
 title="10화. 상자야 어디 있니? — 정리 정돈", short="상자야 어디 있니?", song_id="box", song_short="장난감 정리",
 theme="놀고 나면 제자리, 정리 정돈. 친구마다 자기 몸 색 장난감과 상자.",
 twist="치키 주황 상자는… 치키가 깔고 앉아 있었다!",
 bau="다 놀면 제자리!",
 lines=[("치키","실컷 놀았다!",""),("바우","어이쿠, 장난감이 가득하네.",""),("바우","다 놀면 제자리!",""),("치키","어? 내 상자가 없다!",""),
        ("치키","친구들아, 같이 찾자!","♻ 1화 06"),("모두","좋아!","♻ 1화 07"),("내레이션","치키 상자는 어디 있을까?","뒤에 3초 쉼"),
        ("치키","내가 앉아 있었네!",""),("모두","하하하!","♻ 3화 11"),("모두","영차, 영차!",""),("내레이션","방이 어떻게 됐을까?","뒤에 2초 쉼"),("모두","깨끗해!","♻ 6화"),("치키","안녕!","♻ 1화 18")],
 verses=[("공을 굴려 데굴데굴","크앙! 로로가 쏙","노란 상자 쏙 (쏙!)"),("블록 높이 차곡차곡","쭈욱~ 토롱이 쏙","초록 상자 쏙 (쏙!)"),
         ("비행기가 슝슝슝","슝~ 피오가 쏙","파란 상자 쏙 (쏙!)"),("치키 상자 어디 있니?","두리번 두리번 (어디 있지?)","주황 주황 내 상자 (어디?)")],
 chorus="상자야 어디 있니?",
 scenes=[
  ("S02","실컷 놀았다!","0:20–0:30","CRTP",10,img("CRTP","In a cozy round play room inside a cave house, Chiqui, Roro, Torong and Pio sit happily among scattered toys: an ORANGE toy car, a YELLOW ball, GREEN building blocks and a SKY-BLUE toy airplane.","Each toy matches its owner's body color."),vid("CRTP","The friends stretch and smile happily among the toys after playing.")),
  ("S03","장난감이 가득하네","0:30–0:35","B",5,img("B",f"{D['B']} stands at the door of the messy play room full of scattered toys, raising the white eyebrows with a funny surprised face.",""),vid("B","Grandpa Bau looks around the messy room, chuckles and shakes the head gently.")),
  ("S04","다 놀면 제자리!","0:35–0:40","B",5,img("B",f"{D['B']} stands next to four small toy boxes in a row: one ORANGE box, one YELLOW box, one GREEN box and one SKY-BLUE box, pointing at them kindly.","Exactly four boxes."),vid("B","Grandpa Bau points at the toy boxes one by one and nods with a warm smile.")),
  ("S05","어? 내 상자가 없다!","0:40–0:45","C",5,img("C",f"{D['C']} holds an ORANGE toy car and looks at a row of only three toy boxes (YELLOW, GREEN, SKY-BLUE) with a surprised face.","No orange box visible."),vid("C","Chiqui looks at the boxes, looks left and right, and makes a surprised face.")),
  ("S06","친구들아, 같이 찾자!","0:45–0:50","C",5,img("C",f"{D['C']} sits on a small round cushion in the play room, waving both arms and calling friends.","The cushion is soft and round."),vid("C","Chiqui waves both arms and calls out happily while sitting.")),
  ("S07","좋아!","0:50–0:55","RTP",5,img("RTP","In the play room, Roro, Torong and Pio nod eagerly, ready to tidy up.",""),vid("RTP","The friends nod together and cheer.")),
  ("S09","로로 · 노란 상자","1:05–1:15","R",10,img("R",f"In the play room, {D['R']} rolls a YELLOW ball toward a YELLOW toy box.","Exactly one yellow ball and one yellow box."),vid("R","Roro rolls the yellow ball into the yellow box, it drops in, and Roro does a cute happy roar.")),
  ("S10","토롱 · 초록 상자","1:15–1:25","T",10,img("T",f"In the play room, {D['T']} gently picks up GREEN building blocks with the mouth and stacks them into a GREEN toy box on a high shelf.","Green blocks and one green box."),vid("T","Torong stretches the neck up and places the green blocks into the green box on the shelf one by one, smiling proudly.")),
  ("S11","피오 · 파란 상자","1:25–1:35","P",10,img("P",f"In the play room, {D['P']} flies holding a SKY-BLUE toy airplane toward a SKY-BLUE toy box.","Exactly one sky-blue airplane and one sky-blue box."),vid("P","Pio flies the airplane in a gentle loop and drops it into the sky-blue box, flapping both wings twice happily.")),
  ("S12","치키 상자는?","1:35–1:45","C",10,img("C",f"Front view of {D['C']} sitting on a low round seat in the play room, holding an ORANGE toy car and looking around with a puzzled face.","The seat is under Chiqui; its color cannot be seen clearly."),vid("C","Chiqui looks left, then right, searching, while still sitting, and scratches the head, puzzled.")),
  ("S13","같이 찾아 줄게","1:45–1:55","CRTP",10,img("CRTP","Roro, Torong and Pio come to Chiqui, who is sitting and holding an orange toy car, and look around the room together kindly.",""),vid("CRTP","The friends gather around Chiqui and look around together, turning their heads.")),
  ("S14","치키 상자는 어디 있을까?","1:55–2:00","C",5,img("C",f"Medium close-up of {D['C']} sitting on the sandy beach, seen from the front from the belly up, facing the viewer with big round curious eyes and a small open mouth, one front paw raised beside the cheek as if wondering. The head is only slightly tilted; the face, the yellow-spotted orange frill and both horns are fully inside the frame with space above the frill. Behind Chiqui: soft golden sand, gentle blue sea and a clear sky. No footprints are visible anywhere in this picture.","Exactly one Chiqui with one round head, three horns and one frill; normal body proportions.",True),vid("C","Chiqui tilts the head and looks at the viewer as if asking 'Where is it?'.")),
  ("S15","내가 앉아 있었네!","2:00–2:10","C",10,img("C",f"{D['C']} stands up and looks down: the seat Chiqui was sitting on is actually an ORANGE toy box. Chiqui laughs with surprise.","Exactly one orange box."),vid("C","Chiqui stands up, looks down at the orange box, laughs happily, opens it and puts the orange toy car inside.")),
  ("S16","다 놀면 제자리!","2:10–2:20","B",10,img("B",f"{D['B']} smiles warmly in the tidy play room, next to the four closed toy boxes (orange, yellow, green, sky-blue) neatly in a row.","Exactly four boxes."),vid("B","Grandpa Bau nods proudly and gives a gentle thumbs-up with a front paw.")),
  ("S17","영차, 영차!","2:20–2:30","CRTP",10,img("CRTP","Chiqui, Roro, Torong and Pio carry their own toy boxes to a shelf together: Chiqui an ORANGE box, Roro a YELLOW box, Torong a GREEN box (in the mouth), Pio a SKY-BLUE box.","Each box matches its owner's body color."),vid("CRTP","The friends carry the boxes and place them on the shelf in a row, cheering; each box keeps its color.")),
  ("S18","깨끗해!","2:30–2:40","BCRTP",10,img("BCRTP","All five friends stand in the clean, tidy play room facing the viewer with big happy smiles; the four toy boxes sit neatly on the shelf behind them.",""),vid("BCRTP","Everyone looks around the clean room and cheers, bouncing happily together.")),
 ])

def write(ep, e):
    d = R / "episodes" / ep
    for sub in ("images", "clips", "audio/ko", "audio/songs"):
        (d / sub).mkdir(parents=True, exist_ok=True)
    sc = e["scenes"]
    newsec = sum(s[4] for s in sc)
    reuse_end = "4화 S20 춤·S21 노을(2:40–3:00)" if ep != "ep09" else "없음 (잠자는 엔딩을 이 화에서 만든다)"
    md = [f"# {e['title']} (약 3분)", "", f"- 주제: {e['theme']}", f"- 반전: {e['twist']}", f"- 바우 할아버지 한마디: \"{e['bau']}\"",
          f"- 새로 만드는 장면 {len(sc)}개({newsec}초). 다시 쓰는 영상: 1화 오프닝(0:00–0:20), 1화 `ep01_v05` + 2화 `ep02_s08`(0:55–1:05), 엔딩 {reuse_end}",
          "- 지킬 것: CLAUDE.md 3장 안전 문장 (프롬프트에 이미 넣어 둠)", "- 가사: `lyrics_ko.md`", "", "## 장면 목록", "",
          "| 장면 | 시간 | 나오는 친구 | 내용 |", "| --- | --- | --- | --- |", "| S01 | 0:00–0:20 | | (1화 오프닝 재사용) |"]
    for sid, name, t, refs, sec, *_ in sc:
        md.append(f"| {sid} | {t} | {', '.join(NM[r] for r in refs) or '없음'} | {name} |")
        if sid == "S07": md.append("| S08 | 0:55–1:05 | | (재사용) 1화 치키 달리기 + 2화 다 같이 출발 · 🎵 노래 후렴 |")
    if ep != "ep09": md += ["| S19 | 2:40–2:50 | | (재사용) 4화 S20 다 같이 춤 · 🎵 엔딩 |", "| S20 | 2:50–3:00 | | (재사용) 4화 S21 노을 인사 · 🎵 엔딩 |"]
    md += ["", "## 대사 모음 (녹음용)", "", "| 번호 | 역할 | 대사 | 비고 |", "| --- | --- | --- | --- |"]
    md += [f"| {i} | {w} | {t} | {n} |" for i, (w, t, n) in enumerate(e["lines"], 1)]
    new = [l for l in e["lines"] if "♻" not in l[2]]
    md += ["", f"새로 녹음할 음성: {len(new)}줄 (모두 대사는 두 목소리) → 약 {round(0.25 * (len(new) + sum(1 for l in new if l[0] == '모두')), 1)} 크레딧.", ""]
    (d / "script.md").write_text("\n".join(md), encoding="utf-8")
    v = e["verses"]
    lyr = "\n".join(["[Chorus]", "쿵쿵 쾅! 쿵쿵 쾅!", f"{e['chorus']} (어디 있니?)", "친구들아 같이 가자", "치키치키 출발!", ""] +
                    sum(([f"[Verse {i}]", *v[i - 1], ""] for i in range(1, 5)), []) +
                    ["[Chorus]", "쿵쿵 쾅! 쿵쿵 쾅!", f"{e['chorus']} (어디 있니?)", "친구들아 같이 가자", "치키치키 출발!", "", "[End]"])
    (d / "lyrics_ko.md").write_text(f"# {e['title']} 가사 (한국어)\n\n오프닝·엔딩·배경음악은 1화 곡. 새 노래 1곡, 1~5화와 같은 후렴 틀·박자.\n\n```\n{lyr}\n```\n\n- Suno Duration은 Custom 65~70초.\n", encoding="utf-8")
    json.dump(dict(title=f"치키 {ep[2:].lstrip('0')}화 노래", h1=f"{ep[2:].lstrip('0')}화 · {e['song_short']} 노래 (Suno)",
                   lead="이번 화는 <b>이 노래 1곡만</b> 만들면 돼요. 오프닝·엔딩·배경음악은 1화 곡을 그대로 써요.",
                   note="마지막 후렴 \"치키치키 출발!\"까지 끝까지 나오는지 들어 보고, WAV로 받아 올려 주세요.",
                   duration="<b>Custom</b> — 65~70초.",
                   songs=[dict(id=e["song_id"], title=e["short"], short=e["song_short"], where="0:55–1:55 · 시리즈 후렴 틀", inst=False,
                               style="call-and-response with short pauses for kids to echo, slow easy tempo 96 bpm, {BASE}", lyrics=lyr)]),
              open(d / "songs.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    out = [dict(id=a, name=b, time=c, refs=list(r), sec=s, img=i, vid=vv) for a, b, c, r, s, i, vv in sc]
    (d / "scenes.json").write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    if not (d / "STATUS.md").exists():  # 진행 기록은 덮어쓰지 않는다
     (d / "STATUS.md").write_text(f"# {e['title']} 진행 상태\n\n| 항목 | 상태 |\n| --- | --- |\n| 대본·가사·프롬프트 | 완료 (2026-11-18) |\n| 그림 {len(sc)}장 | 아직 |\n| 영상 {len(sc)}컷 | 아직 |\n| 노래 | 아직 (Suno 65~70초) |\n| 음성 | 아직 |\n", encoding="utf-8")
    print(ep, len(sc), "scenes", newsec, "sec,", len(new), "new lines")

for ep, e in EPS.items():
    write(ep, e)
