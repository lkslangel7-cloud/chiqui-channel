import React from "react";
import { Composition } from "remotion";
import { EpisodeVideo } from "./Episode";
import { ep01Ko } from "./episodes/ep01_ko";
import { ep01Ko3min } from "./episodes/ep01_ko_3min";
import { FPS, episodeFrames } from "./types";

export const RemotionRoot: React.FC = () => (
  <>
    <Composition
      id="ep01-ko"
      component={EpisodeVideo}
      durationInFrames={episodeFrames(ep01Ko3min)}
      fps={FPS}
      width={1920}
      height={1080}
      defaultProps={{ episode: ep01Ko3min }}
    />
    <Composition
      id="ep01-ko-30s"
      component={EpisodeVideo}
      durationInFrames={episodeFrames(ep01Ko)}
      fps={FPS}
      width={1920}
      height={1080}
      defaultProps={{ episode: ep01Ko }}
    />
  </>
);
