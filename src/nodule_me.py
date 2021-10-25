# pyinstaller nodule_me.py --onefile --noconsole --icon=nodule_me.ico
# pyuic5 ./qt_designer/ui_noduleme.ui -o ./qt_designer/ui_noduleme.py
# pyuic5 ui_label.ui -o ui_label.py
# pyuic5 ui_pen.ui -o ui_pen.py
# pyuic5 ui_hello.ui -o ui_hello.py

import sys, os
import glob
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QButtonGroup
from PyQt5.QtGui import QPixmap, QImage, QPalette
from PyQt5.QtCore import Qt
import pydicom
import cv2
import numpy as np
from qt_designer.ui_noduleme import *
from qt_designer.ui_hello import *
from handler.handler import Handler
from handler.view_handler import ViewHander
from classes.message_dialog import MessageDialog



class MyForm(QWidget):

    __is_finish_init = False

    def __init__(self, parent=None):
        super().__init__()

        # ダイアログの設定
        self.setWindowFlags(
            Qt.Window|
            Qt.WindowMinimizeButtonHint|
            Qt.WindowCloseButtonHint
            )

        # 起動時の画像
        img = cv2.imread("./ui/wait_image.png")
        cv2.imshow("wait please...", img)
        cv2.waitKey(1)

        super(MyForm, self).__init__(parent)
        print("== SETTING Main Dialog ==")

        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)

        print("== Handler setting... ==")
        #ハンドラのセット
        Handler.set_main_dialog(self)
        Handler.set_label_image(self.ui.labelImage)
        Handler.set_button_open(self.ui.buttonOpen)
        Handler.set_button_save(self.ui.buttonSave)
        Handler.set_button_save_as_new(self.ui.buttonSaveAsNew)
        Handler.set_label_histogram(self.ui.labelHistogram)
        Handler.set_slider_max_histogram(self.ui.sliderMaxHistogram)
        Handler.set_slider_min_histogram(self.ui.sliderMinHistogram)
        Handler.set_slider_index(self.ui.sliderIndex)
        Handler.set_label_map(self.ui.labelMap)
        Handler.set_button_zoom_up(self.ui.buttonZoomUp)
        Handler.set_button_zoom_down(self.ui.buttonZoomDown)
        Handler.set_button_zoom_default(self.ui.buttonZoomDefault)
        Handler.set_scroll_bar_x(self.ui.scrollBarX)
        Handler.set_scroll_bar_y(self.ui.scrollBarY)
        Handler.set_spin_max_histogram(self.ui.spinMaxHistogram)
        Handler.set_spin_min_histogram(self.ui.spinMinHistogram)
        Handler.set_spin_index(self.ui.spinIndex)
        Handler.set_table_widget_labels(self.ui.tableWidgetLabels)
        Handler.set_button_switch_solo_all(self.ui.buttonSwitchSoloAll)
        Handler.set_button_switch_my_everyone(self.ui.buttonSwitchMyEveryone)
        Handler.set_button_delete_label(self.ui.buttonDeleteLabel)
        Handler.set_button_corsor(self.ui.buttonCoursor)
        Handler.set_button_pen(self.ui.buttonPen)
        Handler.set_button_pinset(self.ui.buttonPinset)
        Handler.set_button_eracer(self.ui.buttonEracer)
        Handler.set_button_tube(self.ui.buttonTube)
        Handler.set_button_snake(self.ui.buttonACMSnake)
        Handler.set_button_levelset(self.ui.buttonLevelset)
        Handler.set_combo_box_user(self.ui.comboBoxUser)
        Handler.set_label_info(self.ui.labelInfo)
        Handler.set_widget_levelset(self.ui.widgetLevelset)
        Handler.set_label_levelset_iteration(self.ui.labelLevelsetIteration)
        Handler.set_label_levelset_alpha(self.ui.labelLevelsetAlpha)
        Handler.set_label_levelset_lambda(self.ui.labelLevelsetLambda)
        Handler.set_label_levelset_epsilon(self.ui.labelLevelsetEpsilon)
        Handler.set_label_levelset_sigma(self.ui.labelLevelsetSigma)
        Handler.set_slider_levelset_iteration(self.ui.sliderLevelsetIteration)
        Handler.set_slider_levelset_alpha(self.ui.sliderLevelsetAlpha)
        Handler.set_slider_levelset_lambda(self.ui.sliderLevelsetLambda)
        Handler.set_slider_levelset_sigma(self.ui.sliderLevelsetSigma)
        Handler.set_slider_levelset_epsilon(self.ui.sliderLevelsetEpsilon)
        Handler.set_button_levelset_ok(self.ui.buttonLevelsetOk)
        Handler.set_hander_end_levelset()

        # LABEL TAB系
        self.group = QButtonGroup()
        self.group.addButton(self.ui.radioButton1,1)
        self.group.addButton(self.ui.radioButton2,2)
        self.group.addButton(self.ui.radioButton3,3)
        self.group.addButton(self.ui.radioButton4,4)
        self.group.addButton(self.ui.radioButton5,5)
        Handler.set_radio_buttons_writting([
            self.ui.radioButton1,
            self.ui.radioButton2,
            self.ui.radioButton3,
            self.ui.radioButton4,
            self.ui.radioButton5,
            ])
        Handler.set_text_edit_comments_writting(self.ui.textEditCommentsWritting)
        Handler.set_combo_box_nodule_id_writting(self.ui.comboBoxNoduleIdWritting)
        Handler.set_button_ok_writting(self.ui.buttonOkWritting)
        Handler.set_table_widget_writting(self.ui.tableWidgetWritting)
        Handler.set_button_delete_writting(self.ui.buttonDeleteWritting)
        Handler.set_widget_writting(self.ui.widgetWritting)
        ViewHander.initialize()
        print("== Handler set complete! ==")

        cv2.destroyAllWindows()

        Handler.set_hello_dialog(HelloDialog(self))
        Handler.set_message_dialog(MessageDialog(self))

        Handler.initialize()
        MyForm.__is_finish_init = True


    def resizeEvent(self, evt):
        if(MyForm.__is_finish_init):
            ViewHander.resize_window()
            Handler.resize_window()


class HelloDialog(QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_HelloDialog()
        self.ui.setupUi(self)

        Handler.set_combo_box_user_hello(self.ui.comboBoxUserHello)
        Handler.set_button_start_hello(self.ui.buttonStartHello)



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
