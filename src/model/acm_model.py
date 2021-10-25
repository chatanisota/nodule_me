import cv2
from classes.snake import Snake
from classes.levelset import Levelset
from classes.levelset_parameters import LevelsetParameter

import asyncio
import json

class ACMModel:

    __start_point = None
    __end_point = None

    __current_levelset_parameters_key = [
        int((len(LevelsetParameter.Iterations)-1)/2),
        int((len(LevelsetParameter.Alphas)-1)/2),
        int((len(LevelsetParameter.Lambdas)-1)/2),
        int((len(LevelsetParameter.Epsilons)-1)/2),
        int((len(LevelsetParameter.Sigmas)-1)/2)
    ]

    __levelset_thread = None

    def initiarize_results():
        return [
            [
                [
                    [
                        [
                            [] for i in range(len(LevelsetParameter.Sigmas))
                        ] for j in range(len(LevelsetParameter.Epsilons))
                    ] for k in range(len(LevelsetParameter.Lambdas))
                ] for l in range(len(LevelsetParameter.Alphas))
            ] for m in range(len(LevelsetParameter.Iterations))
        ]

    __levelset_results = initiarize_results()



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
        if(not ACMModel.__start_point[0] == ACMModel.__end_point[0]):
            if(not ACMModel.__start_point[1] == ACMModel.__end_point[1]):
                points = ACM.snake(img_array, ACMModel.__start_point, ACMModel.__end_point)
                points = ACMModel.__round_points(points)
                return points
        return points

    def acm_levelset(img_array, callback):
        if(not ACMModel.__start_point[0] == ACMModel.__end_point[0]):
            if(not ACMModel.__start_point[1] == ACMModel.__end_point[1]):
                ACMModel.__levelset_thread = Levelset(img_array,ACMModel.__start_point,ACMModel.__end_point)
                ACMModel.__levelset_thread.thread.connect(ACMModel.__levelset_calculated)
                ACMModel.__levelset_thread.finished.connect(callback)

                if not ACMModel.__levelset_thread.isRunning():
                    ACMModel.__levelset_thread.restart()
                ACMModel.__levelset_thread.start()

    def cansel_levelset():
        if ACMModel.__levelset_thread != None and ACMModel.__levelset_thread.isRunning():
            ACMModel.__levelset_thread.stop()
            ACMModel.__levelset_thread = None

    def __levelset_calculated(json_str):
        data = json.loads(json_str)
        iteration = data['iteration']
        alpha = data['alpha']
        lambda_i = data['lambda']
        epsilon = data['epsilon']
        sigma = data['sigma']
        ACMModel.__levelset_results[iteration][alpha][lambda_i][epsilon][sigma] = data['result']



        #points = ACMModel.__round_points(points)


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

    def set_levelset_parameters(iteration, alpha, lambda_v, epsilon, sigma):
        ACMModel.__current_levelset_parameters_key[0] = iteration
        ACMModel.__current_levelset_parameters_key[1] = alpha
        ACMModel.__current_levelset_parameters_key[2] = lambda_v
        ACMModel.__current_levelset_parameters_key[3] = epsilon
        ACMModel.__current_levelset_parameters_key[4] = sigma

    def get_levelset_parameters_key():
        return ACMModel.__current_levelset_parameters_key

    def get_levelset_parameters_value():
        return [
            LevelsetParameter.Iterations[ACMModel.__current_levelset_parameters_key[0]],
            LevelsetParameter.Alphas[ACMModel.__current_levelset_parameters_key[1]],
            LevelsetParameter.Lambdas[ACMModel.__current_levelset_parameters_key[2]],
            LevelsetParameter.Epsilons[ACMModel.__current_levelset_parameters_key[3]],
            LevelsetParameter.Sigmas[ACMModel.__current_levelset_parameters_key[4]]
        ]

    def get_levelset_result():
        iteration   = ACMModel.__current_levelset_parameters_key[0]
        alpha       = ACMModel.__current_levelset_parameters_key[1]
        lambda_i    = ACMModel.__current_levelset_parameters_key[2]
        epsilon     = ACMModel.__current_levelset_parameters_key[3]
        sigma       = ACMModel.__current_levelset_parameters_key[4]
        print(str(iteration)+" "+str(alpha)+" "+str(lambda_i)+" "+str(epsilon)+" "+str(sigma))
        if(len(ACMModel.__levelset_results[iteration][alpha][lambda_i][epsilon][sigma]) > 0):
            return ACMModel.__levelset_results[iteration][alpha][lambda_i][epsilon][sigma]
        else:
            return []
