import os
import re

def readlines(file):
    with open(file, 'r') as f:
        return [l.strip() for l in f.readlines()]

def mkdir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def test(name):
    ds = '/usr/src/datasets/'
    remapped_src = os.path.join(ds,name,'remapped/labels')
    detect_src = f'/usr/src/yolov5/runs/detect/{name}/labels/'
    reannotated_dest = os.path.join(ds,name, 'reannotated/labels')
    mkdir(reannotated_dest)

    command = f'ls {detect_src} | wc -l'
    print(command)
    os.system(command)
    num_missing_files = 0
    fs = os.listdir(remapped_src)
    for f in fs:
        if f not in os.listdir(detect_src):
            num_missing_files += 1
            continue
        else:
            lines_input = readlines(os.path.join(remapped_src,f)) +  readlines(os.path.join(detect_src,f))
            lines_output = readlines(os.path.join(reannotated_dest, f))
            if lines_input != lines_output:
                print(f, lines_input, lines_output)
                print('Lines input not equal to lines output!')
                return

    print(f'{num_missing_files}/{len(fs)} files from {remapped_src} missing from {detect_src}')
    #print(remapped_src, detect_src, reannotated_dest)

test('n1000t')