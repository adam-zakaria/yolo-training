import imp
from math import dist
import os
from collections import Counter
import copy
#overlaying the classes on top of each other on a hist could be nice!

n = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
        'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
        'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
        'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
        'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
        'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
        'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
        'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
        'hair drier', 'toothbrush']  # class names


#{class: count}
def distribution(label_files: str) -> dict:
    """
    read all label files
    count each label
    print distribution
    """
    c = Counter()
    for f in os.listdir(label_files):
        with open(os.path.join(label_files, f)) as f1:
            for l in f1:
                label = l.split()[0]
                c.update([label])
    return c 
"""
Counter, specifically c.update, must not work how it seems, because 
"""

def remap(c: Counter) -> dict:
    d = {}
    for k in c.keys():
        name = n[int(k)]
        d[name] = c[k]
    return d

def percentage(d: dict):
    total = sum(list(d.values()))
    #c = d
    for k,v in d.items():
        d[k] = v/total
    return d

if __name__ == '__main__':
    ct = distribution('/usr/src/datasets/nightowls_training_out_reannotated_with_coco/labels')
    cv = distribution('/usr/src/datasets/nightowls_validation_out_reannotated_with_coco/labels')
    dt = remap(ct)
    dv = remap(cv)
    dt1 = percentage(dt)
    dv1 = percentage(dv)