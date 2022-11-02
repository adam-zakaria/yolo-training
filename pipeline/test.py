import os
import re

def rl(file):

    with open(file, 'r') as f:
        return [l.strip() for l in f.readlines()]

def test(name):

    ds = '/usr/src/datasets/'
    remapped_src = os.path.join(ds,name,'remapped/labels')
    detect_src = f'/usr/src/yolov5/runs/detect/{name}/labels/'
    reannotated_dest = os.path.join(ds,name, 'reannotated/labels')

    command = f'ls {detect_src} | wc -l'
    print(command)
    os.system(command)
    num_missing_files = 0
    for f in os.listdir(remapped_src)[:]:
        if f not in os.listdir(detect_src):
            num_missing_files += 1
            continue
        #print(f)
        #lines_input = rl(os.path.join(remapped_src,f)) +  rl(os.path.join(detect_src,f))
        #lines_output = rl(os.path.join(reannotated_dest, f))
        #print(f'len(lines_input): {len(lines_input)}')
        #print(f'len(lines_output): {len(lines_output)}')

    print(f'{num_missing_files}/{len(os.listdir(remapped_src)[:])} files from {remapped_src} missing from {detect_src}')
    #print(remapped_src, detect_src, reannotated_dest)

test('n1000t')