# 输入控制区间 a,b,控制精度e,最大循环次数M
import math
def function1(x:float):
    return math.exp(-x*x)
def function2(x:float):
    if(x==0):
        return 1
    else:
        return math.sin(x)/x
    #第一个方程式
def trvase1(a:float,b:float,sigma:float,M:int):
    m = int(0)
    h = (b-a)/(math.pow(2,m))
    T0 = [0]*M
    T1 = [0]*M
    T2 = [0]*M
    T3 = [0]*M
    T0[0] = h/2*(function1(a)+function1(b))
    m+=1
    while(m<=M):
        hm = (b - a) / (math.pow(2, m))
        T0[m] = 1/2*T0[m-1]
        for i in range(int(math.pow(2,m-1))):
            k = i+1
            T0[m] += hm*function1(a+(2*k-1)*hm)
        T1[m-1] = (4*T0[m]-T0[m-1])/3
        if(m>1):
            T2[m-2] = (16*T1[m-1]-T1[m-2])/15
        if(m>2):
            T3[m-3] = (64*T2[m-2]-T2[m-3])/63
        if(m>3):
            if(math.fabs(math.pow(T3[m-3],3)-math.pow(T3[m-4],3))<sigma):
                break
        m+=1
    print("I1使用龙贝格公式的结果是:{}   迭代次数是{}次".format(T3[m-3], m))
def trvase2(a:float,b:float,sigma:float,M:int):
    m = int(0)
    h = (b-a)/(math.pow(2,m))
    T0 = [0]*M
    T1 = [0]*M
    T2 = [0]*M
    T3 = [0]*M
    T0[0] = h/2*(function2(a)+function2(b))
    m+=1
    while(m<=M):
        hm = (b - a) / (math.pow(2, m))
        T0[m] = 1/2*T0[m-1]
        for i in range(int(math.pow(2,m-1))):
            k = i+1
            T0[m] += hm*function2(a+(2*k-1)*hm)
        T1[m-1] = (4*T0[m]-T0[m-1])/3
        if(m>1):
            T2[m-2] = (16*T1[m-1]-T1[m-2])/15
        if(m>2):
            T3[m-3] = (64*T2[m-2]-T2[m-3])/63
        if(m>3):
            if(math.fabs(math.pow(T3[m-3],3)-math.pow(T3[m-4],3))<sigma):
                break
        m+=1
    print("I2使用龙贝格公式的结果是:{}   迭代次数是{}次".format(T3[m-3], m))
if __name__ == '__main__':
    trvase1(0,1,1e-6,100)
    trvase2(0,1,1e-6,100)