from model.map_model import MapModel
from model.label_model import LabelModel
from model.dicom_model import DicomModel
from model.view_model import ViewModel
from model.image_model import ImageModel
from model.user_model import UserModel
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QAbstractItemView
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from classes.label import Label



class LabelController:

    __label_dialog = None
    __text_edit_comments = None
    __radio_buttons = None
    __table_widget_labels = None
    # ラベル一覧
    __current_select_label_index = -1
    __button_switch_solo_all = None
    __button_switch_my_everyone = None
    __button_delete_label = None
    # ペン関連
    __pen_dialog = None
    __label_pen_dialog = None


    @staticmethod
    def set_label_dialog(ui):
        LabelController.__label_dialog = ui

    @staticmethod
    def set_text_edit_comments(ui):
        LabelController.__text_edit_comments = ui

    @staticmethod
    def set_radio_buttons(uis):
        LabelController.__radio_buttons = uis

    @staticmethod
    def set_combo_box_nodule_id(ui):
        LabelController.__combo_box_nodule_id = ui

    @staticmethod
    def set_button_switch_solo_all(ui):
        LabelController.__button_switch_solo_all = ui

    @staticmethod
    def set_button_switch_my_everyone(ui):
        LabelController.__button_switch_my_everyone = ui

    @staticmethod
    def set_button_delete_label(ui):
        LabelController.__button_delete_label = ui

    @staticmethod
    def set_table_widget_labels(ui):
        LabelController.__table_widget_labels = ui
        LabelController.__table_widget_labels.setEditTriggers(QAbstractItemView.NoEditTriggers)
        LabelController.__table_widget_labels.setSelectionBehavior(QAbstractItemView.SelectRows)
        LabelController.__table_widget_labels.setSelectionMode(QAbstractItemView.SingleSelection)
        header = LabelController.__table_widget_labels.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.Stretch)

    @staticmethod
    def set_pen_dialog(ui):
        LabelController.__pen_dialog = ui
        LabelController.__pen_dialog.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint)

    @staticmethod
    def set_label_pen_dialog(ui):
        LabelController.__label_pen_dialog = ui

    # --------------------------------------------------------------

    @staticmethod
    def pen_add(x, y):
        temp_pos = MapModel.click_pos_to_image_pos((x, y))
        LabelModel.set_cursor_point(temp_pos)
        LabelModel.add_point(DicomModel.get_current_index())

    @staticmethod
    def pen_move(x, y):
        temp_pos = MapModel.click_pos_to_image_pos((x, y))
        LabelModel.set_cursor_point(temp_pos)

    @staticmethod
    def pen_end():
        LabelModel.regist_writting_label(LabelModel.generate_label_id(), DicomModel.get_current_index())

    @staticmethod
    def regist_writting_labels():
        LabelModel.regist_writting_labels()

    @staticmethod
    def pinset_press(x, y):
        temp_pos = MapModel.click_pos_to_image_pos((x, y))
        LabelModel.set_approach_refpoint(temp_pos, DicomModel.get_current_index())
        LabelModel.start_dragging_point()

    @staticmethod
    def pinset_move(x, y):
        temp_pos = MapModel.click_pos_to_image_pos((x, y))
        LabelModel.set_cursor_point(temp_pos)
        LabelModel.set_approach_refpoint(temp_pos, DicomModel.get_current_index())

    @staticmethod
    def pinset_drag(x, y):
        target_pos = MapModel.click_pos_to_image_pos((x, y))
        LabelModel.move_dragging_point(target_pos, DicomModel.get_current_index())

    @staticmethod
    def eracer_move(x, y):
        temp_pos = MapModel.click_pos_to_image_pos((x, y))
        LabelModel.set_cursor_point(temp_pos)
        LabelModel.set_approach_refpoint(temp_pos, DicomModel.get_current_index())


    @staticmethod
    def eracer_release(x, y):
        temp_pos = MapModel.click_pos_to_image_pos((x, y))
        LabelModel.set_approach_refpoint(temp_pos, DicomModel.get_current_index())
        LabelModel.delete_point()
        LabelModel.check_and_delete_labels()
        LabelModel.set_approach_refpoint(temp_pos, DicomModel.get_current_index())

    @staticmethod
    def tube_add(x, y):
        LabelModel.insert_point()

    @staticmethod
    def tube_move(x, y):
        temp_pos = MapModel.click_pos_to_image_pos((x, y))
        LabelModel.set_approach_refpoint(temp_pos, DicomModel.get_current_index())
        LabelModel.set_cursor_point(temp_pos)
        LabelModel.set_insert_refpoint()

    @staticmethod
    def is_writting_label():
        return LabelModel.is_writting_label()

    @staticmethod
    def is_writting_labels():
        return LabelModel.is_writting_labels()



    @staticmethod
    def open_label_dialog():
        LabelController.__combo_box_nodule_id.clear()
        LabelController.__combo_box_nodule_id.addItem("New nodule")
        LabelController.__combo_box_nodule_id.addItems(["add label into nodule id :" + str(s) for s in LabelModel.get_nodule_id_list()])
        LabelController.__show_label_dialog()

    @staticmethod
    def label_dialog_ok():
        LabelModel.regist_writting_labels(LabelController.__get_nodule_id(), LabelController.__get_malignant_level(), LabelController.__get_comments(), UserModel.get_current_user_id())
        LabelController.__label_dialog.accept() #ダイアログを閉じる
        LabelController.update_table_widget_labels()

    @staticmethod
    def label_dialog_cancel():
        LabelController.__close_label_dialog()

    @staticmethod
    def pen_add_cancel():
        LabelModel.reset_writting_label()

    @staticmethod
    def pen_regist_cancel():
        LabelModel.reset_writting_labels()

    @staticmethod
    def update_pen_dialog():
        if(LabelModel.is_writting_labels() or LabelModel.is_writting_label()):
            LabelController.__show_pen_dialog()
            LabelController.__update_label_pen_dialog()
        else:
            LabelController.__close_pen_dialog()

    @staticmethod
    def __update_label_pen_dialog():
        labeling_num = LabelModel.get_writting_labels_num()
        if(labeling_num <= 0):
            text = "first"
        else:
            text = str(labeling_num)
        LabelController.__label_pen_dialog.setText(text)

    @staticmethod
    def __show_label_dialog():
        if(not LabelController.__label_dialog.isVisible()):
            LabelController.__label_dialog.show()

    @staticmethod
    def __close_label_dialog():
        if(LabelController.__label_dialog.isVisible()):
            LabelController.__label_dialog.accept()

    @staticmethod
    def __show_pen_dialog():
        if(not LabelController.__pen_dialog.isVisible()):
            LabelController.__pen_dialog.move(0,0)
            LabelController.__pen_dialog.show()

    @staticmethod
    def __close_pen_dialog():
        if(LabelController.__pen_dialog.isVisible()):
            LabelController.__pen_dialog.accept()

    @staticmethod
    def switch_solo_all():
        LabelModel.switch_solo_all()

    @staticmethod
    def switch_my_everyone():
        LabelModel.switch_my_everyone()


    #テーブルの選択行が移動したとき
    @staticmethod
    def move_to_current_label():
        label = LabelModel.get_current_selected_label()
        if(not label == None):
            DicomModel.set_current_index(label.get_index())
            MapModel.move_area(
                label.get_center_point(),
                ViewModel.get_canvas_window_size(),
                ImageModel.get_array_pixel_color().shape
            )

    # Deleteボタンを押したとき
    @staticmethod
    def delete_current_select_label():
        LabelModel.delete_current_select_label()
        LabelModel.set_current_selected_label(None)

    @staticmethod
    def __get_malignant_level():
        malignant_level = 0
        for i, radio in enumerate(LabelController.__radio_buttons):
            if radio.isChecked() == True:
                malignant_level = i + 1
        return malignant_level

    @staticmethod
    def __get_comments():
        return LabelController.__text_edit_comments.toPlainText()

    @staticmethod
    def __get_nodule_id():
        # nodule_idをコンボボックスより返す
        index = LabelController.__combo_box_nodule_id.currentIndex()
        if(index == 0):
            return LabelModel.generate_nodule_id()
        else:
            nodule_list = LabelModel.get_nodule_id_list()
            return nodule_list[index-1]


    @staticmethod
    def update_table_widget_labels():
        # テーブル全体
        labels = LabelModel.get_labels_refined_all(DicomModel.get_current_index(), UserModel.get_current_user_id())
        LabelController.__table_widget_labels.blockSignals(True)
        if(len(labels)>0):

            LabelController.__table_widget_labels.setRowCount(len(labels))

            for r, label in enumerate(labels):
                nodule = LabelModel.get_nodule_by_label(label)
                user = UserModel.get_user_by_id(nodule.get_user_id())
                malignant_level = str(nodule.get_malignant_level())
                comments = nodule.get_comments()
                LabelController.__table_widget_labels.setItem(r, 0, QTableWidgetItem(str(label.get_nodule_id())))
                LabelController.__table_widget_labels.setItem(r, 1, QTableWidgetItem(str(label.get_index())))
                LabelController.__table_widget_labels.setItem(r, 2, QTableWidgetItem(malignant_level))
                LabelController.__table_widget_labels.setItem(r, 3, QTableWidgetItem(user.get_name()))
                LabelController.__table_widget_labels.setItem(r, 4, QTableWidgetItem(comments))
        else:
            LabelController.__table_widget_labels.setRowCount(0)

        if(LabelModel.is_solo()):
            LabelController.__button_switch_solo_all.setIcon(QIcon("./ui/solo.png"))
        else:
            LabelController.__button_switch_solo_all.setIcon(QIcon("./ui/all.png"))

        if(LabelModel.is_my()):
            LabelController.__button_switch_my_everyone.setIcon(QIcon("./ui/my.png"))
        else:
            LabelController.__button_switch_my_everyone.setIcon(QIcon("./ui/everyone.png"))

        # 選択部分
        current_items = LabelController.__table_widget_labels.selectedItems()
        if(len(current_items)>0):
            #ラベルが選択されている
            row = current_items[0].row()
            # id = int(LabelController.__table_widget_labels.item(row, 0).text()) #id取得
            labels = LabelModel.get_labels_refined_all(DicomModel.get_current_index(), UserModel.get_current_user_id())
            label = labels[row]
            LabelModel.set_current_selected_label(label)
        else:
            #何も選択されていない
            LabelModel.set_current_selected_label(None)

        if(LabelModel.get_current_selected_label() == None):
            LabelController.__button_delete_label.setVisible(False)
        else:
            LabelController.__button_delete_label.setVisible(True)
        LabelController.__table_widget_labels.blockSignals(False)
