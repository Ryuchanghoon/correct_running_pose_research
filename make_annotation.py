import json


videos_data = [
    {
        "video_file": "video1.mp4",
        "annotations": [
            {"frame": "video1_frame_001.jpg", "label": "answer"},
            {"frame": "video1_frame_002.jpg", "label": "wrong"}
        ]
    },
    {
        "video_file": "video2.mp4",
        "annotations": [
            {"frame": "video2_frame_001.jpg", "label": "answer"},
            {"frame": "video2_frame_002.jpg", "label": "wrong"}
        ]
    }
]


data = {
    "videos": videos_data
}


with open("multiple_videos_annotations.json", "w") as json_file:
    json.dump(data, json_file, indent=4)



print("complete!")