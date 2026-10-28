import React from "react";
import {
  AbsoluteFill,
  Audio,
  Freeze,
  Img,
  OffthreadVideo,
  Sequence,
  interpolate,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { getVideoMetadata } from "./videoMeta";
import { FPS, type Episode, type Line, type Scene } from "./types";

const fontFace = `
@font-face {
  font-family: "Jua";
  src: url("${staticFile("fonts/Jua.ttf")}") format("truetype");
}`;

const speakerColor: Record<string, string> = {
  치키: "#7cc242",
  브론티: "#5aa9e6",
  피코: "#f2b705",
  티노: "#f28c28",
};

const Caption: React.FC<{ line: Line; frames: number }> = ({ line, frames }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 4, frames - 4, frames], [0, 1, 1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const isNarration = line.speaker === "나레이션";
  return (
    <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center", paddingBottom: 56, opacity }}>
      <div
        style={{
          fontFamily: "Jua",
          fontSize: 54,
          lineHeight: 1.25,
          color: "#3a2a1a",
          background: "rgba(255,255,255,0.92)",
          border: `6px solid ${isNarration ? "#ffffff" : speakerColor[line.speaker] ?? "#ffffff"}`,
          borderRadius: 36,
          padding: "14px 40px",
          maxWidth: 1500,
          textAlign: "center",
          boxShadow: "0 6px 0 rgba(0,0,0,0.12)",
        }}
      >
        {!isNarration && (
          <span style={{ color: speakerColor[line.speaker], marginRight: 18 }}>{line.speaker}</span>
        )}
        {line.text}
      </div>
    </AbsoluteFill>
  );
};

const KenBurns: React.FC<{ src: string; frames: number; index: number }> = ({ src, frames, index }) => {
  const frame = useCurrentFrame();
  const progress = frame / frames;
  const scale = 1.02 + 0.08 * progress;
  const dir = index % 2 === 0 ? 1 : -1;
  const x = dir * 30 * (progress - 0.5);
  return (
    <AbsoluteFill style={{ overflow: "hidden" }}>
      <Img
        src={staticFile(src)}
        style={{ width: "100%", height: "100%", objectFit: "cover", transform: `scale(${scale}) translateX(${x}px)` }}
      />
    </AbsoluteFill>
  );
};

const MIN_RATE = 0.75;

// 영상 조각(5초)을 장면 길이에 맞춰 재생 속도를 조절한다.
// 0.75배속으로도 모자라면 끝까지 재생한 뒤 마지막 프레임을 천천히 확대하며 잡아 둔다.
const Clip: React.FC<{ src: string; frames: number }> = ({ src, frames }) => {
  const frame = useCurrentFrame();
  const clipSeconds = getVideoMetadata(src).duration;
  const playbackRate = Math.max(MIN_RATE, clipSeconds / (frames / FPS));
  const playFrames = Math.min(frames, Math.floor((clipSeconds / playbackRate) * FPS) - 1);
  const hold = frame >= playFrames;
  const scale = hold ? interpolate(frame, [playFrames, frames], [1, 1.05]) : 1;
  const style = { width: "100%", height: "100%", objectFit: "cover" as const, transform: `scale(${scale})` };
  return (
    <AbsoluteFill style={{ overflow: "hidden" }}>
      {hold ? (
        <Freeze frame={playFrames - 1}>
          <OffthreadVideo src={staticFile(src)} muted playbackRate={playbackRate} style={style} />
        </Freeze>
      ) : (
        <OffthreadVideo src={staticFile(src)} muted playbackRate={playbackRate} style={style} />
      )}
    </AbsoluteFill>
  );
};

const SceneView: React.FC<{ scene: Scene; frames: number; index: number }> = ({ scene, frames, index }) => {
  const frame = useCurrentFrame();
  const fadeIn = interpolate(frame, [0, 6], [0, 1], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ opacity: fadeIn, backgroundColor: "#bfe6ff" }}>
      {scene.kind === "image" ? (
        <KenBurns src={scene.src} frames={frames} index={index} />
      ) : (
        <Clip src={scene.src} frames={frames} />
      )}
      {scene.lines.map((line, i) => {
        const from = Math.round(line.at * FPS);
        const next = scene.lines[i + 1];
        const until = next ? Math.round(next.at * FPS) : frames;
        return (
          <Sequence key={i} from={from} durationInFrames={until - from} layout="none">
            <Audio src={staticFile(line.audio)} />
            <Caption line={line} frames={until - from} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};

const Title: React.FC<{ title: string }> = ({ title }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 8, 70, 85], [0, 1, 1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  return (
    <AbsoluteFill style={{ padding: 48, opacity }}>
      <div
        style={{
          fontFamily: "Jua",
          fontSize: 60,
          color: "#ffffff",
          WebkitTextStroke: "3px #5a3d1e",
          paintOrder: "stroke fill",
          textShadow: "0 5px 0 rgba(0,0,0,0.2)",
        }}
      >
        아기공룡 치키 · {title}
      </div>
    </AbsoluteFill>
  );
};

export const EpisodeVideo: React.FC<{ episode: Episode }> = ({ episode }) => {
  const { durationInFrames } = useVideoConfig();
  const frame = useCurrentFrame();
  const fadeOut = interpolate(frame, [durationInFrames - 20, durationInFrames], [1, 0], {
    extrapolateLeft: "clamp",
  });
  let start = 0;
  return (
    <AbsoluteFill style={{ backgroundColor: "#000" }}>
      <style>{fontFace}</style>
      <AbsoluteFill style={{ opacity: fadeOut }}>
        {episode.scenes.map((scene, i) => {
          const frames = Math.round(scene.duration * FPS);
          const from = start;
          start += frames;
          return (
            <Sequence key={i} from={from} durationInFrames={frames}>
              <SceneView scene={scene} frames={frames} index={i} />
            </Sequence>
          );
        })}
        <Sequence from={0} durationInFrames={90}>
          <Title title={episode.title} />
        </Sequence>
      </AbsoluteFill>
      {episode.bgm && (
        <Audio
          src={staticFile(episode.bgm)}
          volume={(f) => 0.18 * interpolate(f, [durationInFrames - 30, durationInFrames], [1, 0], { extrapolateLeft: "clamp" })}
        />
      )}
    </AbsoluteFill>
  );
};
