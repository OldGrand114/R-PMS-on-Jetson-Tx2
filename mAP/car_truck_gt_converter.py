import os
import shutil

# 아래 디렉토리들은 본인에게 맞는 디렉토리로 다 바꿔야 한다.
os.chdir('/home/tkol/mAP/ground-truth')


if not os.path.exists('/home/tkol/mAP/ground-truth/backup2'): # if it doesn't exist already
  os.makedirs('/home/tkol/mAP/ground-truth/backup2')

os.system('mv *.txt backup2')

os.chdir('backup2')

gt_list = os.listdir()

for txt_name in gt_list:
    os.chdir('/home/tkol/mAP/ground-truth/backup2')
    txt_old = open(txt_name, 'r')
    os.chdir('/home/tkol/mAP/ground-truth')
    txt_new = open(txt_name, 'w')
    line = txt_old.readlines()
    for obj in line:
        if obj[0:5] == 'truck':
            backline = obj[5:]
            convert_line = 'car' + backline
            #print(convert_line)
            txt_new.write(convert_line)
        else:
            txt_new.write(obj)

    txt_new.close()
    txt_old.close()

