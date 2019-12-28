import matplotlib.pyplot as plt
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
def h(x,y,a):
    ans=0.0
    for i in range(len(y)):
        t=y[i]
        for j in range(len(y)):
            if i !=j:
                t*=(a-x[j])/(x[i]-x[j])
        ans +=t
    return ans
def f(x:float):
    return 1/(1+x**2)
def interpolation(n:int):
    x1 = -5
    x = [-5,]
    y = []
    y_true = []
#print(float(x1))
    j = 10/n
    for i in range(n):
        x1 = round(x1+j,7)
        x.append(x1)
    for i in x:
        y.append(f(i))
    #预测值
    x_predict = [-5]
    y_predict = []
    x2 = -5
    for i in range(1000):
        x2 = round(x2+0.01,7)
        x_predict.append(x2)
    for i in x_predict:
        y_predict.append(h(x,y,i))
        y_true.append(f(i))
    # # 将第一个画板划分为2行1列组成的区块，并获取到第一块区域
    # ax1 = plt.subplot(211)
    #
    # # 在第一个子区域中绘图
    # plt.scatter(x,y,marker="o",color  = "red",s = 40)
    # plt.scatter(x_predict,y_predict,marker=".",color  = "green",s = 10)
    # 选中第二个子区域，并绘图
    ax2 = plt.subplot(221)
    plt.scatter(x_predict, y_predict, marker=".", color="green", s=10)
    plt.scatter(x_predict,y_true,marker="o",color  = "blue",s = 10)#原函数图像
    # ax1.set_title("拟合点对过点的拟合情况")
    ax2.set_title("5个插值下拟合点对真实点的拟合情况")
def interpolation2(n:int):
    x1 = -5
    x = [-5,]
    y = []
    y_true = []
#print(float(x1))
    j = 10/n
    for i in range(n):
        x1 = round(x1+j,7)
        x.append(x1)
    for i in x:
        y.append(f(i))
    #预测值
    x_predict = [-5]
    y_predict = []
    x2 = -5
    for i in range(1000):
        x2 = round(x2+0.01,7)
        x_predict.append(x2)
    for i in x_predict:
        y_predict.append(h(x,y,i))
        y_true.append(f(i))
    # # 将第一个画板划分为2行1列组成的区块，并获取到第一块区域
    # ax1 = plt.subplot(211)
    #
    # # 在第一个子区域中绘图
    # plt.scatter(x,y,marker="o",color  = "red",s = 40)
    # plt.scatter(x_predict,y_predict,marker=".",color  = "green",s = 10)
    # 选中第二个子区域，并绘图
    ax2 = plt.subplot(222)
    plt.scatter(x_predict, y_predict, marker=".", color="green", s=10)
    plt.scatter(x_predict,y_true,marker="o",color  = "blue",s = 10)#原函数图像
    # ax1.set_title("拟合点对过点的拟合情况")
    ax2.set_title("10个插值下拟合点对真实点的拟合情况")
def interpolation3(n:int):
    x1 = -5
    x = [-5,]
    y = []
    y_true = []
#print(float(x1))
    j = 10/n
    for i in range(n):
        x1 = round(x1+j,7)
        x.append(x1)
    for i in x:
        y.append(f(i))
    #预测值
    x_predict = [-5]
    y_predict = []
    x2 = -5
    for i in range(1000):
        x2 = round(x2+0.01,7)
        x_predict.append(x2)
    for i in x_predict:
        y_predict.append(h(x,y,i))
        y_true.append(f(i))
    # # 将第一个画板划分为2行1列组成的区块，并获取到第一块区域
    # ax1 = plt.subplot(211)
    #
    # # 在第一个子区域中绘图
    # plt.scatter(x,y,marker="o",color  = "red",s = 40)
    # plt.scatter(x_predict,y_predict,marker=".",color  = "green",s = 10)
    # 选中第二个子区域，并绘图
    ax2 = plt.subplot(223)
    plt.scatter(x_predict, y_predict, marker=".", color="green", s=10)
    plt.scatter(x_predict,y_true,marker="o",color  = "blue",s = 10)#原函数图像
    # ax1.set_title("拟合点对过点的拟合情况")
    ax2.set_title("15个插值下拟合点对真实点的拟合情况")
def interpolation4(n:int):
    x1 = -5
    x = [-5,]
    y = []
    y_true = []
#print(float(x1))
    j = 10/n
    for i in range(n):
        x1 = round(x1+j,7)
        x.append(x1)
    for i in x:
        y.append(f(i))
    #预测值
    x_predict = [-5]
    y_predict = []
    x2 = -5
    for i in range(1000):
        x2 = round(x2+0.01,7)
        x_predict.append(x2)
    for i in x_predict:
        y_predict.append(h(x,y,i))
        y_true.append(f(i))
    # # 将第一个画板划分为2行1列组成的区块，并获取到第一块区域
    # ax1 = plt.subplot(211)
    #
    # # 在第一个子区域中绘图
    # plt.scatter(x,y,marker="o",color  = "red",s = 40)
    # plt.scatter(x_predict,y_predict,marker=".",color  = "green",s = 10)
    # 选中第二个子区域，并绘图
    ax2 = plt.subplot(224)
    plt.scatter(x_predict, y_predict, marker=".", color="green", s=10)
    plt.scatter(x_predict,y_true,marker="o",color  = "blue",s = 10)#原函数图像
    # ax1.set_title("拟合点对过点的拟合情况")
    ax2.set_title("20个插值下拟合点对真实点的拟合情况")
if __name__ == '__main__':
    # n = int(input("取多少个插值点进行多项式插值?"))
    interpolation(5)
    interpolation2(10)
    interpolation3(15)
    interpolation4(20)
    plt.show()
