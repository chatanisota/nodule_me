
from classes.label import Label
import copy


#ラベルのポイントを参照するためのクラス
class Refpoint:

    __label = None
    __index = 0

    def __init__(self, label, index_of_point):
        self.__label = label
        self.__index = index_of_point

    def get_point(self):
        return self.__label.get_point_by_index(self.__index)

    def get_index(self):
        return self.__index

    def get_label(self):
        return self.__label

    def get_prev_refpoint(self):
        if(self.__index - 1 < 0):
            return Refpoint(self.__label, self.__label.get_point_size()-1)
        return Refpoint(self.__label, self.__index - 1)

    def get_next_refpoint(self):
        if(self.__index + 1 >= self.__label.get_point_size()):
            return Refpoint(self.__label, 0)
        return Refpoint(self.__label, self.__index + 1)

    def change_point(self, point):
        self.__label.set_point_with_index(point, self.__index)

    def insert(self, point):
        self.__label.insert(point, self.__index)

    def delete(self):
        self.__label.delete(self.__index)

    def is_same_label(self, label):
        return self.__label is label

    # 一時期的に、インサートされたラベルを返す
    def get_label_tempolary_inserted(self, point):
        temp_label = copy.deepcopy(self.__label)
        temp_label.insert(point, self.__index)
        return temp_label
