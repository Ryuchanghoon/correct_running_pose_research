import cv2
import os


video_file = r'data\answer\video\0001.mp4'
output_dir = r'data\answer\frame\0001'


cap = cv2.VideoCapture(video_file)


frame_interval = 5 # 총 5 프레임마다 추출.

frame_count = 0
saved_frame_count = 0



while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # 5프레임 간격 이미지 저장.
    if frame_count % frame_interval == 0:
        frame_filename = os.path.join(output_dir, f'frame_{saved_frame_count:d}.jpg')
        cv2.imwrite(frame_filename, frame)
        saved_frame_count += 1
    
    frame_count += 1

cap.release()
print('complete !')