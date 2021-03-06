import cv2
from classes.snake import Snake
from classes.acm import ACM

class ACMModel:

    __start_point = None
    __end_point = None

    def set_start_point(pos):
        ACMModel.__start_point = pos

    def set_end_point(pos):
        ACMModel.__end_point = pos

    def get_start_point():
        return ACMModel.__start_point

    def get_end_point():
        return ACMModel.__end_point

    def reset_start_point():
        ACMModel.__start_point = None

    def reset_end_point():
        ACMModel.__end_point = None

    def is_selecting():
        return (not ACMModel.__start_point == None)

    def draw_area(img, start_point, end_point):
        cv2.rectangle(img, start_point, end_point, (255, 0, 0), thickness=1)
        return img

    def acm_snake(img_array):
        points = Snake.snake(img_array, ACMModel.__start_point, ACMModel.__end_point, num_v=50, iteration=500)
        points = ACMModel.__round_points(points)
        return points

    def acm_acm(img_array):
        if(not ACMModel.__start_point[0] == ACMModel.__end_point[0]):
            if(not ACMModel.__start_point[1] == ACMModel.__end_point[1]):
                print("oooooooooooooooo")
                points = ACM.acm(img_array, ACMModel.__start_point, ACMModel.__end_point)
                points = ACMModel.__round_points(points)
                return points
        return []

    def __round_points(points):
        prev_point = [-1,-1]
        return_point = []
        for point in points:
            point = [int(point[0]),int(point[1])]
            if(prev_point[0]==point[0] and prev_point[1]==point[1]):
                continue
            return_point.append(point)
            prev_point = point
        return return_point
