import cv2
import numpy as np
from classes.label import Label
from classes.nodule import Nodule
from classes.tool import Tool
from classes.refpoint import Refpoint
from classes.color import Color
from classes.user import User
from classes.label_for_display import LabelForDisplay
from copy import copy



class LabelModel:

    __writting_label = None          # ラベル作成中のラベル
    __writting_labels = []         # 結節作成中のラベル群
    __labels = []
    __nodules = []
    __cursor_point = None       # カーソル（マウス）の場所を示す点
    __current_selected_table_label = None # ラベルテーブルで選択されているラベル
    __current_selected_table_writting = None # 書きかけ中のテーブルで選択されているラベル
    __approach_refpoint = None  # 最も接近しているラベルのポイント
    __dragging_refpoint = None  # ドラッグしているラベルのポイント
    __insert_refpoint = None    # 新たに挿入されるであろうポイントの一つ前のポイント
    __writting_label_color = Color.red()
    __is_solo = False           # solo/all
    __is_my = False             # my/everyone
    # キャッシュ
    __cashe_label_for_display = None
    __cashe_labels_refined_all_for_display = None
    __cashe_labels_refined_by_index_for_display = None

    @staticmethod
    def is_writting_label():
        return not LabelModel.__writting_label == None

    @staticmethod
    def is_writting_labels():
        return len(LabelModel.__writting_labels) > 0

    @staticmethod
    def get_writting_label():
        return LabelModel.__writting_label

    @staticmethod
    def get_writting_labels_num():
        return len(LabelModel.__writting_labels)

    @staticmethod
    def __do_contain_writting_labels(label):
        return label in LabelModel.__writting_labels

    @staticmethod
    def __do_contain_writting_label(label):
        return label is LabelModel.__writting_label

    @staticmethod
    def get_labels_all():
        labels = copy(LabelModel.__labels)
        if LabelModel.is_writting_labels():
            labels.extend(LabelModel.__writting_labels)
        if LabelModel.is_writting_label():
            labels.extend([LabelModel.__writting_label])
        return labels

    @staticmethod
    def get_labels_saved():
        return LabelModel.__labels

    @staticmethod
    def get_labels_writting():
        labels = copy(LabelModel.__writting_labels)
        if LabelModel.is_writting_label():
            labels.extend([LabelModel.__writting_label])
        return labels

    # ソロインデックス／オールインデックスで絞り込み
    @staticmethod
    def __refine_solo_labels(labels, current_index):
        if(LabelModel.is_solo()):
            # 現在のインデックスのみ
            temp_labels = []
            for label in labels:
                if(current_index == label.get_index()):
                    temp_labels.append(label)
            labels = temp_labels
        return labels

    # 自分／全員で絞り込み
    @staticmethod
    def __refine_my_labels(labels, current_user_id):
        if(LabelModel.is_my()):
            # 自分の書いたラベルのみ
            temp_labels = []
            for label in labels:
                nodule = LabelModel.get_nodule_by_label(label)
                if(current_user_id == nodule.get_user_id() or nodule.get_user_id() == User.WRITTING_ID):
                    temp_labels.append(label)
            labels = temp_labels
        return labels

    # ラベルテーブル一覧に表示する用
    @staticmethod
    def get_labels_refined_all_for_label_tables(current_index, current_user_id):
        labels = LabelModel.get_labels_saved()
        labels = LabelModel.__refine_solo_labels(labels, current_index)
        labels = LabelModel.__refine_my_labels(labels, current_user_id)
        return labels

    # ラベルテーブル一覧に表示する用
    @staticmethod
    def get_labels_all_for_writting():
        labels = LabelModel.get_labels_writting()
        return labels

    # 画面に描画する用
    @staticmethod
    def get_labels_refined_all_for_display(current_index, current_user_id):
        if(not LabelModel.__cashe_labels_refined_all_for_display == None):
            return LabelModel.__cashe_labels_refined_all_for_display
        labels = LabelModel.get_labels_all()
        labels = LabelModel.__refine_solo_labels(labels, current_index)
        labels = LabelModel.__refine_my_labels(labels, current_user_id)
        LabelModel.__cashe_labels_refined_all_for_display = labels
        return labels

    # 画面に描画する用
    @staticmethod
    def get_labels_refined_by_index_for_display(current_index, current_user_id):
        if(not LabelModel.__cashe_labels_refined_by_index_for_display == None):
            return LabelModel.__cashe_labels_refined_by_index_for_display
        labels = LabelModel.get_labels_by_index(current_index)
        labels = LabelModel.__refine_my_labels(labels, current_user_id)
        LabelModel.__cashe_labels_refined_by_index_for_display = labels
        return labels


    # 表示のみに一時的に利用するラベル
    @staticmethod
    def create_labels_for_display(labels, tool):
        if(not LabelModel.__cashe_label_for_display == None):
            return LabelModel.__cashe_label_for_display
        label_for_displays = []
        for label in labels:
            label_for_display = LabelForDisplay()
            label_for_display.set_label(label)
            if(tool == Tool.PINSET or tool == Tool.ERACER):
                label_for_display.set_highlight_index(LabelModel.__get_highlight_index(label))
            # TUBE インサート系
            if(tool == Tool.TUBE and LabelModel.__is_approach_label(label)):
                temp_label = LabelModel.__get_label_tempolary_inserted()
                if(not temp_label == None):
                    label_for_display.set_points(temp_label.get_points())
                else:
                    label_for_display.set_points(label.get_points())
            else:
                label_for_display.set_points(label.get_points())
            # ラベリング中
            if(LabelModel.__do_contain_writting_labels(label)):
                label_for_display.set_writting()
            elif(LabelModel.__do_contain_writting_label(label)):
                label_for_display.set_writting()
                label_for_display.set_open()
                if(tool == Tool.PEN):
                    # カーソルをポイントとして追加
                    label_for_display.add_cursor_point(LabelModel.get_cursor_point())
            label_for_displays.append(label_for_display)
            LabelModel.__cashe_label_for_display = label_for_displays
        return label_for_displays

    @staticmethod
    def get_labels_by_index(index):
        return_labels = []
        for label in LabelModel.get_labels_all():
            if(index == label.get_index()):
                return_labels.append(label)
        return return_labels

    # 画面に表示する用
    @staticmethod
    def get_labels_for_display_by_index(index, current_user_id):
        labels = LabelModel.get_labels_by_index(index)
        labels = LabelModel.__refine_my_labels(labels, current_user_id)
        return labels

    @staticmethod
    def get_label_by_id(id):
        for label in LabelModel.get_labels_all():
            if(id == label.get_label_id()):
                return label
        return None #エラー

    @staticmethod
    def get_nodules_all():
        return LabelModel.__nodules

    @staticmethod
    def get_nodule_id_list():
        nodule_id_list = []
        for nodule in LabelModel.__nodules:
            nodule_id_list.append(nodule.get_nodule_id())
        return nodule_id_list

    @staticmethod
    def get_nodule_by_id(id):
        for nodule in LabelModel.__nodules:
            if(id == nodule.get_nodule_id()):
                return nodule
        return None #エラー

    @staticmethod
    def get_nodule_by_label(label):
        if(LabelModel.__do_contain_writting_label(label) or LabelModel.__do_contain_writting_labels(label)):
            # 作成中のラベルである場合
            return Nodule.prefab_writting_nodule()
        return LabelModel.get_nodule_by_id(label.get_nodule_id())

    # ADD
    @staticmethod
    def add_point(index):
        if(LabelModel.__writting_label == None):
            LabelModel.__writting_label = Label()
            LabelModel.__writting_label.set_index(index)

        if(not LabelModel.__cursor_point == None):
            LabelModel.__writting_label.add(LabelModel.__cursor_point)

    @staticmethod
    def get_writting_label_color():
        return LabelModel.__writting_label_color

    @staticmethod
    def set_cursor_point(target_pos):
        LabelModel.__cursor_point = target_pos

    @staticmethod
    def get_cursor_point():
        cursor_point = LabelModel.__cursor_point
        if(cursor_point == None):
            return [0,0]
        return cursor_point

    @staticmethod
    def get_cursor_point_for_infolabel():
        if(not LabelModel.__cursor_point == None):
            return "( "+str(LabelModel.__cursor_point[0])+" , "+str(LabelModel.__cursor_point[1])+" ) "
        return None

    @staticmethod
    def set_current_selected_table_label(label):
        LabelModel.__current_selected_table_label = label

    @staticmethod
    def get_current_selected_table_label():
        return LabelModel.__current_selected_table_label

    @staticmethod
    def set_current_selected_table_writting(label):
        LabelModel.__current_selected_table_writting = label

    @staticmethod
    def get_current_selected_table_writting():
        return LabelModel.__current_selected_table_writting

    @staticmethod
    def reset_cursor_point():
        LabelModel.__cursor_point = None

    # ラベル一つ分を登録
    @staticmethod
    def regist_writting_label(label_id, index):
        LabelModel.__writting_label.regist(label_id, index)
        LabelModel.__writting_labels.append(LabelModel.__writting_label)
        LabelModel.__writting_label = None

    # ラベル一つ分を登録
    @staticmethod
    def regist_writting_label_by_acm(points, label_id, index):
        LabelModel.__writting_label = Label()
        LabelModel.__writting_label.set_points(np.array(points))
        LabelModel.__writting_label.set_index(index)
        LabelModel.__writting_label.regist(label_id, index)
        LabelModel.__writting_labels.append(LabelModel.__writting_label)
        LabelModel.__writting_label = None

    # 結節一つ分（複数ラベル）を登録、regist_writting_label()の後に行う
    @staticmethod
    def regist_writting_labels(nodule_id, malignant_level, comments, user_id):
        writting_labels = LabelModel.__writting_labels
        nodule = Nodule()
        nodule.regist(nodule_id, malignant_level, comments, user_id)
        LabelModel.__nodules.append(nodule)
        for writting_label in LabelModel.__writting_labels:
            writting_label.set_nodule_id(nodule_id)
            LabelModel.__labels.append(writting_label)
        LabelModel.__writting_labels = []

    @staticmethod
    def reset_writting_label():
        LabelModel.__writting_label = None

    @staticmethod
    def reset_writting_labels():
        LabelModel.__writting_labels = []

    @staticmethod
    def set_approach_refpoint(target_pos, index):
        labels_list = LabelModel.get_labels_by_index(index)
        if(len(labels_list) <= 0):
            return 0
        # 近い ラベル を探す
        LabelModel.__approach_refpoint = LabelModel.__get_neighbor_refpoint(target_pos, labels_list)

    @staticmethod
    def start_dragging_point():
        LabelModel.__dragging_refpoint = LabelModel.__approach_refpoint

    @staticmethod
    def move_dragging_point(target_pos, index):
        if( not LabelModel.__dragging_refpoint == None ):
            LabelModel.__dragging_refpoint.change_point(target_pos)

    @staticmethod
    def __get_neighbor_refpoint(target_pos, labels_list):
        # ラベル自体の検索
        ans_label = None
        ans_index = None
        temp_distance = 0.0
        distance = float('inf')

        for label in labels_list:
            points = label.get_points()
            for index, point in enumerate(points):
                temp_distance = np.linalg.norm((target_pos[0] - point[0], target_pos[1] - point[1]))
                if(temp_distance < distance):
                    distance = temp_distance
                    ans_label = label
                    ans_index = index

        return Refpoint(ans_label, ans_index)

    @staticmethod
    def __get_insert_refpoint(neighbor_refpoint):
        neighbor_point = LabelModel.__cursor_point

        # 次のポイントとの距離
        distance_next = float('inf')
        next_refpoint = neighbor_refpoint.get_next_refpoint()
        next_point = next_refpoint.get_point()
        next_distance = np.linalg.norm((neighbor_point[0] - next_point[0], neighbor_point[1] - next_point[1]))

        # 前のポイントとの距離
        distance_prev = float('inf')
        prev_refpoint = neighbor_refpoint.get_prev_refpoint()
        prev_point = prev_refpoint.get_point()
        prev_distance = np.linalg.norm((neighbor_point[0] - prev_point[0], neighbor_point[1] - prev_point[1]))

        if(prev_distance < next_distance):
            # 前 - 〇　- 後　とあったときに、前の方が近い場合、前を返す
            return neighbor_refpoint
        else:
            return next_refpoint

    @staticmethod
    def set_insert_refpoint():
        if(not LabelModel.__approach_refpoint == None):
            LabelModel.__insert_refpoint = LabelModel.__get_insert_refpoint(LabelModel.__approach_refpoint)

    @staticmethod
    def __get_label_tempolary_inserted():
        if(not LabelModel.__insert_refpoint == None and not LabelModel.__cursor_point == None and not LabelModel.__approach_refpoint == None ):
            return LabelModel.__insert_refpoint.get_label_tempolary_inserted(LabelModel.__cursor_point)
        return None

    @staticmethod
    def insert_point():
        if(not LabelModel.__insert_refpoint == None):
            LabelModel.__insert_refpoint.insert(LabelModel.__cursor_point)

    @staticmethod
    def delete_point():
        if(not LabelModel.__approach_refpoint == None):
            LabelModel.__approach_refpoint.delete()

    # 削除が必要なラベルがないかをチェック
    @staticmethod
    def check_and_delete_labels():
        for i in range(len(LabelModel.__labels)):
            if(LabelModel.__labels[i].get_point_size() <= 0):
                LabelModel.__labels.pop(i)

        if(len(LabelModel.__writting_labels)>0):
            for i in range(len(LabelModel.__writting_labels)):
                if(LabelModel.__writting_labels[i].get_point_size() <= 0):
                    LabelModel.__writting_labels.pop(i)
        LabelModel.refpoint_reset()

    @staticmethod
    def delete_current_selected_table_label():

        if(LabelModel.__current_selected_table_label == None):
            return None

        if(len(LabelModel.__labels)>0):
            temp_label = copy(LabelModel.__labels)
            for i in range(len(LabelModel.__labels)):
                if(LabelModel.__labels[i] is LabelModel.__current_selected_table_label):
                    temp_label.pop(i)
            LabelModel.__labels = temp_label

        LabelModel.refpoint_reset()

    @staticmethod
    def delete_current_selected_table_writting():

        if(LabelModel.__current_selected_table_writting == None):
            return None

        if(len(LabelModel.__writting_labels)>0):
            temp_label = copy(LabelModel.__writting_labels)
            for i in range(len(LabelModel.__writting_labels)):
                if(LabelModel.__writting_labels[i] is LabelModel.__current_selected_table_writting):
                    temp_label.pop(i)
            LabelModel.__writting_labels = temp_label

        if(LabelModel.__writting_label is LabelModel.__current_selected_table_writting):
            LabelModel.__writting_label = None
        LabelModel.refpoint_reset()


    # 切り替え
    @staticmethod
    def switch_solo_all():
        LabelModel.__is_solo = not LabelModel.__is_solo

    @staticmethod
    def switch_my_everyone():
        LabelModel.__is_my = not LabelModel.__is_my

    @staticmethod
    def is_solo():
        return LabelModel.__is_solo

    @staticmethod
    def is_my():
        return LabelModel.__is_my

    @staticmethod
    def __is_approach_label(label):
        return (not LabelModel.__approach_refpoint == None) and LabelModel.__approach_refpoint.is_same_label(label)

    @staticmethod
    def __get_highlight_index(label):
        if(LabelModel.__is_approach_label(label)):
            # 接近ラベルと同じラベルだったとき
            index = LabelModel.__approach_refpoint.get_index()
            return index
        return -1

    @staticmethod
    def draw_points(img, label_for_displays, tool):
        for label_for_display in label_for_displays:

            line_color = label_for_display.get_line_color()
            points = label_for_display.get_calculated_points()
            prev_point = []
            for i, point in enumerate(points):

                # 点の描写
                if(i == label_for_display.get_highlight_index()):
                    point_color = Color.red()
                else:
                    point_color = Color.aqua()

                if(tool == Tool.PEN):
                    cv2.circle(img, (int(point[0]), int(point[1])), 2, point_color.get_color(), -1)
                elif(tool == Tool.PINSET):
                    cv2.circle(img, (int(point[0]), int(point[1])), 5, point_color.get_color(), 2)
                elif(tool == Tool.ERACER):
                    cv2.circle(img, (int(point[0]), int(point[1])), 5, point_color.get_color(), 2)
                elif(tool == Tool.TUBE):
                    cv2.circle(img, (int(point[0]), int(point[1])), 2, point_color.get_color(), -1)

                # 線の描写
                if(len(prev_point) > 0):
                    cv2.line(img, (int(point[0]), int(point[1])), (int(prev_point[0]), int(prev_point[1])), line_color.get_color(), thickness=1, lineType=cv2.LINE_AA)
                prev_point = point

            if(label_for_display.get_is_close()):
                cv2.line(img, (int(points[0,0]), int(points[0,1])), (int(points[-1,0]), int(points[-1,1])), line_color.get_color(), thickness=1, lineType=cv2.LINE_AA)
        return img

    @staticmethod
    def draw_cursor(img, point):
        color = Color.red()
        cv2.circle(img, (int(point[0]), int(point[1])), 2, color.get_color(), -1)
        return img


    @staticmethod
    def generate_label_id():
        id = 1
        for label in reversed(LabelModel.get_labels_all()):
            if(id <= label.get_label_id()):
                id = label.get_label_id() + 1
        return id

    @staticmethod
    def generate_nodule_id():
        id = 1
        for label in reversed(LabelModel.__nodules):
            if(id <= label.get_nodule_id()):
                id = label.get_nodule_id() + 1
        return id

    #書き込み用
    def input_labels(labels):
        LabelModel.__labels = labels

    def input_nodules(nodules):
        LabelModel.__nodules = nodules

    # ポイントの削除系した後はこれをする
    def refpoint_reset():
        LabelModel.__approach_refpoint = None
        LabelModel.__dragging_refpoint = None
        LabelModel.__insert_refpoint = None

    def reset():
        LabelModel.__writting_label = None
        LabelModel.__labels = []
        LabelModel.__cursor_point = None
        LabelModel.__approach_refpoint = None
        LabelModel.__dragging_refpoint = None
        LabelModel.__insert_refpoint = None

    # キャッシュ
    def reset_cashe():
        LabelModel.__cashe_label_for_display = None
        LabelModel.__cashe_labels_refined_all_for_display = None
        LabelModel.__cashe_labels_refined_by_index_for_display = None
