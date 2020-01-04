# https://qiita.com/Ken227/items/aee6c82ec6bab92e6abf

import numpy as np
import cv2
import math
from scipy import signal, interpolate
import matplotlib.pyplot as plt

# Num of
M = 50

#
def spline(x,y,point,deg):
    tck,u = interpolate.splprep([x,y],k=deg,s=0)
    u = np.linspace(0,1,num=point,endpoint=True)
    spline = interpolate.splev(u,tck)
    return spline[0],spline[1]


def ellipse_ft(x, y, N=100, S=100):
    y_plt = np.concatenate([y,y])
    x_plt = np.concatenate([x,x])
    plt.plot(y_plt)
    plt.plot(x_plt)
    plt.show()

    a = np.zeros(N)
    b = np.zeros(N)
    c = np.zeros(N)
    d = np.zeros(N)

    pi_t = 2*math.pi/x.shape[0]
    for n in range(N):
        for t in range(x.shape[0]):
            a[n] +=  x[t]*math.cos(n*(pi_t*t-math.pi))
            b[n] +=  x[t]*math.sin(n*(pi_t*t-math.pi))
            c[n] +=  y[t]*math.cos(n*(pi_t*t-math.pi))
            d[n] +=  y[t]*math.sin(n*(pi_t*t-math.pi))
        a[n] = a[n]/N
        b[n] = b[n]/N
        c[n] = c[n]/N
        d[n] = d[n]/N

    plt.plot(a)
    plt.plot(b)
    plt.plot(c)
    plt.plot(d)
    plt.show()

    f = np.zeros(S)
    g = np.zeros(S)
    pi_s = 2*math.pi/S
    for s in range(S):
        f[s] = a[0]
        g[s] = c[0]
        for n in range(1,N):
            f[s] += a[n]*math.cos(n*(pi_s*s-math.pi)) + b[n]*math.sin(n*(pi_s*s-math.pi))
            g[s] += c[n]*math.cos(n*(pi_s*s-math.pi)) + d[n]*math.sin(n*(pi_s*s-math.pi))

    plt.plot(g)
    plt.plot(f)
    plt.show()

    return f,g

def draw_bound(x,y,title="image",skip=5):
    img = cv2.imread('./CT.jpg')
    img = cv2.resize(img,(img.shape[0]*3,img.shape[1]*3))

    for i in range(x.shape[0]):
        if(i==0):
            cv2.circle(img,(int(x[i]),int(y[i])),5,(122,255,122),-1)
        else:
            cv2.circle(img,(int(x[i]),int(y[i])),2,(255,255,0),-1)
            if(i%skip==0):
                cv2.putText(img, str(i), (int(x[i]), int(y[i])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1, cv2.LINE_AA)

        if(i==0):
            cv2.line(img, (int(x[0]),int(y[0])), (int(x[-1]),int(y[-1])), (0, 255, 255), thickness=1, lineType=cv2.LINE_AA)
        else:
            cv2.line(img, (int(x[i-1]),int(y[i-1])), (int(x[i]),int(y[i])), (0, 255, 255), thickness=1, lineType=cv2.LINE_AA)

    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def align_doubling(x,y):
    return x[1:], y[1:]

def align_beginning(x, y, standard_x, standard_y):
    #search recently point from standard_xy
    length = np.zeros(x.shape[0])
    for i in range(x.shape[0]):
        length[i] = (x[i] - standard_x)**2 + (y[i] - standard_y)**2

    argmin = np.argmin(length)
    if(argmin>0):
        print("MISS")
        tmp_x = np.concatenate([x, x[0:argmin]])
        new_x = tmp_x[argmin:]
        tmp_y = np.concatenate([y, y[0:argmin]])
        new_y = tmp_y[argmin:]
    else:
        new_x = x
        new_y = y

    return new_x, new_y

def align_CW(x,y):
    s = 0
    for i in range(1,x.shape[0]):
        s += x[i-1]*y[i] - x[i]*y[i-1]

    if s > 0 :
        print("CCW")
        x = x[::-1]
        y = y[::-1]
    return x, y

def align_ending(x,y):
    x = np.append(x, x[0])
    y = np.append(y, y[0])
    return x,y


def has_duplicates(seq):
    return len(seq) != len(set(seq))


#main

ground_x = np.zeros(M)
ground_y = np.zeros(M)
standard_x = 0
standard_y = 0

i = 0
file_list = ['./points1.npy','./points2.npy','./points3.npy','./points4.npy']
for s in file_list:
    i += 1
    points = np.load(s)
    points = np.append(points, [points[0,:]], axis=0)

    draw_bound(points[:,0], points[:,1],str(i)+" input",1)
    x, y = spline(points[:,0], points[:,1], M, 1)
    draw_bound(x, y, str(i)+" spline")
    x, y = align_CW(x, y)
    draw_bound(x, y, str(i)+" CW")
    x, y = align_doubling(x,y)
    print(has_duplicates(x))
    if(i>1):
        x, y = align_beginning(x, y, standard_x, standard_y)
    else:
        standard_x = x[0]
        standard_y = y[0]
    x, y = align_ending(x, y)

    draw_bound(x,y, str(i)+" align")
    print(x)
    print(y)

    f, g = ellipse_ft(x, y, M, M)
    draw_bound(f,g, str(i)+" ellipse")
    ground_x += f
    ground_y += g
    #draw_bound(ground_x/i, ground_y/i)

ground_x /= len(file_list)
ground_y /= len(file_list)

#print(ground_x,ground_y)
draw_bound(ground_x, ground_y, "GROUND TRUTH")
