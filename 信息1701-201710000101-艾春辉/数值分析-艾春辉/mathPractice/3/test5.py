import numpy as np
import matplotlib.pyplot as plt
x = [2, 3, 4, 7, 8, 10, 11, 14, 16, 18, 19]
y = [106.42, 108.2, 109.5, 110, 109.93, 110.49, 110.59, 110.6, 110.76, 111, 111.2]
for i in range(len(x)):
    print(str(x[i])+"   "+str(y[i]))
n = len(x)
x00 = n
x01=x02=x12=x22 = 0#严格按照书上公式进行解决
y00 = y10 = y20 = 0
for i in range(len(x)):
    x01 += x[i]
    x02 += x[i]**2
    x12 += x[i]**3
    x22 += x[i]**4
    y00 += y[i]
    y10 += y[i]*x[i]
    y20 += y[i]*(x[i]**2)
phiphi = np.zeros((3,3))
#初始赋值
#x,y = phiphi.shape
phiphi[0,0],phiphi[0,1],phiphi[0,2],phiphi[1,0],phiphi[1,1],phiphi[1,2],phiphi[2,0],phiphi[2,1],phiphi[2,2] = x00,x01,x02,x01,x02,x12,x02,x12,x22
yphi = np.zeros((3,1))
yphi[0,0],yphi[1,0],yphi[2,0] = y00,y10,y20
#[[x00,x01,x02],[x01,x02,x12][x02,x12,x22]]
mat1 = np.mat(phiphi).I * np.mat(yphi)
# print(phiphi)
print(mat1)
x_test = np.linspace(-1, 20, 1000)
y_test =  mat1[0, 0] + mat1[1,0]*x_test+mat1[2,0]*x_test**2
# print(x_test)
# print(y_test)
# 注意
# print((mat1[0, 0] + mat1[1,0]*x+mat1[2,0]*x**2))
# print("平方误差是：{}".format(np.sum(np.array(y - (mat1[0, 0] + mat1[1,0]*x+mat1[2,0]*x**2)) ** 2)))
sigma = 0
for i in range(len(y)):
    sigma+= (y[i]-(mat1[0, 0] + mat1[1,0]*x[i]+mat1[2,0]*x[i]**2)) ** 2
print("拟合函数等于{}+{}x+{}x^2".format(mat1[0,0],mat1[1,0],mat1[2,0]))
print("平方误差是{}".format(sigma))
plt.scatter(x, y, marker="o", color="red", s=40)
plt.scatter(x_test, y_test, marker=".", color='blue', s=10)
plt.show()