<img src="https://github.com/adam-zakaria/yolo-training/blob/main/imgs/yolo-after-dark-logo-crop.png">

# Architecture

<img src="https://github.com/adam-zakaria/yolo-training/blob/main/imgs/yolo_training_architecture.png">

# Setup
These instructions are not thoroughly tested and will need to be troubleshooted - use them as a guideline :)

## Container setup
I slightly augment the command from https://github.com/ultralytics/yolov5/wiki/Docker-Quickstart
```
sudo docker run --ipc=host -it --gpus all ultralytics/yolov5:latest
```
to enable multiple containers to share the datasets folder on the host, to expose a port in the container on Purple (to enable FiftyOne remote use) and to add a name to the container. Fill in the information in the angle brackets before executing the command.
```
docker run --name <container_name> --ipc=host -dit -v /home/mxu/Downloads/yolo_datasets:/usr/src/raw_datasets -p <host_port>:<container_port> --gpus all ultralytics/yolov5:latest
```
I've had trouble limiting the gpu access to a single GPU (I've specifically been instructed to use GPU 1) during docker run, so instead run 
```
export CUDA_VISIBLE_DEVICES=1
```
once in the container. 
Enter the container with
```
docker exec -it <your-container> bash
```

## Clone the pipeline
```
cd /usr/src/
git clone https://github.com/adam-zakaria/yolo-training.git
```

## Apply Seung Jae's dual validation patch
```
git config --global user.email "you@example.com"
git clone https://github.com/adam-zakaria/sj_yolo.git
cd sj_yolo/
git diff df80e7c723b5722fe5b8d935ace73b8b28572ed4 > /usr/src/app/dual_val.patch
cd /usr/src/app
git checkout -b dual_val
git reset --hard df80e7c723b5722fe5b8d935ace73b8b28572ed4
git apply dual_val.patch
git add .
git commit -m "dual val patch"
```

## Training
Trainings are configured by yaml files, which by default exist in /usr/src/app/data. Here is Ultralytics' documentation on training custom data like we are doing: https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data See 1.1 Create dataset.yaml for information on the yaml files. Note: the collapsible menu in section 1 needs to be expanded to reveal section 1.1.

Below is an example of a train command that is run in the background and will not exit if the terminal that executes the command exits. This has been important for me because I haven't been able to prevent my machine from sleeping and sometimes trainings exit prematurely. 
```
cd /usr/src/app
nohup python train.py --batch 80 --device 0 --weights yolov5n.pt --data /usr/src/datasets/dataset.yaml --epochs 50 --name n130064t_n51848v_c5000v_remapped &
```
There are also detect.py and val.py scripts that are relatively similar. Below are sample commands:
```
python val.py --task val --data /usr/src/yolov5/data/n25000t.yaml --weights yolov5n.pt --device 1 --verbose --save-txt --save-hybrid --save-conf --save-json  --name yolov5n_n5000v_remapped
```
```
python detect.py --data "" --source /usr/src/datasets/n1000t/remapped/images --weights yolov5x.pt --save-txt --name n1000t
```
It is less common to use val.py now that we have dual-validation support.

## FiftyOne
I've set up FiftyOne but have not documented it. If there is interest in using it please let me know and I can organize documentation.

## The code
### Executing a stage of the pipeline
At the bottom of each file in the pipeline there exist strings that should be populated with the name of the dataset that you wish to apply a specific pipeline stage to. For instance, in base.py simply pass the dataset like so: ```produce_dataset('n100t')``` Datasets must be in the form <dataset_name><number of images><training or validation>, i.e. 'n12400t', 'n242v', 'c2422t', 'c224v', where n and c stand for nightowls and coco.

### Adding a dataset
To add support for a new dataset, the first step would be to add cases for the dataset in ```dataset_helper()``` in base.py and add files to the specified locations. I have not thought about adding support for new datasets beyond this step.

### Reannotate.py
Reannotate requires that a detection be run on the Nightowls data like so:
```python detect.py --data "" --source /usr/src/datasets/n1000t/remapped/images --weights yolov5x.pt --save-txt --name n1000t```
Notice that yolov5x.pt is used: we want the best annotations possible so we use the largest model.

## VSCode Remote Connection
To connect to the container remotely using VSCode bring up the command palette with ctrl+shift+p and type 'Connect to Host'.
### Problems
There is a problem where I am repeatedly prompted for a password despite typing in the correct one. A solution for me was ctrl+shift+p 'Kill VSCode Server on Host'.
A lot of other problems have occurred that I have not documented. Please pull me in if you are experiencing a stubborn issue and I may be able to help.
