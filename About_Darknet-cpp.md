# 1. darknet-cpp from
  https://github.com/prabindh/darknet



# 2. How to use commands of YOLOv3
## 1. train

####  1) 처음부터
    ./darknet detector train (.data파일 위치) (.cfg파일 위치)
    ./darknet detector train mmi10/MyObj.data mmi10/yolov3-tiny-mmi10.cfg
  
  
####  2) 특정 weight 부터
    ./darknet detector train (.data파일 위치) (.cfg파일 위치) (.weights 위치)
    ./darknet detector train mmi10/MyObj.data mmi10/yolov3-tiny-mmi10.cfg mmi9/backup4/yolov3-tiny-mmi9_350000.weights
  
  
####  3) backup file 부터
    ./darknet detector train (.data파일 위치) (.cfg파일 위치) (.backup파일 위치)
    ./darknet detector train mmi10/MyObj.data mmi10/yolov3-tiny-mmi10.cfg mmi10/backup4/yolov3-tiny-mmi10.backup
  
  
## 2. Validation
    ./darknet detector valid (.data파일 위치) (.cfg파일 위치) (.weights 위치) -thresh 0.4(옵션. 안 써도 됨) 
    ./darknet detector valid mmi9/MyObj.data mmi9/yolov3-tiny-mmi9.cfg mmi9/backup66/yolov3-tiny-mmi9_940000.weights -thresh 0.4 
  
   
## 3. Demo
    ./darknet detector(.data파일 위치) (.cfg파일 위치) (.weights 위치) (비디오 파일 위치) -thresh 0.4(옵션. 안 써도 됨) 
    ./darknet detector demo mmi10/MyObj.data mmi10/yolov3-tiny-mmi10.cfg mmi10/backup2/yolov3-tiny-mmi10_275000.weights Traffic2.avi -thresh 0.4



