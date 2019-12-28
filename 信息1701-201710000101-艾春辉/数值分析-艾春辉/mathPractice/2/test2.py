# 牛顿法
def function(x:float)->float:#函数表示
    return pow(x,3)+pow(x,2)-3*x-3
def function_grad(x:float)->float:#函数导数
    return 3*pow(x,2)+2*x-3
def niudun(x0:float,N,sigma:float,sita:float)->float:#牛顿迭代法
    n=0
    while(True):
        if(function_grad(x0)==0 or n>N):
            print("程序失败，结束")
            return
        else:
            x1 = x0 - function(x0)/function_grad(x0)
            n = n+1
            if(abs(x1-x0)<sigma or abs(function(x1))<sita):
                print("函数近似解为:x = {}".format(x1))
                print("函数近似解的值为：{}".format(function(x1)))
                print("函数迭代次数为:{}次".format(n))
                return
            x0 = x1


if __name__ == '__main__':
    # 二分法
    x0 = float(input("请输入初始x0: "))
    sigma = float(input("请输入根的容许误差："))
    # sigma = 1e-6
    # sita = 1e-9
    sita = float(input("请输入函数值的容许误差："))
    N = 1000
    niudun(x0,N,sigma,sita)
