# AIIC
Code for Fourth session China Graduate AI Innovation Competition : Applied practice competition questions

## Installation

```shell
conda create -n aiic python=3.7 -y
conda activate aiic
conda install pytorch==1.10.0 torchvision==0.11.0 torchaudio==0.10.0 cudatoolkit=11.3 -c pytorch -c conda-forge
conda install cython scipy
pip install -U 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI'
```
```
# linux only , windows pass this step
python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu113/torch1.10/index.html
```


## Data Prepare

Download [data](https://drive.google.com/file/d/1hB6UX7rIsnNiOmh5vp1EeHtEBtrdCnUr/view?usp=sharing) to `$AIIC/data`


### Set Your own COCO Dataset Config

my dataset example:
```shell
    ├── data
    │   └── ship2022
    │       ├── annotations
    │       │   ├── objectDetection_test2022.json
    │       │   ├── objectDetection_train2022.json
    │       │   └── objectDetection_val2022.json
    │       ├── test2022
    │       │   └── jpgs
    │       ├── train2022
    │       │   └──jpgs
    │       └── val2022
    │           └──jpgs
    ├── datasets
    │   ├── coco_eval.py
    │   ├── coco_panoptic.py
    │   ├── coco.py
    │   ├── __init__.py
    │   ├── panoptic_eval.py
    │   └── transforms.py

```
set `datasets/coco.py` with dataset 

```python
def build(image_set, args):
    root = Path(args.coco_path)
    assert root.exists(), f'provided COCO path {root} does not exist'
    mode = 'objectDetection'
    PATHS = {
        "train": (root / "train2022", root / "annotations" / f'{mode}_train2022.json'),
        "val": (root / "val2022", root / "annotations" / f'{mode}_val2022.json'),
    }

    img_folder, ann_file = PATHS[image_set]
    dataset = CocoDetection(img_folder, ann_file, transforms=make_coco_transforms(image_set), return_masks=args.masks)
    return dataset
```
## Inference

```
python inference.py --batch_size 2 --no_aux_loss --eval --resume detr-r50-e632da11.pth --coco_path data/ship2022/
```

## Train

```
python main.py --batch_size 2 --coco_path data/ship2022/
```

## Test
```
python test.py --batch_size 2 --no_aux_loss --eval --resume detr-r50-e632da11.pth --coco_path data/ship2022/
```