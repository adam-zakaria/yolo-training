#!/bin/bash
echo 'ls /usr/src/datasets/nightowls_val1/labels/* | wc -l' 
echo 'ls /usr/src/datasets/nightowls_val1/images/* | wc -l' 
ls /usr/src/datasets/nightowls_val1/labels/* | wc -l
ls /usr/src/datasets/nightowls_val1/images/* | wc -l

echo 'ls /usr/src/datasets/coco_val1/labels/* | wc -l' 
echo 'ls /usr/src/datasets/coco_val1/images/* | wc -l' 
ls /usr/src/datasets/coco_val1/labels/* | wc -l
ls /usr/src/datasets/coco_val1/images/* | wc -l

echo 'ls /usr/src/datasets/coco_train1/labels/* | wc -l' 
echo 'ls /usr/src/datasets/coco_train1/images/* | wc -l' 
ls /usr/src/datasets/coco_train1/labels/* | wc -l
ls /usr/src/datasets/coco_train1/images/* | wc -l

echo 'ls /usr/src/datasets/nightowls_train1/labels/* | wc -l' 
echo 'ls /usr/src/datasets/nightowls_train1/images/* | wc -l' 
ls /usr/src/datasets/nightowls_train1/labels/* | wc -l
ls /usr/src/datasets/nightowls_train1/images/* | wc -l

echo 'ls /usr/src/datasets/nightowls_train1_reannotated_with_coco/labels/* | wc -l' 
echo 'ls /usr/src/datasets/nightowls_train1_reannotated_with_coco/images/* | wc -l' 
ls /usr/src/datasets/nightowls_train1_reannotated_with_coco/labels/* | wc -l
ls /usr/src/datasets/nightowls_train1_reannotated_with_coco/images/* | wc -l


echo 'ls /usr/src/datasets/nightowls_val1_reannotated_with_coco/labels/* | wc -l' 
echo 'ls /usr/src/datasets/nightowls_val1_reannotated_with_coco/images/* | wc -l' 
ls /usr/src/datasets/nightowls_val1_reannotated_with_coco/labels/* | wc -l
ls /usr/src/datasets/nightowls_val1_reannotated_with_coco/images/* | wc -l

#echo 'ls /usr/src/datasets/combined_final/labels/* | wc -l' 
#echo 'ls /usr/src/datasets/combined_final/images/* | wc -l' 
#ls /usr/src/datasets/combined_final/labels/* | wc -l
#ls /usr/src/datasets/combined_final/images/* | wc -l
