# 새 대화 시작용 인수인계 (2026-11-26)

새 대화의 Claude는 이 파일과 CLAUDE.md를 먼저 읽고 이어서 한다. 규칙은 모두 CLAUDE.md에 있다.

## 새 컨테이너에서 가장 먼저 (중요)

합격 그림·영상(약 6GB)과 `output/*.mp4`는 용량 때문에 git에 없다. 새 대화는 빈 컨테이너에서 시작하므로:

1. 합격 그림·영상: `python3 -I tools/restore_media.py` (전부) 또는 `python3 -I tools/restore_media.py ep32 ep33`(필요한 화만)
   - `tools/media_manifest.txt`(1052개)의 파일 이름 끝 11글자가 공유 코드라서 Higgsfield에서 같은 파일을 다시 받는다(테스트에서 바이트까지 동일).
   - 로컬로 고친 파일(`_fix`·`_bright`·`_local_zoom`, ep24 S04·S07 그림)은 git에 들어 있다.
   - 새로 합격시키면 manifest에 한 줄 추가한다: `ls episodes/*/images/web/* episodes/*/clips/web/* > tools/media_manifest.txt`
2. 완성 영상(9~12화 hq.mp4)은 클립을 받은 뒤 다시 조립하거나, 완성 영상 페이지에서 내려받는다.

## 페이지 (아티팩트, 같은 URL에 계속 다시 올림)

- 완성 영상 + 진행 현황 탭: https://claude.ai/artifact/VrXoeRAAETxzuRQbFUxKJ6
  - 만들기: `python3 prompts/build_video_page.py <스크래치패드>/videopage`
  - 올리기: index.html. 새로 완성한 화는 `v/epXX.mp4`·`t/epXX.jpg`·`th/epXX.jpg`도 `files`로 올린다(바꿀 때는 `overwrite_unread`).
  - 새 대화에서는 먼저 Artifact `read`로 이 URL을 읽어야 다시 올릴 수 있다.
- 쇼츠 미리보기: https://claude.ai/artifact/AHwnLSqUeQMDebTUCyaX7L (`prompts/build_shorts_page.py`)
- 화별 장면·노래 페이지: `episodes/pages.json`
  - 장면 페이지 다시 만들기: `prompts/build_scene_page.py episodes/epXX "N화. 제목"`

## 진행 상태

| 화 | 상태 |
|---|---|
| 1~8화 | 유튜브 업로드 완료 |
| 9~12화 | 고화질 완성: `output/ep09_ko_v2_hq`, `ep10_ko_v2_hq`, `ep11_ko_v1_hq`, `ep12_ko_v2_hq` (.mp4 + .srt), upload_info.md 있음 |
| 13~25화 (폴더) | 그림·영상 완료, 노래 기다림 (노래가 오면 음성 → 조립 → 썸네일 → 업로드 정보 → 페이지) |
| 26~31화 | 그림·영상 거의 완료. 정확한 개수는 진행 현황 탭 |
| 32~36화 | 그림 완료, 영상 확인 남음 |
| 37~40화 | 그림부터 시작 |

- 웹 무제한은 2026-11-29(일)까지.
- 20화(크리스마스, 폴더 ep25)는 12월 중순 전에 올린다. 방송 번호는 `episodes/upload_order.json`을 따른다.
- 36화는 「고마워!」로 바꿨다. 가을 낙엽 주제는 `prompts/keep_ep36_fall.py`에 보관(내년용).

## 작업 방법

- 사용자가 Higgsfield 웹에서 만들고 `https://higgsfield.ai/s/CODE` 링크를 보낸다.
- 받기와 장면 맞추기:
  - `python3 -I tools/fetch_any.py <dir> CODE…` — 내려받으며 프롬프트로 장면을 찾는다.
  - `EP=epXX python3 -I tools/matchep.py <dir> -- CODE…` — `S##_CODE.png`로 이름을 바꾼다.
  - `tools/matchall.py` — 26~40화 전체에서 비슷한 프롬프트 상위 3개를 보여 준다.
- 합격 파일 저장 위치: `episodes/epXX/images/web/S##_CODE.png`, `clips/web/S##_CODE.mp4`. 공통 컷은 `episodes/common/`.
- 확인 방법:
  - 영상은 1초 간격 프레임 전부와 합격 그림을 한 장에 모아 본다.
  - 반복 소품은 크게 잘라 특징 3~4개를 대조한다.
- 그림 프롬프트 생성기: `prompts/make_ep26_40.py`. 다시 생성하면 다른 화의 STATUS.md는 되돌린다.
- 조립:
  - 11~12화 방식: `python3 -I scripts/build_ep11_15.py epXX` (노래 파일·길이를 거기에 추가)
  - 기본 2560×1440 고화질. **조립은 한 번에 하나만** 돌린다(동시에 돌리면 파일이 깨짐).
- 음성: elevenlabs_v4, 줄당 약 0.23크레딧. **크레딧을 쓰기 전에 반드시 비용을 알리고 확인받는다.**
  - voice_id: 치키 0178ef57-ada4-43d9-992b-8d9221045bb4, 바우 ca12fd00-218c-5198-b10c-7d36e768c12c, 내레이션 c25f78a0-714e-42af-8da3-a399cef94968, 로로 5c615d8a-5135-539d-8ab0-497b7ceabbae
- 커밋: `git -c user.name=lkslangel7 -c user.email=lkslangel7@gmail.com commit` 후 push.

## 나중에 할 일

- 11화부터 쇼츠 만들기
- 모음집 (1시간짜리 포함)
- 영어·스페인어판
- 업스케일 테스트 (선택)
