#列主元高斯消去法
# a= [[0.101, 2.304, 3.555, 1.183],
#     [-1.347, 3.712, 4.623, 2.137],
#     [-2.835, 1.072, 5.643, 3.035]]
a = [[0.3*pow(10,-15),59.14,3,1,59.17],[5.291,-6.13,-1,2,46.78],[11.2,9,5,2,1],[1,2,1,1,2]]
# print(len(a))
# print(len(a[0]))
N = len(a)
x = [0]*N
max = 0
s = -1
temp = []
m = 0
for i in range(N-1): # for 1:n-1
    # find the max row
    for j in range(i,N):
        if(abs(a[j][i])>max):
            max = a[j][i]
            s = j
    # exchange it
    temp = a[i]
    a[i] = a[s]
    a[s] = temp
    max = 0
    s = -1
    for j in range(i+1,N):
        m = a[j][i]/a[i][i]
        a[j][i] = 0
        for k in range(i+1,N+1):
            a[j][k] = a[j][k] - a[i][k]*m
print(a)
x[N-1] = a[N-1][N]/a[N-1][N-1]#反解
num = N-2
#采取消减增广矩阵最后一列
while(num>=0):
    for i in range(num+1,N):
        a[num][N] = a[num][N] - a[num][i]*x[i]
    # print(a)
    x[num] = a[num][N]/a[num][num]
    num -=1
# print("(x1,x2,x3)'=({},{},{})'".format(x[0],x[1],x[2]))
print("(x1,x2,x3,x4)'=({},{},{},{})'".format(x[0],x[1],x[2],x[3]))
