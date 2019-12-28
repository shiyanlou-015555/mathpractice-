#4阶龙格库塔
def function1(x:float,y:float):
    return y**2
def function2(x:float,y:float):
    return  x/y
def tranvese1():
    y0 = 1
    x0 = 0
    y1 = 1
    x1 = 0
    for i in range(4):
        K1 = function1(x0,y0)
        K2 = function1(x0+0.05,y0+0.05*K1)
        K3 = function1(x0+0.05,y0+0.05*K2)
        K4 = function1(x0+0.1,y0+0.1*K3)
        y1 = y0+(0.1/6)*(K1+2*K2+2*K3+K4)
        x1=round(x1+0.1,4)
        y0 = y1
        x0 = x1
        print("x={}时候近似解是{}".format(x1,y1))
def tranvese2():
    y0 = 1
    x0 = 2.0
    y1 = 1
    x1 = 2.0
    for i in range(6):
        K1 = function2(x0,y0)
        K2 = function2(x0+0.05,y0+0.05*K1)
        K3 = function2(x0+0.05,y0+0.05*K2)
        K4 = function2(x0+0.1,y0+0.1*K3)
        y1 = y0+(0.1/6)*(K1+2*K2+2*K3+K4)
        x1=round(x1+0.1,4)
        y0 = y1
        x0 = x1
        print("x={}时候近似解是{}".format(x1,y1))
if __name__ == '__main__':
    tranvese1()
