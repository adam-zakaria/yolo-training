import os
import shutil
from pathlib import Path
import glob
import shutil 

def remove_files(img_dir, label_dir):
    files = glob.glob(f'{img_dir}*')
    for f in files:
        os.remove(f)
    files = glob.glob(f'{label_dir}*')
    for f in files:
        os.remove(f)


#Map every NO category to COCO's person (0)
def remap_labels_no_to_coco(nightowls_labels_path, remapped_labels_path):
    #fs = os.listdir('/usr/src/datasets/nightowls_val/labels')
    fs = os.listdir(nightowls_labels_path)
    for f in fs:
        filename_nightowls = f'{nightowls_labels_path}{f}'
        ls = "" 
        print(f)
        print('Nightowls:')
        with open(filename_nightowls, encoding='latin-1') as fx:
            for l in fx:
                l = l.split()
                l[0] = '0'
                l = ' '.join(l) + '\n'
                ls += l
        with open(f'{remapped_labels_path}{f}','w' ,encoding='latin-1') as fy:
            fy.write(f'{ls}')
        #Copy all images in nightowls_labels_path to remapped_labels_path
        #shutil.copy(f'{nightowls_images_path}{f}',f'{remapped_images_path}{f}')

def copy_images_to_dataset_dir(src_image_dir, dest_image_dir):
    """
    Straightforward - copy files from src dir to dest dir
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

def prepare_remapped_train_set():
    train_labels = '/usr/src/datasets/nightowls_train1/labels/'
    train_remapped_labels = '/usr/src/datasets/nightowls_train1_remapped/labels/'
    train_images = '/usr/src/datasets/nightowls_train1/images/'
    train_remapped_images = '/usr/src/datasets/nightowls_train1_remapped/images/'

    remove_files(train_remapped_labels, train_remapped_images)
    #shutil.rmtree(train_remapped_labels)
    #shutil.rmtree(train_remapped_images)

    remap_labels_no_to_coco(train_labels, train_remapped_labels)
    copy_images_to_dataset_dir(Path(train_images), Path(train_remapped_images))
    os.system(f'ls {train_remapped_images} | wc -l')
    os.system(f'ls {train_remapped_labels} | wc -l')

def prepare_remapped_val_set():
    val_labels = '/usr/src/datasets/nightowls_val1/labels/'
    val_remapped_labels = '/usr/src/datasets/nightowls_val1_remapped/labels/'
    val_images =  '/usr/src/datasets/nightowls_val1/images/'
    val_remapped_images = '/usr/src/datasets/nightowls_val1_remapped/images/'
    shutil.rmtree
    remove_files(val_remapped_labels, val_remapped_images)

    remap_labels_no_to_coco(val_labels,val_remapped_labels)
    copy_images_to_dataset_dir(Path(val_images), Path(val_remapped_images))
    os.system(f'ls {val_remapped_images} | wc -l')
    os.system(f'ls {val_remapped_labels} | wc -l')

if __name__ == "__main__":
    #A good refactor would be prepare_remapped_sets() and pass in args (more clear interface)
    prepare_remapped_train_set()
    #480
    #480
    prepare_remapped_val_set()
    #98
    #98