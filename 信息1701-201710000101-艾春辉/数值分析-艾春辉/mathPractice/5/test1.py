#改进欧拉法
import math
def function1(x:float,y:float):
    return y**2
def function2(x:float,y:float):
    return  x/y
def function3(x:float,y:float):
    if x==0:
        return 1
    return  math.sin(x)/x
def tranvese1():
    y0 = 1
    x0 = 0
    y1 = 1
    x1 = 0
    for i in range(4):
        y1 = y0+0.1*function1(x0,y0)
        x1=round(x1+0.1,4)
        y1 = y0+0.1*0.5*(function1(x0,y0)+function1(x1,y1))
        y0 = y1
        x0 = x1
        print("x={}时候近似解是{}".format(x1,y1))
def tranvese2():
    y0 = 1
    x0 = 2
    y1 = 1
    x1 = 2
    for i in range(6):
        y1 = y0+0.1*function2(x0,y0)
        x1 = round(x1+0.1,4)
        y1 = y0+0.1*0.5*(function2(x0,y0)+function2(x1,y1))
        y0 = y1
        x0 = x1
        print("x={}时候近似解是{}".format(x1,y1))
def tranvese3():
    y0 = 0
    x0 = 0
    y1 = 0
    x1 = 0
    for i in range(10):
        y1 = y0+0.1*function3(x0,y0)
        x1=round(x1+0.1,4)
        y1 = y0+0.1*0.5*(function3(x0,y0)+function3(x1,y1))
        y0 = y1
        x0 = x1
        print("x={}时候近似解是{}".format(x1,y1))
if __name__ == '__main__':
    tranvese3()