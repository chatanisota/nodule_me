from PyQt5.QtGui import QPixmap, QImage, QPalette
from model.image_model import ImageModel
from model.view_model import ViewModel
from model.map_model import MapModel
from model.label_model import LabelModel
from model.dicom_model import DicomModel
from model.tool_model import ToolModel
from model.user_model import UserModel
import numpy as np
import functools
from classes.color import Color
from classes.nodule import Nodule
from classes.tool import Tool
from classes.label_for_display import LabelForDisplay


class MapController():

    __label_map = None
    __scroll_bar_x = None
    __scroll_bar_y = None

    @staticmethod
    def set_label_map(label_map):
        MapController.__label_map = label_map

    @staticmethod
    def set_button_zoom_up(ui):
        pass

    @staticmethod
    def set_button_zoom_down(ui):
        pass

    @staticmethod
    def set_button_zoom_default(ui):
        pass

    @staticmethod
    def set_scroll_bar_x(ui):
        MapController.__scroll_bar_x = ui

    @staticmethod
    def set_scroll_bar_y(ui):
        MapController.__scroll_bar_y = ui

    @staticmethod
    def change_window():
        MapModel.change_window(ViewModel.get_canvas_window_size(), ImageModel.get_array_pixel_color().shape)

    @staticmethod
    def update_from_zoom():
        img_array = ImageModel.get_array_pixel_color()
        MapController.__zoom_filter(img_array)

    @staticmethod
    def update_from_maker():
        img_array = ImageModel.get_array_pixel_map_zoom()
        MapController.__maker_filter(img_array)

    @staticmethod
    def __zoom_filter(img_array):
        #ズーム系
        img_array = MapModel.display_window(img_array, ViewModel.get_canvas_window_size(), ViewModel.get_zoom_window_size())
        ImageModel.set_array_pixel_map_zoom(img_array)
        MapController.__maker_filter(img_array)

    @staticmethod
    def __maker_filter(img_array):
        #マーカ系
        img_array = MapController.draw_points_zoom(img_array)
        MapController.__repaint(img_array)

    @staticmethod
    def __repaint(img):
        #画像描写
        qimg = QImage(img, img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_RGB888)
        MapController.__label_map.setPixmap(QPixmap.fromImage(qimg))
        #スライドバー初期化
        MapController.__reset_slide_bar()

    @staticmethod
    def __reset_slide_bar():
        MapController.__scroll_bar_x.blockSignals(True)
        MapController.__scroll_bar_y.blockSignals(True)
        MapController.__scroll_bar_x.setMaximum(MapModel.get_scroll_bar_max_x(ViewModel.get_canvas_window_size(), ImageModel.get_array_pixel_color().shape))
        MapController.__scroll_bar_x.setMinimum(MapModel.get_scroll_bar_min_x(ViewModel.get_canvas_window_size()))
        MapController.__scroll_bar_y.setMaximum(MapModel.get_scroll_bar_max_y(ViewModel.get_canvas_window_size(), ImageModel.get_array_pixel_color().shape))
        MapController.__scroll_bar_y.setMinimum(MapModel.get_scroll_bar_min_y(ViewModel.get_canvas_window_size()))
        MapController.__scroll_bar_x.setValue(MapModel.get_start_pos_x(ViewModel.get_canvas_window_size()))
        MapController.__scroll_bar_y.setValue(MapModel.get_start_pos_y(ViewModel.get_canvas_window_size()))
        MapController.__scroll_bar_y.blockSignals(False)
        MapController.__scroll_bar_x.blockSignals(False)

    # マップがクリックされたときのその点を中心とする移動
    # 現在は使用されていない
    #@staticmethod
    #def press(x, y):
    #    MapModel.move_area(
    #        MapModel.map_pos_to_image_pos((x, y), ImageModel.get_array_pixel_color().shape, ViewModel.get_zoom_window_size()),
    #        ViewModel.get_canvas_window_size(),
    #        ImageModel.get_array_pixel_color().shape
    #    )

    @staticmethod
    def drag_start(x, y):
        MapModel.drag_start(
            MapModel.map_pos_to_image_pos((x, y), ImageModel.get_array_pixel_color().shape, ViewModel.get_zoom_window_size())
        )

    @staticmethod
    def drag(x, y):
        MapModel.drag_area(
            MapModel.map_pos_to_image_pos((x, y), ImageModel.get_array_pixel_color().shape, ViewModel.get_zoom_window_size()),
            ViewModel.get_canvas_window_size(),
            ImageModel.get_array_pixel_color().shape
        )

    @staticmethod
    def wheel(delta):
        if(delta>0):
            MapModel.zoom_up(1.05, ViewModel.get_canvas_window_size(), ImageModel.get_array_pixel_color().shape)
        else:
            MapModel.zoom_down(1.05, ViewModel.get_canvas_window_size(), ImageModel.get_array_pixel_color().shape)

    @staticmethod
    def zoom_up():
        MapModel.zoom_up(1.5, ViewModel.get_canvas_window_size(), ImageModel.get_array_pixel_color().shape)

    @staticmethod
    def zoom_down():
        MapModel.zoom_down(1.5, ViewModel.get_canvas_window_size(), ImageModel.get_array_pixel_color().shape)

    @staticmethod
    def zoom_default():
        MapModel.zoom_default(ViewModel.get_canvas_window_size(), ImageModel.get_array_pixel_color().shape)

    @staticmethod
    def change_scroll_bar():
        MapModel.move_area(
            (MapController.__scroll_bar_x.value(), MapController.__scroll_bar_y.value()),
            ViewModel.get_canvas_window_size(),
            ImageModel.get_array_pixel_color().shape
        )

    # マップ用ラベル描写
    @staticmethod
    def draw_points_zoomaa(img):

        # 現在追加中のラベルの描写
        if(LabelModel.is_writting_label()):
            writting_label = LabelModel.get_writting_label()
            points = writting_label.get_points()
            if(len(points)>0):
                points = np.apply_along_axis(lambda xy: MapModel.image_pos_to_map_pos(xy, ImageModel.get_array_pixel_color().shape, ViewModel.get_zoom_window_size()), 1, points)
                img = LabelModel.draw_points_map(img, points, ToolModel.get_tool(), False, LabelModel.get_writting_label_color())

        # 既存のラベルの描写
        labels_list = LabelModel.get_labels_by_index(DicomModel.get_current_index())
        for label in labels_list:
            points = label.get_points()
            points = np.apply_along_axis(lambda xy: MapModel.image_pos_to_map_pos(xy, ImageModel.get_array_pixel_color().shape, ViewModel.get_zoom_window_size()), 1, points)
            if(LabelModel.do_containing_writting_labels(label)):
                # 追加中の結節の一部ラベル
                line_color = Color.red()
            else:
                nodule = LabelModel.get_nodule_by_label(label)
                line_color = UserModel.get_user_color_by_id(nodule.get_user_id())
            img = LabelModel.draw_points(img, points, ToolModel.get_tool(), True, line_color)

        return img

    @staticmethod
    def draw_points_zoom(img):
        tool = ToolModel.get_tool()
        labels = LabelModel.get_labels_refined_by_index(DicomModel.get_current_index(), UserModel.get_current_user_id())
        label_for_displays = LabelModel.create_labels_for_display(labels, tool)
        for label_for_display in label_for_displays:
            label_for_display.set_calculated_points(np.apply_along_axis(lambda xy: MapModel.image_pos_to_map_pos(xy, ImageModel.get_array_pixel_color().shape, ViewModel.get_zoom_window_size()), 1, label_for_display.get_points()))
            nodule = LabelModel.get_nodule_by_label(label_for_display.get_label())
            line_color = UserModel.get_user_color_by_id(nodule.get_user_id())
            if(line_color==None):
                line_color = Color.red()
            label_for_display.set_line_color(line_color)
        img = LabelModel.draw_points(img, label_for_displays, Tool.PEN)
        # カーソル描写
        if(tool == Tool.PEN or tool == Tool.TUBE):
            cursor_point = LabelModel.get_cursor_point()
            calculated_cursor_point = MapModel.image_pos_to_map_pos(cursor_point, ImageModel.get_array_pixel_color().shape, ViewModel.get_zoom_window_size())
            img = LabelModel.draw_cursor(img, calculated_cursor_point)

        return img
