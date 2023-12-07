import matplotlib.pyplot as plt
from sympy import *
k = 0
a = []
for x in range(1,5):
    k += Pow(7/6, x)
    a.append(k)

plt.plot(a, color="#eded33")
plt.show()


x = Symbol('x')
f = Pow(7/6,x)

for k in range(1,20):
    a= Sum(f, (x,1,k)).doit()
    print(k,"차 급수",N(a))

