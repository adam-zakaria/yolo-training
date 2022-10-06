import os 
import random
import shutil
from pathlib import Path
import glob


#Keep the nightowls_combined_with_coco data in place,
#But create train.txt and val.txt to reference each set
#Copy the nightowls val set and the coco val set
#and create the text files


#Write two files referencing files in two image directories
#Assumes correct number of images in dirs
def write_txt_file(img_dir1, img_dir2, dest_dir, txt_file):
    fs = [os.path.join(dest_dir, f) for f in os.listdir(img_dir1) + os.listdir(img_dir2)]
    random.shuffle(fs)
    print(fs)
    with open(txt_file,'w') as txt:
        for f in fs:
            #txt.write(os.path.join('img_dir1', f) + '\n')
            txt.write(f'{f}\n')
            print(f)
            #txt.write( + '\n')

#Same as above, but only use one dataset
def write_txt_file_pure(img_dir1, dest_dir, txt_file):
    fs = [os.path.join(dest_dir, f) for f in os.listdir(img_dir1)]
    random.shuffle(fs)
    print(fs)
    with open(txt_file,'w') as txt:
        for f in fs:
            txt.write(f'{f}\n')
            print(f)

def copy_datasets(src, dest):
    #Straightforward - copy files from src dir to dest dir
    src = Path(src)
    dest = Path(dest)
    fs = os.listdir(src)
    for f in fs:
        if os.path.isfile(src/f):
            shutil.copyfile(src/f, dest/f)
        else:
            print(f'{src/f} is not a file')
    return

def remove_files(dirs):
    for dir in dirs:
        files = glob.glob(f'{dir}*')
        for f in files:
            os.remove(f)

def print_sanity_checks(dir):
    print(f'ls {dir} | wc -l ; ls {dir} | wc -l')
    os.system(f'ls {dir} | wc -l ; ls {dir} | wc -l')

#another sanity check
def print_lines_in_txt_files():
    #print('wc -l /usr/src/datasets/combined_final/train.txt')
    print('')
    print('--------------')
    os.system('wc -l /usr/src/datasets/combined_final/train.txt')
    #print('wc -l /usr/src/datasets/combined_final/val.txt')
    os.system('wc -l /usr/src/datasets/combined_final/val.txt')
    print('--------------')

if __name__ == "__main__":
    nightowls_val_images = '/usr/src/datasets/nightowls_val1/images'
    nightowls_val_labels = '/usr/src/datasets/nightowls_val1_reannotated_with_coco/labels'
    nightowls_train_images = '/usr/src/datasets/nightowls_train1/images'
    nightowls_train_labels = '/usr/src/datasets/nightowls_train1_reannotated_with_coco/labels'

    coco_val_images =  '/usr/src/datasets/coco_val1/images'
    coco_train_images =  '/usr/src/datasets/coco_train1/images'
    coco_val_labels =  '/usr/src/datasets/coco_val1/labels'
    coco_train_labels =  '/usr/src/datasets/coco_train1/labels'

    final_train_images = '/usr/src/datasets/combined_final/train/images/'
    final_train_labels = '/usr/src/datasets/combined_final/train/labels/'
    final_train = '/usr/src/datasets/combined_final/train/'
    final_val_images = '/usr/src/datasets/combined_final/val/images/'
    final_val_labels = '/usr/src/datasets/combined_final/val/labels/'
    final_val =  '/usr/src/datasets/combined_final/val/'

    train_txt = '/usr/src/datasets/combined_final/train.txt'
    val_txt = '/usr/src/datasets/combined_final/val.txt'

    nct_ncv = False
    nct_nv = True
    if nct_ncv:
        #Write train.txt, with combined coco and no images
        write_txt_file(coco_train_images, nightowls_train_images, final_train_images, train_txt)
        #Write val.txt, with combined coco and no images
        write_txt_file(coco_val_images, nightowls_val_images, final_val_images, val_txt)

        #Write val.txt, with ONLY no

        remove_files([final_val_labels, final_val_images, final_train_labels, final_train_images])

        copy_datasets(nightowls_val_labels, final_val_labels)
        copy_datasets(nightowls_val_images, final_val_images)
        copy_datasets(nightowls_train_labels, final_train_labels)
        copy_datasets(nightowls_train_images, final_train_images)

        copy_datasets(coco_val_images, final_val_images)
        copy_datasets(coco_val_labels, final_val_labels)
        copy_datasets(coco_train_labels, final_train_labels)
        copy_datasets(coco_train_images, final_train_images)

        for dir in [final_val_labels, final_val_images, final_train_labels, final_train_images]:
            print_sanity_checks(dir)
    if nct_nv:
        write_txt_file(coco_train_images, nightowls_train_images, final_train_images, train_txt)
        write_txt_file_pure(nightowls_val_images, final_val_images, val_txt)
        remove_files([final_train_labels, final_train_images, final_val_labels, final_val_images])

        copy_datasets(coco_train_labels, final_train_labels)
        copy_datasets(coco_train_images, final_train_images)
        copy_datasets(nightowls_train_labels, final_train_labels)
        copy_datasets(nightowls_train_images, final_train_images)
        copy_datasets(nightowls_val_labels, final_val_labels)
        copy_datasets(nightowls_val_images, final_val_images)
        for dir in [final_train_labels, final_train_images, final_val_labels, final_val_images]:
            print_sanity_checks(dir)
        print_lines_in_txt_files()