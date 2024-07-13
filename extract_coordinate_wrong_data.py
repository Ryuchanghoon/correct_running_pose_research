import json
import pandas as pd
import mediapipe as mp
import cv2
import numpy as np



mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, model_complexity=2)


def calculate_angle(a, b, c):
    a = np.array(a)  
    b = np.array(b)  
    c = np.array(c)
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
        
    return angle

with open(r'data\wrong\wrong_data_annotations.json', 'r') as f:
    data = json.load(f)


results = []

for video in data['videos']:
    video_file = video['video_file']
    
    for annotation in video['annotations']:
        frame_file = annotation['frame']
        label = annotation['label']
        

        image_path = frame_file
        image = cv2.imread(image_path)
        height, width, _ = image.shape
        
        
        results_pose = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        if results_pose.pose_landmarks:
            landmarks = results_pose.pose_landmarks.landmark
            
            # 좌표 추출 (7, 11, 13, 15, 23, 25, 27)
            points = {index: (landmarks[index].x * width, landmarks[index].y * height) for index in [7, 11, 13, 15, 23, 25, 27]} # 절대 좌표 계산.
            
            
            arm_angle = calculate_angle(points[11], points[13], points[15])
            leg_angle = calculate_angle(points[23], points[25], points[27])
            shoulder_angle = calculate_angle(points[7], points[11], points[23])
            hip_angle = calculate_angle(points[11], points[23], points[27])
            
            result = {
                'Time/Frame': frame_file,
                'X7': points[7][0], 'Y7': points[7][1],
                'X11': points[11][0], 'Y11': points[11][1],
                'X13': points[13][0], 'Y13': points[13][1],
                'X15': points[15][0], 'Y15': points[15][1],
                'X23': points[23][0], 'Y23': points[23][1],
                'X25': points[25][0], 'Y25': points[25][1],
                'X27': points[27][0], 'Y27': points[27][1],
                'Arm Angle': arm_angle,
                'Leg Angle': leg_angle,
                'Shoulder Angle': shoulder_angle,
                'Hip Angle': hip_angle,
                'Label': 0  # label값 0. wrong 데이터
            }
            
            results.append(result)


df = pd.DataFrame(results)

df.to_csv('wrong_annotated_data.csv', index=False)