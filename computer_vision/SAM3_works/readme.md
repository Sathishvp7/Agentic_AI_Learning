# SAM3 — Video Object Tracking with Segment Anything Model 3

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-orange)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow)
![Gradio](https://img.shields.io/badge/UI-Gradio-pink)
![License](https://img.shields.io/badge/License-MIT-green)

---

## Overview

This project demonstrates **prompt-driven video object segmentation and tracking** using **SAM 3 (Segment Anything Model 3)** by Meta, accessed via HuggingFace Transformers.

Unlike classical trackers (MOSSE, CSRT) that rely on correlation filters and operate frame-by-frame without memory, SAM 3 maintains a **stateful inference session** across frames — enabling robust tracking through lighting changes, partial occlusion, and crowded scenes.

---

## Demo

> Single-point tracking on a basketball game clip — player tracked through full motion sequence.

![Demo Output](outputs/output_tracked.mp4)

---

## Background — Why SAM3?

Two classical approaches were evaluated before adopting SAM3:

| Tracker | Approach | Limitation |
|---|---|---|
| **MOSSE** | Minimum Output Sum of Square Error — correlation filter in frequency domain | Breaks under lighting changes and non-rigid deformation |
| **CSRT** — Discriminative Correlation Filter | Spatial reliability map + HOG/ColorNames features | Loses target when objects overlap or exit frame briefly |

Both are fast but **stateless** — each frame is processed independently with no temporal memory. SAM3 solves this through its session-based propagation architecture.

---

## How SAM3 Works

```
User prompt (text / point / box)
           │
           ▼
  processor.init_video_session()
           │  creates stateful memory object
           ▼
  Frame 0  ──►  SAM3 Encoder  ──►  Mask + Memory Bank
           │
           ▼
  Frame 1..N  ──►  propagate_in_video_iterator()
                   │  cross-attention with memory bank
                   │  mask deformed to match motion
                   ▼
              Per-frame binary masks + bounding boxes
```

The **inference session** is the core mechanism — it accumulates temporal context from previous frames so the model knows *where the object was* when predicting *where it is now*.

---

## Key Concepts Covered

### 1. Prompt Types
SAM3 accepts three types of prompts — no retraining required for any of them:

- **Text prompt** — `"person"`, `"player in white"`, `"ball"`
- **Point prompt** — `[x, y]` coordinate with label `1` (foreground) or `0` (background)
- **Bounding box prompt** — `[x1, y1, x2, y2]` with positive/negative labels

### 2. Inference Session as Memory
Unlike stateless trackers, SAM3 initializes a session object once and feeds frames into it sequentially. The session holds:
- Encoded features of the target object
- Memory bank of past frame embeddings
- Object IDs for multi-object tracking

### 3. Mask Propagation
`propagate_in_video_iterator()` walks through all frames, using cross-attention between current frame features and the stored memory bank to produce per-frame segmentation masks.

### 4. Multi-Object Tracking
Multiple objects can be tracked simultaneously by assigning separate `obj_id` values at session initialization. Each object maintains an independent memory state.

### 5. Streaming / Real-time Mode
For webcam/live feeds, a persistent `STREAM_STATE` dict keeps the session alive between frames — enabling real-time tracking without reinitializing the model.

---

## Model Variants Used

| Model | Use Case |
|---|---|
| `Sam3VideoModel` | Text-prompted video segmentation |
| `Sam3TrackerVideoModel` | Point/box-prompted object tracking |

Both loaded from `facebook/sam3` via HuggingFace.

---

## Project Structure

```
sam3-video-tracking/
│
├── outputs/
│   └── output_tracked.mp4       # Sample tracked output video
│
└── README.md
```

> Note: Source code is not included in this repository.
> This repo documents the approach, architecture, and results.

---

## Pipeline Summary

```
Input Video (mp4)
      │
      ▼
load_video_opencv()              # OpenCV-based loader (robust to codec issues)
      │                          # replaces transformers load_video (PyAV backend)
      ▼
processor.init_video_session()   # Creates inference session with memory
      │
      ▼
add_inputs_to_inference_session() # Registers point/text prompt on frame 0
      │
      ▼
model(frame_idx=0)               # Segments target on first frame
      │
      ▼
propagate_in_video_iterator()    # Propagates mask through all frames
      │
      ▼
post_process_masks()             # Resizes masks to original resolution
      │
      ▼
cv2.VideoWriter()                # Writes annotated output video
```

---

## Known Limitations

### ID Switching (Hijack Problem)
When two people overlap for extended frames, the tracker can drift to the wrong person. This is an inherent limitation of mask-propagation trackers.

**Mitigation strategies for production:**
- Pair SAM3 with a **ReID (Re-Identification)** module — verify appearance every N frames against a stored descriptor from frame 0
- **Depth anchoring** — use LiDAR/depth camera to reject candidates at different 3D positions
- **Trajectory prediction** — flag sudden centroid jumps as hijack signals and trigger re-acquisition

### Performance
SAM3 runs a full vision encoder on every frame — it is **not real-time** in batch video mode on consumer GPUs. Approximate throughput:

| Hardware | Frames/sec (approx) |
|---|---|
| A100 | ~7–8 fps |
| T4 (Colab) | ~2–3 fps |
| RTX 3060/3070 | ~1–2 fps |
| CPU only | ~0.1 fps |

For real-time use cases, the **streaming mode** (single-frame forward pass) is significantly faster.

---

## Use Cases

- Sports analytics — player tracking
- Robotics — person follower in dynamic environments
- Surveillance — identity-consistent tracking in crowds
- Medical imaging — instrument or region tracking across scan frames
- Video annotation — automated mask generation for labeling pipelines

---

## References

- [SAM 3 — Meta AI](https://ai.meta.com/sam2/)
- [HuggingFace Transformers — SAM3](https://huggingface.co/facebook/sam3)
- [Gradio](https://www.gradio.app/)
- [OpenCV](https://opencv.org/)
- MOSSE: *Visual Object Tracking using Adaptive Correlation Filters* — Bolme et al., CVPR 2010
- CSRT: *Discriminative Correlation Filter Tracker with Channel and Spatial Reliability* — Lukezic et al., CVPR 2017

---

## License

MIT License — see [LICENSE](LICENSE) for details.
