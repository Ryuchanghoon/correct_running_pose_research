## openPose


import cv2
import numpy as np
import csv


BODY_PARTS = { "Head": 0, "Neck": 1, "RShoulder": 2, "RElbow": 3, "RWrist": 4,
                "LShoulder": 5, "LElbow": 6, "LWrist": 7, "RHip": 8, "RKnee": 9,
                "RAnkle": 10, "LHip": 11, "LKnee": 12, "LAnkle": 13, "Chest": 14,
                "Background": 15 }

POSE_PAIRS = [ ["Head", "Neck"], ["Neck", "RShoulder"], ["RShoulder", "RElbow"],
                ["RElbow", "RWrist"], ["Neck", "LShoulder"], ["LShoulder", "LElbow"],
                ["LElbow", "LWrist"], ["Neck", "Chest"], ["Chest", "RHip"], ["RHip", "RKnee"],
                ["RKnee", "RAnkle"], ["Chest", "LHip"], ["LHip", "LKnee"], ["LKnee", "LAnkle"] ]


protoFile = "pose_deploy.prototxt"
weightsFile = "pose_iter_584000.caffemodel"


net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)


image = cv2.imread("data/answer/test_image/untitled_design.jpg")

imageHeight, imageWidth, _ = image.shape


inpBlob = cv2.dnn.blobFromImage(image, 1.0 / 255, (imageWidth, imageHeight), (0, 0, 0), swapRB=False, crop=False)


net.setInput(inpBlob)


output = net.forward()


H = output.shape[2]
W = output.shape[3]
print("이미지 ID : ", len(output[0]), ", H : ", output.shape[2], ", W : ", output.shape[3]) # 이미지 ID


points = []
for i in range(0, 15):
    
    probMap = output[0, i, :, :]

    minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

    x = (imageWidth * point[0]) / W
    y = (imageHeight * point[1]) / H

    if prob > 0.1:
        cv2.circle(image, (int(x), int(y)), 3, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
        cv2.putText(image, "{}".format(i), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, lineType=cv2.LINE_AA)
        points.append((int(x), int(y)))
    else:
        points.append(None)

cv2.imshow("Output-Keypoints", image)
cv2.waitKey(0)


imageCopy = image.copy()


for pair in POSE_PAIRS:
    partA = pair[0]             
    partA = BODY_PARTS[partA]   
    partB = pair[1]             
    partB = BODY_PARTS[partB]   

    
    if points[partA] and points[partB]:
        cv2.line(imageCopy, points[partA], points[partB], (0, 255, 0), 2)

cv2.imshow("Output-Keypoints", imageCopy)
cv2.waitKey(0)
cv2.destroyAllWindows()


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


left_shoulder = points[BODY_PARTS["LShoulder"]]
left_elbow = points[BODY_PARTS["LElbow"]]
left_wrist = points[BODY_PARTS["LWrist"]]



if left_shoulder and left_elbow and left_wrist:
    left_arm_angle = calculate_angle(left_shoulder, left_elbow, left_wrist)
else:
    left_arm_angle = None


with open('untitled_design_coordinates_openPose.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["left_shoulder_x", "left_shoulder_y", "left_elbow_x", "left_elbow_y", "left_wrist_x", "left_wrist_y", "left_arm_angle"])
    if left_shoulder and left_elbow and left_wrist:
        writer.writerow([left_shoulder[0], left_shoulder[1], left_elbow[0], left_elbow[1], left_wrist[0], left_wrist[1], left_arm_angle])
    else:
        writer.writerow([None, None, None, None, None, None, None])