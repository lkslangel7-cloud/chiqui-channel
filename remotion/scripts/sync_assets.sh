#!/usr/bin/env bash
# assets/의 장면 그림·영상 조각을 Remotion public/로 복사한다.
set -euo pipefail
cd "$(dirname "$0")/../.."
mkdir -p remotion/public/scenes remotion/public/clips
cp assets/scenes/*.png remotion/public/scenes/
cp assets/clips/*.mp4 remotion/public/clips/
