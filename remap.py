import os
import shutil
from pathlib import Path
import glob
import shutil 

def remove_files(img_dir, label_dir):
    # Remove all files from a folder but do not delete the folder
    files = glob.glob(f'{img_dir}*')
    for f in files:
        os.remove(f)
    files = glob.glob(f'{label_dir}*')
    for f in files:
        os.remove(f)

def remap_labels_no_to_coco(nightowls_labels_path, remapped_labels_path):
    # Remove Nightowls ignore area, and map every other category to person (0)
    fs = os.listdir(nightowls_labels_path)
    for f in fs:
        filename_nightowls = f'{nightowls_labels_path}{f}'
        ls = "" 
        with open(filename_nightowls, encoding='latin-1') as fx:
            for l in fx:
                l = l.split()
                l[0] = '0'
                l = ' '.join(l) + '\n'
                ls += l
        with open(f'{remapped_labels_path}{f}','w' ,encoding='latin-1') as fy:
            fy.write(f'{ls}')

def copy_images(src_image_dir, dest_image_dir):
    """
    Straightforward - copy files from src dir to dest dir
    """
    fs = os.listdir(src_image_dir)
    for f in fs:
        if os.path.isfile(src_image_dir/f):
            shutil.copyfile(src_image_dir/f, dest_image_dir/f)
        else:
            print(f'{src_image_dir/f} is not a file')
    return

def remap_dataset(dirs):
    remove_files(dirs['remapped_labels'], dirs['remapped_images'])

    remap_labels_no_to_coco(dirs['labels'], dirs['remapped_labels'])
    copy_images(Path(dirs['images']), Path(dirs['remapped_images']))


def mkdir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

def create_dataset_dirs(dataset_names):
    #Create a set of input and output dirs for each dataset
    datasets_dirs = []
    for name in dataset_names:
        src = f'/usr/src/datasets/source/{name}'
        dest = f'/usr/src/datasets/{name}/remapped'
        datasets_dirs.append(dict(labels = f'{src}/labels/',
                                remapped_labels = f'{dest}/labels/',
                                images =  f'{src}/images/',
                                remapped_images = f'{dest}/images/'
                                ))
    for dataset_dirs in datasets_dirs:
        mkdir(dataset_dirs['remapped_labels'])
        mkdir(dataset_dirs['remapped_images'])
    return datasets_dirs

def test_dirs(remapped_labels):
    fs = os.listdir(remapped_labels)
    for f in fs:
        remapped_label = f'{remapped_labels}{f}'
        ls = "" 
        with open(remapped_label, encoding='latin-1') as fx:
            for l in fx:
                l = l.split()
                if l[0] != '0':
                    print(f'Class {l[0]} found')
                    print("All classes should map to COCO's person class. Exiting")
            
    print("Test passed: all remapped label files only reference class 0, COCO's person class.")

def print_num_files_in_dir(dir):
    print(f"ls {dir} | wc -l")
    os.system(f"ls {dir} | wc -l")


if __name__ == "__main__":

    # change these for each run, assumes source/{name} is populated:
    # source should be put under the dataset, i.e. n1000t/base/:
    # supports multiple dataset_names
    #dataset_names = ['n25000t','n5000t']
    dataset_names = ['n100t', 'n100v']
    for dirs in create_dataset_dirs(dataset_names):
        remap_dataset(dirs)
        print_num_files_in_dir(dirs['remapped_labels'])
        print_num_files_in_dir(dirs['remapped_images'])
        test_dirs(dirs['remapped_labels'])