# AIIC
Code for Fourth session China Graduate AI Innovation Competition : Applied practice competition questions

## Data Prepare

Download [data]() to `$AIIC/data`
> Upload data to this repository when competition end


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
    |       |   └── jpgs
    │       ├── train2022
    |       |   └──jpgs
    │       └── val2022
    |           └──jpgs
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

## Train

```python
python main.py --batch_size 2 --coco_path data/ship2022/

```