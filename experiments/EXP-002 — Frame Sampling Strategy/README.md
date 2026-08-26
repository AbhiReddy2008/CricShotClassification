# EXP-002 — Baseline Frame Sampling

## Objective

To reduce the number of frames processed from each cricket video while preserving the temporal coverage of the complete video.

The dataset contains videos with varying numbers of frames. Processing every frame would increase computational cost, especially during subsequent spatial feature extraction.

Therefore, a baseline frame-sampling strategy was designed to obtain a fixed target of 30 frames whenever sufficient frames are available.

---

## Dataset Characteristics Relevant to Sampling

The dataset audit performed in EXP-001 showed:

| Property | Result |
|---|---:|
| Total videos | 1,888 |
| Minimum frames/video | 25 |
| Maximum frames/video | 229 |
| Average frames/video | 64.41 |
| Median frames/video | 56 |

The variation in temporal length makes frame sampling necessary before feature extraction.

---

## Baseline Sampling Strategy

The baseline uses **uniform temporal sampling**.

The sampling rule is:

```text
If frame_count >= 30:
    Uniformly sample 30 frames

If frame_count < 30:
    Retain all available frames