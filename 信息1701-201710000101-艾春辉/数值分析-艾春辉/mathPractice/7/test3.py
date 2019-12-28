# import numpy as np
# a = [2,-3]
# b = [1,1]
# res = np.array(a)*1 +np.array(b)*1
# print(res)
import numpy as np
s = 0
M = 100 # 最大迭代次数
w = 1#w>1
sigma = 0.00001
# a = [[5,2,1],[2,8,-3],[1,-3,-6]]
# b = [8,21,1]
a = [[-4,1,1,1],[1,-4,1,1],[1,1,-4,1],[1,1,1,-4]]
b = [1,1,1,1]
N = len(a)
X_b = [0]*N
X_a = [0]*N
maxstep = 1000
while(s<M and maxstep>sigma):
    # temp = X_a
    # X_b = temp
    for i in range(N):
        X_b[i] = X_a[i]
    for i in range(N):
        m = b[i]
        for j in range(i):
            m -= a[i][j]*X_a[j]
        for j in range(i+1,N):
            m -= a[i][j]*X_b[j]
        X_a[i] = m/a[i][i]
    X_a = (np.array(X_a)*w+(1-w)*np.array(X_b)).tolist()
    # print(X_a)
    # print(X_a)
    # print(X_b)
    res = abs(np.array(X_a)-np.array(X_b))
    # print(res)
    maxstep = res[np.argmax(res)]
    s+=1
print(X_a)
print("迭代次数是{}".format(s))