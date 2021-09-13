import numpy as np
from skimage.segmentation import active_contour
import cv2

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

        #
        # ここにLevel set methodを実装してね
        #

        # 肺結節を囲んだ領域
        counters = [[100,100],[130,100],[150,70],[170,100],[200,100],
            [180,120],[190,150],[150,130],[110,150],[120,120],[135,125]]

        return counters
