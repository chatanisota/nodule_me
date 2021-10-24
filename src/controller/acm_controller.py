from model.map_model import MapModel
from model.acm_model import ACMModel
from model.dicom_model import DicomModel
from model.label_model import LabelModel
from model.image_model import ImageModel

class ACMController:

    __label_levelset_iteration = None
    __label_levelset_alpha = None
    __label_levelset_lambda = None
    __label_levelset_epsilon = None
    __label_levelset_sigma = None
    __slider_levelset_iteration = None
    __slider_levelset_alpha = None
    __slider_levelset_lambda = None
    __slider_levelset_epsilon = None
    __slider_levelset_sigma = None

    @staticmethod
    def set_label_levelset_iteration(ui):
        ACMController.__label_levelset_iteration = ui

    @staticmethod
    def set_label_levelset_alpha(ui):
        ACMController.__label_levelset_alpha = ui

    @staticmethod
    def set_label_levelset_lambda(ui):
        ACMController.__label_levelset_lambda = ui

    @staticmethod
    def set_label_levelset_epsilon(ui):
        ACMController.__label_levelset_epsilon = ui

    @staticmethod
    def set_label_levelset_sigma(ui):
        ACMController.__label_levelset_sigma = ui

    @staticmethod
    def set_slider_levelset_iteration(slider_levelset_iteration):
        ACMController.__slider_levelset_iteration = slider_levelset_iteration
        ACMController.__slider_levelset_iteration.setMinimum(0)
        ACMController.__slider_levelset_iteration.setMaximum(10)
        ACMController.__slider_levelset_iteration.setValue(5)

    @staticmethod
    def set_slider_levelset_alpha(slider_levelset_alpha):
        ACMController.__slider_levelset_alpha = slider_levelset_alpha
        ACMController.__slider_levelset_alpha.setMinimum(0)
        ACMController.__slider_levelset_alpha.setMaximum(10)
        ACMController.__slider_levelset_alpha.setValue(5)

    @staticmethod
    def set_slider_levelset_lambda(slider_levelset_lambda):
        ACMController.__slider_levelset_lambda = slider_levelset_lambda
        ACMController.__slider_levelset_lambda.setMinimum(0)
        ACMController.__slider_levelset_lambda.setMaximum(10)
        ACMController.__slider_levelset_lambda.setValue(5)

    @staticmethod
    def set_slider_levelset_epsilon(slider_levelset_epsilon):
        ACMController.__slider_levelset_epsilon = slider_levelset_epsilon
        ACMController.__slider_levelset_epsilon.setMinimum(0)
        ACMController.__slider_levelset_epsilon.setMaximum(10)
        ACMController.__slider_levelset_epsilon.setValue(5)

    @staticmethod
    def set_slider_levelset_sigma(slider_levelset_sigma):
        ACMController.__slider_levelset_sigma = slider_levelset_sigma
        ACMController.__slider_levelset_sigma.setMinimum(0)
        ACMController.__slider_levelset_sigma.setMaximum(10)
        ACMController.__slider_levelset_sigma.setValue(5)


    @staticmethod
    def change_levelset_parameters():

        if ( ACMController.__slider_levelset_iteration == None
            or ACMController.__slider_levelset_alpha == None
            or ACMController.__slider_levelset_lambda == None
            or ACMController.__slider_levelset_epsilon == None
            or ACMController.__slider_levelset_sigma == None ):
            return

        ACMModel.set_levelset_parameters(
            ACMController.__slider_levelset_iteration.value(),
            ACMController.__slider_levelset_alpha.value(),
            ACMController.__slider_levelset_lambda.value(),
            ACMController.__slider_levelset_epsilon.value(),
            ACMController.__slider_levelset_sigma.value(),
        )
        parameters = ACMModel.get_levelset_parameters()
        ACMController.__label_levelset_iteration.setText(str(parameters[0]))
        ACMController.__label_levelset_alpha.setText(str(parameters[1]))
        ACMController.__label_levelset_lambda.setText(str(parameters[2]))
        ACMController.__label_levelset_epsilon.setText(str(parameters[3]))
        ACMController.__label_levelset_sigma.setText(str(parameters[4]))

    @staticmethod
    def change_min_slider():
        min = ACMController.__slider_min_histogram.value()
        HistogramModel.set_min(min)
        ACMController.__slider_levelset_.setValue(HistogramModel.get_max())
        ACMController.__spin_min_histogram.blockSignals(True)
        ACMController.__spin_levelset_.blockSignals(True)
        ACMController.__spin_min_histogram.setValue(HistogramModel.get_min())
        ACMController.__spin_levelset_.setValue(HistogramModel.get_max())
        ACMController.__spin_min_histogram.blockSignals(False)
        ACMController.__spin_levelset_.blockSignals(False)

    @staticmethod
    def change_max_spin():
        max = ACMController.__spin_levelset_.value()
        HistogramModel.set_max(max)
        ACMController.__slider_levelset_.setValue(HistogramModel.get_max())
        ACMController.__slider_min_histogram.setValue(HistogramModel.get_min())
        ACMController.__spin_min_histogram.blockSignals(True)
        ACMController.__spin_min_histogram.setValue(HistogramModel.get_min())
        ACMController.__spin_min_histogram.blockSignals(False)

    @staticmethod
    def change_min_spin():
        min = ACMController.__spin_min_histogram.value()
        HistogramModel.set_min(min)
        ACMController.__slider_levelset_.setValue(HistogramModel.get_max())
        ACMController.__slider_min_histogram.setValue(HistogramModel.get_min())
        ACMController.__spin_levelset_.blockSignals(True)
        ACMController.__spin_levelset_.setValue(HistogramModel.get_max())
        ACMController.__spin_levelset_.blockSignals(False)

    def acm_press(x, y):
        temp_pos = MapModel.click_pos_to_image_pos((x, y))
        ACMModel.set_start_point(temp_pos)

    def acm_drag(x, y):
        if(ACMModel.is_selecting()):
            temp_pos = MapModel.click_pos_to_image_pos((x, y))
            ACMModel.set_end_point(temp_pos)

    def acm_release(x, y):
        ACMController.acm_drag(x, y)
        points = ACMModel.acm_acm(ImageModel.get_array_pixel_hist())
        if(len(points)>0):
            LabelModel.regist_writting_label_by_acm(points, LabelModel.generate_label_id(), DicomModel.get_current_index())
        ACMModel.reset_start_point()
        ACMModel.reset_end_point()
