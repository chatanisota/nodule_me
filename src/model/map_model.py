import cv2
import numpy as np

class MapModel:

    __start_pos_x = 0
    __start_pos_y = 0
    __drag_start_point = (0,0)

    __zoom_scale = 1.0
    __MAX_ZOOM_SCALE = 64.0
    __MIN_ZOOM_SCALE = 0.5

    @staticmethod
    def display_window(img_array, canvas_size, zoom_size):

        sx, ex, sy, ey, _ = MapModel.__area(canvas_size, img_array.shape)
        img_array = cv2.rectangle(img_array, (sx, sy), (ex, ey), (255,0,0), 2)
        img_array = cv2.resize(img_array, dsize=zoom_size)

        return img_array

    @staticmethod
    def zoom_cut(img_array, canvas_size):
        sx, ex, sy, ey, dsize = MapModel.__area(canvas_size, img_array.shape)
        img_array = img_array[sy: ey, sx: ex ].copy()
        img_array = cv2.resize(img_array, dsize=dsize, interpolation=cv2.INTER_LINEAR)   #バイリニア補間（ふつう）
        return img_array

    @staticmethod
    def __area(canvas_size, image_size):

        dsize = list(canvas_size)
        sx = MapModel.__start_pos_x
        ex = MapModel.__start_pos_x + int(canvas_size[0] / MapModel.__zoom_scale)
        sy = MapModel.__start_pos_y
        ey = MapModel.__start_pos_y + int(canvas_size[1] / MapModel.__zoom_scale)

        if(ey >= image_size[0]):
            ey = image_size[0]
            if(sy <= 0):
                dsize[1] = int(image_size[0] * MapModel.__zoom_scale)
        if(ex >= image_size[1]):
            ex = image_size[1]
            if(sx <= 0):
                dsize[0] = int(image_size[1] * MapModel.__zoom_scale)

        return sx, ex, sy, ey, tuple(dsize)


    @staticmethod
    def change_window(canvas_size, image_size):
        sx = MapModel.__start_pos_x
        ex = MapModel.__start_pos_x + int(canvas_size[0] / MapModel.__zoom_scale)
        sy = MapModel.__start_pos_y
        ey = MapModel.__start_pos_y + int(canvas_size[1] / MapModel.__zoom_scale)

        #windowを広げたとき、zoomエリア終端が画像からはみ出そうなら、始点を移動させる
        if(ex >= image_size[1]):
            if(sx > 0):
                new_ex = image_size[1] - 1
                new_sx = sx - (ex - image_size[1]) #はみ出た分引く
                MapModel.__start_pos_x = max(0, new_sx)

        if(ey >= image_size[0]):
            if(sy > 0):
                new_ey = image_size[0] - 1
                new_sy = sy - (ey - image_size[0]) #はみ出た分引く
                MapModel.__start_pos_y = max(0, new_sy)

    @staticmethod
    def map_pos_to_image_pos(point_pos, image_size, zoom_size):
        #クリックされた場所 / マップの大きさ (この時点で、0-1:画像全体の何パーセント時点か) * キャンバスの大きさ
        target_pos_x = int(round(point_pos[0] * image_size[1] / zoom_size[0]))
        target_pos_y = int(round(point_pos[1] * image_size[0] / zoom_size[1]))
        return (target_pos_x, target_pos_y)

    @staticmethod
    def image_pos_to_map_pos(point_pos, image_size, zoom_size):
        target_pos_x = int(round(point_pos[0] * zoom_size[0] / image_size[1]))
        target_pos_y = int(round(point_pos[1] * zoom_size[1] / image_size[0]))
        return (target_pos_x, target_pos_y)

    @staticmethod
    def click_pos_to_image_pos(point_pos):
        #クリックされた場所 / マップの大きさ (この時点で、0-1:画像全体の何パーセント時点か) * キャンバスの大きさ
        target_pos_x = MapModel.__start_pos_x + int(round(point_pos[0] / MapModel.__zoom_scale))
        target_pos_y = MapModel.__start_pos_y + int(round(point_pos[1] / MapModel.__zoom_scale))
        return (target_pos_x, target_pos_y)

    @staticmethod
    def image_pos_to_canvas_pos(point_pos):
        target_pos_x = int(round((point_pos[0] - MapModel.__start_pos_x) * MapModel.__zoom_scale))
        target_pos_y = int(round((point_pos[1] - MapModel.__start_pos_y) * MapModel.__zoom_scale))
        return (target_pos_x, target_pos_y)

    @staticmethod
    def drag_start(point_pos):
        MapModel.__drag_start_point = (point_pos[0] - MapModel.__start_pos_x, point_pos[1] - MapModel.__start_pos_y)

    @staticmethod
    def drag_area(point_pos, canvas_size, image_size):
        sx = point_pos[0] - MapModel.__drag_start_point[0]
        ex = sx + int(canvas_size[0] / MapModel.__zoom_scale )
        sy = point_pos[1] - MapModel.__drag_start_point[1]
        ey = sy + int(canvas_size[1] / MapModel.__zoom_scale )
        width = ex - sx
        height = ey - sy

        if(ey >= image_size[0]):
            ey = image_size[0] - 1
            sy = ey - height
            if(sy >= 0):
                MapModel.__start_pos_y = sy
        elif(sy < 0):
            sy = 0
            ey = sy + height
            if(ey <= image_size[0]):
                MapModel.__start_pos_y = sy
        else:
            MapModel.__start_pos_y = sy

        if(ex >= image_size[1]):
            ex = image_size[1] - 1
            sx = ex - width
            if(sx >= 0):
                MapModel.__start_pos_x = sx
        elif(sx < 0):
            sx = 0
            ex = sx + width
            if(ex <= image_size[1]):
                MapModel.__start_pos_x = sx
        else:
            MapModel.__start_pos_x = sx

    @staticmethod
    def move_area(point_pos, canvas_size, image_size):
        sx = point_pos[0] - int(canvas_size[0] / MapModel.__zoom_scale / 2)
        ex = point_pos[0] + int(canvas_size[0] / MapModel.__zoom_scale / 2)
        sy = point_pos[1] - int(canvas_size[1] / MapModel.__zoom_scale / 2)
        ey = point_pos[1] + int(canvas_size[1] / MapModel.__zoom_scale / 2)
        width = ex - sx
        height = ey - sy

        if(ey >= image_size[0]):
            ey = image_size[0] - 1
            sy = ey - height
            if(sy >= 0):
                MapModel.__start_pos_y = sy
        elif(sy < 0):
            sy = 0
            ey = sy + height
            if(ey <= image_size[0]):
                MapModel.__start_pos_y = sy
        else:
            MapModel.__start_pos_y = sy

        if(ex >= image_size[1]):
            ex = image_size[1] - 1
            sx = ex - width
            if(sx >= 0):
                MapModel.__start_pos_x = sx
        elif(sx < 0):
            sx = 0
            ex = sx + width
            if(ex <= image_size[1]):
                MapModel.__start_pos_x = sx
        else:
            MapModel.__start_pos_x = sx

    @staticmethod
    def zoom_up(rate, canvas_size, image_size):
        if(MapModel.__zoom_scale <= MapModel.__MAX_ZOOM_SCALE):
            MapModel.change_zoom_scale(canvas_size, image_size, MapModel.__zoom_scale * rate)
        else:
            MapModel.change_zoom_scale(canvas_size, image_size, MapModel.__MAX_ZOOM_SCALE)

    @staticmethod
    def zoom_down(rate, canvas_size, image_size):
        if(MapModel.__zoom_scale >= MapModel.__MIN_ZOOM_SCALE):
            MapModel.change_zoom_scale(canvas_size, image_size, MapModel.__zoom_scale / rate)
        else:
            MapModel.change_zoom_scale(canvas_size, image_size, MapModel.__MIN_ZOOM_SCALE)

    @staticmethod
    def zoom_default(canvas_size, image_size):
        MapModel.change_zoom_scale(canvas_size, image_size, 1.0)

    @staticmethod
    def change_zoom_scale(canvas_size, image_size, value):
        center_x = MapModel.__start_pos_x + int(canvas_size[0] / MapModel.__zoom_scale / 2)
        center_y = MapModel.__start_pos_y + int(canvas_size[1] / MapModel.__zoom_scale / 2)

        MapModel.__zoom_scale = value

        sx = center_x - int(canvas_size[0] / MapModel.__zoom_scale / 2)
        ex = center_x + int(canvas_size[0] / MapModel.__zoom_scale / 2)
        sy = center_y - int(canvas_size[1] / MapModel.__zoom_scale / 2)
        ey = center_y + int(canvas_size[1] / MapModel.__zoom_scale / 2)

        MapModel.__start_pos_x = sx
        MapModel.__start_pos_y = sy
        #windowを広げたとき、zoomエリア終端が画像からはみ出そうなら、始点を移動させる
        if(ex >= image_size[1]):
            if(sx > 0):
                new_sx = sx - (ex - image_size[1]) #はみ出た分引く
                MapModel.__start_pos_x = max(0, new_sx)
            else:
                MapModel.__start_pos_x = 0

        if(sx < 0):
                MapModel.__start_pos_x = 0

        if(ey >= image_size[0]):
            if(sy > 0):
                new_ey = image_size[0] - 1
                new_sy = sy - (ey - image_size[0]) #はみ出た分引く
                MapModel.__start_pos_y = max(0, new_sy)
            else:
                MapModel.__start_pos_y = 0

        if(sy < 0):
                MapModel.__start_pos_y = 0

    #ツールバー用
    @staticmethod
    def get_scroll_bar_max_x(canvas_size, image_size):
        ans = image_size[1] - int(canvas_size[0] / MapModel.__zoom_scale / 2)
        if(ans>0):
            return ans
        else:
            return 0

    @staticmethod
    def get_scroll_bar_max_y(canvas_size, image_size):
        ans = image_size[0] - int(canvas_size[1] / MapModel.__zoom_scale / 2)
        if(ans>0):
            return ans
        else:
            return 0

    @staticmethod
    def get_scroll_bar_min_x(canvas_size):
        return int(canvas_size[0] / MapModel.__zoom_scale / 2)

    @staticmethod
    def get_scroll_bar_min_y(canvas_size):
        return int(canvas_size[1] / MapModel.__zoom_scale / 2)


    @staticmethod
    def get_start_pos_x(canvas_size):
        return MapModel.__start_pos_x + int(canvas_size[0] / MapModel.__zoom_scale / 2)

    @staticmethod
    def get_start_pos_y(canvas_size):
        return MapModel.__start_pos_y + int(canvas_size[1] / MapModel.__zoom_scale / 2)

    @staticmethod
    def reset():
        MapModel.__start_pos_x = 0
        MapModel.__start_pos_y = 0
        MapModel.__zoom_scale = 1.0
