"""最小二乘法"""
#线性拟合
import numpy as np
import matplotlib.pyplot as plt

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
    X = fun2ploy(x)
    # 直接求解
    mat1 = np.mat(X)
    mat2 = np.mat(y).T
    # print(mat1)
    # print(mat2)
    mat3 = (mat1.T * mat1).I * mat1.T * mat2
    # print(mat3)
    # print(mat1*mat3    # 在第一个子区域中绘图
    print("平方误差是：{}".format(np.sum(np.array(mat2-mat1*mat3)**2)))
    x_test = np.linspace(0,7,1000)
    y_test = x_test*mat3[1,0]+mat3[0,0]
    # print(x_test)
    # print(y_test)
    plt.scatter(x,y,marker="o",color  = "red",s = 40)
    plt.scatter(x_test,y_test,marker=".",color = 'blue',s = 10)
    plt.show()
if __name__ == '__main__':
    x = [1,2,3,4,5]
    y = [4,4.5,6,8,8.5]
    leastseq_byploy(x,y)