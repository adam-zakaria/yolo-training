import os

nightowls_labels_path = '/usr/src/datasets/nightowls_val/labels/'
yolo_labels_path = '/usr/src/yolov5/runs/detect/exp22/labels/'

fs = os.listdir('/usr/src/datasets/nightowls_val/labels')
##print(len(fs))
for f in fs:
    filename_nightowls = f'{nightowls_labels_path}{f}'
    filename_yolo = f'{yolo_labels_path}{f}'
    print(f)
    with open(filename_nightowls, encoding='latin-1') as fx:
        num_ped_nightowls = 0
        for l in fx:
            print(l)
            num_ped_nightowls += 1
        #print(f'{num_ped_nightowls}: num_ped_nightowls')
    if f not in os.listdir(yolo_labels_path):
        print(f'{f} not in {yolo_labels_path}')
        continue 
    print('--------')
    with open(filename_yolo, encoding='latin-1') as fy:
        #print(fy)
        num_ped_yolo = 0
        for l in fy:
            print(l)
            ##print(type(l.split()[0]))
            if int(l.split()[0]) == 0:
                num_ped_yolo += 1
        ##print(f'{num_ped_yolo}: num_ped_yolo')
    print(f'num_ped_nightowls == num_ped_yolo: {num_ped_nightowls==num_ped_yolo}')
    print('------------------------------------')