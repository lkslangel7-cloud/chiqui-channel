# 1화 3분판 전체 애니메이션 계획

지금 3분판(`remotion/episodes-src/ep01_ko_3min.json`)에서 그림(확대·이동)으로 처리한 16개 장면을 모두 AI 영상으로 바꾸는 계획.
크레딧이 생기면 이 표 그대로 생성하고, 스펙의 `kind`를 `video`, `src`를 `clips/ep01_aNN.mp4`로 바꾼 뒤 다시 빌드한다.

- 모델: `kling3_0`, mode `std`, sound `off`, 16:9, 시작 이미지 = 아래 Job ID
- 길이: 장면 길이를 올림한 초(대사 길이에 맞춤). 합계 150초 ≈ 225크레딧 (초당 1.5)
- 모든 프롬프트 앞에 `2D cartoon animation.`, 끝에 `Smooth gentle motion. Keep the flat 2D cartoon style and character designs unchanged.`를 붙인다.
- 생성 후 `remotion/src/videoMeta.ts`에 각 영상의 실제 길이를 적는다.

| 파일 | 장면 | 시작 이미지 Job ID | 길이 | 프롬프트 (가운데 부분) |
| --- | --- | --- | --- | --- |
| ep01_a01 | s01 섬 전경(제목) | c9aa368a-be7d-408e-921f-b6dbc852b0aa | 5s | Slow aerial glide toward the island; waves sparkle, clouds drift, the smiling volcano puffs a small cloud, rainbow shimmers. No characters. |
| ep01_a02 | s02 치키 도착 | ef851b3c-42c2-447a-9e5d-97c9b3c59653 | 9s | Chiqui walks forward along the dirt path with the leaf bundle bouncing on its back, stops, looks left and right in amazement, then smiles wide and hops once with excitement. |
| ep01_a03 | s11 새 집 | 63fbcba4-69ae-4ede-9b56-0f5c9d599877 | 7s | Chiqui pats the leaf bundle, looks proudly at the round leaf door, then turns toward the valley, tilts its head thinking, and nods happily. Flowers sway. |
| ep01_a04 | s03 덤불 뒤 | 1c622a59-aa13-4c5e-b139-07182b1866d5 | 7s | Chiqui slowly rises from behind the bush, eyes widening with excitement; in the background Bronti, Pico and Tino play and splash at the lake. |
| ep01_a05 | s04 수줍은 치키 | 910f4edb-9e4c-4303-a16a-f2d200242215 | 9s | Chiqui blushes, fidgets with its front feet, glances toward the friends and quickly ducks back behind the bush, blinking nervously. |
| ep01_a06 | s13 나무 아래 | 34a8df96-6cea-495e-9ba6-848978ba47f8 | 9s | Chiqui sits under the tree and sighs, head drooping; a leaf drifts slowly down and lands beside Chiqui; light sparkles on the distant lake. |
| ep01_a07 | s05 반짝이는 뿔 | 8e28d3ea-32d1-406c-9769-f5db14d780a2 | 10s | Chiqui's three horns keep glowing pink, blue and yellow; Chiqui looks up at the sparkles, giggles, counts the horns with a nod, then puffs up its chest bravely. |
| ep01_a08 | s14 브론티에게 다가감 | 8420ae78-469b-431d-99c8-1e9b8d0a03cd | 8s | Chiqui takes small brave steps toward Bronti, pausing once with a deep breath; Bronti keeps nibbling leaves and then notices Chiqui. |
| ep01_a09 | s06 브론티와 인사 | 95d5b678-28c3-43b9-9919-14a671e043a7 | 12s | Chiqui waves up at Bronti; Bronti slowly lowers her long neck, smiles and nods; Chiqui's pink horn glows; Chiqui bounces happily. Talking expressions. |
| ep01_a10 | s15 하늘의 피코 | 0f80413b-9243-4272-a08e-d6536299ebf2 | 8s | Pico circles high in the sky with a cheeky grin; Chiqui and Bronti follow Pico with their eyes in surprise, heads turning upward. |
| ep01_a11 | s07 피코와 치키 | 2790ae9d-f8ef-4846-8f98-ed3f826c9ea9 | 9s | Pico hovers and chats cheerfully with Chiqui, flapping wings; Chiqui looks up admiringly and flaps its little front feet like wings. Chiqui's blue horn glows. |
| ep01_a12 | s16 나무 뒤 티노 | b220f88c-a8ad-4e09-8114-ccddcd8ffd49 | 12s | Chiqui, Bronti and Pico lean curiously toward the big tree; Tino peeks out, hides, then peeks out again shyly; Pico points a wing toward Tino. |
| ep01_a13 | s08 치키와 티노 | 7608edd9-b078-49af-9525-267ae50203dc | 12s | Tino steps out from the tree and talks shyly; Chiqui nods warmly; Tino's nervous smile turns into a big happy smile and both giggle. Chiqui's yellow horn glows. |
| ep01_a14 | s18 찾았다! | 0c4f2479-8c5a-4f35-bda4-496ce6fad98c | 12s | Bronti peeks over the rock and finds Chiqui; Chiqui pops up laughing; Pico and Tino run out of hiding and everyone laughs together in golden light. |
| ep01_a15 | s09 넷이 함께 | 7a4088fd-07a3-42dc-8ee3-2aebedcefac3 | 9s | The four friends stand together smiling at the viewer, gently swaying; Pico flaps lightly; the rainbow and lake sparkle. |
| ep01_a16 | s10 노을 인사 | 319adb6b-73c9-4075-9ccd-30fca97e6292 | 12s | Sunset; the four friends wave goodbye to the viewer, Chiqui waves the biggest; the sun slowly sinks and the first stars twinkle. |

## 선택: 정지 화면이 생기는 기존 영상 늘리기 (약 50크레딧 추가)

대사가 길어서 5초 영상 뒤에 마지막 화면이 멈춰 있는 장면들. 같은 시작 이미지로 길게 다시 만들면 멈춤이 없어진다.

| 파일 | 지금 장면 길이 | 다시 만들 길이 |
| --- | --- | --- |
| ep01_c01 (섬 전경) | 9.3s | 10s |
| ep01_c06 (물수제비) | 7.9s | 8s |
| ep01_c02 (뿔이 빛남) | 7.5s | 8s |
| ep01_c07 (숨바꼭질) | 8.6s | 9s |
