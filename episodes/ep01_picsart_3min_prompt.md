# 1화 픽스아트용 3분 영상 프롬프트 (대사 포함)

Higgsfield로 만든 1화 3분판(`output/ep01_ko.mp4`)과 같은 장면 순서·구도·대사로 맞춘 프롬프트.
장면 23개, 합계 약 3분 7초. 대사는 `episodes/ep01_script_3min.md`와 같다.

## 쓰는 법

1. `assets/characters/`의 기준 이미지 4장(chiqui, bronti, pico, tino)을 레퍼런스로 올린다.
2. 긴 대본을 한 번에 받는 기능이면 **[A] 전체 프롬프트**를 통째로 넣는다.
3. 한 번에 5~10초씩만 만드는 기능이면 **[B] 장면별 프롬프트**를 쓴다. 매번 `공통 머리말` + 장면 하나를 붙여 넣고, 나온 영상을 순서대로 이어 붙인다.
4. 장면 그림이 있으면 `assets/scenes/`의 같은 번호 그림을 시작 이미지로 넣으면 Higgsfield판과 가장 비슷하게 나온다.

## 공통 머리말

```
2D children's cartoon episode "Chiqui's Three Hellos". Korean dialogue, spoken clearly and slowly for preschoolers, with Korean subtitles at the bottom.

Setting: Rainbow Valley, a small cozy island with a gentle sleeping volcano with a smiling smoke cloud, rolling green hills, a sparkling blue lake, a round forest, fluffy cloud hills and a rainbow sky.

Characters (keep exactly the same in every shot, match the reference images):
- Chiqui: cute baby triceratops, soft lime-green body, cream belly, big sparkling dark eyes, rosy cheeks, three short rounded pale-peach horns, small rounded frill with tiny pastel dots, short stubby legs. Voice: bright, high, curious little child.
- Bronti: gentle young brontosaurus, soft sky-blue body, pale cream belly, very long neck, calm kind half-closed eyes, lighter blue spots on the back. Voice: soft, calm big sister.
- Pico: playful baby pteranodon, butter-yellow body, light orange wings, small pointed crest, short rounded beak, cheeky grin. Voice: playful, quick, bouncy.
- Tino: shy baby tyrannosaurus, tangerine-orange body, cream belly, tiny arms held together, gentle nervous smile, blushing cheeks, cute and not scary. Voice: small, shy, trailing off.
- Narrator: warm, gentle adult female storyteller voice.

Style: clean 2D children's cartoon, smooth soft shading, thick friendly outlines, simple rounded shapes, pastel colors, preschool animation look, warm gentle mood, smooth cheerful motion, soft ukulele and glockenspiel background music, 16:9.
```

## [A] 전체 프롬프트 (공통 머리말 뒤에 이어 붙인다)

```
Scenes in order (about 3 minutes total):

1. (5s) Wide shot of Rainbow Valley island in the morning, title moment, no characters, gentle camera push-in.
2. (9s) Same valley, clouds drift, the volcano puffs a little cloud.
   Narrator: "화산 너머 작은 섬, 레인보우 밸리예요."
   Narrator: "숲도 있고, 호수도 있고, 구름 언덕도 있어요."
3. (8s) Chiqui arrives on a winding dirt path with a leaf bundle on its back, looking around amazed; lake, volcano and rainbow behind.
   Narrator: "레인보우 밸리에 아기 공룡 치키가 이사 왔어요."
   Chiqui: "와, 여기가 우리 새 동네야!"
4. (7s) Chiqui stands proudly in front of a small round cave home with a round leaf door and a flower garden, the leaf bundle unpacked.
   Chiqui: "짐 정리 끝! 이제 뭐 하고 놀지?"
   Chiqui: "그래, 친구를 찾아보자!"
5. (6s) Chiqui peeks from behind a round green bush in the foreground; far away at the lake Bronti, Pico and Tino are playing.
   Narrator: "호숫가에서 신나는 소리가 들려요."
   Chiqui: "우와, 친구들이다!"
6. (8s) At the lakeside Pico tosses a flat pebble that skips three times across the water; Tino jumps and claps, Bronti smiles.
   Pico: "누가 누가 멀리 던지나! 하나, 둘, 셋!"
   Tino: "우와, 피코 최고!"
7. (8s) Close-up of Chiqui hiding behind the bush, blushing, fidgeting with its front feet, a small nervous sweat drop.
   Narrator: "친구를 사귀고 싶지만, 너무 부끄러웠어요."
   Chiqui: "뭐라고 말을 걸지? 왜 이렇게 떨릴까?"
8. (8s) Chiqui sits alone under a big tree, looking down sadly, one leaf falling slowly.
   Narrator: "치키는 그만 혼자 돌아서고 말았어요."
   Chiqui: "나는… 친구를 못 사귈지도 몰라."
9. (8s) Chiqui looks up in wonder as its three horns light up one by one, pink, sky blue, golden yellow, with sparkles and little stars.
   Narrator: "그때, 뿔 세 개가 반짝 빛났어요!"
   Chiqui: "안녕! 헬로! 올라!"
10. (10s) Chiqui with glowing horns, bouncing with joy in a flower meadow.
   Narrator: "뿔 하나마다 다른 나라 인사를 알려 줬어요."
   Chiqui: "인사하는 방법이 세 가지나 있네!"
   Chiqui: "좋아, 용기를 내 보자!"
11. (8s) Chiqui walks bravely along a flower path toward Bronti, who is nibbling leaves from a tall tree.
   Narrator: "치키는 먼저 키 큰 브론티에게 다가갔어요."
   Chiqui: "두근두근… 할 수 있어!"
12. (11s) Chiqui waves up at Bronti; Bronti lowers her long neck kindly and smiles. Chiqui's pink horn glows.
   Chiqui: "안녕! 나는 치키야!"
   Bronti: "안녕, 치키! 반가워."
   Bronti: "천천히 해도 괜찮아. 우리 같이 놀래?"
   Chiqui: "응, 좋아!"
13. (7s) Pico flies high in the blue sky with wings spread; Chiqui and Bronti look up in surprise.
   Narrator: "그때, 하늘에서 누군가 슝 내려왔어요."
   Pico: "내가 먼저 보고 올게!"
14. (4s) Pico swoops down in a playful loop and lands in front of Chiqui, flapping. Chiqui's blue horn glows.
   Chiqui: "헬로!"
   Pico: "헬로! 나는 피코야!"
15. (9s) Pico and Chiqui face each other on the meadow, both grinning.
   Pico: "너 새로 왔구나? 하늘에서 다 봤지!"
   Chiqui: "피코, 하늘을 나는 거 정말 멋지다!"
16. (11s) Chiqui, Bronti and Pico look curiously toward a big tree; Tino peeks shyly from behind the trunk.
   Narrator: "그런데 나무 뒤에서 누가 살짝 보고 있었어요."
   Chiqui: "어? 저기 누구지?"
   Pico: "아, 티노야! 부끄럼쟁이 티노!"
17. (5s) Tino slowly steps out from behind the tree and gives a small shy wave. Chiqui's yellow horn glows.
   Chiqui: "올라!"
   Tino: "나도… 같이 해도 돼?"
18. (11s) Chiqui smiles warmly at Tino at the forest edge; Tino's nervous smile becomes a happy smile.
   Chiqui: "그럼! 우리 같이 놀자!"
   Tino: "고마워. 사실 나도 인사하고 싶었는데, 부끄러웠어."
   Chiqui: "나도 그랬어! 우리 똑같다!"
19. (9s) Hide-and-seek: Bronti covers her eyes against a tree, counting; Chiqui hides behind a rock with horns poking out, Tino's tail sticks out of a bush, Pico peeks from the leaves.
   Bronti: "우리 숨바꼭질 할까? 내가 술래 할게!"
   Bronti: "하나, 둘, 셋, 넷, 다섯!"
20. (11s) Bronti finds Chiqui behind the rock; everyone comes out laughing in golden afternoon light.
   Bronti: "찾았다! 치키 뿔이 보여!"
   Chiqui: "헤헤, 뿔이 세 개라서 숨기 어려워!"
   Narrator: "넷은 해가 질 때까지 신나게 놀았어요."
21. (4s) The four friends on a grassy hill by the lake bounce in rhythm and wave at the viewer, rainbow behind.
   All four together: "우리는 이제 친구!"
22. (8s) Same four friends standing together, smiling at the viewer.
   Narrator: "먼저 인사하면, 친구가 생겨요!"
   Narrator: "여러분도 오늘, 친구에게 먼저 인사해 볼까요?"
23. (12s) Sunset over Rainbow Valley; Chiqui in front waving goodbye at the viewer, friends behind waving, first stars appear. Music swells for the ending.
   Chiqui: "안녕! 헬로! 올라! 또 만나!"
```

## [B] 장면별 프롬프트

장면 하나만 만들 때는 `공통 머리말` 뒤에 아래 형식으로 한 장면만 붙인다.

```
Make one shot only, {초}s:
{위 [A]에서 해당 번호의 장면 설명과 대사}
Keep the characters identical to the reference images.
```

예시 (장면 12, 11초):

```
Make one shot only, 11s:
Chiqui waves up at Bronti; Bronti lowers her long neck kindly and smiles. Chiqui's pink horn glows.
Chiqui: "안녕! 나는 치키야!"
Bronti: "안녕, 치키! 반가워."
Bronti: "천천히 해도 괜찮아. 우리 같이 놀래?"
Chiqui: "응, 좋아!"
Keep the characters identical to the reference images.
```

## 참고

- 장면 번호와 Higgsfield판 그림 파일: 1·2 `s01`/`c01`, 3 `s02`, 4 `s11`, 5 `s03`, 6 `s12`/`c06`, 7 `s04`, 8 `s13`, 9 `c02`, 10 `s05`, 11 `s14`, 12 `s06`, 13 `s15`, 14 `c03`, 15 `s07`, 16 `s16`, 17 `c04`, 18 `s08`, 19 `s17`/`c07`, 20 `s18`, 21 `c05`, 22 `s09`, 23 `s10`.
- AI 영상 도구가 만든 한국어 목소리와 자막은 발음·글자가 틀릴 수 있다. 어색하면 대사 없이 영상만 만들고, 이미 만든 ElevenLabs 음성(`audio/ep01_ko/`)과 자막은 Remotion에서 입히는 쪽이 안정적이다.
