import tkinter #python3
from tkinter import messagebox as tkMessageBox #python3
from tkinter import filedialog as tkFileDialog #python3
import glob
from model.other_model import OtherModel
from model.dicom_model import DicomModel
from model.image_model import ImageModel

class FileController():

    @staticmethod
    def OpenDir():

        root = tkinter.Tk() #python3
        root.withdraw()

        #カレントファイルを指定
        select_dir = tkFileDialog.askdirectory(initialdir = OtherModel.get_current_dir())
        OtherModel.set_current_dir(select_dir)
        file_list = glob.glob(select_dir+'/*.dcm')

        if(file_list is None):
            return None

        #カレントファイルよりDICOMデータを読み込む
        DicomModel.read_dicom(file_list)
        dicom_data = DicomModel.get_dicom_slice()
        ImageModel.read_dicom(dicom_data.pixcel_array, dicom_data.pixel_array.shape[0], dicom_data.pixel_array.shape[1])
