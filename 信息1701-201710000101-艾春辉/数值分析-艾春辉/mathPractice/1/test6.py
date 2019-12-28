a = float(input(("请输入数值a：")))
x0 = float(input(("请确认初始值：")))
x = []
x.append(x0)
x.append(0.5*(x0+a/x0))
i=1
while(abs((x[i]-x[i-1])/x[i])>0.00001):
    i+=1
    x.append(0.5*(x[i-1]+a/x[i-1]))
print('迭代次数为{}次'.format(i))
print('最后近似值为{}'.format(x[len(x)-1]))