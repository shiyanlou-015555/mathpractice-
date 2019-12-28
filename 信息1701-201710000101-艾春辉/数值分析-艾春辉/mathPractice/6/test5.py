import numpy as np
#矩阵求逆
A = [[2,2,3],[1,-1,0],[-1,2,1]]
N = len(A)
a = np.zeros((N,2*N))
# print(A)
for i in range(N):
    for j in range(2*N):
        if(i<N and j<N):
            a[i][j] = A[i][j]
        elif(j-N == i):
            a[i][j] = 1
# print(a)
#消元法
for i in range(N):
    for j in range(i+1,N):
        m = a[j][i]/a[i][i]
        a[j][i] = 0
        for k in range(i+1,2*N):
            a[j][k] = a[j][k] - a[i][k]*m
# print(a)
s1 = N-1
# s2 = N - 2
while(s1>=1):
    s2 = s1-1
    while(s2>=0):
        m = a[s2][s1]/a[s1][s1]
        a[s2][s1] = 0
        for i in range(N,2*N):
            # print(i)
            a[s2][i] = a[s2][i] - a[s1][i]*m
        s2-=1
    s1-=1
# print(a)
sum = 1
for i in range(N):
    sum*=a[i][i]
print("行列式等于{}".format(sum))
for i in range(N):
    m = 1/a[i][i]
    a[i] = a[i]*m
# print(a)
print(a[:,[i for i in range(N,2*N)]])