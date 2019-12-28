#第一个函数I1
import math
def function1(x:float):
    return math.exp(-x*x)
def function2(x:float):
    if(x==0):
        return 1
    else:
        return math.sin(x)/x
if __name__ == '__main__':
    a = 0
    b = 1
    print("I1使用梯形公式结果是:{}".format((b-a)/2*(function1(a)+function1(b))))
    print("I1使用辛普森公式结果是:{}".format((b-a)/6*(function1(a)+4*function1((a+b)/2)+function1(b))))
    print("I2使用梯形公式结果是:{}".format((b-a)/2*(function2(a)+function2(b))))
    print("I2使用辛普森公式结果是:{}".format((b-a)/6*(function2(a)+4*function2((a+b)/2)+function2(b))))
