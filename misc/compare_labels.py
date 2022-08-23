import os

combine_labels = True
nightowls_labels_path = '/usr/src/datasets/nightowls_val/labels/'
yolo_labels_path = '/usr/src/yolov5/runs/detect/exp22/labels/'
combined_labels_path = '/usr/src/datasets/combined_labels/'

fs = os.listdir('/usr/src/datasets/nightowls_val/labels')
for f in fs:
    filename_nightowls = f'{nightowls_labels_path}{f}'
    filename_yolo = f'{yolo_labels_path}{f}'
    print(f)
    #print('Nightowls:')
    with open(filename_nightowls, encoding='latin-1') as fx:
        num_ped_nightowls = 0
        for l in fx:
            #print(l)
            num_ped_nightowls += 1
    if f not in os.listdir(yolo_labels_path):
        #print(f'{f} not in {yolo_labels_path}')
        continue 
    #print('--------')
    #print('YOLO:')
    with open(filename_yolo, encoding='latin-1') as fy:
        num_ped_yolo = 0
        for l in fy:
            #print(l)
            category = int(l.split()[0])
            if category == 0: #person
                num_ped_yolo += 1
            else:
                if combine_labels:
                    with open(f'{combined_labels_path}{f}','a' ,encoding='latin-1') as fz:
                        fz.write(f'{l}')
    if num_ped_nightowls <  num_ped_yolo:
        print(f'num_ped_nightowls < num_ped_yolo: {num_ped_nightowls <  num_ped_yolo}')
    ##print(f'num_ped_nightowls == num_ped_yolo: {num_ped_nightowls==num_ped_yolo}')
    #print('------------------------------------')
