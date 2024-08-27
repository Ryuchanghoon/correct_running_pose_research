import json




videos_data = [
    {
        "video_file": "data/test/answer/video/0001.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0001/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0001/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0001/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0001/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0001/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0001/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0001/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0001/frame_7.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0001/frame_8.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0001/frame_9.jpg", "label" : "answer"}
            
        ]
    },
    {
        "video_file": "data/test/answer/video/0002.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0002/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0002/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0002/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0002/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0002/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0002/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0002/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0002/frame_7.jpg", "label" : "answer"}
        ]
    },

    {
        "video_file": "data/test/answer/video/0003.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0003/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0003/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0003/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0003/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0003/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0003/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0003/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0003/frame_7.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0003/frame_8.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0003/frame_9.jpg", "label" : "answer"}          
        ]
    },
    {
        "video_file": "data/test/answer/video/0004.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0004/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0004/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0004/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0004/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0004/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0004/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0004/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0004/frame_7.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0004/frame_8.jpg", "label" : "answer"}             
        ]
    },
    {
        "video_file": "data/test/anawer/video/0005.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0005/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0005/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0005/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0005/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0005/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0005/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0005/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0005/frame_7.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0005/frame_8.jpg", "label" : "answer"}          
        ]
    },
    {
        "video_file": "data/test/answer/video/0006.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0006/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0006/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0006/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0006/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0006/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0006/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0006/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0006/frame_7.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0006/frame_8.jpg", "label" : "answer"}           
        ]
    },
    {
        "video_file": "data/test/answer/video/0007.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0007/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0007/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0007/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0007/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0007/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0007/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0007/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0007/frame_7.jpg", "label" : "answer"}            
        ]
    },
    {
        "video_file": "data/test/answer/video/0008.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0008/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0008/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0008/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0008/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0008/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0008/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0008/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0008/frame_7.jpg", "label" : "answer"}         
        ]
    },
    {
        "video_file": "data/test/answer/video/0009.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0009/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0009/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0009/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0009/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0009/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0009/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0009/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0009/frame_7.jpg", "label" : "answer"}           
        ]
    },
    {
        "video_file": "data/test/answer/video/0010.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0010/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0010/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0010/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0010/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0010/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0010/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0010/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0010/frame_7.jpg", "label" : "answer"}           
        ]
    },
    {
        "video_file": "data/test/answer/video/0011.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0011/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0011/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0011/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0011/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0011/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0011/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0011/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0011/frame_7.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0011/frame_8.jpg", "label" : "answer"}              
        ]
    },
    {
        "video_file": "data/test/answer/video/0012.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0012/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0012/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0012/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0012/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0012/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0012/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0012/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0012/frame_7.jpg", "label" : "answer"}            
        ]
    },
    {
        "video_file": "data/test/answer/video/0013.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0013/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0013/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0013/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0013/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0013/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0013/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0013/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0013/frame_7.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0013/frame_8.jpg", "label" : "answer"}            
        ]
    },
    {
        "video_file": "data/test/answer/video/0014.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0014/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0014/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0014/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0014/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0014/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0014/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0014/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0014/frame_7.jpg", "label" : "answer"}            
        ]
    },
    {
        "video_file": "data/test/answer/video/0015.mp4",
        "annotations": [
            {"frame": "data/test/answer/frame/0015/frame_0.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0015/frame_1.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0015/frame_2.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0015/frame_3.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0015/frame_4.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0015/frame_5.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0015/frame_6.jpg", "label" : "answer"},
            {"frame": "data/test/answer/frame/0015/frame_7.jpg", "label" : "answer"}         
        ]
    }
    


]


data = {
    "videos": videos_data
}


with open("test_answer_data_annotations.json", "w") as json_file:
    json.dump(data, json_file, indent=4)



print("complete!")