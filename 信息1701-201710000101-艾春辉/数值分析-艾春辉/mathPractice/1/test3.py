#第一种可微方法
import math
def function(x):
    #定义函数
    return math.pow(x,3)
def method_1(i:int):
    x0 = 1
    h = math.pow(10,-i)
    fx = (function(x0+h)-function(x0))/h
    return fx
def method_2(i:int):
    x0 = 1
    h = math.pow(10,-i)
    fx = (function(x0+h)-function(x0-h))/(2*h)
    return fx
if __name__ == '__main__':
    print("第一种方法    第二种方法")
    for i in range(16):
        print(str(method_1(i))+"   "+str(method_2(i)))