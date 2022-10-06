import os

"""
Make sure validation images in final come from val folders
Same for training.
"""

nightowls_val_images = '/usr/src/datasets/nightowls_val1/images'
nightowls_val_labels = '/usr/src/datasets/nightowls_combined_with_coco_val/labels'
nightowls_train_images = '/usr/src/datasets/nightowls_train1/images'
nightowls_train_labels = '/usr/src/datasets/nightowls_combined_with_coco_train/labels'

coco_val_images =  '/usr/src/datasets/coco_val1/images'
coco_train_images =  '/usr/src/datasets/coco_train1/images'
coco_val_labels =  '/usr/src/datasets/coco_val1/labels'
coco_train_labels =  '/usr/src/datasets/coco_train1/labels'

final_train_images = '/usr/src/datasets/combined_final/train/images/'
final_train_labels = '/usr/src/datasets/combined_final/train/labels/'
final_val_images = '/usr/src/datasets/combined_final/val/images/'
final_val_labels = '/usr/src/datasets/combined_final/val/labels/'


#Maybe I should replace these file paths with the original datasets. Not just the ones I created using the COCO API. i.e. val2017, train2017, nightowls_validation, 

for f in os.listdir(final_train_images):
    if f.endswith('.jpg'):
        if f not in os.listdir(coco_train_images): print('bad')
    elif f.endswith('.png'):
        if f not in os.listdir(nightowls_train_images): print('bad')

for f in os.listdir(final_val_images):
    if f.endswith('.jpg'):
        if f not in os.listdir(coco_val_images): print('bad')
    elif f.endswith('.png'):
        if f not in os.listdir(nightowls_val_images): print('bad')
    