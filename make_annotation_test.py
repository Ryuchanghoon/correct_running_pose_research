import json




videos_data = [
    {
        "video_file": "data/test/video/0001.mp4",
        "annotations": [
            {"frame": "data/test/frame/0001/frame_0.jpg"},
            {"frame": "data/test/frame/0001/frame_1.jpg"},
            {"frame": "data/test/frame/0001/frame_2.jpg"},
            {"frame": "data/test/frame/0001/frame_3.jpg"},
            {"frame": "data/test/frame/0001/frame_4.jpg"},
            {"frame": "data/test/frame/0001/frame_5.jpg"},
            {"frame": "data/test/frame/0001/frame_6.jpg"}
            
        ]
    },
    {
        "video_file": "data/test/video/0002.mp4",
        "annotations": [
            {"frame": "data/test/frame/0002/frame_0.jpg"},
            {"frame": "data/test/frame/0002/frame_1.jpg"},
            {"frame": "data/test/frame/0002/frame_2.jpg"},
            {"frame": "data/test/frame/0002/frame_3.jpg"},
            {"frame": "data/test/frame/0002/frame_4.jpg"},
            {"frame": "data/test/frame/0002/frame_5.jpg"},
            {"frame": "data/test/frame/0002/frame_6.jpg"}            
        ]
    },

    {
        "video_file": "data/test/video/0003.mp4",
        "annotations": [
            {"frame": "data/test/frame/0003/frame_0.jpg"},
            {"frame": "data/test/frame/0003/frame_1.jpg"},
            {"frame": "data/test/frame/0003/frame_2.jpg"},
            {"frame": "data/test/frame/0003/frame_3.jpg"},
            {"frame": "data/test/frame/0003/frame_4.jpg"},
            {"frame": "data/test/frame/0003/frame_5.jpg"},
            {"frame": "data/test/frame/0003/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0004.mp4",
        "annotations": [
            {"frame": "data/test/frame/0004/frame_0.jpg"},
            {"frame": "data/test/frame/0004/frame_1.jpg"},
            {"frame": "data/test/frame/0004/frame_2.jpg"},
            {"frame": "data/test/frame/0004/frame_3.jpg"},
            {"frame": "data/test/frame/0004/frame_4.jpg"},
            {"frame": "data/test/frame/0004/frame_5.jpg"},
            {"frame": "data/test/frame/0004/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0005.mp4",
        "annotations": [
            {"frame": "data/test/frame/0005/frame_0.jpg"},
            {"frame": "data/test/frame/0005/frame_1.jpg"},
            {"frame": "data/test/frame/0005/frame_2.jpg"},
            {"frame": "data/test/frame/0005/frame_3.jpg"},
            {"frame": "data/test/frame/0005/frame_4.jpg"},
            {"frame": "data/test/frame/0005/frame_5.jpg"},
            {"frame": "data/test/frame/0005/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0006.mp4",
        "annotations": [
            {"frame": "data/test/frame/0006/frame_0.jpg"},
            {"frame": "data/test/frame/0006/frame_1.jpg"},
            {"frame": "data/test/frame/0006/frame_2.jpg"},
            {"frame": "data/test/frame/0006/frame_3.jpg"},
            {"frame": "data/test/frame/0006/frame_4.jpg"},
            {"frame": "data/test/frame/0006/frame_5.jpg"},
            {"frame": "data/test/frame/0006/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0007.mp4",
        "annotations": [
            {"frame": "data/test/frame/0007/frame_0.jpg"},
            {"frame": "data/test/frame/0007/frame_1.jpg"},
            {"frame": "data/test/frame/0007/frame_2.jpg"},
            {"frame": "data/test/frame/0007/frame_3.jpg"},
            {"frame": "data/test/frame/0007/frame_4.jpg"},
            {"frame": "data/test/frame/0007/frame_5.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0008.mp4",
        "annotations": [
            {"frame": "data/test/frame/0008/frame_0.jpg"},
            {"frame": "data/test/frame/0008/frame_1.jpg"},
            {"frame": "data/test/frame/0008/frame_2.jpg"},
            {"frame": "data/test/frame/0008/frame_3.jpg"},
            {"frame": "data/test/frame/0008/frame_4.jpg"},
            {"frame": "data/test/frame/0008/frame_5.jpg"},
            {"frame": "data/test/frame/0008/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0009.mp4",
        "annotations": [
            {"frame": "data/test/frame/0009/frame_0.jpg"},
            {"frame": "data/test/frame/0009/frame_1.jpg"},
            {"frame": "data/test/frame/0009/frame_2.jpg"},
            {"frame": "data/test/frame/0009/frame_3.jpg"},
            {"frame": "data/test/frame/0009/frame_4.jpg"},
            {"frame": "data/test/frame/0009/frame_5.jpg"},
            {"frame": "data/test/frame/0009/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0010.mp4",
        "annotations": [
            {"frame": "data/test/frame/0010/frame_0.jpg"},
            {"frame": "data/test/frame/0010/frame_1.jpg"},
            {"frame": "data/test/frame/0010/frame_2.jpg"},
            {"frame": "data/test/frame/0010/frame_3.jpg"},
            {"frame": "data/test/frame/0010/frame_4.jpg"},
            {"frame": "data/test/frame/0010/frame_5.jpg"},
            {"frame": "data/test/frame/0010/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0011.mp4",
        "annotations": [
            {"frame": "data/test/frame/0011/frame_0.jpg"},
            {"frame": "data/test/frame/0011/frame_1.jpg"},
            {"frame": "data/test/frame/0011/frame_2.jpg"},
            {"frame": "data/test/frame/0011/frame_3.jpg"},
            {"frame": "data/test/frame/0011/frame_4.jpg"},
            {"frame": "data/test/frame/0011/frame_5.jpg"},
            {"frame": "data/test/frame/0011/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0012.mp4",
        "annotations": [
            {"frame": "data/test/frame/0012/frame_0.jpg"},
            {"frame": "data/test/frame/0012/frame_1.jpg"},
            {"frame": "data/test/frame/0012/frame_2.jpg"},
            {"frame": "data/test/frame/0012/frame_3.jpg"},
            {"frame": "data/test/frame/0012/frame_4.jpg"},
            {"frame": "data/test/frame/0012/frame_5.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0013.mp4",
        "annotations": [
            {"frame": "data/test/frame/0013/frame_0.jpg"},
            {"frame": "data/test/frame/0013/frame_1.jpg"},
            {"frame": "data/test/frame/0013/frame_2.jpg"},
            {"frame": "data/test/frame/0013/frame_3.jpg"},
            {"frame": "data/test/frame/0013/frame_4.jpg"},
            {"frame": "data/test/frame/0013/frame_5.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0014.mp4",
        "annotations": [
            {"frame": "data/test/frame/0014/frame_0.jpg"},
            {"frame": "data/test/frame/0014/frame_1.jpg"},
            {"frame": "data/test/frame/0014/frame_2.jpg"},
            {"frame": "data/test/frame/0014/frame_3.jpg"},
            {"frame": "data/test/frame/0014/frame_4.jpg"},
            {"frame": "data/test/frame/0014/frame_5.jpg"},
            {"frame": "data/test/frame/0014/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0015.mp4",
        "annotations": [
            {"frame": "data/test/frame/0015/frame_0.jpg"},
            {"frame": "data/test/frame/0015/frame_1.jpg"},
            {"frame": "data/test/frame/0015/frame_2.jpg"},
            {"frame": "data/test/frame/0015/frame_3.jpg"},
            {"frame": "data/test/frame/0015/frame_4.jpg"},
            {"frame": "data/test/frame/0015/frame_5.jpg"}         
        ]
    },
    {
        "video_file": "data/test/video/0016.mp4",
        "annotations": [
            {"frame": "data/test/frame/0016/frame_0.jpg"},
            {"frame": "data/test/frame/0016/frame_1.jpg"},
            {"frame": "data/test/frame/0016/frame_2.jpg"},
            {"frame": "data/test/frame/0016/frame_3.jpg"},
            {"frame": "data/test/frame/0016/frame_4.jpg"},
            {"frame": "data/test/frame/0016/frame_5.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0017.mp4",
        "annotations": [
            {"frame": "data/test/frame/0017/frame_0.jpg"},
            {"frame": "data/test/frame/0017/frame_1.jpg"},
            {"frame": "data/test/frame/0017/frame_2.jpg"},
            {"frame": "data/test/frame/0017/frame_3.jpg"},
            {"frame": "data/test/frame/0017/frame_4.jpg"},
            {"frame": "data/test/frame/0017/frame_5.jpg"}        
        ]
    },
    {
        "video_file": "data/test/video/0018.mp4",
        "annotations": [
            {"frame": "data/test/frame/0018/frame_0.jpg"},
            {"frame": "data/test/frame/0018/frame_1.jpg"},
            {"frame": "data/test/frame/0018/frame_2.jpg"},
            {"frame": "data/test/frame/0018/frame_3.jpg"},
            {"frame": "data/test/frame/0018/frame_4.jpg"},
            {"frame": "data/test/frame/0018/frame_5.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0019.mp4",
        "annotations": [
            {"frame": "data/test/frame/0019/frame_0.jpg"},
            {"frame": "data/test/frame/0019/frame_1.jpg"},
            {"frame": "data/test/frame/0019/frame_2.jpg"},
            {"frame": "data/test/frame/0019/frame_3.jpg"},
            {"frame": "data/test/frame/0019/frame_4.jpg"},
            {"frame": "data/test/frame/0019/frame_5.jpg"},
            {"frame": "data/test/frame/0019/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0020.mp4",
        "annotations": [
            {"frame": "data/test/frame/0020/frame_0.jpg"},
            {"frame": "data/test/frame/0020/frame_1.jpg"},
            {"frame": "data/test/frame/0020/frame_2.jpg"},
            {"frame": "data/test/frame/0020/frame_3.jpg"},
            {"frame": "data/test/frame/0020/frame_4.jpg"},
            {"frame": "data/test/frame/0020/frame_5.jpg"}         
        ]
    },
    {
        "video_file": "data/test/video/0021.mp4",
        "annotations": [
            {"frame": "data/test/frame/0021/frame_0.jpg"},
            {"frame": "data/test/frame/0021/frame_1.jpg"},
            {"frame": "data/test/frame/0021/frame_2.jpg"},
            {"frame": "data/test/frame/0021/frame_3.jpg"},
            {"frame": "data/test/frame/0021/frame_4.jpg"},
            {"frame": "data/test/frame/0021/frame_5.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0022.mp4",
        "annotations": [
            {"frame": "data/test/frame/0022/frame_0.jpg"},
            {"frame": "data/test/frame/0022/frame_1.jpg"},
            {"frame": "data/test/frame/0022/frame_2.jpg"},
            {"frame": "data/test/frame/0022/frame_3.jpg"},
            {"frame": "data/test/frame/0022/frame_4.jpg"},
            {"frame": "data/test/frame/0022/frame_5.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0023.mp4",
        "annotations": [
            {"frame": "data/test/frame/0023/frame_0.jpg"},
            {"frame": "data/test/frame/0023/frame_1.jpg"},
            {"frame": "data/test/frame/0023/frame_2.jpg"},
            {"frame": "data/test/frame/0023/frame_3.jpg"},
            {"frame": "data/test/frame/0023/frame_4.jpg"},
            {"frame": "data/test/frame/0023/frame_5.jpg"},
            {"frame": "data/test/frame/0023/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0024.mp4",
        "annotations": [
            {"frame": "data/test/frame/0024/frame_0.jpg"},
            {"frame": "data/test/frame/0024/frame_1.jpg"},
            {"frame": "data/test/frame/0024/frame_2.jpg"},
            {"frame": "data/test/frame/0024/frame_3.jpg"},
            {"frame": "data/test/frame/0024/frame_4.jpg"},
            {"frame": "data/test/frame/0024/frame_5.jpg"},
            {"frame": "data/test/frame/0024/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0025.mp4",
        "annotations": [
            {"frame": "data/test/frame/0025/frame_0.jpg"},
            {"frame": "data/test/frame/0025/frame_1.jpg"},
            {"frame": "data/test/frame/0025/frame_2.jpg"},
            {"frame": "data/test/frame/0025/frame_3.jpg"},
            {"frame": "data/test/frame/0025/frame_4.jpg"},
            {"frame": "data/test/frame/0025/frame_5.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0026.mp4",
        "annotations": [
            {"frame": "data/test/frame/0026/frame_0.jpg"},
            {"frame": "data/test/frame/0026/frame_1.jpg"},
            {"frame": "data/test/frame/0026/frame_2.jpg"},
            {"frame": "data/test/frame/0026/frame_3.jpg"},
            {"frame": "data/test/frame/0026/frame_4.jpg"},
            {"frame": "data/test/frame/0026/frame_5.jpg"},
            {"frame": "data/test/frame/0026/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0027.mp4",
        "annotations": [
            {"frame": "data/test/frame/0027/frame_0.jpg"},
            {"frame": "data/test/frame/0027/frame_1.jpg"},
            {"frame": "data/test/frame/0027/frame_2.jpg"},
            {"frame": "data/test/frame/0027/frame_3.jpg"},
            {"frame": "data/test/frame/0027/frame_4.jpg"},
            {"frame": "data/test/frame/0027/frame_5.jpg"},
            {"frame": "data/test/frame/0027/frame_6.jpg"}            
        ]
    },
    
    {
        "video_file": "data/test/video/0028.mp4",
        "annotations": [
            {"frame": "data/test/frame/0028/frame_0.jpg"},
            {"frame": "data/test/frame/0028/frame_1.jpg"},
            {"frame": "data/test/frame/0028/frame_2.jpg"},
            {"frame": "data/test/frame/0028/frame_3.jpg"},
            {"frame": "data/test/frame/0028/frame_4.jpg"},
            {"frame": "data/test/frame/0028/frame_5.jpg"},
            {"frame": "data/test/frame/0028/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0029.mp4",
        "annotations": [
            {"frame": "data/test/frame/0029/frame_0.jpg"},
            {"frame": "data/test/frame/0029/frame_1.jpg"},
            {"frame": "data/test/frame/0029/frame_2.jpg"},
            {"frame": "data/test/frame/0029/frame_3.jpg"},
            {"frame": "data/test/frame/0029/frame_4.jpg"},
            {"frame": "data/test/frame/0029/frame_5.jpg"},
            {"frame": "data/test/frame/0029/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0030.mp4",
        "annotations": [
            {"frame": "data/test/frame/0030/frame_0.jpg"},
            {"frame": "data/test/frame/0030/frame_1.jpg"},
            {"frame": "data/test/frame/0030/frame_2.jpg"},
            {"frame": "data/test/frame/0030/frame_3.jpg"},
            {"frame": "data/test/frame/0030/frame_4.jpg"},
            {"frame": "data/test/frame/0030/frame_5.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0031.mp4",
        "annotations": [
            {"frame": "data/test/frame/0031/frame_0.jpg"},
            {"frame": "data/test/frame/0031/frame_1.jpg"},
            {"frame": "data/test/frame/0031/frame_2.jpg"},
            {"frame": "data/test/frame/0031/frame_3.jpg"},
            {"frame": "data/test/frame/0031/frame_4.jpg"},
            {"frame": "data/test/frame/0031/frame_5.jpg"},
            {"frame": "data/test/frame/0031/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0032.mp4",
        "annotations": [
            {"frame": "data/test/frame/0032/frame_0.jpg"},
            {"frame": "data/test/frame/0032/frame_1.jpg"},
            {"frame": "data/test/frame/0032/frame_2.jpg"},
            {"frame": "data/test/frame/0032/frame_3.jpg"},
            {"frame": "data/test/frame/0032/frame_4.jpg"},
            {"frame": "data/test/frame/0032/frame_5.jpg"},
            {"frame": "data/test/frame/0032/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0033.mp4",
        "annotations": [
            {"frame": "data/test/frame/0033/frame_0.jpg"},
            {"frame": "data/test/frame/0033/frame_1.jpg"},
            {"frame": "data/test/frame/0033/frame_2.jpg"},
            {"frame": "data/test/frame/0033/frame_3.jpg"},
            {"frame": "data/test/frame/0033/frame_4.jpg"},
            {"frame": "data/test/frame/0033/frame_5.jpg"}      
        ]
    },
    {
        "video_file": "data/test/video/0034.mp4",
        "annotations": [
            {"frame": "data/test/frame/0034/frame_0.jpg"},
            {"frame": "data/test/frame/0034/frame_1.jpg"},
            {"frame": "data/test/frame/0034/frame_2.jpg"},
            {"frame": "data/test/frame/0034/frame_3.jpg"},
            {"frame": "data/test/frame/0034/frame_4.jpg"},
            {"frame": "data/test/frame/0034/frame_5.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0035.mp4",
        "annotations": [
            {"frame": "data/test/frame/0035/frame_0.jpg"},
            {"frame": "data/test/frame/0035/frame_1.jpg"},
            {"frame": "data/test/frame/0035/frame_2.jpg"},
            {"frame": "data/test/frame/0035/frame_3.jpg"},
            {"frame": "data/test/frame/0035/frame_4.jpg"},
            {"frame": "data/test/frame/0035/frame_5.jpg"},
            {"frame": "data/test/frame/0035/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0036.mp4",
        "annotations": [
            {"frame": "data/test/frame/0036/frame_0.jpg"},
            {"frame": "data/test/frame/0036/frame_1.jpg"},
            {"frame": "data/test/frame/0036/frame_2.jpg"},
            {"frame": "data/test/frame/0036/frame_3.jpg"},
            {"frame": "data/test/frame/0036/frame_4.jpg"},
            {"frame": "data/test/frame/0036/frame_5.jpg"},
            {"frame": "data/test/frame/0036/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0037.mp4",
        "annotations": [
            {"frame": "data/test/frame/0037/frame_0.jpg"},
            {"frame": "data/test/frame/0037/frame_1.jpg"},
            {"frame": "data/test/frame/0037/frame_2.jpg"},
            {"frame": "data/test/frame/0037/frame_3.jpg"},
            {"frame": "data/test/frame/0037/frame_4.jpg"},
            {"frame": "data/test/frame/0037/frame_5.jpg"},
            {"frame": "data/test/frame/0037/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0038.mp4",
        "annotations": [
            {"frame": "data/test/frame/0038/frame_0.jpg"},
            {"frame": "data/test/frame/0038/frame_1.jpg"},
            {"frame": "data/test/frame/0038/frame_2.jpg"},
            {"frame": "data/test/frame/0038/frame_3.jpg"},
            {"frame": "data/test/frame/0038/frame_4.jpg"},
            {"frame": "data/test/frame/0038/frame_5.jpg"},
            {"frame": "data/test/frame/0038/frame_6.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0039.mp4",
        "annotations": [
            {"frame": "data/test/frame/0039/frame_0.jpg"},
            {"frame": "data/test/frame/0039/frame_1.jpg"},
            {"frame": "data/test/frame/0039/frame_2.jpg"},
            {"frame": "data/test/frame/0039/frame_3.jpg"},
            {"frame": "data/test/frame/0039/frame_4.jpg"},
            {"frame": "data/test/frame/0039/frame_5.jpg"}            
        ]
    },
    {
        "video_file": "data/test/video/0040.mp4",
        "annotations": [
            {"frame": "data/test/frame/0040/frame_0.jpg"},
            {"frame": "data/test/frame/0040/frame_1.jpg"},
            {"frame": "data/test/frame/0040/frame_2.jpg"},
            {"frame": "data/test/frame/0040/frame_3.jpg"},
            {"frame": "data/test/frame/0040/frame_4.jpg"},
            {"frame": "data/test/frame/0040/frame_5.jpg"},
            {"frame": "data/test/frame/0040/frame_6.jpg"}            
        ]
    },


]


data = {
    "videos": videos_data
}


with open("test_data_annotations.json", "w") as json_file:
    json.dump(data, json_file, indent=4)



print("complete!")