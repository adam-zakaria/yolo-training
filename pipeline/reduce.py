import os
from pathlib import Path
import shutil
def remove_classes(src_dir, dest_dir):
    """Move from 80 coco classes to 6"""
    classes = [0,1,2,3,5,6] #'person','bicycle','car','motorcycle','bus','truck',
    for f in os.listdir(src_dir):
        ls = ""
        with open(os.path.join(src_dir,f), encoding='latin-1') as fx:
            for l in fx:
                if l.split()[0] in classes:
                    ls += l
        with open(os.path.join(dest_dir,f),'w' ,encoding='latin-1') as fy:
            fy.write(f'{ls}')

def copy_images(src_image_dir, dest_image_dir):
    """
    Straightforward - copy files from src dir to dest dir
    """
    src_image_dir = Path(src_image_dir)
    dest_image_dir = Path(dest_image_dir)
    fs = os.listdir(src_image_dir)
    for f in fs:
        #src = str(src_image_dir/f.split('.')[0]) + image_extension
        #dest = str(dest_image_dir/ f.split('.')[0]) + image_extension
        if os.path.isfile(src_image_dir/f):
            shutil.copyfile(src_image_dir/f, dest_image_dir/f)
        else:
            print(f'{src_image_dir/f} is not a file')
    return

if __name__ == "__main__":
    #coco val, nightowls val, nightowls train
    remove_classes('/usr/src/datasets/source/c5000v/labels', '/usr/src/datasets/c5000v/reduced/labels')
    #YOLO requires that labels and images are siblings
    copy_images('/usr/src/datasets/source/c5000v/images', '/usr/src/datasets/c5000v/reduced/images')