import numpy as np


x = [0,1,2,3,4,5,6,7,8]
argmin = 3
tmp_x = np.concatenate([x, x[0:argmin]])

print(tmp_x[argmin:-1])
print(tmp_x[argmin:])
