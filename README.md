# R-PMS-on-Jetson-Tx2
Real-time Pedestrian Monitoring System on NVIDIA Jetson Tx2 using YOLOv3

ubuntu 터미널에 다음과 같이 치세요 : git clone https://github.com/OldGrand114/R-PMS-on-Jetson-Tx2.git


# Intro...
졸업 프로젝트(디자인 프로젝트) 결과 백업용.
참고 하실 분은 참고하시되 한정된 주제에 대해 간략히 정리한 것이라 큰 도움은 안 됨.

디자인 프로젝트의 일환으로 Jetson Tx2 보드 상에서 YOLOv3을 이용한 Object Detection을 구현.
YOLOv3와 YOLOv3-tiny 비교 결과 YOLOv3는 약 2fps, YOLOv3-tiny는 약 20 fps를 보였으며 YOLOv3-tiny를 수정하여 성능 개선을 꾀함.

약 6~7m 높이에 설치되는 가로등에 설치되는 CCTV 환경을 가정함.
객체의 크기가 영상 내에서 매우 작게 나타난다는 특징이 있음.
이에 따라 오토바이 탑승자, 자전거 탑승자의 경우 오토바이 부분, 자전거 부분을 사람과 구분하여 GT(Ground-Truth)로 설정할 경우 영상에서 매우 작게 나타나 제대로 된 학습이 불가능함.
따라서 자전거, 보행자 class를 탑승자와 함께 묶어 GT를 설정하였으나 Network capacity의 한계로 class간 오검출 현상이 발생함.
추후 학습 시 자전거 class 오토바이 class 삭제 및 자전거 탑승자는 person class로 셜정, 오토바이 class는 negative image로 설정할 것을 추천.

# 구현 목표
1. 처리속도 : 입력 영상 크기와 동일한 크기의 출력 영상에 대해 약 10 fps 
2. Person, Car, Bicycle, Motorcycle, Truck의 5가지 class에 대해 검출 시도
3. mAP 90% 이상
4. Person missing rate 5% 이하

cf) 자전거 class를 제외하고 평가시 목표 달성. 포함 시 오검출 현상으로 정성적 평가는 매우 떨어짐.ㅠㅠ

# 개발 환경
0. Jetson Tx2 보드 1대, 학습용 PC 1대, 노트북 1대
1. 공통
 - Ubuntu 16.04
 - CUDA 9.0
 - CUDNN 7.1.4
 - OpenCV 3.3.1
 
2. 학습용 PC
 - NVIDIA Geforce GTX 1070 TI
 
3. 실험용 노트북 PC
 - NVIDIA Geforce GTX 1060

# YOLOv3
Joseph Redmon과 Ali Farhadi를 찬양하십시오. 갓갓
YOLO 및 Darknet은 YOLO를 구글에서 검색하시고 홈페이지 들어가서 다운받으세요. 링크는 서비스

https://pjreddie.com/darknet/yolo/

https://github.com/pjreddie/darknet

https://github.com/AlexeyAB/darknet

YOLO는 C로 작성된 Darknet Framework로 구현되어 있으며 자세한 설명은 위의 홈페이지를 참고하시면 Tutorial은 끝.
천천히 따라 해보시는게 최소삽질로 최대이득을 볼 수 있습니다.

# 내맘대로 YOLO 설명(일단은 돌려보기)
0. YOLO 홈페이지에서 Darknet 설치 및 tutorial 해봤다는 가정하에 진행.
1. mmi9 폴더를 darknet 하위로 이동
 1-1. yolov3-tiny-mmi9.cfg
     1) cfg 파일에서 본인이 원하는 네트워크 구성 가능.
     2) class 개수를 C라고 할 때
        (1) [yolo] 에서 classes 를 C로 설정.
        (2) [yolo] 바로 위 [convolutional]에서 filters를 (C+5)*3 으로 설정.
        (3) [net]에서 입력 영상 resizing 크기는 width, height를 변경할 수 있음(32배수)
        (4) [upsample]에서 stride를 조절하여 upsampling 배수 조절 가능(클수록 작은 물체를 더 잘 검출하나 연산량 많이 요구)
        (5) [route]는 network load 하면서 입력 dimension 잘 보고 조절해야.......
1-2. MyObj.data
     1) 학습 관련 directory 설정 파일
     2) classes 는 목표 class 개수로 알아서 설정.
     3) train에는 training image data가 저장되어 있는 txt 파일 directory로 설정.
     4) names에는 각 class의 이름이 적혀있는 파일의 directory로 설정.
     5) valid에는 Validation set directory 설정.
     6) backup에는 weight 파일 및 backup 파일 directory 설정.
1-3. MyObj.names
     1) Class 이름 적어 놓은 파일
        
        


