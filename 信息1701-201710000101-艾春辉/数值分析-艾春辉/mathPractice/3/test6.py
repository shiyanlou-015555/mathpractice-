import numpy as np
import matplotlib.pyplot as plt
import math
# 增加
def fun2ploy(x:[]):
    '''
    数据转化为[x^0,x^1,x^2,...x^n]
    首列变1
    '''
    lens = len(x)
    X = np.ones([lens,2])
    for i in range(lens):
       X[i,1] = x[i]
    return X


def leastseq_byploy(x:[], y:[]):
    '''
    最小二乘求解
    '''
    t = 1/np.array(x)
    z = np.log(np.array(y)).tolist()
    X = fun2ploy(t.tolist())
    # print(t.tolist())
    # 直接求解
    mat1 = np.mat(X)
    mat2 = np.mat(z).T
    print((mat1.T * mat1).I * mat1.T)
    mat3 = (mat1.T * mat1).I * mat1.T * mat2 #beta的值
    # print(mat3)
    # print(mat1*mat3    # 在第一个子区域中绘图
    print(mat3)
    a = math.exp(mat3[0,0])
    b = mat3[1,0]
    sigma = 0
    for i in range(len(y)):
        sigma += (y[i] - (a*math.exp(b/x[i]))) ** 2
    print("拟合函数是{}*exp({}/x)".format(a,b))
    print("平方误差是{}".format(sigma))
    x_test = np.linspace(1,20,1000)
    # print(b/np.array(x_test))
    y_test = a*np.exp(b/np.array(x_test))
    # print(y_test)
    # print(x_test)
    # print(y_test)
    plt.scatter(x,y,marker="*",color  = "red",s = 40)
    plt.scatter(x_test,y_test,marker=".",color = 'blue',s = 10)
    plt.show()
if __name__ == '__main__':
    x = [2, 3, 4, 7, 8, 10, 11, 14, 16, 18, 19]
    y = [106.42, 108.2, 109.5, 110, 109.93, 110.49, 110.59, 110.6, 110.76, 111, 111.2]
    leastseq_byploy(x,y)
    # y = a*e^{b/x} 等价于 z = kt +c
