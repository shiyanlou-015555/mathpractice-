import math
# 拉格朗日插值
def h(x,y,a):
    ans=0.0
    for i in range(len(y)):
        t=y[i]
        for j in range(len(y)):
            if i !=j:
                t*=(a-x[j])/(x[i]-x[j])
        ans +=t
    return ans
if __name__ == '__main__':
    xx = input("请输入x的值：").split()  # 输入的x，是一个字符串数组，需要进行解析成整型
    x = [float(x1) for x1 in xx]
    yy = input("请输入y的值：").split()  # 输入的y，是一个字符串数组，需要进行解析成整型
    y = [float(y1) for y1 in yy]
    print("拉格朗日插值公式对于x={}时候的预测值为{},真实值为{}".format(11.5,h(x, y, 11.5),math.sin(math.radians(11.5))))