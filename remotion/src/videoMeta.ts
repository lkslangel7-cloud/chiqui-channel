// 영상 조각 길이(초). 새 조각을 추가하면 ffprobe로 확인해 적는다.
const durations: Record<string, number> = {
  "clips/ep01_c02.mp4": 5.04,
  "clips/ep01_c03.mp4": 5.04,
  "clips/ep01_c04.mp4": 5.04,
  "clips/ep01_c01.mp4": 5.04,
  "clips/ep01_c05.mp4": 5.04,
  "clips/ep01_c06.mp4": 5.04,
  "clips/ep01_c07.mp4": 5.04,
};

export const getVideoMetadata = (src: string) => ({ duration: durations[src] ?? 5 });
