import json




videos_data = [
    {
        "video_file": "wrong/0001.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"}
            

        ]
    },
    {
        "video_file": "wrong/0002.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0003.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
        ]
    },


    {
        "video_file": "wrong/0004.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
        ]
    },
    
    {
        "video_file": "wrong/0005.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"}
            
        ]
    },

    {
        "video_file": "wrong/0006.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"}
        ]
    },

    {
        "video_file": "wrong/0007.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"}
        ]
    },
    
    {
        "video_file": "wrong/0008.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"}

        ]
    },

    {
        "video_file": "wrong/0009.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0010.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },

    {
        "video_file": "wrong/0011.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
        ]
    },

    {
        "video_file": "wrong/0012.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}

        ]
    },

    {
        "video_file": "wrong/0013.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },

    {
        "video_file": "wrong/0014.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0015.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0016.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0017.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },

    {
        "video_file": "wrong/0018.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0019.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },

    {
        "video_file": "wrong/0020.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0021.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0022.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0023.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },



    {
        "video_file": "wrong/0024.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0025.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0026.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0027.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"}
        ]
    },


    {
        "video_file": "wrong/0028.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0029.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },

    {
        "video_file": "wrong/0030.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0031.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0032.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0033.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"},
            {"frame": "frame_4.jpg", "label": "wrong"}
            
        ]
    },


    {
        "video_file": "wrong/0034.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"}
            
        ]
    },

    {
        "video_file": "wrong/0035.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"}
        ]
    },


    {
        "video_file": "wrong/0036.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"}
        ]
    },


    {
        "video_file": "wrong/0037.mp4",
        "annotations": [
            {"frame": "frame_0.jpg", "label": "wrong"},
            {"frame": "frame_1.jpg", "label": "wrong"},
            {"frame": "frame_2.jpg", "label": "wrong"},
            {"frame": "frame_3.jpg", "label": "wrong"}
        ]
    }


]


data = {
    "videos": videos_data
}


with open("wrong_data_annotations.json", "w") as json_file:
    json.dump(data, json_file, indent=4)



print("complete!")