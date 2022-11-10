# YOLO at night

[<img src="https://github.com/adam-zakaria/yolo-training/blob/main/imgs/yolo-after-dark-logo.png">](YOLO after dark)


# Nightowls 
Nightowls paper
https://www.robots.ox.ac.uk/~vgg/publications/2018/Neumann18b/neumann18b.pdf
"As a result, the dataset contains 279k fully annotated frames with 42, 273
pedestrians, where 32k frames contain at least one annotated object and the
remaining 247k are the background images"

Nightowls training

# COCO
https://cocodataset.org/#download

class distributions do not seem to be on the website, but they are likely somewhere.
coco val class distro
https://blog.roboflow.com/coco-dataset/

https://arxiv.org/pdf/1405.0312.pdf


# Some pycocotools notes
"""
getImgIds() -> list[imgId] 
loadImgs(ids : [imgId]) -> list[img]
getAnnIds(imgIds: list[imgId]) -> list[annId]
loadAnns(ids: list[annId]) -> list[ann]

*One imgId can be multiple annIds
*One annId is one ann


#imgIds need to have annotations and those annotations bboxes must not be negative
#write_label_files need
    #filename, which are in imgs
    #catIds, which are in anns
    #bboxes, which are in anns
"""