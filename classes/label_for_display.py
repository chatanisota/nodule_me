import numpy as np
from classes.color import Color
from classes.user import User
from copy import deepcopy

class LabelForDisplay:

    __label = None
    __is_writting = False
    __line_color = Color.red()
    __is_close = True           # ラベルの開口可否
    __highlight_index = -1
    __points = []
    __calculated_points = []


    def set_label(self, label):
        self.__label = label

    def get_label(self):
        return self.__label

    def get_nodule_id(self):
        return self.__label.get_nodule_id()

    def set_points(self, points):
        self.__points = deepcopy(points)

    def set_calculated_points(self, calculated_points):
        self.__calculated_points = calculated_points

    def get_calculated_points(self):
        return self.__calculated_points

    def add_cursor_point(self, cursor_point):
        self.__points = np.append(self.__points, [[cursor_point[0], cursor_point[1]]], axis=0)

    def get_points(self):
        return self.__points

    def set_line_color(self, line_color):
        self.__line_color = line_color

    def get_line_color(self):
        return self.__line_color

    def set_highlight_index(self, highlight_index):
        self.__highlight_index = highlight_index

    def get_highlight_index(self):
        return self.__highlight_index

    def set_open(self):
        self.__is_close = False

    def get_is_close(self):
        return self.__is_close

    def set_writting(self):
        self.__is_writting = True

    def get_is_writting(self):
        return self.__is_writting
