import numpy as np
import collections as cl
from classes.user import User

class Nodule:

    nodule_id = 0
    malignant_level = 0
    comments = ""
    user_id = 0
    WRITTING_ID = -1

    def regist(self, nodule_id, malignant_level, comments, user_id):
        self.nodule_id = nodule_id
        self.malignant_level = malignant_level
        self.comments = comments
        self.user_id = user_id

    def get_malignant_level(self):
        return self.malignant_level

    def get_nodule_id(self):
        return self.nodule_id

    def get_comments(self):
        return self.comments

    def get_user_id(self):
        return self.user_id

    def get_center_point(self):
        ave = np.average(self.points, axis = 0)
        return (int(ave[0]), int(ave[1]))

    @staticmethod
    def prefab_writting_nodule():
        nodule = Nodule()
        nodule.regist(Nodule.WRITTING_ID, 0, "[labeling]", User.WRITTING_ID)
        return nodule

    #書き込み用
    def get_json(self):
        json = cl.OrderedDict()
        json["nodule_id"] = self.nodule_id
        json["malignant_level"] = self.malignant_level
        json["comments"] = self.comments
        json["user_id"] = self.user_id
        return json

    #読み込み用
    def set_json(self, json):
        self.nodule_id = int(json["nodule_id"])
        self.malignant_level = json["malignant_level"]
        self.comments = json["comments"]
        self.user_id = json["user_id"]
