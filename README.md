# CricShotClassification

## Overview

CricShotClassification is a deep learning based video understanding project for automatic classification of cricket batting shots from video sequences.

The project focuses on learning both spatial information from individual video frames and temporal information from the sequence of frames.

## Objectives

- Classify cricket batting shots from video.
- Extract meaningful spatial features from video frames.
- Model temporal information present in batting actions.
- Investigate attention mechanisms for improved feature representation.
- Establish a reliable baseline and compare it with the proposed approach.
- Perform controlled experiments and ablation studies.
- Build a reproducible foundation for future sports analytics applications.

## Dataset

The project uses the CricShot10 dataset.

Dataset analysis and preprocessing specifications will be documented before model development.

## Proposed Approach

```text
Input Video
     ↓
Uniform Frame Sampling
     ↓
Frame Preprocessing
     ↓
EfficientNet-B0
     ↓
Spatial Features
     ↓
BiGRU
     ↓
Temporal Attention
     ↓
Classification