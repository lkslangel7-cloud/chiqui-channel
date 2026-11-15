# higgsfield.ai 웹에서 직접 만들 때 쓰는 프롬프트

웹사이트에서 무제한으로 그림·영상을 만들 때 그대로 복사해서 쓰는 프롬프트 모음.
캐릭터 모습은 `CLAUDE.md` 캐릭터 표와 `characters/*_sheet.png`가 기준이다.

## 0. 웹에서 만드는 순서

1. higgsfield.ai에 로그인한다 (이 프로젝트와 같은 계정).
2. **Image** 메뉴에서 모델을 고른다. 모델 이름 옆에 **Unlimited** 표시가 있는 것을 고르면 크레딧이 들지 않는다.
   - 표시가 있으면 우선순위: GPT Image 2.5 → Nano Banana Pro → Nano Banana 2
3. **레퍼런스 이미지**에 해당 캐릭터의 레퍼런스 시트를 넣는다. 캐릭터 일관성의 핵심이다.
   - 같은 계정이라 웹의 생성 기록(History)에 시트가 남아 있다. 거기서 고르거나, 이 저장소의 `characters/` 폴더 파일을 내려받아 올린다.
   - 여러 캐릭터가 나오는 장면은 나오는 캐릭터의 시트를 모두 넣는다.
4. 아래 **[장면 프롬프트]** 하나를 복사해 붙여 넣는다. 비율은 유튜브용 **16:9**, 숏폼용 **9:16**.
5. 여러 장 뽑아서 캐릭터가 시트와 같은 것만 고른다. 색·뿔·무늬가 다르면 버린다.
6. 고른 그림으로 영상을 만든다: **Video** 메뉴 → Unlimited 표시가 있는 모델(예: Kling 3.0) → 그림을 시작 프레임(Start image)으로 → **[영상 프롬프트]** 붙여 넣기 → 5초.
7. 마음에 든 그림·영상은 내려받아 파일 이름을 `ep01_s01.png`, `ep01_c01.mp4` 형식으로 정리한다. 같은 계정의 생성 기록에 남으니, Claude에게 "웹에서 만든 것 가져와줘"라고 하면 기록에서 찾아 정리할 수 있다 (안 되면 파일을 직접 올린다).

## 1. 공통 문구

모든 그림 프롬프트 끝에 붙는 화풍 문구 (아래 프롬프트에는 이미 들어 있다):

```
Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text.
```

캐릭터 설명 (프롬프트에 캐릭터를 새로 넣을 때 이 문장을 그대로 쓴다):

| 캐릭터 | 설명 문장 |
| --- | --- |
| 치키 | Chiqui, a cute baby triceratops with a warm bright orange body, cream belly, three short rounded cream horns, rounded orange frill with small yellow spots, big round brown eyes and rosy cheeks |
| 로로 | Roro, a cute baby tyrannosaurus with a sunny yellow body, cream belly, small orange spots on the back, tiny arms, tiny rounded friendly teeth, not scary |
| 토롱 | Torong, a cute young brachiosaurus with a soft green body, pale mint belly, lighter green spots, long gentle neck and a small bump on the head |
| 피오 | Pio, a cute little baby pteranodon with a soft sky-blue body, darker blue wings, small crest and a short rounded pale-yellow beak |
| 바우 할아버지 | Grandpa Bau, a kind old ankylosaurus with a lavender-purple body, darker purple rounded armor bumps, a round tail club, small round glasses and fluffy white eyebrows |

## 2. 장면 프롬프트 (그림)

자주 쓰는 장면들. 레퍼런스에 나오는 캐릭터의 시트를 넣고 쓴다.

### 마을·배경 (레퍼런스 없음)

**S01 공룡 마을 전경**
```
Wide establishing shot of a colorful volcanic island dinosaur village in the morning: a friendly smiling volcano puffing a small cloud, rolling green hills, round cave houses with leaf doors, a sparkling lake, giant ferns and palm trees, fluffy clouds and a rainbow. No characters. Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text.
```

**S02 치키네 동굴 집 앞**
```
A cozy round cave house with a big round leaf door, a small flower garden and a stepping-stone path in a colorful dinosaur village, morning light. No characters. Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text.
```

**S03 바우 할아버지의 화석 도서관**
```
A warm cozy library inside a big hollow rock, wooden shelves filled with books and cute fossils, a big round window, soft lamp light, a small blackboard with simple dinosaur doodles. No characters. Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text.
```

### 캐릭터 장면 (레퍼런스: 해당 캐릭터 시트)

**S10 다섯 친구 단체 인사** — 시트 5장 모두
```
Use the reference sheets as the exact character designs. Chiqui, Roro, Torong, Pio and Grandpa Bau standing together in a row on a grassy hill in the dinosaur village, all smiling and waving at the viewer; Torong tall at the back, Pio flying just above, Grandpa Bau at the side. Bright sunny day, rainbow in the sky. Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text.
```

**S11 치키 "치키치키 출발!"** — 치키 시트
```
Use the reference sheet as the exact character design. Chiqui the orange baby triceratops running forward excitedly on a dirt path toward the viewer, one foot raised, big happy open-mouth smile, little dust puffs behind. Dinosaur village background. Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text.
```

**S12 로로의 크앙 댄스** — 로로 시트
```
Use the reference sheet as the exact character design. Roro the yellow baby tyrannosaurus doing a funny dance on a round play rock, tiny arms up, playful cute roar with mouth open, little music notes floating around. Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text.
```

**S13 토롱이 높은 열매 따기** — 토롱 + 치키 시트
```
Use the reference sheets as the exact character designs. Torong the green brachiosaurus gently stretching the long neck up to pick a round red fruit from a tall tree, while Chiqui the orange baby triceratops looks up and cheers. Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text.
```

**S14 피오의 하늘 비행** — 피오 시트
```
Use the reference sheet as the exact character design. Pio the sky-blue baby pteranodon flying happily over the dinosaur village with wings spread wide, shy little smile, fluffy clouds around, the village small below. Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text.
```

**S15 바우 할아버지의 상식 코너** — 바우 시트
```
Use the reference sheet as the exact character design. Grandpa Bau the purple ankylosaurus sitting in the cozy fossil library, pointing at a big picture book of dinosaurs with a warm smile, glasses on the nose. Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text.
```

**S16 다 같이 춤추기** — 시트 5장 모두
```
Use the reference sheets as the exact character designs. Chiqui, Roro, Torong, Pio and Grandpa Bau dancing together in a circle in a flower meadow, arms and wings up, happy faces, little music notes floating. Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text.
```

**S17 공룡알 세기** — 치키 + 로로 시트
```
Use the reference sheets as the exact character designs. Chiqui and Roro sitting in a soft straw nest, happily counting five round pastel-colored dinosaur eggs lined up in a row in front of them. Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text.
```

**S18 양치하기** — 치키 시트
```
Use the reference sheet as the exact character design. Chiqui the orange baby triceratops brushing teeth with a small toothbrush in front of a round mirror in a cozy cave bathroom, white foam bubbles, cheerful face. Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text.
```

**S19 잘 자 인사** — 시트 5장 모두
```
Use the reference sheets as the exact character designs. Chiqui, Roro, Torong, Pio and Grandpa Bau waving goodnight to the viewer under a starry night sky in the dinosaur village, a gentle moon, soft warm glow. Soft 3D toy-like clay style, smooth rounded shapes, soft studio lighting, gentle pastel color palette, very simple and readable for toddlers, no text.
```

## 3. 영상 프롬프트 (그림 → 5초 애니메이션)

위 장면 그림을 시작 프레임으로 넣고 쓴다. 대사가 없는 장면 위주로 만들고, 소리는 끈다(음성·노래는 따로 입힌다).

| 장면 | 영상 프롬프트 |
| --- | --- |
| S01 마을 전경 | `Slow gentle camera push-in over the dinosaur village; clouds drift, the smiling volcano puffs a little cloud, the lake sparkles. Calm smooth motion. Keep the soft 3D clay style unchanged.` |
| S10 단체 인사 | `The five dinosaur friends wave at the viewer and bounce happily in place, Pio flaps gently above. Cheerful simple motion, camera stays still. Keep the characters and soft 3D clay style unchanged.` |
| S11 치키 출발 | `Chiqui runs happily toward the camera with bouncy steps, little dust puffs behind, big smile. Smooth cheerful motion. Keep the character and soft 3D clay style unchanged.` |
| S12 로로 댄스 | `Roro dances left and right with tiny arms up, gives a cute playful roar, then giggles. Rhythmic bouncy motion, camera stays still. Keep the character and soft 3D clay style unchanged.` |
| S13 열매 따기 | `Torong slowly stretches the long neck up, gently picks the red fruit and lowers it to Chiqui, who jumps with joy. Gentle smooth motion. Keep the characters and soft 3D clay style unchanged.` |
| S14 피오 비행 | `Pio glides in a gentle loop over the village, flapping wings softly, clouds drifting past. Smooth calm motion. Keep the character and soft 3D clay style unchanged.` |
| S15 상식 코너 | `Grandpa Bau turns a page of the big book, adjusts the glasses and nods with a warm smile. Slow gentle motion, camera stays still. Keep the character and soft 3D clay style unchanged.` |
| S16 단체 춤 | `The five friends dance around in a circle, hopping and swaying to a happy rhythm. Joyful rhythmic motion, camera slowly circles. Keep the characters and soft 3D clay style unchanged.` |
| S17 알 세기 | `Chiqui touches each egg one by one from left to right while Roro nods along, both smiling. Slow simple motion. Keep the characters and soft 3D clay style unchanged.` |
| S18 양치 | `Chiqui brushes teeth up and down with a happy rhythm, foam bubbles float up, then smiles at the mirror showing clean teeth. Simple motion. Keep the character and soft 3D clay style unchanged.` |
| S19 잘 자 | `The friends wave goodnight slowly and yawn, stars twinkle, the moon glows softly. Very calm slow motion. Keep the characters and soft 3D clay style unchanged.` |

## 4. 결과가 이상할 때

- 캐릭터 색·무늬가 바뀌면: 레퍼런스 시트를 다시 넣었는지 확인하고, 프롬프트 맨 앞에 위 표의 캐릭터 설명 문장을 붙인다.
- 캐릭터가 너무 많아 흐트러지면: 한 장면에 2~3마리만 넣는다.
- 영상에서 모습이 녹아내리면: 움직임 문장을 짧게 줄이고 `slow`, `gentle`을 넣는다.
- 글자가 생기면: `no text`가 들어 있는지 확인한다.
