import sys
import json
import os

def folder_exist(data_path):
    exist = os.path.exists(data_path)
    if not exist:
        os.mkdir(data_path)
    return exist

def merge(data_path):
    annotation_folder_name = 'annotations'
    # # get train test val data folder's abspath 
    # if folder_exist(data_path):
    #     sub_folders = os.listdir(os.path.abspath(data_path))
    #     if annotation_folder_name in sub_folders:
    #         annotation_path = os.path.abspath(os.path.join(data_path, annotation_folder_name))
    #         annotation_files = os.listdir(annotation_path)
    # for i, folder in enumerate(sub_folders):
    #     if folder.__contains__("train"):
    #         train_jpgs = os.listdir(os.path.abspath(os.path.join(data_path, folder)))
    #         for ann in annotation_files:
    #             if ann.__contains__("train"):
    #                 train_annotation = json.load(open(os.path.join(annotation_path,ann)))
    #                 for id, image in enumerate(train_annotation['images']):
    #                     print(image['file_name'])

if __name__ == '__main__':
    merge("data/ship2022")
