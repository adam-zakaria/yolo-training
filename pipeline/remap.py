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


#Remove Nightowls ignore area, and map every other category to person (0)
#
def remap_labels_no_to_coco(nightowls_labels_path, remapped_labels_path, remap_ignore_areas=True):
    #fs = os.listdir('/usr/src/datasets/nightowls_val/labels')
    fs = os.listdir(nightowls_labels_path)
    for f in fs:
        filename_nightowls = f'{nightowls_labels_path}{f}'
        ls = "" 
        print(f)
        with open(filename_nightowls, encoding='latin-1') as fx:
            for l in fx:
                l = l.split()
                if not remap_ignore_areas: 
                    if l[0] == 3: continue #Remove 'ignore area' labels
                l[0] == '0'
                l = ' '.join(l) + '\n'
                ls += l
        with open(f'{remapped_labels_path}{f}','w' ,encoding='latin-1') as fy:
            fy.write(f'{ls}')
        #Copy all images in nightowls_labels_path to remapped_labels_path
        #shutil.copy(f'{nightowls_images_path}{f}',f'{remapped_images_path}{f}')

def copy_images(src_image_dir, dest_image_dir):
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

def remap_dataset(dirs):
    remove_files(dirs['remapped_labels'], dirs['remapped_images'])

    remap_labels_no_to_coco(dirs['labels'], dirs['remapped_labels'])
    copy_images(Path(dirs['images']), Path(dirs['remapped_images']))

    print(f"ls {dirs['remapped_images']} | wc -l")
    os.system(f"ls {dirs['remapped_labels']} | wc -l")

if __name__ == "__main__":

    #           ***change these for each run, assumes source/{name} is populated***:
    dir_names = ['n25000t','n5000v']

    def create_dataset_dirs(dataset_names):
        datasets_dirs = []
        for name in dataset_names:
            src = f'/usr/src/datasets/source/{name}'
            dest = f'/usr/src/datasets/{name}/remapped'
            datasets_dirs.append(dict(labels = f'{src}/labels/',
                                    remapped_labels = f'{dest}/labels/',
                                    images =  f'{src}/images/',
                                    remapped_images = f'{dest}/images/'
                                    ))
            return datasets_dirs

    for dirs in create_dataset_dirs(dir_names):
        remap_dataset(dirs)

    #Remap Nightowls to COCO
    #To remap a dataset, add an append statement like below. Comment or remove those unwanted.
    #train_name = 'n25000t'
    #val_name = 'n5000v'
#    train = '/usr/src/datasets/source/n25000t'
#    train_remapped =  f'/usr/src/datasets/n25000t/remapped/'
#    datasets_dirs = []
#    datasets_dirs.append(nightowls_train := dict(labels = f'{train}/labels/',
#                                                    remapped_labels = f'{train_remapped}/labels/',
#                                                    images =  f'{train}/images/',
#                                                    remapped_images = f'{train_remapped}/images/'
#                                                    ))
#    val = '/usr/src/datasets/source/n5000v'
#    val_remapped =  f'/usr/src/datasets/n5000v/remapped'
#
#    datasets_dirs.append(nightowls_validation := dict(labels = f'{val}/labels/',
#                                                    remapped_labels = f'{val_remapped}/labels/',
#                                                    images =  f'{val}/images/',
#                                                    remapped_images = f'{val_remapped}/images/'
#                                                    ))
