#病态问题
a1=0.99
x1=1/(1-pow(a1,2))
x2=(-a1)/(1-pow(a1,2))
x3=4/(4-pow(a1,2))
x4=(-a1)/(4-pow(a1,2))
a2=0.991
y1=1/(1-pow(a2,2))
y2=(-a2)/(1-pow(a2,2))
y3=4/(4-pow(a2,2))
y4=(-a2)/(4-pow(a2,2))
print("在a={0}中第一个方程组的解是x1={1},x2={2}".format(a1,x1,x2))
print("在a={0}中第一个方程组的解是x1={1},x2={2}".format(a2,y1,y2))
print("在a={0}中第二个方程组的解是x1={1},x2={2}".format(a1,x3,x4))
print("在a={0}中第二个方程组的解是x1={1},x2={2}".format(a2,y3,y4))