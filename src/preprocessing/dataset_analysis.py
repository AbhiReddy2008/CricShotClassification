import os
import cv2
import pandas as pd

data = []
rawData_path = "F:/CricShotClassification/Dataset/rawData"

for class_name in os.listdir(rawData_path):
    class_path = os.path.join(rawData_path,class_name)
    for video in os.listdir(class_path):
        video_path = os.path.join(class_path,video)
        cap = cv2.VideoCapture(video_path)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        relative_path = os.path.join("Dataset","rawData",class_name,video)
        duration = frame_count/fps
        is_readable = cap.isOpened()

        data.append([video,class_name,relative_path,frame_count,fps,duration,frame_width,frame_height,is_readable])
        cap.release()

dataframe = pd.DataFrame(data,columns=["video_name","class_name","video_path","frame_count","fps","duration_sec","width","height","is_readable"])

dataframe.to_csv(r"F:\CricShotClassification\Dataset\datasetAnalysis\dataset_statistics.csv",index=False)
