# openmpf-personal

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