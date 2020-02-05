import tkinter #python3
from tkinter import messagebox as tkMessageBox #python3
from tkinter import filedialog as tkFileDialog #python3
import glob
import tqdm
import os

import json
import collections as cl
import numpy as np
from classes.label import Label
from classes.nodule import Nodule
import cv2

class FileModel:

    __is_save_more_than_once = False
    __select_open_file = 'c:/'   #'c:/' #Windows
    __select_save_file = 'c:/'   #'c:/' #Windows

    @staticmethod
    def select_open_file():
        root = tkinter.Tk() #python3
        root.withdraw()
        select_file = tkFileDialog.askopenfilename(initialdir = os.path.dirname(FileModel.__select_open_file), filetypes = [("dicom json png files", "*.dcm;*.json;*.png")])
        FileModel.__select_open_file = select_file
        print(select_file)
        FileModel.__is_save_more_than_once = False

    @staticmethod
    def select_save_file():
        root = tkinter.Tk() #python3
        root.withdraw()
        select_file = tkFileDialog.asksaveasfilename(initialdir = os.path.dirname(FileModel.__select_save_file), filetypes = [("json files","*.json")])
        FileModel.__select_save_file = select_file
        FileModel.__is_save_more_than_once = True

    @staticmethod
    def do_exist_select_open_file():
        return os.path.exists(FileModel.__select_open_file)

    @staticmethod
    def is_open_file_dcm():
        root_ext_pair = os.path.splitext(FileModel.__select_open_file)
        return root_ext_pair[1] == ".dcm"

    @staticmethod
    def is_open_file_json():
        root_ext_pair = os.path.splitext(FileModel.__select_open_file)
        return root_ext_pair[1] == ".json"

    @staticmethod
    def is_open_file_png():
        root_ext_pair = os.path.splitext(FileModel.__select_open_file)
        return root_ext_pair[1] == ".png"

    @staticmethod
    def get_select_open_dir():
        return os.path.dirname(FileModel.__select_open_file)

    @staticmethod
    def get_select_open_file():
        return FileModel.__select_open_file

    @staticmethod
    def get_select_open_file_npy():
        root_ext_pair = os.path.splitext(FileModel.__select_open_file)
        return root_ext_pair[0] + ".npy"

    @staticmethod
    def get_select_save_file_json():
        root_ext_pair = os.path.splitext(FileModel.__select_save_file)
        return root_ext_pair[0] + ".json"

    @staticmethod
    def get_select_save_file_npy():
        root_ext_pair = os.path.splitext(FileModel.__select_save_file)
        return root_ext_pair[0] + ".npy"


    @staticmethod
    def get_labels():
        with open(FileModel.get_select_open_file()) as f:
            df = json.load(f)

        labels_json = df["nodule_me"]["labels"]
        labels = []
        for label_json in labels_json:
            label = Label()
            label.set_json(label_json)
            labels.append(label)
        return labels

    @staticmethod
    def get_nodules():
        with open(FileModel.get_select_open_file()) as f:
            df = json.load(f)

        nodules_json = df["nodule_me"]["nodules"]
        nodules = []
        for nodule_json in nodules_json:
            nodule = Nodule()
            nodule.set_json(nodule_json)
            nodules.append(nodule)
        return nodules

    @staticmethod
    def get_npy():
        return np.load(FileModel.get_select_open_file_npy())

    @staticmethod
    def get_pixel_spacing():
        with open(FileModel.get_select_open_file()) as f:
            df = json.load(f)
        pixel_spacing = df["PixelSpacing"]
        return pixel_spacing

    @staticmethod
    def get_slice_thickness():
        with open(FileModel.get_select_open_file()) as f:
            df = json.load(f)
        slice_thickness = df["SliceThickness"]
        return slice_thickness



    @staticmethod
    def get_png():
        img = cv2.imread(FileModel.get_select_open_file_png(), 0)
        return img.astype(np.int16)


    @staticmethod
    def get_init_top_png():
        img = cv2.imread("./ui/top_image.png", 0)
        return img.astype(np.int16)


    @staticmethod
    def is_save_more_than_once():
        return FileModel.__is_save_more_than_once




    """
    {
        nodule_me: {
            "labels": [
                {
                    label_id: 1,
                    points: [
                        [21,22],[35,40],[25,30]
                    ]
                },
                {
                    label_id: 2,
                    points: [
                        [21,22],[35,40]
                    ]
                }
            ],
            "nodule": [
                {
                    user_id: 101,
                    malignant_level: 5,
                    comments: "hogehogehoge",
                },
                {

                },
            ]
        }
    }
    """

    @staticmethod
    def save_as_json(labels, nodules, slices, pixel_spacing, slice_thickness):
        ys = cl.OrderedDict()
        nodule_me_json = cl.OrderedDict()

        labels_json = []
        for label in labels:
            labels_json.append(label.get_json())
        nodule_me_json["labels"] = labels_json

        nodules_json = []
        for nodule in nodules:
            nodules_json.append(nodule.get_json())
        nodule_me_json["nodules"] = nodules_json

        ys["nodule_me"] = nodule_me_json
        ys["PixelSpacing"] = pixel_spacing
        ys["SliceThickness"] = slice_thickness
        print(ys)

        fw = open(FileModel.get_select_save_file_json(),'w')
        json.dump(ys, fw, indent=4)

        np.save(FileModel.get_select_save_file_npy(), slices)
