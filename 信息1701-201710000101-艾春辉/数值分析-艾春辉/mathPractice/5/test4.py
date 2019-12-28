import math
a = float(input("左端点: "))
b = float(input("右端点："))
y0 = float(input("初始点: "))
sigma = float(input("容许误差："))
maxStep = float(input("最大步长："))
minStep = float(input("最小步长: "))
t = a
y = y0
h = maxStep
sita = 0
def function1(x:float,y:float):
    return y**2
while(h>=minStep):
    # k1 = h*function1(t,y)
    #     # k2 = h*function1(t+h/4,y+k1/4)
    #     # k3 = h*function1(t+3/8*h,y+3/32*k1+9/32*k2)
    #     # k4 = h*function1(t+12/13*h,y+1932/2197*k1-7200/2197*k2+7296/2197*k3)
    #     # k5 = h*function1(t+h,y+439/216*k1-8*k2+3680/513*k3-845/4104*k4)
    #     # k6 = h*function1(t+h/2,y-8/27*k1+2*k2-3544/2565*k3+1859/4104*k4-11/40*k5)
    #     # R = abs(1/360*k1-128/4275*k3-2197/75240*k4+1/50*k5+2/55*k6)
    k1 = h * function1(t, y)
    k2 = h * function1(t + h / 4, y + k1 / 4)
    k3 = h * function1(t + 3 * h / 8, y + 3 * k1 / 32 + 9 * k2 / 32)
    k4 = h * function1(t + 12 * h / 13, y + 1932 * k1 / 2197 - 7200 * k2 / 2197 + 7296 * k3 / 2197)
    k5 = h * function1(t + h, y + 439 * k1 / 216 - 8 * k2 + 3680 * k3 / 513 - 845 * k4 / 4104)
    k6 = h * function1(t + h / 2, y - 8 / 27 * k1 + 2 * k2 - 3544 / 2565 * k3 + 1859 * k4 / 4104 - 11 / 40 * k5)
    R = abs(k1 / 360 - 128 * k3 / 4275 - 2197 * k4 / 75240 + k5 / 50 + 2 * k6 / 55)
    if(R<=(h*sigma)):
        t = t+h
        y = y+25/216*k1+1408/2565*k3+2197/4104*k4-1/5*k5
        print("RKF算法预测在x={}时候y={}此时步长h={}".format(t,y,h))
    sita = 0.84*((sigma*h/R)**(1/4))
    if(sita<=0.1):
        h = 0.1*h
    elif(sita>=4):
        h = 4*h
    else:
        h = sita*h
    if(h>maxStep):
        h = maxStep
    if(t==b):
        print("停止计算")
        break
    if((t+h)>b):
        h = b-t
