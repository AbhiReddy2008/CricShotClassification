# EXP-001 — Dataset Audit

## Objective

To systematically analyse the CricShot10 dataset and obtain its basic statistical and technical characteristics before designing the preprocessing and frame-sampling pipeline.

## Dataset

The dataset contains cricket batting videos belonging to 10 different shot categories.

A Python-based dataset analysis script was developed using OpenCV, Python, and Pandas to automatically inspect the videos and generate a dataset statistics CSV file.

## Methodology

Each class directory was traversed programmatically. For every video, the following metadata was extracted:

* Video name
* Class name
* Relative video path
* Total frame count
* Frames per second (FPS)
* Video duration
* Frame width
* Frame height
* Video readability

The extracted information was stored in a CSV file for further analysis.

## Results

### Overall Dataset

| Parameter         | Result |
| ----------------- | -----: |
| Total videos      |  1,888 |
| Number of classes |     10 |
| Readable videos   |  1,888 |
| Unreadable videos |      0 |

### Class Distribution

| Shot Class | Number of Videos |
| ---------- | ---------------: |
| Cover      |              188 |
| Defense    |              192 |
| Flick      |              181 |
| Hook       |              181 |
| Late Cut   |              182 |
| Lofted     |              198 |
| Pull       |              179 |
| Square Cut |              200 |
| Straight   |              193 |
| Sweep      |              194 |
| **Total**  |        **1,888** |

### Video Characteristics

| Property            |   Result |
| ------------------- | -------: |
| Minimum frame count |       25 |
| Maximum frame count |      229 |
| Average frame count |    64.41 |
| Median frame count  |       56 |
| Minimum duration    | 1.00 sec |
| Maximum duration    | 7.90 sec |
| Average duration    | 2.56 sec |
| Median duration     | 2.24 sec |

### FPS Distribution

The dataset primarily consists of videos recorded at 25 FPS.

| FPS | Number of Videos |
| --: | ---------------: |
|  25 |            1,839 |
|  29 |                5 |
|  30 |               44 |

Therefore, 25 FPS is the dominant frame rate in the dataset.

### Resolution Distribution

| Resolution | Number of Videos |
| ---------- | ---------------: |
| 1280 × 720 |            1,874 |
| 640 × 480  |               13 |
| 720 × 480  |                1 |

The dataset is highly consistent in terms of resolution, with the majority of videos having a resolution of 1280 × 720.

## Observations

1. The dataset contains 1,888 videos distributed across 10 cricket shot categories.
2. All analysed videos were successfully readable.
3. The number of videos per class is relatively similar, indicating no extreme class imbalance.
4. Video frame counts vary considerably, ranging from 25 to 229 frames.
5. The average video contains approximately 64 frames.
6. Video durations vary from approximately 1 second to 7.9 seconds.
7. Most videos are recorded at 25 FPS.
8. The dataset has highly consistent spatial resolution, with 1,874 of the 1,888 videos having a resolution of 1280 × 720.
9. The variation in video length and frame count is an important consideration when designing the frame-sampling strategy.

## Conclusion

The dataset audit confirms that the CricShot10 dataset is suitable for further preprocessing and modelling.

The major finding relevant to the next stage is the variation in temporal length across videos. Since the videos contain between 25 and 229 frames, processing every frame may introduce unnecessary computational cost.

Therefore, the next experiment will investigate suitable frame-sampling strategies that can reduce computational requirements while retaining sufficient temporal information for cricket shot classification.

## Output

The complete dataset metadata has been stored in:

`Dataset/datasetAnalysis/dataset_statistics.csv`

## Next Experiment

**EXP-002 — Frame Sampling Strategy**
