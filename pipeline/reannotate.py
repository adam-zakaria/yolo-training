import os

#Reannotate Nightowls with YOLO AKA combine nightowls labels on nightowls with coco labels on nightowls into the same label file:
#*Assumes a detection has been run and the results are at <some_dir>
#
#There may be some amount of nightowls images that do not get a COCO label, because for whatever reason YOLO will not do a detection on those particular images.
#The following message will be produced in those cases:
#58c5832ebc2601370015a360.txt not in /usr/src/yolov5/runs/detect/exp8/labels/
#On one run, for 186 NO Val images there were 6 missing:
#root@5dcf6e04dbba:/usr/src/yolov5/misc# ls /usr/src/datasets/nightowls_val1_remapped/labels/ | wc -l
#196
#root@5dcf6e04dbba:/usr/src/yolov5/misc# ls /usr/src/yolov5/runs/detect/exp8/labels/ | wc -l
#nightowls combined with coco should really be renamed nightowls annotated with coco

def preamble():
    #PATHS (can be shared between functions)
    clear_output_dirs()
    cp_images()

#Make these files into variables
def clear_output_dirs():
    #This only does images...not sure why
    #it is images and labels for train and val.

    #remove_command_train = 'rm -rf '
    base_path = '/usr/src/datasets'
    reannotated_val = 'nightowls_val1_reannotated_with_coco'
    reannotated_val = 'nightowls_val1_reannotated_with_coco'
    remove_command_val = f'rm -rf {base_path}/{reannotated_val}/images/*; rm -rf ${base_path}/{reannotated_val}/labels/*'
    remove_command_train = f'rm -rf {base_path}/{reannotated_val}/images/*; rm -rf ${base_path}/{reannotated_val}/labels/*'
    reannotated_images_nightowls_train = f'rm -rf {base_path}/nightowls_train1_reannotated_with_coco/images/*;rm -rf /usr/src/datasets/nightowls_train1_reannotated_with_coco/labels/*'
    os.system(remove_command_val)
    os.system(reannotated_images_nightowls_train)

    print(remove_command_val)
    print(reannotated_images_nightowls_train)
    #We only work with the labels and don't modify the images, so just pass them through the pipeline untouched

def cp_all_files(src, dest):
    print(f'cp -R ${src}/* {dest}/images/')
    os.system(f'cp -R ${src}/* {dest}/images/')


#Make these files into variables
#def cp_images():
#    reannotated_images_nightowls_val = 'rm -rf /usr/src/datasets/nightowls_val1_reannotated_with_coco/images/*;rm -rf /usr/src/datasets/nightowls_val1_reannotated_with_coco/labels/*'
#    reannotated_images_nightowls_train = 'rm -rf /usr/src/datasets/nightowls_train1_reannotated_with_coco/images/*;rm -rf /usr/src/datasets/nightowls_train1_reannotated_with_coco/labels/*'
#    print('cp -R /usr/src/datasets/nightowls_train1_remapped/images/* /usr/src/datasets/nightowls_train1_reannotated_with_coco/images/')
#    os.system('cp -R /usr/src/datasets/nightowls_train1_remapped/images/* /usr/src/datasets/nightowls_train1_reannotated_with_coco/images/')
#
#    os.system('cp -R /usr/src/datasets/nightowls_val1_remapped/images/* /usr/src/datasets/nightowls_val1_reannotated_with_coco/images/')
#    print('cp -R /usr/src/datasets/nightowls_val1_remapped/images/* /usr/src/datasets/nightowls_val1_reannotated_with_coco/images/')

#Remove person detection from coco detections (detect.py output)
def remove_persons_from_labels(labels_file):
    with open(labels_file, encoding='latin-1') as fx:
        ls = ""
        for l in fx:
            if l.split()[0] == '0': continue
            else: 
                print(l)
                ls += l
    with open(labels_file, 'w', encoding='latin-1') as fy:
        fy.write(ls)
    return

#Append the COCO labels for some Nightowls image to the Nightowls label file of the same name
#Generic function used for train and val
#Expects label dirs to exist
def append_coco_labels_to_nightowls_labels(nightowls_labels, coco_labels, combined_labels):
    num_missing_files = 0
    #go through nightowls label files
    for f in os.listdir(nightowls_labels):
        with open(os.path.join(nightowls_labels,f), encoding='latin-1') as fx:
            ls = "" 
            #get all the lines for a specific file
            for l in fx:
                ls += l
            #if this label file does not have a coco equivalent, skip and print warning
            if f not in os.listdir(coco_labels):
                print(f'{f} not in {coco_labels}')
                num_missing_files += 1
                continue 
            else:
            #otherwise, write the coco labels to the combined file, first removing the persons labels
            #then, write the nightowls labels to the combined file
                remove_persons_from_labels(f'{coco_labels}{f}')
                with open(os.path.join(coco_labels,f), encoding='latin-1') as fy:
                    with open(os.path.join(combined_labels,f),'w' ,encoding='latin-1') as fz:
                        fz.write(ls)
                    with open(os.path.join(combined_labels,f),'a' ,encoding='latin-1') as fz:
                        for l in fy:
                            fz.write(f'{l}')
    #print(f'num_missing_files: {num_missing_files}')
    print(f'missing {num_missing_files}/{len(os.listdir(nightowls_labels))} files')

def print_sanity_checks(combined_dir):
    print(f'ls {combined_dir}labels | wc -l ; ls {combined_dir}labels | wc -l')
    os.system(f'ls {combined_dir}labels | wc -l ; ls {combined_dir}labels | wc -l')


if __name__ == "__main__":

    #Preface ------------------------
    #preamble()
    #----------------------------------

    def create_dataset_dirs(dataset_names):
        datasets_dirs = []
        ds = '/usr/src/datasets/'
        for name in dataset_names:
            nightowls_src = os.path.join(ds,name,'remapped/labels')
            coco_src = f'/usr/src/yolov5/runs/detect/{name}/labels/' #See above
            nightowls_dest = os.path.join(ds,name, 'reannotated/labels')
            datasets_dirs.append([nightowls_src, coco_src, nightowls_dest])
        return datasets_dirs

    def r(file):
        with open(file, 'r') as f:
            return f.read()

    def rl(file):
        with open(file, 'r') as f:
            return [l.strip() for l in f.readlines()]

    def w(file, data):
        with open(file, 'w') as f:
            f.write(data)

    def test(name):
        ds = '/usr/src/datasets/'
        remapped_src = os.path.join(ds,name,'remapped/labels')
        detect_src = f'/usr/src/yolov5/runs/detect/{name}/labels/'
        reannotated_dest = os.path.join(ds,name, 'reannotated/labels')
        for l in os.listdir(remapped_src)[0:3]:
            lines_input = rl(os.path.join(remapped_src)) +  rl(os.path.join(detect_src))
            lines_output = rl(os.path.join(reannotated_dest))
            print(f'len(lines_input): {len(lines_input)}')
            print(f'len(lines_output): {len(lines_output)}')
        print(dataset_dirs)


        """
        for f in os.listdir(nightowls_labels):
            with open(os.path.join(nightowls_labels,f), encoding='latin-1') as fx:
                ls = "" 
                #get all the lines for a specific file
                for l in fx:
                    ls += l
                #if this label file does not have a coco equivalent, skip and print warning
                if f not in os.listdir(coco_labels):
                    print(f'{f} not in {coco_labels}')
                    num_missing_files += 1
                    continue 
                else:
                #otherwise, write the coco labels to the combined file, first removing the persons labels
                #then, write the nightowls labels to the combined file
                    remove_persons_from_labels(f'{coco_labels}{f}')
                    with open(os.path.join(coco_labels,f), encoding='latin-1') as fy:
                        with open(os.path.join(combined_labels,f),'w' ,encoding='latin-1') as fz:
                            fz.write(ls)
                        with open(os.path.join(combined_labels,f),'a' ,encoding='latin-1') as fz:
                            for l in fy:
                                fz.write(f'{l}')
            """

    names = ['n1000t']
    for dataset_dirs in create_dataset_dirs(names): 
        append_coco_labels_to_nightowls_labels(*dataset_dirs)
    test('n1000t')