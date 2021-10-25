import numpy as np
import cv2
from library.level_set_method.find_lsf import FinfLSF
from library.level_set_method.potential_func import DOUBLE_WELL, SINGLE_WELL
from skimage import measure
from PyQt5 import QtCore
from classes.levelset_parameters import LevelsetParameter
import time
import json
# https://fereria.github.io/reincarnation_tech/11_PySide/02_Tips/06_qthread_01/
# スレッドの記事

class Levelset(QtCore.QThread):

    thread = QtCore.pyqtSignal(str)

    __img_array = []
    __start_point = []
    __end_point = []

    def __init__(self, img_array, start_pos, end_pos, parent=None):

        self.__img_array = img_array
        self.__start_point = start_pos
        self.__end_point = end_pos

        QtCore.QThread.__init__(self, parent)

        self.mutex = QtCore.QMutex()
        self.stopped = False

    def __del__(self):
        # Threadオブジェクトが削除されたときにThreadを停止する(念のため)
        self.stop()
        self.wait()

    def stop(self):
        with QtCore.QMutexLocker(self.mutex):
            self.stopped = True

    def restart(self):
        with QtCore.QMutexLocker(self.mutex):
            self.stopped = False

    def run(self):
        for alpha_i, alpha in enumerate(LevelsetParameter.Alphas):
            for lambda_i, lambda_v in enumerate(LevelsetParameter.Lambdas):
                for epsilon_i, epsilon in enumerate(LevelsetParameter.Epsilons):
                    for sigma_i, sigma in enumerate(LevelsetParameter.Sigmas):

                        params = Levelset.parameters(
                            self.__img_array,
                            self.__start_point,
                            self.__end_point,
                            alpha,
                            lambda_v,
                            epsilon,
                            sigma
                        )

                        lsf = FinfLSF()
                        lsf.setup(**params)

                        for iteration_i, iteration in enumerate(LevelsetParameter.Iterations):
                            if self.stopped:
                                break

                            while(lsf.calc() < iteration):
                                if self.stopped:
                                    break

                            phi = lsf.finish()

                            counters = measure.find_contours(phi, 0)

                            result = []
                            for counter in counters[0]:
                                result.append([int(counter[0]),int(counter[1])])

                            data = {
                                'iteration': iteration_i,
                                'alpha': alpha_i,
                                'lambda': lambda_i,
                                'epsilon': epsilon_i,
                                'sigma' : sigma_i,
                                'result' : result
                            }
                            self.thread.emit(json.dumps(data))


    # img: 現在のスライス１枚の画像
    # start_pos: 選択した赤いエリアの左上の座標
    # end_pos: 選択した赤いエリアの右下の座標
    @staticmethod
    def parameters(img, start_pos, end_pos, alpha, lambda_v, epsilon, sigma):
        start_x = min(start_pos[1], end_pos[1])
        end_x = max(start_pos[1], end_pos[1])
        start_y = min(start_pos[0], end_pos[0])
        end_y = max(start_pos[0], end_pos[0])
        height = end_y - start_y
        width = end_x - start_x
        center_x = start_x + width/2
        center_y = start_y + height/2

        # initialize LSF as binary step function
        c0 = 2
        initial_lsf = c0 * np.ones(img.shape)
        # generate the initial region R0 as two rectangles
        initial_lsf[start_y:end_y, start_x:end_x] = -c0

        # parameters
        params = {
            'img': img,
            'initial_lsf': initial_lsf,
            'timestep': 1,  # time step
            'iter_inner': 8,
            'lmda': lambda_v,  # coefficient of the weighted length term L(phi)
            'alfa': alpha,  # coefficient of the weighted area term A(phi)
            'epsilon': epsilon,  # parameter that specifies the width of the DiracDelta function
            'sigma': sigma,  # scale parameter in Gaussian kernel
            'potential_function': DOUBLE_WELL,
        }

        return params
