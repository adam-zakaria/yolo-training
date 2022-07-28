# %%
%matplotlib inline
from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import json
pylab.rcParams['figure.figsize'] = (8.0, 10.0)


# %%
dataDir='/Users/azakaria/Downloads'
dataType='val2017'
annFile=f'{dataDir}/annotations/instances_{dataType}.json'

# %%
# initialize COCO api for instance annotations
coco=COCO(annFile)

# %%
# display COCO categories and supercategories
cats = coco.loadCats(coco.getCatIds())
cat_map = {}
for i,cat in enumerate(cats):
    cat_map[cat['id']] = i
#print(len(cats))
#print(coco.anns.keys()) #keys are the image ids I believe
#print(coco.anns[1768].keys())
nms=[cat['name'] for cat in cats]
#print(nms)
#print([cat['id'] for cat in cats])
print(cat_map)

# %%
catIds = coco.getCatIds()
def get_img_ids_for_training(catIds):
    imgIds = []
    for catId in catIds:
        imgIds_current_batch = coco.getImgIds(catIds=[catId])[:3000]
        if(len(imgIds_current_batch) < 30):
            print('ERROR! Not 30 images in this category!')
        imgIds = imgIds + imgIds_current_batch
    return imgIds

# %%
from pathlib import Path
def coco_to_yolo_bb(x1, y1, w, h, image_w, image_h):
    #"bbox": [x,y,width,height], (COCO)
    #x_center y_center width height (YOLO)
    return [((2*x1 + w)/(2*image_w)) , ((2*y1 + h)/(2*image_h)), w/image_w, h/image_h]
ann_c = set()
def write_label_file(imgId):
    # using with statement
    img = coco.loadImgs(imgId)[0]
    label_dir = Path('/Users/azakaria/Code/openmpf-yolo-training/dataset/labels')
    filename = img['file_name'].split('.')[0] + '.txt'
    #print(img['file_name'])
    with open(label_dir/filename, 'w') as file:
        for ann in coco.loadAnns(coco.getAnnIds(imgIds = imgId, catIds=catIds)):
            ann_c.add(ann["category_id"])
            if ann["category_id"] > 80:
                print(ann["category_id"])
            x_center, y_center, width, height = coco_to_yolo_bb(*ann['bbox'], img['width'], img['height'])
            file.write(f'{cat_map[ann["category_id"]]}\t{x_center}\t{y_center}\t{width}\t{height}\n')
    return

# %%


# %%
img_ids = get_img_ids_for_training(catIds)
for img_id in img_ids:
    write_label_file(img_id)

print(len(ann_c))
print(ann_c)

# %%
import os
import shutil

def copy_images_for_dataset_dir():
    src_image_dir = Path('/Users/azakaria/Downloads/val2017')
    fs = os.listdir('/Users/azakaria/Code/openmpf-yolo-training/dataset/labels')
    for f in fs:
        src = str(src_image_dir/f.split('.')[0]) + '.jpg'
        dest = '/Users/azakaria/Code/openmpf-yolo-training/dataset/images/' + f.split('.')[0] + '.jpg'
        print(str(src_image_dir/f.split('.')[0]) + '.jpg')
        shutil.copyfile(src, dest)
        #print(image_dir/f.split('.')[0])
    return
copy_images_for_dataset_dir()


