
from model.dicom_model import DicomModel
from model.file_model import FileModel
from model.label_model import LabelModel
from model.map_model import MapModel

class FileController():

    __button_open = None
    __button_save = None
    __button_save_as_new = None

    @staticmethod
    def set_button_open(ui):
        FileController.__button_open = ui

    @staticmethod
    def set_button_save(ui):
        FileController.__button_save = ui

    @staticmethod
    def set_button_save_as_new(ui):
        FileController.__button_save_as_new = ui

    @staticmethod
    def init_open():
        DicomModel.open_png(FileModel.get_init_top_png())


    @staticmethod
    def open():
        FileModel.select_open_file()
        if(FileModel.do_exist_select_open_file() == False):
            # ファイルが存在しない
            return 0
        LabelModel.reset()
        DicomModel.reset()
        MapModel.reset()
        if FileModel.is_open_file_dcm():
            # DICOM データを読み込み
            DicomModel.open_dicom(FileModel.get_select_open_dir())

        elif FileModel.is_open_file_json():
            # json データを読み込み
            LabelModel.input_labels(FileModel.get_labels())
            LabelModel.input_nodules(FileModel.get_nodules())
            DicomModel.open_heads(FileModel.get_pixel_spacing(), FileModel.get_slice_thickness())
            DicomModel.open_npy(FileModel.get_npy())

        elif FileModel.is_open_file_png():
            DicomModel.open_png(FileModel.get_png())

    @staticmethod
    def save():
        if(not FileModel.is_save_more_than_once()):
            FileModel.select_save_file()
        FileModel.save_as_json(LabelModel.get_labels_all(), LabelModel.get_nodules_all(), DicomModel.get_dicom_slices(), DicomModel.get_pixel_spacing(), DicomModel.get_slice_thickness())

    @staticmethod
    def save_as_new():
        FileModel.select_save_file()
        FileModel.save_as_json(LabelModel.get_labels_all(), LabelModel.get_nodules_all(), DicomModel.get_dicom_slices(), DicomModel.get_pixel_spacing(), DicomModel.get_slice_thickness())
