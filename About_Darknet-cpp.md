# 1. darknet-cpp from
  https://github.com/prabindh/darknet

<br>

# 2. How to use commands of YOLOv3
## 1) train

####  (1)  처음부터
    ./darknet detector train (.data파일 위치) (.cfg파일 위치)
    ./darknet detector train mmi10/MyObj.data mmi10/yolov3-tiny-mmi10.cfg

####  (2)  특정 weight 부터
    ./darknet detector train (.data파일 위치) (.cfg파일 위치) (.weights 위치)
    ./darknet detector train mmi10/MyObj.data mmi10/yolov3-tiny-mmi10.cfg mmi9/backup4/yolov3-tiny-mmi9_350000.weights

####  (3)  backup file 부터
    ./darknet detector train (.data파일 위치) (.cfg파일 위치) (.backup파일 위치)
    ./darknet detector train mmi10/MyObj.data mmi10/yolov3-tiny-mmi10.cfg mmi10/backup4/yolov3-tiny-mmi10.backup
<br>

## 2) Validation
    ./darknet detector valid (.data파일 위치) (.cfg파일 위치) (.weights 위치) -thresh 0.4(옵션. 안 써도 됨) 
    ./darknet detector valid mmi9/MyObj.data mmi9/yolov3-tiny-mmi9.cfg mmi9/backup66/yolov3-tiny-mmi9_940000.weights -thresh 0.4 
<br>

원래는 명령어를 돌리면 "result"라는 폴더에 "comp4_det_test_(레이블명)"으로 저장만 된다. (YOLOv3 코드가 그렇게 설정)<br>
[![detector.c 참조](https://i.postimg.cc/NjbcsKGd/validation-code.png)](https://postimg.cc/TKySQYDb)<br>
그러나 mAP를 구하기 위해 mAP 구하는 평가 코드에 YOLOv3 valid 명령과 연동시켜 동시에 돌아가게 하였음.<br>


## 3) Demo
    ./darknet detector(.data파일 위치) (.cfg파일 위치) (.weights 위치) (비디오 파일 위치) -thresh 0.4(옵션. 안 써도 됨) 
    ./darknet detector demo mmi10/MyObj.data mmi10/yolov3-tiny-mmi10.cfg mmi10/backup2/yolov3-tiny-mmi10_275000.weights Traffic2.avi -thresh 0.4
<br>

# 3. What I changed
## 1) image -> structure
yolov3에서는 코드 작성자가 본인이 image 저장용 structure를 만들어서 사용. channel은 rgb이고 normalized되어 있어서, 이를 opencv에 쓸 Mat로 변환함.
<br> 
<br>

## 2) cvui 사용
출처 : https://github.com/Dovyski/cvui<br>
사용법 : https://dovyski.github.io/cvui/<br><br><br>

* 정말 도움 많이 받았다. 굉장히 사용하기 간편하고, 디자인도 괜찮고, 기능도 많다.<br>
* 이를 통해 gui를 구성했으며, original, icon, video select mode로 나뉜다.<br>
* icon 모드의 경우, 아이콘으로 마우스 이동 시 해당 아이콘 기능을 설명.
<br> 
<br>

## 3) Alarm 기능 설정
* 화면에 ROI를 표시할 수 있게 하였다. 점 4개 찍어서 만들 수도 있고, 사각형을 그릴 수도 있다.<br>
* 또한 ROI의 투명도도 조절 가능하며, 어떤 object를 알람 띄울 것인지도 선택 가능.<br>
Alarm의 경우도 person/bicycle, car는 ROI와 겹칠 시 바닥에 각각 빨강, 파랑 alaram이 뜨며, 투명도 조절 가능
<br> 
<br>

## 4) 그 외 기능
* FPS 표시 가능.<br>
* Threshold(정확히는 predicted probability) 표시 가능.<br>
* object별 predicted probability 표시 가능.<br>



