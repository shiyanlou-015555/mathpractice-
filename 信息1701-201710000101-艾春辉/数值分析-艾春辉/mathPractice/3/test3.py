import numpy as np
import matplotlib.pyplot as plt
# 预测函数,利用拉格朗日插值函数进行分段线性插值
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#分段线性插值函数
def h(x:[],y:[],a):
    ans = (a-x[1])/(x[0]-x[1])*y[0]+(a-x[0])/(x[1]-x[0])*y[1]
    return ans
#实际目标函数
def f(x:float):
    return 1/(1+x**2)
#查找第一个不符合的
def search(nums:[],target:float)->int:
    if(len(nums)==0):
        return 0
    low = 0
    high = len(nums)-1
    while(low<high):
        mid = low + ((high-low)>>1)
        if(nums[mid]<target):
            low = mid+1
        else:
            if(mid==0 or nums[mid-1]<target):
                return  mid
            else:
                high = mid-1
    return len(nums)-1
# print(search([1,2,3,4],2.5))
#设置基本点
def show(n:int):
    x1 = -5
    x = [-5,]
    y = []
    for i in range(n):
        x1 = round(x1+10/float(n),7)
        x.append(x1)
    for i in x:
        y.append(f(i))
    # 假设有一个输入点
        #预测值
    x_predict = [-5]
    y_predict = []
    y_true = []
    x2 = -5
    for i in range(1000):
        x2 = round(x2+0.01,7)
        x_predict.append(x2)
    for i in x_predict:
        j=0
        for k in range(len(x)):
            if x[k]>i:
                j=k
                break
        #取出两个值进行线性插值
        x_find = []
        x_find.append(x[j-1])
        x_find.append(x[j])
        y_find = []
        y_find.append(y[j-1])
        y_find.append(y[j])
        y_predict.append(h(x_find,y_find,i))
        y_true.append(f(i))
    # 将第一个画板划分为2行1列组成的区块，并获取到第一块区域
    # ax1 = plt.subplot(211)
    #
    # # 在第一个子区域中绘图
    # plt.scatter(x,y,marker="o",color  = "red",s = 40)
    # plt.scatter(x_predict,y_predict,marker=".",color  = "green",s = 10)
    # 选中第二个子区域，并绘图
    ax2 = plt.subplot(221)
    plt.scatter(x_predict, y_predict, marker=".", color="green", s=20)
    plt.scatter(x_predict,y_true,marker=".",color  = "blue",s = 20)#原函数图像
    # ax1.set_title("拟合点对过点的拟合情况")
    ax2.set_title("5个分段节点拟合点对真实点的拟合情况")
    # plt.show()
def show2(n:int):
    x1 = -5
    x = [-5,]
    y = []
    for i in range(n):
        x1 = round(x1+10/float(n),7)
        x.append(x1)
    for i in x:
        y.append(f(i))
    # 假设有一个输入点
        #预测值
    x_predict = [-5]
    y_predict = []
    y_true = []
    x2 = -5
    for i in range(1000):
        x2 = round(x2+0.01,7)
        x_predict.append(x2)
    for i in x_predict:
        j=0
        for k in range(len(x)):
            if x[k]>i:
                j=k
                break
        #取出两个值进行线性插值
        x_find = []
        x_find.append(x[j-1])
        x_find.append(x[j])
        y_find = []
        y_find.append(y[j-1])
        y_find.append(y[j])
        y_predict.append(h(x_find,y_find,i))
        y_true.append(f(i))
    # 将第一个画板划分为2行1列组成的区块，并获取到第一块区域
    # ax1 = plt.subplot(211)
    #
    # # 在第一个子区域中绘图
    # plt.scatter(x,y,marker="o",color  = "red",s = 40)
    # plt.scatter(x_predict,y_predict,marker=".",color  = "green",s = 10)
    # 选中第二个子区域，并绘图
    ax2 = plt.subplot(222)
    plt.scatter(x_predict, y_predict, marker=".", color="green", s=20)
    plt.scatter(x_predict,y_true,marker=".",color  = "blue",s = 20)#原函数图像
    # ax1.set_title("拟合点对过点的拟合情况")
    ax2.set_title("10个分段节点拟合点对真实点的拟合情况")
    # plt.show()
def show3(n:int):
    x1 = -5
    x = [-5,]
    y = []
    for i in range(n):
        x1 = round(x1+10/float(n),7)
        x.append(x1)
    for i in x:
        y.append(f(i))
    # 假设有一个输入点
        #预测值
    x_predict = [-5]
    y_predict = []
    y_true = []
    x2 = -5
    for i in range(1000):
        x2 = round(x2+0.01,7)
        x_predict.append(x2)
    for i in x_predict:
        j=0
        for k in range(len(x)):
            if x[k]>i:
                j=k
                break
        #取出两个值进行线性插值
        x_find = []
        x_find.append(x[j-1])
        x_find.append(x[j])
        y_find = []
        y_find.append(y[j-1])
        y_find.append(y[j])
        y_predict.append(h(x_find,y_find,i))
        y_true.append(f(i))
    # 将第一个画板划分为2行1列组成的区块，并获取到第一块区域
    # ax1 = plt.subplot(211)
    #
    # # 在第一个子区域中绘图
    # plt.scatter(x,y,marker="o",color  = "red",s = 40)
    # plt.scatter(x_predict,y_predict,marker=".",color  = "green",s = 10)
    # 选中第二个子区域，并绘图
    ax2 = plt.subplot(223)
    plt.scatter(x_predict, y_predict, marker=".", color="green", s=20)
    plt.scatter(x_predict,y_true,marker=".",color  = "blue",s = 20)#原函数图像
    # ax1.set_title("拟合点对过点的拟合情况")
    ax2.set_title("15个分段节点拟合点对真实点的拟合情况")
    # plt.show()
def show4(n:int):
    x1 = -5
    x = [-5,]
    y = []
    for i in range(n):
        x1 = round(x1+10/float(n),7)
        x.append(x1)
    for i in x:
        y.append(f(i))
    # 假设有一个输入点
        #预测值
    x_predict = [-5]
    y_predict = []
    y_true = []
    x2 = -5
    for i in range(1000):
        x2 = round(x2+0.01,7)
        x_predict.append(x2)
    for i in x_predict:
        j=0
        for k in range(len(x)):
            if x[k]>i:
                j=k
                break
        #取出两个值进行线性插值
        x_find = []
        x_find.append(x[j-1])
        x_find.append(x[j])
        y_find = []
        y_find.append(y[j-1])
        y_find.append(y[j])
        y_predict.append(h(x_find,y_find,i))
        y_true.append(f(i))
    # 将第一个画板划分为2行1列组成的区块，并获取到第一块区域
    # ax1 = plt.subplot(211)
    #
    # # 在第一个子区域中绘图
    # plt.scatter(x,y,marker="o",color  = "red",s = 40)
    # plt.scatter(x_predict,y_predict,marker=".",color  = "green",s = 10)
    # 选中第二个子区域，并绘图
    ax2 = plt.subplot(224)
    plt.scatter(x_predict, y_predict, marker=".", color="green", s=20)
    plt.scatter(x_predict,y_true,marker=".",color  = "blue",s = 20)#原函数图像
    # ax1.set_title("拟合点对过点的拟合情况")
    ax2.set_title("20个分段节点拟合点对真实点的拟合情况")
    # plt.show()

if __name__ == '__main__':
    # n = int(input("选择分段线性插值的节点个数?  "))
    show(5)
    show2(10)
    show3(15)
    show4(20)
    plt.show()

