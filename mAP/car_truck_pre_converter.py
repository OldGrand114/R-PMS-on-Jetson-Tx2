import os
import shutil

os.chdir('/home/tkol/mAP/predicted')

if not os.path.exists('/home/tkol/mAP/predicted/backup'): # if it doesn't exist already
  os.makedirs('/home/tkol/mAP/predicted/backup')

os.system('mv *.txt backup')

os.chdir('backup')

gt_list = os.listdir()

for txt_name in gt_list:
    os.chdir('/home/tkol/mAP/predicted/backup')
    txt_old = open(txt_name, 'r')
    os.chdir('/home/tkol/mAP/predicted')
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

