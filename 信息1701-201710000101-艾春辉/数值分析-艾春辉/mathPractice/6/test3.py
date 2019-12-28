import numpy as np
#顺序高斯消去法 LU分解
# a= [[0.101, 2.304, 3.555],
#     [-1.347, 3.712, 4.623],
#     [-2.835, 1.072, 5.643]]
# b = [1.183,2.137,3.035]
a = [[0.3*pow(10,-15),59.14,3,1]
    ,[5.291,-6.13,-1,2],
     [11.2,9,5,2]
    ,[1,2,1,1,]]
b = [59.17,46.78,1,2]
# print(len(a))
# print(len(a[0]))
N = len(a)
x = [0]*N
#消元法
for i in range(N-1):
    if(a[i][i] == 0):
        print("求解失败")
        break
    for j in range(i+1,N):
        a[j][i] = a[j][i] / a[i][i]; # 矩阵A的严格下三角部分存储L矩阵的严格下三角部分
        for k in range(i+1,N):
            a[j][k] = a[j][k] - a[j][i] * a[i][k];

print(a)
#解LY = b
Y = [0]*N
for i in range(N):
    Y[i] = b[i]
    for j in range(0,i):
        Y[i]-=a[i][j]*Y[j]
x[N-1] = Y[N-1]/a[N-1][N-1]#反解
num = N-2
#采取消减增广矩阵最后一列
while(num>=0):
    for i in range(num+1,N):
        Y[num]= Y[num] - a[num][i]*x[i]
    # print(a)
    x[num] = Y[num]/a[num][num]
    num -=1
print("(x1,x2,x3,x4)'=({},{},{},{})'".format(x[0],x[1],x[2],x[3]))