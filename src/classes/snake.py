#coding:utf-8

# https://qiita.com/kinketsucom/items/3d48f8705cde44d88eaf
import numpy as np
import cv2
import math
import copy
from tqdm import tqdm

class Snake:

    def snake(img, start_pos, end_pos, num_v=50, iteration=50):
        print("num_v:",num_v)
        print("iteration:",iteration)
        gray_test = img

        start_x = min(start_pos[0], end_pos[0])
        end_x = max(start_pos[0], end_pos[0])
        start_y = min(start_pos[1], end_pos[1])
        end_y = max(start_pos[1], end_pos[1])
        height = end_y - start_y
        width = end_x - start_x


        #N 頂点の数
        N = num_v

        #v 頂点　v[_,0]:x v[_,1]:y
        v = np.zeros((N,2))
        start_v = np.zeros((N,2))
        vec_g = np.zeros(2)
        #頂点のスタート位置
        for i in range(0,N):
        #    if(i<N/4):
        #        v[i] = [height/(N/4)*i,0]
        #    elif(i<2*N/4):
        #        v[i] = [height-1,width/(N/4)*(i-N/4)]
        #    elif(i<3*N/4):
        #        v[i] = [height-1-height/(N/4)*(i-2*N/4),width-1]
        #    else:
        #        v[i] = [0,width-1 - width/(N/4)*(i-3*N/4)]
            if(i<N/4):
                v[i] = [start_x + width * i * 4/N, start_y]
            elif(i<2*N/4):
                v[i] = [end_x, start_y + height * (4/N * i - 1)]
            elif(i<3*N/4):
                v[i] = [end_x - width * (4/N * i - 2), end_y]
            else:
                v[i] = [start_x, end_y - height * (4/N * i -3)]


        #初期輪郭点が円形の場合はこっち
        # for i in range(0,N):
        #     v[i] = [ height/2*math.sin(2*math.pi*i/N)+height/2, width/2*math.cos(2*math.pi*i/N)+width/2]
        #     start_v[i] = [ height/2*math.sin(2*math.pi*i/N)+height/2, width/2*math.cos(2*math.pi*i/N)+width/2]


        start_v = copy.deepcopy(v)

        #パラメータ
        alpha =1
        beta = 1
        gamma = 10
        kappa =1

        def EpsIn(vec0,vec1,vec2):#test
            value = 0
            value += alpha*np.linalg.norm(vec1-vec0)**2+beta*np.linalg.norm(vec2-2*vec1+vec0)**2
            value /= 2
        #     print("In:"+str(value))
            return value

        def EpsEx(vec0,pix):#gray
            value = 0
            x = int(vec0[0])
            y = int(vec0[1])

            if(x+1 >= height or y+1 >= width):
                return float('inf')
            else:
                I = [abs(int(pix[x+1,y]) - int(pix[x,y])) ,abs(int(pix[x,y+1])-int(pix[x,y]))]
                value = -gamma*np.linalg.norm(I)**2
        #         print("Ex:"+str(value))
                return value

        def EpsCon(vec0,vec_g):#test
            value = 0
            value += kappa*np.linalg.norm((vec0[0] - vec_g[0],vec0[1]-vec_g[1]))**2
        #     print("Con:"+str(value))
            return value

        def Energy(vec0,vec1,vec2,vec_g,pix):
            value = 0
            value = EpsIn(vec0,vec1,vec2)+EpsEx(vec0,pix)+EpsCon(vec0,vec_g)
        #     print("Result:"+str(value))
            return value
        #探索
        n = 500
        dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
        dy = [1, 0, -1, 1, 0, -1, 1, 0, -1]
        # dx = [1,1,1,0,0,0,-1,-1,-1]
        # dy = [1,-1,0,1,-1,0,1,-1,0]
        #210
        #543
        #876

        flag = 4
        for loop in range(0,n):
            for i in range(0,N):
                flag = 4
                eps_min = float('inf')
                vec_g = [0,0]

                #重心中心にするならこれ
        #         for j in range(0,N):
        #             vec_g += [v[j,0],v[j,1]]

                for j in range(0,9):
                    move  = [v[i,0]+dx[j], v[i,1]+dy[j]]
                    if(move[0] < 0 or move[1] < 0 or move[0] >= height  or move[1] >= width):
                        continue #はみ出し処理

                    #重心中心にするならこれ
                    #vec_g += [dx[j],dy[j]]
                    #vec_g =[vec_g[0]/N, vec_g[1]/N]
                    #画像中心を基準に
                    vec_g = [int(height/2),int(width/2)]

                    energy = Energy(move,v[(i+1)%N],v[(i+2)%N],vec_g,gray_test)
                    if(eps_min>energy):
                        eps_min = energy
                        flag = j
                v[i] += [dx[flag],dy[flag]]

        print(v)
        return v
