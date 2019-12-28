import math
def function1(x:float):
    return math.exp(-x*x)
def function2(x:float):
    if(x==0):
        return 1
    else:
        return math.sin(x)/x
    #第一个方程式
def trvase1(a:float,b:float,sigma:float):
    n = int(0)
    h0 = (b-a)/2
    S0 = h0/3*(function1(a)+4*function1((a+b)/2)+function1(b))
    while(1):
        n+=1
        h1 = h0/2
        m = int(math.pow(2,n-1))
        S1 = S0/2
        for i in range(2*m):
            j = i+1
            S1+= h1/3*(4*function1(a+(2*j-1)*h1))
        for i in range(m):
            j = i + 1
            S1 -= h1 / 3 * (2 * function1(a + (4 * j - 2) * h1))
        if(math.fabs(S1-S0)<sigma):
            break
        else:
            S0 = S1
            h0 = h1
    print("I1使用复化辛普森公式的结果是:{}   迭代次数是{}次".format(S1, n))
def trvase2(a:float,b:float,sigma:float):
    n = int(0)
    h0 = (b-a)/2
    S0 = h0/3*(function2(a)+4*function2((a+b)/2)+function2(b))
    while(1):
        n+=1
        h1 = h0/2
        m = int(math.pow(2,n-1))
        S1 = S0/2
        for i in range(2*m):
            j = i+1
            S1+= h1/3*(4*function2(a+(2*j-1)*h1))
        for i in range(m):
            j = i + 1
            S1 -= h1 / 3 * (2 * function2(a + (4 * j - 2) * h1))
        if(math.fabs(S1-S0)<sigma):
            break
        else:
            S0 = S1
            h0 = h1
    print("I2使用复化辛普森公式的结果是:{}   迭代次数是{}次".format(S1, n))
if __name__ == '__main__':
    trvase1(0,1,1e-6)
    trvase2(0,1,1e-6)