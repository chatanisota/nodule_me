
from PyQt5.QtGui import QPixmap, QImage
import pydicom
import glob
import numpy as np
import cv2

class DicomModel():

    __dicom_pixel_spacing     = None
    __dicom_slice_thickness   = None
    __dicom_slices   = None
    __current_index  = 0

    @staticmethod
    def get_dicom_slice():
        return DicomModel.__dicom_slices[DicomModel.__current_index]

    @staticmethod
    def get_dicom_slice_num():
        return len(DicomModel.__dicom_slices)

    @staticmethod
    def open_dicom(select_dir):
        # カレントファイルを指定
        file_list_origin = glob.glob(select_dir+'/*.dcm')

        file_list = []
        # DIRFILE.dcmは削除
        for file in file_list_origin:
            if not ("DIRFILE.dcm" in file):
                print(file)
                file_list.append(file)

        if(file_list is None):
            return None

        # カレントファイルよりDICOMデータを読み込む
        slices = [pydicom.read_file(s) for s in file_list]

        slices.sort(key = lambda x: float(x.ImagePositionPatient[2]))

        DicomModel.__dicom_slices  = [s.pixel_array for s in slices]
        DicomModel.__dicom_slice_thickness = slices[0].SliceThickness
        DicomModel.__dicom_pixel_spacing = slices[0].PixelSpacing
        DicomModel.__current_index = 0

    @staticmethod
    def open_heads(pixel_spacing, slice_thickness):
        DicomModel.__dicom_slice_thickness = slice_thickness
        DicomModel.__dicom_pixel_spacing = pixel_spacing

    @staticmethod
    def open_png(np_array):
        DicomModel.__dicom_slices = [np_array]

    @staticmethod
    def set_current_index(index):
        DicomModel.__current_index = index

    @staticmethod
    def get_current_index():
        return DicomModel.__current_index

    @staticmethod
    def get_pixel_spacing():
        pixel_spacing = DicomModel.__dicom_pixel_spacing
        return [float(pixel_spacing[0]),float(pixel_spacing[1])]

    @staticmethod
    def get_slice_thickness():
        return DicomModel.__dicom_slice_thickness

    #出力用
    @staticmethod
    def get_dicom_slices():
        return DicomModel.__dicom_slices

    #書き込み用
    @staticmethod
    def open_npy(npys):
        DicomModel.__dicom_slices = [n for n in npys]

    @staticmethod
    def reset():
        DicomModel.__current_index  = 0
