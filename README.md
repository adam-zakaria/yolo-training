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
to enable multiple containers to share the datasets folder on the host. I also add support for exposing port 5151 in the container on the host to use FiftyOne remotely. 
```
docker run --gpus 1 --ipc=host -dit -v /home/mxu/Downloads/yolo_datasets:/usr/src/raw_datasets ultralytics/yolov5:latest -p 5151:5151
```
I've had trouble limiting the gpu access to a single GPU (I've specifically been instructed to use GPU 1) during docker run, so instead run 
```
export CUDA_VISIBLE_DEVICES=1
```
once in the container. 

## Applying Seung Jae's dual validation patch
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

## FiftyOne
I've set up FiftyOne but have not documented it. If there is interest in using it please let me know and I can organize documentation.