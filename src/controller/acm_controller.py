from model.map_model import MapModel
from model.acm_model import ACMModel
from model.dicom_model import DicomModel
from model.label_model import LabelModel
from model.image_model import ImageModel
from classes.levelset_parameters import LevelsetParameter

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

    __button_levelset_ok = None

    __hander_end_levelset = None

    @staticmethod
    def set_label_levelset_iteration(ui):
        ACMController.__label_levelset_iteration = ui
        ACMController.__label_levelset_iteration.setText(str(ACMModel.get_levelset_parameters_value()[0]))

    @staticmethod
    def set_label_levelset_alpha(ui):
        ACMController.__label_levelset_alpha = ui
        ACMController.__label_levelset_alpha.setText(str(ACMModel.get_levelset_parameters_value()[1]))


    @staticmethod
    def set_label_levelset_lambda(ui):
        ACMController.__label_levelset_lambda = ui
        ACMController.__label_levelset_lambda.setText(str(ACMModel.get_levelset_parameters_value()[2]))


    @staticmethod
    def set_label_levelset_epsilon(ui):
        ACMController.__label_levelset_epsilon = ui
        ACMController.__label_levelset_epsilon.setText(str(ACMModel.get_levelset_parameters_value()[3]))


    @staticmethod
    def set_label_levelset_sigma(ui):
        ACMController.__label_levelset_sigma = ui
        ACMController.__label_levelset_sigma.setText(str(ACMModel.get_levelset_parameters_value()[4]))

    @staticmethod
    def set_hander_end_levelset(handler):
        ACMController.__hander_end_levelset = handler

    @staticmethod
    def set_slider_levelset_iteration(slider_levelset_iteration):
        ACMController.__slider_levelset_iteration = slider_levelset_iteration
        ACMController.__slider_levelset_iteration.setMinimum(0)
        ACMController.__slider_levelset_iteration.setMaximum(len(LevelsetParameter.Iterations)-1)
        ACMController.__slider_levelset_iteration.blockSignals(True)
        ACMController.__slider_levelset_iteration.setValue(int((len(LevelsetParameter.Iterations)-1)/2))
        ACMController.__slider_levelset_iteration.blockSignals(False)

    @staticmethod
    def set_slider_levelset_alpha(slider_levelset_alpha):
        ACMController.__slider_levelset_alpha = slider_levelset_alpha
        ACMController.__slider_levelset_alpha.setMinimum(0)
        ACMController.__slider_levelset_alpha.setMaximum(len(LevelsetParameter.Alphas)-1)
        ACMController.__slider_levelset_alpha.blockSignals(True)
        ACMController.__slider_levelset_alpha.setValue(int((len(LevelsetParameter.Alphas)-1)/2))
        ACMController.__slider_levelset_alpha.blockSignals(False)

    @staticmethod
    def set_slider_levelset_lambda(slider_levelset_lambda):
        ACMController.__slider_levelset_lambda = slider_levelset_lambda
        ACMController.__slider_levelset_lambda.setMinimum(0)
        ACMController.__slider_levelset_lambda.setMaximum(len(LevelsetParameter.Lambdas)-1)
        ACMController.__slider_levelset_lambda.blockSignals(True)
        ACMController.__slider_levelset_lambda.setValue(int((len(LevelsetParameter.Lambdas)-1)/2))
        ACMController.__slider_levelset_lambda.blockSignals(False)

    @staticmethod
    def set_slider_levelset_epsilon(slider_levelset_epsilon):
        ACMController.__slider_levelset_epsilon = slider_levelset_epsilon
        ACMController.__slider_levelset_epsilon.setMinimum(0)
        ACMController.__slider_levelset_epsilon.setMaximum(len(LevelsetParameter.Epsilons)-1)
        ACMController.__slider_levelset_epsilon.blockSignals(True)
        ACMController.__slider_levelset_epsilon.setValue(int((len(LevelsetParameter.Epsilons)-1)/2))
        ACMController.__slider_levelset_epsilon.blockSignals(False)

    @staticmethod
    def set_slider_levelset_sigma(slider_levelset_sigma):
        ACMController.__slider_levelset_sigma = slider_levelset_sigma
        ACMController.__slider_levelset_sigma.setMinimum(0)
        ACMController.__slider_levelset_sigma.setMaximum(len(LevelsetParameter.Sigmas)-1)
        ACMController.__slider_levelset_sigma.blockSignals(True)
        ACMController.__slider_levelset_sigma.setValue(int((len(LevelsetParameter.Sigmas)-1)/2))
        ACMController.__slider_levelset_sigma.blockSignals(False)

    @staticmethod
    def set_button_levelset_ok(ui):
        ACMController.__button_levelset_ok = ui

    @staticmethod
    def change_levelset_parameters():

        ACMModel.set_levelset_parameters(
            ACMController.__slider_levelset_iteration.value(),
            ACMController.__slider_levelset_alpha.value(),
            ACMController.__slider_levelset_lambda.value(),
            ACMController.__slider_levelset_epsilon.value(),
            ACMController.__slider_levelset_sigma.value(),
        )
        parameters = ACMModel.get_levelset_parameters_value()
        ACMController.__label_levelset_iteration.setText(str(parameters[0]))
        ACMController.__label_levelset_alpha.setText(str(parameters[1]))
        ACMController.__label_levelset_lambda.setText(str(parameters[2]))
        ACMController.__label_levelset_epsilon.setText(str(parameters[3]))
        ACMController.__label_levelset_sigma.setText(str(parameters[4]))
        ACMController.__set_levelset_result()

    #
    # Snake method
    #

    def snake_press(x, y):
        temp_pos = MapModel.click_pos_to_image_pos((x, y))
        ACMModel.set_start_point(temp_pos)

    def snale_drag(x, y):
        if(ACMModel.is_selecting()):
            temp_pos = MapModel.click_pos_to_image_pos((x, y))
            ACMModel.set_end_point(temp_pos)

    def snake_release(x, y):
        ACMController.snake_drag(x, y)
        points = ACMModel.acm_snake(ImageModel.get_array_pixel_hist())
        if(len(points)>0):
            LabelModel.regist_writting_label_by_acm(points, LabelModel.generate_label_id(), DicomModel.get_current_index())
        ACMModel.reset_start_point()
        ACMModel.reset_end_point()

    #
    # level set method
    #

    def levelset_press(x, y):
        temp_pos = MapModel.click_pos_to_image_pos((x, y))
        ACMModel.set_start_point(temp_pos)

    def levelset_drag(x, y):
        if(ACMModel.is_selecting()):
            temp_pos = MapModel.click_pos_to_image_pos((x, y))
            ACMModel.set_end_point(temp_pos)

    def levelset_release(x, y):
        ACMController.levelset_drag(x, y)
        ACMModel.acm_levelset(ImageModel.get_array_pixel_hist(), ACMController.__hander_end_levelset)
        ACMModel.reset_start_point()
        ACMModel.reset_end_point()

    def levelset_regist():
        LabelModel.regist_suspended_label(LabelModel.generate_label_id(), DicomModel.get_current_index())
        LabelModel.reset_suspended_label()

    def levelset_end():
        ACMController.__set_levelset_result()

    def __set_levelset_result():
        points = ACMModel.get_levelset_result()
        print(points)
        LabelModel.reset_suspended_label()
        if(len(points)>0):
            LabelModel.add_suspended_label(points, DicomModel.get_current_index())

    def update_acm():
        if(LabelModel.is_suspended_label()):
            ACMController.__button_levelset_ok.setEnabled(True)
        else:
            ACMController.__button_levelset_ok.setEnabled(False)
