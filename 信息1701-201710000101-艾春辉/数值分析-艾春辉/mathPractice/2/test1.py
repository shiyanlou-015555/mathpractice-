import math
# 设置函数
def function(x):
    return math.pow(x,3)+math.pow(x,2)-3*x-3
n = 0
def twice_split():
    global a
    global b
    global n
    fa = function(a)
    fb = function(b)
    #如果fa<fb
    if fa*fb<0:
        while(math.fabs(b-a)>sigma):#如果>误差可以处理
            x = (a+b)/2
            f = function(x)
            if math.fabs(f)<log:#达到精确度
                print("近似根为{}".format(x))
                print("二分次数为{}".format(n))
                print("近似根对应函数值为{}".format(function(x)))
            else:
                if fa*f<0:
                    b = x
                    fb = f
                else:
                    a = x
                    fa = f
                n=n+1
        print("近似根为{}".format(x))
        print("二分次数为{}".format(n))
        print("近似根对应函数值为{}".format(function(x)))
    else:
        print("算法失败")
if __name__ == '__main__':
    # 二分法
    a = float(input("请输入左边界："))
    b = float(input("请输入右边界："))
    sigma = float(input("请输入根的容许误差："))
    # sigma = 1e-6
    # log = 1e-9
    log = float(input("请输入函数值的容许误差："))
    twice_split()



