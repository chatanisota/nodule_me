import numpy as np
import collections as cl
from classes.user import User

class Label:

    label_id = 0
    nodule_id = 0
    index = 0
    points = []
    is_delete = False

    def add(self, point):
        if(len(self.points)<=0):
            self.points = [[int(point[0]),int(point[1])]]
        else:
            self.points = np.append(self.points, [[int(point[0]),int(point[1])]], axis=0)

    def regist(self, label_id, index):
        self.label_id = label_id
        self.index = index

    def set_nodule_id(self, nodule_id):
        self.nodule_id = nodule_id

    def insert(self, point, index):
        self.points = np.insert(self.points, index, point, axis=0)

    def delete(self, index):
        self.points = np.delete(self.points, index, 0)

    def get_points(self):
        if(len(self.points) <= 0):
            return []
        else:
            return self.points

    def get_point_by_index(self, index):
        return self.points[index]

    def get_point_size(self):
        return len(self.points)

    def set_point_with_index(self, target_pos, index):
        self.points[index] = target_pos

    def set_index(self, index):
        self.index = index

    def get_index(self):
        return self.index

    def get_label_id(self):
        return self.label_id

    def get_nodule_id(self):
        return self.nodule_id

    def get_center_point(self):
        ave = np.average(self.points, axis = 0)
        return (int(ave[0]), int(ave[1]))

    #書き込み用
    def get_json(self):
        json = cl.OrderedDict()
        json["label_id"] = self.label_id
        json["nodule_id"] = self.nodule_id
        json["index"] = self.index
        json["points"] = self.get_points().tolist()
        return json

    #読み込み用
    def set_json(self, json):
        self.points = np.array(json["points"])
        self.label_id = int(json["label_id"])
        self.nodule_id = int(json["nodule_id"])
        self.index = json["index"]
        print("paaaan",self.label_id)
