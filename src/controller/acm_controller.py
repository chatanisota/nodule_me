from model.map_model import MapModel
from model.acm_model import ACMModel
from model.dicom_model import DicomModel
from model.label_model import LabelModel
from model.image_model import ImageModel

class ACMController:

    def acm_press(x, y):
        temp_pos = MapModel.click_pos_to_image_pos((x, y))
        ACMModel.set_start_point(temp_pos)

    def acm_drag(x, y):
        if(ACMModel.is_selecting()):
            temp_pos = MapModel.click_pos_to_image_pos((x, y))
            ACMModel.set_end_point(temp_pos)

    def acm_release(x, y):
        points = ACMModel.acm_acm(ImageModel.get_array_pixel_hist())
        LabelModel.regist_writting_label_by_acm(points, LabelModel.generate_label_id(), DicomModel.get_current_index())
        ACMModel.reset_start_point()
        ACMModel.reset_end_point()

    def acm_snake(x, y):
        # do
        ACMController.acm_drag(x, y)
        points = ACMModel.acm_acm(ImageModel.get_array_pixel_hist())
        print(points)
        LabelModel.regist_writting_label_by_acm(points, LabelModel.generate_label_id(), DicomModel.get_current_index())
        ACMModel.reset_start_point()
        ACMModel.reset_end_point()
