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
            return S1
        else:
            S0 = S1
            h0 = h1
    # print("I1使用复化辛普森公式的结果是:{}   迭代次数是{}次".format(S1, n))
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
            return T1
        else:
            T0 = T1
            h0 = h1
    # print("I2使用复化梯形公式的结果是:{}   迭代次数是{}次".format(T1,n))
def solve(a:float,b:float,sigma:float,ans:float):
    mid = (a+b)/2
    l = trvase1(a,mid,sigma)
    r = trvase1(mid,b,sigma)
    if(abs(l+r-ans)<=sigma):
        return ans
    return solve(a,mid,sigma,l)+solve(mid,b,sigma,r)
def solve2(a:float,b:float,sigma:float,ans:float):
    mid = (a+b)/2
    l = trvase2(a,mid,sigma)
    r = trvase2(mid,b,sigma)
    if(abs(l+r-ans)<=sigma):
        return ans
    return solve2(a,mid,sigma,l)+solve2(mid,b,sigma,r)
if __name__ == '__main__':
    a = 0
    b = 1
    sigma = 1e-6
    ans =  trvase1(0,1,1e-6)
    print("I1使用自适应算法得到结果是{}".format(solve(a,b,sigma,ans)))
    ans = trvase2(0, 1, 1e-6)
    print("I2使用自适应算法得到结果是{}".format(solve2(a,b,sigma,ans)))

