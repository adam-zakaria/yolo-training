import os
from pathlib import Path
import shutil
def remove_classes(src_dir, dest_dir):
    """Move from 80 coco classes to 6"""
    classes_mapping = {'0':'0','1':'1','2':'2','3':'3','5':'4','6':'5'} #'person','bicycle','car','motorcycle','bus','truck',
    classes = ['0','1','2','3','5','6'] #'person','bicycle','car','motorcycle','bus','truck',
    for f in os.listdir(src_dir):
        ls = ""
        with open(os.path.join(src_dir,f), encoding='latin-1') as fx:
            for l in fx:
                l = l.split()
                clas = l[0]
                if clas in classes_mapping.keys():
                    l[0] = classes_mapping[clas]
                    l = ' '.join(l) + '\n'
                    print(l)
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

def mkdir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
if __name__ == "__main__":
    #coco

#    for name in ['c5000v']:
#        remove_classes(f'/usr/src/datasets/source/{name}/labels', f'/usr/src/datasets/{name}/reduced/labels')
#        #YOLO requires that labels and images are siblings
#        copy_images(f'/usr/src/datasets/source/{name}/images', f'/usr/src/datasets/{name}/reduced/images')
#
    #nightowls

    ds = '/usr/src/datasets/'
    names = ['n1000t']
    for name in names:
        reannotated = os.path.join(ds,name,'reannotated')
        reannotated_labels = f'{reannotated}/labels'
        mkdir(reannotated)
        mkdir(reannotated_labels)

    for name in ['n1000t']:
        remove_classes(f'/usr/src/datasets/{name}/reannotated/labels', f'/usr/src/datasets/{name}/reduced/labels')
        #YOLO requires that labels and images are siblings
        #need to look into if symlinks are sufficient
        copy_images(f'/usr/src/datasets/source/{name}/images', f'/usr/src/datasets/{name}/reduced/images')