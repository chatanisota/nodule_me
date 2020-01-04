from model.dicom_model import DicomModel
from model.image_model import ImageModel

class IndexController:

    __slider_index = None
    __spin_index = None

    @staticmethod
    def set_slider_index(slider_index):
        IndexController.__slider_index = slider_index
        IndexController.__slider_index.setMinimum(0)
        IndexController.__slider_index.setMaximum(0)
        IndexController.__slider_index.setValue(0)


    @staticmethod
    def set_spin_index(ui):
        IndexController.__spin_index = ui
        IndexController.__spin_index.setMinimum(0)
        IndexController.__spin_index.setMaximum(0)
        IndexController.__spin_index.setValue(0)

    @staticmethod
    def change_slider():
        index = IndexController.__slider_index.value()
        DicomModel.set_current_index(index)

    @staticmethod
    def change_spin():
        index = IndexController.__spin_index.value()
        DicomModel.set_current_index(index)

    @staticmethod
    def change_image():
        IndexController.__slider_index.setMaximum(DicomModel.get_dicom_slice_num()-1)
        IndexController.__spin_index.setMaximum(DicomModel.get_dicom_slice_num()-1)
        IndexController.__slider_index.setValue(DicomModel.get_current_index())

    @staticmethod
    def update_index():
        IndexController.__slider_index.blockSignals(True)
        IndexController.__spin_index.blockSignals(True)
        IndexController.__spin_index.setValue(DicomModel.get_current_index())
        IndexController.__slider_index.setValue(DicomModel.get_current_index())
        IndexController.__spin_index.blockSignals(False)
        IndexController.__slider_index.blockSignals(False)
