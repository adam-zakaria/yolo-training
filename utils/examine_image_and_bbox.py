#During YOLO training, some images raise the warning:
#train: WARNING ⚠️ /usr/src/datasets/n130064t/base/images/58c583aebc2601370016bfdc.png: ignoring corrupt image/label: non-normalized or out of bounds coordinates [     1.0005      1.0342
#This file was created to confirm that the original bbox is out of the frame and there is no problem with the pipeline.
#Experiments should be run to decide if we should keep the images and simply remove the out of bounds annotations. Intuition says keep the images and remove the bad annotations because there are more good bboxes on the images than bad.

import json

def get_coco_annotation(filename, annotation_file):
    with open(annotation_file) as f:
        j = json.loads(f.read())
        image_data = []
        for e in j['images']:
            if e['file_name'] == filename:
                image_data.append(e)
                for e1 in j['annotations']:
                    if e1['image_id'] == e['id']:
                        image_data.append(e1['bbox'])
                return image_data

def coco_to_yolo_bb(x1, y1, w, h, image_w, image_h):
    return [((2*x1 + w)/(2*image_w)) , ((2*y1 + h)/(2*image_h)), w/image_w, h/image_h]

print(get_coco_annotation('58c583aebc2601370016bfe5.png','/usr/src/raw_datasets/nightowls/nightowls_training.json'))
print('*'*80)
print(get_coco_annotation('58c583aebc2601370016bfe3.png','/usr/src/raw_datasets/nightowls/nightowls_training.json'))
print('*'*80)
print(get_coco_annotation('58c583aebc2601370016bfde.png','/usr/src/raw_datasets/nightowls/nightowls_training.json'))
print('*'*80)
print(get_coco_annotation('58c583aebc2601370016bfdc.png','/usr/src/raw_datasets/nightowls/nightowls_training.json'))