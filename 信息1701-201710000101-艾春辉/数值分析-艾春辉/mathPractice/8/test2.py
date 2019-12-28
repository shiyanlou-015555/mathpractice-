# import numpy as np
# A = [[],[]]
# N = len(A)
# U  = np.mat([1]*N).T
# print(U)
# print(max(U)[0,0])
# 反幂法
import numpy as np
a = [[4,-1,1],[-1,3,-2],[1,-2,3]]#系数矩阵
N = len(a)

A = np.mat(a)
U  = np.mat([1]*N).T
V  = np.mat([1]*N).T
sigma = 0.000001#精度
M = 1000#最大迭代次数
m = 1
k = 0
before = m
while(k<M):
    before = m
    V = A.I*U
    m = max(V)[0,0]
    U = V/m
    if(abs(m-before)<sigma):
        print("特征值为{}".format(1/m))
        print("特征向量为{}".format(U))
        break
    k += 1
print(k)