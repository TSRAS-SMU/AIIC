import sys
import json
import os

def folder_exist(data_path):
    exist = os.path.exists(data_path)
    if not exist:
        os.mkdir(data_path)
    return exist

def repath(data_path):
    annotation_folder_name = 'annotations'
    # get train test val jpg data folder's abspath 
    if folder_exist(data_path):
        sub_folders = os.listdir(os.path.abspath(data_path))
        # get train test val annotation json data folder's abspath 
        if annotation_folder_name in sub_folders:
            annotation_path = os.path.abspath(os.path.join(data_path, annotation_folder_name))
            # annotation_files = os.listdir(annotation_path)
    # repath train test val jpg data path
    for set in ['train', 'test', 'val']:
        # eg: objectDetection_train2022.json 
        # TODO: set your annotation json file's name like eg.
        annotation_name = "objectDetection_" + set + "2022.json"
        for _, folder in enumerate(sub_folders):
            # if folder name contain train or test or val
            if folder.__contains__(set):
                train_jpgs = os.listdir(os.path.abspath(os.path.join(data_path, folder)))
                new_path = {}
                # use id to make sure json's file_name match new_path's value
                for id, jpg in enumerate(train_jpgs):
                    new_path[id] = jpg
                # load json file data
                train_annotation = json.load(open(os.path.join(annotation_path,annotation_name)))
                # update new_path to data
                for key, value in new_path.items():
                    if train_annotation['images'][key]['id'] == key:
                        train_annotation['images'][key]['file_name'] = value
                # write data to output file
                with open(os.path.join(annotation_path,annotation_name), "w") as outfile:
                    outfile.write(json.dumps(train_annotation))
                
if __name__ == "__main__":
    repath("data/ship2022")