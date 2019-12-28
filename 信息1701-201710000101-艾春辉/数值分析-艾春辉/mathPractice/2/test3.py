#单点弦截法
# 牛顿法
def function(x:float)->float:#函数表示
    return pow(x,3)+pow(x,2)-3*x-3
def function_grad(x0:float,x1:float)->float:#函数导数
    return (function(x1)-function(x0))/(x1-x0)
def niudun(x:[],N,sigma:float,sita:float,i:int)->float:#牛顿迭代法
    n=1
    # 如果x1就得到答案，不用再算下面的了
    if (abs(x[i] - x[0]) < sigma or abs(function(x[i])) < sita):
        print("函数近似解为:x = {}".format(x[i]))
        print("函数迭代次数为:{}次".format(n))
        return
    while(True):
        if(n>N):
            print("程序失败，结束")
            return
        else:
            x[i+1] = x[i] - function(x[i])/function_grad(x[i-1],x[i])# 弦解法迭代公式
            i = i+1
            n = n+1
            if(abs(x[i]-x[i-1])<sigma or abs(function(x[i]))<sita):
                print("函数近似解为:x = {}".format(x[i]))
                print("函数迭代次数为:{}次".format(n))
                return



if __name__ == '__main__':
    # 二分法
    x = [0]*1000
    x0 = float(input("请输入初始x0: "))
    sigma = float(input("请输入根的容许误差："))
    # sigma = 1e-6
    # sita = 1e-9
    sita = float(input("请输入函数值的容许误差："))
    x[0] = x0
    x1 = x0-function(x0)/(3*pow(x0,2)+2*x0-3)#先算出来x1
    x[1] = x1
    N = 1000
    niudun(x,N,sigma,sita,1)#调用函数
