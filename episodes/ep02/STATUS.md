# 2화 진행 상태

| 항목 | 상태 |
| --- | --- |
| 대본·가사 | 완료 (`script.md`, `lyrics_ko.md`) |
| 장면 그림 21장 | 사용자가 웹(GPT Image 2.6 Sunburst)에서 완료 → **파일을 채팅에 올려 받아야 함** (웹 결과물은 MCP 기록에 안 보임) |
| 영상 21컷 | 아직 (웹 Seedance 2.5 무제한, 그림을 시작 프레임으로) → 받으면 `clips/ep02_s02.mp4` … `ep02_s21.mp4`로 저장 |
| 풍선 찾기 노래 | 아직 (Suno) → `audio/songs/balloon_song.wav` |
| 대사 음성 21개 | **완료** `audio/ko/` (06·07·08·20은 1화 음성 재사용) |
| 편집 순서표 | 초안 `edit_order.json` (오프닝·엔딩·배경음악은 1화 곡, 오프닝 영상·치키 달리기는 1화 클립) |

완성 명령: `python3 -I scripts/assemble_episode.py episodes/ep02 output/ep02_ko_v1.mp4` (자막 없는 판은 `--no-subs`)
