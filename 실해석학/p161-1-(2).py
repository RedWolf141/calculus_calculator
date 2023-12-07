import matplotlib.pyplot as plt
from sympy import *
k = 0
a = []
b = []
c = []
for x in range(1,20):
    k += factorial(x) / Pow(2,x+4)
    a.append(k)

for x in range(1,40):
    k += factorial(x) / Pow(2,x+4)
    b.append(k)

for x in range(1,60):
    k += factorial(x) / Pow(2,x+4)
    c.append(k)

plt.plot(a)
plt.plot(b)
plt.plot(c)
plt.show()


x = Symbol('x')
f = factorial(x) / Pow(2, x+4)

for k in range(1,20):
    a= Sum(f, (x,1,k)).doit()
    print(k,"차 급수",N(a))

