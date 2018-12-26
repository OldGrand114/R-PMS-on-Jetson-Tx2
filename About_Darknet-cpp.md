# 1. darknet-cpp from
  https://github.com/prabindh/darknet

# 2. How to use commands of YOLOv3
## 1. train

   * ###  처음부터
      ./darknet detector train (.data파일 위치) (.cfg파일 위치)
      
      ./darknet detector train mmi10/MyObj.data mmi10/yolov3-tiny-mmi10.cfg

   * ###  특정 weight 부터
      ./darknet detector train (.data파일 위치) (.cfg파일 위치) (.weights 위치)
      
      ./darknet detector train mmi10/MyObj.data mmi10/yolov3-tiny-mmi10.cfg mmi9/backup4/yolov3-tiny-mmi9_350000.weights

   * ###  backup file 부터
      ./darknet detector train (.data파일 위치) (.cfg파일 위치) (.backup파일 위치)
      
      ./darknet detector train mmi10/MyObj.data mmi10/yolov3-tiny-mmi10.cfg mmi10/backup4/yolov3-tiny-mmi10.backup

   * ###  특
