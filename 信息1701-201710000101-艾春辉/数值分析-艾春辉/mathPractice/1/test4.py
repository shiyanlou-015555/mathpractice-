def method_1():
    res = [0]*101
    res[0] = 0.1823
    for i in range(101):
        if i==0:
            continue
        else:
            res[i] = 1/i - 5*res[i-1]
    return res
def method_2():
    res = [0]*101
    res[100] = 0.001815
    for i in range(101):
        if i==100:
            break
        else:
            res[100-i-1] = 1/5*(1/(100-i)-res[100-i])
    return res

if __name__ == '__main__':
    res1 = method_1()
    res2 = method_2()
    print("第一个方法        第二个方法")
    for i in range(16):
        print(str(res1[i])+"      "+str(res2[i]))
