import os

# 본인이 사용할 디렉토리로 전부 바꿔라

os.chdir('/home/tkol/darknet/results')
os.system('cp *.txt ../../mAP/valid_result')
print('valid_result redirec complete\n')
os.chdir('/home/tkol/mAP/extra')
os.system('python convert_gt_yolo.py') # readme 맨 아래에 코드있는 거 다운받으면 된다.
os.chdir('/home/tkol/mAP/mAP_predict 변환 코드/')
os.system('./Valid_to_mAP')
print('predicted conversion complete\n')
os.chdir('..')
os.system('python3 car_truck_gt_converter.py')
print('GT conversion complete\n')
os.system('python3 car_truck_pre_converter.py')
print('Predicted conversion complete\n')
os.system('python3 main.py -na')
