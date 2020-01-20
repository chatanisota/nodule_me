from PyQt5.QtGui import QPixmap, QImage, QPalette
from model.image_model import ImageModel
from model.dicom_model import DicomModel
from model.histogram_model import HistogramModel
from model.map_model import MapModel
from model.view_model import ViewModel
from model.label_model import LabelModel
from model.tool_model import ToolModel
from model.user_model import UserModel
import numpy as np
from classes.tool import Tool
from classes.color import Color
from classes.nodule import Nodule
from classes.label_for_display import LabelForDisplay


class CanvasController:

    __label_image = None

    @staticmethod
    def set_label_image(label_image):
        CanvasController.__label_image = label_image
        # スケールは1.0
        CanvasController.__label_image.scaleFactor = 1.0

        image = QImage('image2.jpg')
        # ラベルに読み込んだ画像を反映
        CanvasController.__label_image.setPixmap(QPixmap.fromImage(image))

    @staticmethod
    def update_from_zoom():
        img_array = ImageModel.get_array_pixel_color()
        CanvasController.__zoom_filter(img_array)

    @staticmethod
    def update_from_maker():
        img_array = ImageModel.get_array_pixel_canvas_zoom()
        CanvasController.__maker_filter(img_array)

    @staticmethod
    def __zoom_filter(img_array):
        #ズーム系
        img_array = MapModel.zoom_cut(img_array, ViewModel.get_canvas_window_size())
        ImageModel.set_array_pixel_canvas_zoom(img_array)
        CanvasController.__maker_filter(img_array)

    @staticmethod
    def __maker_filter(img_array):
        # マーカ系
        #img_array = LabelModel.draw_points_canvas(img_array, MapModel.image_pos_to_canvas_pos, DicomModel.get_current_index(), ToolModel.get_tool())
        img_array = CanvasController.__draw_points_canvas(img_array)
        ImageModel.set_array_pixel_canvas_maker(img_array)
        CanvasController.__repaint(img_array)

    @staticmethod
    def __repaint(img):
        #画像生成
        qimg = QImage(img, img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_RGB888)
        CanvasController.__label_image.setPixmap(QPixmap.fromImage(qimg))

    # キャンバス用ラベル描写
    @staticmethod
    def __draw_points_canvasaa(img):

        # 現在追加中のラベルの描写
        if(LabelModel.is_writting_label()):
            writting_label = LabelModel.get_writting_label()
            points = writting_label.get_points()
            if(not LabelModel.get_cursor_point() == None and ToolModel.get_tool() == Tool.PEN):
                #現在点の描写

                if(len(points)>0):
                    points = np.vstack((points, LabelModel.get_cursor_point()))
                else:
                    points = [LabelModel.get_cursor_point()]
                #LabelModel.reset_cursor_point()
            if(len(points)>0):
                points = np.apply_along_axis(lambda xy: MapModel.image_pos_to_canvas_pos(xy), 1, points)
                img = LabelModel.draw_points_canvas(img, label_for_display, ToolModel.get_tool())

        # 既存のラベルの描写
        labels_list = LabelModel.get_labels_for_display_by_index(DicomModel.get_current_index(), UserModel.get_current_user_id())
        if(ToolModel.get_tool() == Tool.TUBE):
            label_tempolary_inserted, replaced_label = LabelModel.get_label_tempolary_inserted()
            if(not label_tempolary_inserted == None):
                labels_list.append(label_tempolary_inserted)


        for label in labels_list:
            if(ToolModel.get_tool() == Tool.TUBE and replaced_label is label):
                continue
            points = label.get_points()
            points = np.apply_along_axis(lambda xy: MapModel.image_pos_to_canvas_pos(xy), 1, points)
            highlight_index = LabelModel.get_highlight_index(label)

            if(LabelModel.do_containing_writting_labels(label)):
                # 追加中の結節の一部ラベル
                line_color = Color.red()
            else:
                nodule = LabelModel.get_nodule_by_label(label)
                line_color = UserModel.get_user_color_by_id(nodule.get_user_id())
            img = LabelModel.draw_points_canvas(img, points, ToolModel.get_tool(), True, line_color, highlight_index)

        return img

    @staticmethod
    def __draw_points_canvas(img):
        tool = ToolModel.get_tool()
        labels = LabelModel.get_labels_refined_by_index_for_display(DicomModel.get_current_index(), UserModel.get_current_user_id())
        label_for_displays = LabelModel.create_labels_for_display(labels,  tool)
        for label_for_display in label_for_displays:
            label_for_display.set_calculated_points(np.apply_along_axis(lambda xy: MapModel.image_pos_to_canvas_pos(xy), 1, label_for_display.get_points()))
            nodule = LabelModel.get_nodule_by_label(label_for_display.get_label())
            line_color = UserModel.get_user_color_by_id(nodule.get_user_id())
            if(line_color==None):
                line_color = Color.red()
            label_for_display.set_line_color(line_color)
        img = LabelModel.draw_points(img, label_for_displays, tool)
        # カーソル描写
        if(tool == Tool.PEN or tool == Tool.TUBE):
            cursor_point = LabelModel.get_cursor_point()
            calculated_cursor_point = MapModel.image_pos_to_canvas_pos(cursor_point)
            img = LabelModel.draw_cursor(img, calculated_cursor_point)

        return img
