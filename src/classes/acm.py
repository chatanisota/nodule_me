import numpy as np
from skimage.segmentation import active_contour
import cv2
from level_set_method.find_lsf import find_lsf
from level_set_method.potential_func import DOUBLE_WELL, SINGLE_WELL
from skimage import measure

class ACM:

    def snake(img, start_pos, end_pos):
        v_num = 10
        start_x = min(start_pos[1], end_pos[1])
        end_x = max(start_pos[1], end_pos[1])
        start_y = min(start_pos[0], end_pos[0])
        end_y = max(start_pos[0], end_pos[0])
        height = end_y - start_y
        width = end_x - start_x
        a_axis = width/2
        b_axis = height/2
        center_x = start_x + width/2
        center_y = start_y + height/2

        # 画像を領域内で切り取る
        cut_img = img[start_x:(start_x+width), start_y:(start_y+height)]

        s = np.linspace(0, 2*np.pi, v_num)
        r = width/2 + a_axis * np.sin(s)
        c = height/2 + b_axis * np.cos(s)
        init = np.array([r, c]).T
        #

        cut_img = cv2.GaussianBlur(cut_img,(5,5),0)
        _, cut_img = cv2.threshold(cut_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        #0.1 b:0.01 c:1.0
        counters = active_contour(cut_img, init, alpha=0.1, beta=0.01, gamma=1.0, max_iterations=100)
        counters[:,1] += start_x + 1
        counters[:,0] += start_y + 1

        return counters


    # img: 現在のスライス１枚の画像
    # start_pos: 選択した赤いエリアの左上の座標
    # end_pos: 選択した赤いエリアの右下の座標
    def level_set(img, start_pos, end_pos):
        start_x = min(start_pos[1], end_pos[1])
        end_x = max(start_pos[1], end_pos[1])
        start_y = min(start_pos[0], end_pos[0])
        end_y = max(start_pos[0], end_pos[0])
        height = end_y - start_y
        width = end_x - start_x
        a_axis = width/2
        b_axis = height/2
        center_x = start_x + width/2
        center_y = start_y + height/2
        #
        # ここにLevel set methodを実装してね
        params = ACM.parameters(img, start_x, end_x, start_y, end_y)
        phi = find_lsf(**params)
        #
        print(phi)
        counters = measure.find_contours(phi, 0)
        print(counters[0])

        counters_int = []

        for counter in counters[0]:
            counters_int.append([int(counter[0]),int(counter[1])])
        # 肺結節を囲んだ領域
#        counters = [[100,100],[130,100],[150,70],[170,100],[200,100],
#            [180,120],[190,150],[150,130],[110,150],[120,120],[135,125]]


        return counters_int

    def parameters(img, start_x, end_x, start_y, end_y):
#        img = imread('', True)  # insert file name
        img = np.interp(img, [np.min(img), np.max(img)], [0, 255])

        # initialize LSF as binary step function
        c0 = 2
        initial_lsf = c0 * np.ones(img.shape)
        # generate the initial region R0 as two rectangles
        initial_lsf[start_y:end_y, start_x:end_x] = -c0

        # parameters
        return {
            'img': img,
            'initial_lsf': initial_lsf,
            'timestep': 5,  # time step
            'iter_inner': 5,
            'iter_outer': 60,
            'lmda': 1.5,  # coefficient of the weighted length term L(phi)
            'alfa': 1.5,  # coefficient of the weighted area term A(phi)
            'epsilon': 1.5,  # parameter that specifies the width of the DiracDelta function
            'sigma': 2,  # scale parameter in Gaussian kernel
            'potential_function': DOUBLE_WELL,
        }
