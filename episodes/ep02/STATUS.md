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

## 웹 그림 받기 기록

- 공유 링크(https://higgsfield.ai/s/코드)로 받는다: `og:image`에 원본 PNG 주소가 있다. 받은 파일은 `images/web/`(git 제외).
- 1차(2026-11-16) S02–S11 10장: 그림체·캐릭터는 1화와 같음. **하지만 모두 정사각형(2048x2048)** → 16:9로 다시 만들기로 함.
  코드: S02 QWlYM2g8KXQ, S03 qQMId2wMStY, S04 q1M0CwXWCF0, S05 rXH507xynO8, S06 vC3o58AKLn4, S07 vSUYwKvWVds, S08 3QSW_HXctQY, S09 3ifv2GsPt_A, S10 L3bYCOh0760, S11 qjhTKskd-Fw
- 2차(2026-11-16) S12–S21 11장: 내용·캐릭터·풍선 모두 맞음. 역시 정사각형.
  코드: S12 DR6zQ5WQB6s, S13 TRk30E_gb6I, S14 j1WbbEoXkiI, S15 IjvgsIuyTp0, S16 HR4Il3kY1JE, S17 JyNjI8QUlso, S18a ZlTBSU2yCv8, S18b VC0DwDlQpq8, S19 qx_W4bEG4RU, S20 bOMKABeq-ks, S21 guhFDEAQMis
- 21장 모두 합격(그림체·캐릭터·복제 없음·풍선 개수). 남은 문제는 비율(1:1 → 16:9)뿐. 옆을 늘리기(outpaint)는 장당 2크레딧(MCP에서 웹 그림 Job ID로 가능).
