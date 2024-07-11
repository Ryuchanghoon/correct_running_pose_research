### mediapipe

import cv2
import mediapipe as mp
import pandas as pd
import numpy as np


mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.5) 


coordinates = []


image_files = [r"data\answer\test_image\frame_0.jpg"]


parts_indices = {
    "left_shoulder": mp_pose.PoseLandmark.LEFT_SHOULDER.value,
    "left_elbow": mp_pose.PoseLandmark.LEFT_ELBOW.value,
    "left_wrist": mp_pose.PoseLandmark.LEFT_WRIST.value
}

def calculate_angle(a, b, c):
    """
    Calculate the angle between three points.
    a, b, c are each a tuple of (x, y) coordinates.
    """
    ba = np.array([a[0] - b[0], a[1] - b[1]])
    bc = np.array([c[0] - b[0], c[1] - b[1]])
    
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)
    return np.degrees(angle)


for idx, image_file in enumerate(image_files):
    image = cv2.imread(image_file)
    
    
    if image is None:
        print(f"Error: Unable to read image file {image_file}")
        continue
    

    height, width, _ = image.shape # 절대 좌표값 계산 위함
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = pose.process(image_rgb)
    
    if result.pose_landmarks:
        landmarks = result.pose_landmarks.landmark
        shoulder = (landmarks[parts_indices["left_shoulder"]].x * width, landmarks[parts_indices["left_shoulder"]].y * height) #
        elbow = (landmarks[parts_indices["left_elbow"]].x * width, landmarks[parts_indices["left_elbow"]].y * height) # 
        wrist = (landmarks[parts_indices["left_wrist"]].x * width, landmarks[parts_indices["left_wrist"]].y * height) #
        
        angle = calculate_angle(shoulder, elbow, wrist)
        
        image_coords = {
            "image": idx,
            "left_shoulder_x": shoulder[0],
            "left_shoulder_y": shoulder[1],
            "left_elbow_x": elbow[0],
            "left_elbow_y": elbow[1],
            "left_wrist_x": wrist[0],
            "left_wrist_y": wrist[1],
            "left_arm_angle": angle
        }
        coordinates.append(image_coords)

# DataFrame 변환.
df = pd.DataFrame(coordinates)


csv_file = "frame_0_coordinates.csv"
df.to_csv(csv_file, index=False)

print("complete !!")