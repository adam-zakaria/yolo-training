import os
import shutil
from pathlib import Path

nightowls_labels_path = '/usr/src/datasets/nightowls_val/labels/'
remapped_labels_path = '/usr/src/datasets/nightowls_mapped_to_coco/labels/'
nightowls_images_path = '/usr/src/datasets/nightowls_val/images/'
remapped_images_path = '/usr/src/datasets/nightowls_mapped_to_coco/images/'

os.system("rm -rf /usr/src/datasets/nightowls_mapped_to_coco/labels/* /usr/src/datasets/nightowls_mapped_to_coco/images/*")  

#Map every NO category to COCO's person (0)
fs = os.listdir('/usr/src/datasets/nightowls_val/labels')
for f in fs:
    filename_nightowls = f'{nightowls_labels_path}{f}'
    ls = "" 
    print(f)
    print('Nightowls:')
    with open(filename_nightowls, encoding='latin-1') as fx:
        for l in fx:
            l = l.split()
            l[0] = '0'
            l = '\t'.join(l) + '\n'
            ls += l
    with open(f'{remapped_labels_path}{f}','w' ,encoding='latin-1') as fy:
        fy.write(f'{ls}')

    #Copy all images in nightowls_labels_path to remapped_labels_path
    #shutil.copy(f'{nightowls_images_path}{f}',f'{remapped_images_path}{f}')

nightowls_images_path = '/usr/src/datasets/nightowls_val/images/'
remapped_images_path = '/usr/src/datasets/nightowls_mapped_to_coco/images/'

def copy_images_to_dataset_dir(src_image_dir, dest_image_dir, image_extension):
    """
    x number of labels are written to the labels dir by write_label_files(x)
    This function copies the corresponding images into the sibling images dir, completing the dataset folder for YOLO training
    """
    fs = os.listdir(src_image_dir)
    for f in fs:
        #src = str(src_image_dir/f.split('.')[0]) + image_extension
        #dest = str(dest_image_dir/ f.split('.')[0]) + image_extension
        if os.path.isfile(src_image_dir/f):
            shutil.copyfile(src_image_dir/f, dest_image_dir/f)
        else:
            print(f'{src_image_dir/f} is not a file')
    return

copy_images_to_dataset_dir(Path(nightowls_images_path), Path(remapped_images_path), '.png')

print('ls /usr/src/datasets/nightowls_mapped_to_coco/labels | wc -l ; ls /usr/src/datasets/nightowls_mapped_to_coco/images | wc -l')
os.system('ls /usr/src/datasets/nightowls_mapped_to_coco/labels | wc -l ; ls /usr/src/datasets/nightowls_mapped_to_coco/images | wc -l')
#473
#473
