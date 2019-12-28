import math
#梯形公公式
def function1(x:float):
    return math.exp(-x*x)
def function2(x:float):
    if(x==0):
        return 1
    else:
        return math.sin(x)/x
def trvase1(a:float,b:float,sigma:float):
    n = int(0)
    T0 = (function1(a)+function1(b))/2
    h0 = b-a
    while(1):
        n+=1
        h1 = h0/2
        T1 = T0/2
        # print(math.pow(2,n-1))
        for i in range(int(math.pow(2,n-1))):
            # print(i)
            T1+=h1*function1(a+(2*i+1)*h1)
        if(math.fabs(T1-T0)<sigma):
            break
        else:
            T0 = T1
            h0 = h1
    print("I1使用复化梯形公式的结果是:{}   迭代次数是{}次".format(T1,n))
def trvase2(a:float,b:float,sigma:float):
    n = int(0)
    T0 = (function2(a)+function2(b))/2
    h0 = b-a
    while(1):
        n+=1
        h1 = h0/2
        T1 = T0/2
        #print(math.pow(2,n-1))
        for i in range(int(math.pow(2,n-1))):
            # print(i)
            T1+=h1*function2(a+(2*i+1)*h1)
        if(math.fabs(T1-T0)<sigma):
            break
        else:
            T0 = T1
            h0 = h1
    print("I2使用复化梯形公式的结果是:{}   迭代次数是{}次".format(T1,n))
if __name__ == '__main__':
    trvase1(0,1,1e-6)
    trvase2(0,1,1e-6)