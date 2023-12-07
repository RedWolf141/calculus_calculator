import matplotlib.pyplot as plt
from sympy import *
k = 0
a = []
for x in range(1,200):
    k += Pow(-1,x) * ln(x) / x
    a.append(k)

plt.plot(a, color="#eded33")
plt.show()


x = Symbol('x')
f = Pow (-1,x) * ln(x) / x

for k in range(1,100):
    a= Sum(f, (x,1,k)).doit()
    print(k,"차 급수",N(a))

