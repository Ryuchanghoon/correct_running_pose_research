import json


videos_data = [
    {
        "video_file": "0001.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "answer"},
            {"frame": "frame_1.jpg", "label": "answer"},
            {"frame": "frame_2.jpg", "label": "answer"},
            {"frame": "frame_3.jpg", "label": "answer"},
            {"frame": "frame_4.jpg", "label": "answer"},
            {"frame": "frame_5.jpg", "label": "answer"},
            {"frame": "frame_6.jpg", "label": "answer"},
            {"frame": "frame_7.jpg", "label": "answer"},
            {"frame": "frame_8.jpg", "label": "answer"},
            {"frame": "frame_9.jpg", "label": "answer"},
            {"frame": "frame_10.jpg", "label": "answer"},
            {"frame": "frame_11.jpg", "label": "answer"},
            {"frame": "frame_12.jpg", "label": "answer"},
            {"frame": "frame_13.jpg", "label": "answer"},
            {"frame": "frame_14.jpg", "label": "answer"},
            {"frame": "frame_15.jpg", "label": "answer"},
            {"frame": "frame_16.jpg", "label": "answer"},
            {"frame": "frame_17.jpg", "label": "answer"},
            {"frame": "frame_18.jpg", "label": "answer"},
            {"frame": "frame_19.jpg", "label": "answer"},
            {"frame": "frame_20.jpg", "label": "answer"},
            {"frame": "frame_21.jpg", "label": "answer"}

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