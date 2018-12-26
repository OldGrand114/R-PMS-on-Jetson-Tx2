# R-PMS-on-Jetson-Tx2
Real-time Pedestrian Monitoring System on NVIDIA Jetson Tx2 using YOLOv3

# Intro...
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

cf) 자전거 class를 제외하고 평가시 목표 달성. 포함 시 오검출 현상으로 정성적 평가는 매우 떨어짐.
