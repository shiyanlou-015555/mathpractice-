import numpy as np
a1 = 1.000001
a2 = 1.000000
a3 = 0.0000001
def method_1(a1,a3):
    res = np.float32(a1)
    for i in range(100):#循环100
        res+=np.float32(a3)
    return res
def method_2(a1,a3):
    res = np.float32(0)
    for i in range(100):#循环100
        res+=np.float32(a3)
    return res+np.float32(a1)
print("第一种方法结果是{}".format(method_1(np.float32(a1),np.float32(a3))))
print("第二种方法结果是{}".format(method_2(np.float32(a1),np.float32(a3))))


print("a1/a3+a2的结果是{}".format(np.float32(np.float32(a1)/np.float32(a3)+np.float32(a2))))


print("a1-a2的结果是{}".format(np.float32(np.float32(a1)-np.float32(a2))))