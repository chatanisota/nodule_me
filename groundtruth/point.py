import cv2
import numpy as np

img = cv2.imread('./CT.jpg')
img = cv2.resize(img,(img.shape[0]*3,img.shape[1]*3))

list = np.zeros((1,2))
is_init = True

# mouse callback function
def draw_maker(event,x,y,flags,param):
    global list
    global is_init

    if event == cv2.EVENT_LBUTTONDOWN:
        list = np.append(list, [[int(x),int(y)]], axis=0)
        cv2.circle(img,(x,y),2,(255,255,0),-1)
        if(is_init):
            is_init = False
            list = np.delete(list, 0, 0)
        else:
            cv2.line(img, (int(list[-2,0]),int(list[-2,1])), (int(list[-1,0]),int(list[-1,1])), (0, 255, 255), thickness=1, lineType=cv2.LINE_AA)

        return False

    if event == cv2.EVENT_RBUTTONDOWN:
        return True

# Create a black image, a window and bind the function to window
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_maker)

while(1):
    cv2.imshow('image',img)

    if cv2.waitKey(20) != -1:
        break

cv2.line(img, (int(list[0,0]),int(list[0,1])), (int(list[-1,0]),int(list[-1,1])), (0, 255, 255), thickness=1, lineType=cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
np.save('./points2',list)
cv2.destroyAllWindows()
