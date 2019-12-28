# 显隐式欧拉法
import math
import matplotlib.pyplot as plt
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def function(x:float,y:float):
    return -50*y
def trueNum(x:float):
    return 100*math.exp(-50*x)
def tranvese(h:float):
    res1 = 0
    res2 = 0
    res3 = 0
    y0 = 100
    x0 = 0
    y2 = 100
    x2 = 0
    num1 = []#储存x的值
    num2 = []#储存显示欧拉的值
    num3 = []#储存隐式欧拉的值
    num4 = []#储存真实值的值
    for i in range(int(1/h)):
        y1 = y0+h*function(x0,y0)
        res1 = y1
        y0 = y1
        yk = y2/(1+h*50)
        res2 = yk
        y2 = yk
        x0 = round(x0+h,4)
        x2 = round(x2 + h, 4)
        res3 = trueNum(x0)
        num1.append(x0)
        #print("h={}时候x={}时候显式欧拉法近似解是{}".format(h,x0,res1))
        num2.append(res1)
        # print("h={}时候x={}时候隐式欧拉法近似解是{}".format(h,x0,res2))
        num3.append(res2)
        # print("h={}时候x={}时候准确解解是{}".format(h,x0,res3))
        num4.append(res3)
    # 选中第二个子区域，并绘图
    ax2 = plt.subplot(221)
    plt.scatter(num1, num2, marker=".", color="green", s=200)
    plt.scatter(num1,num4,marker="o",color  = "blue",s = 20)#原函数图像
    # ax1.set_title("拟合点对过点的拟合情况")
    ax2.set_title("h={}显示欧拉公式拟合点对真实点的拟合情况".format(h))
    ax1 = plt.subplot(222)
    plt.scatter(num1, num3, marker=".", color="green", s=20)
    plt.scatter(num1,num4,marker="o",color  = "blue",s = 20)#原函数图像
    # ax1.set_title("拟合点对过点的拟合情况")
    ax1.set_title("h={}隐式欧拉公式拟合点对真实点的拟合情况".format(h))
    plt.show()
tranvese(0.001)