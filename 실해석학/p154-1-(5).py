import matplotlib.pyplot as plt
from sympy import *
k = 0
a = []
for x in range(1,30):
    k += 1 /  ( (x+1)* (x+2) * (x+3))
    a.append(k)

plt.plot(a, color="#eded33")
plt.show()


x = Symbol('x')
f = 1 / ((x+1) * (x+2) * (x+3))

for k in range(1,20):
    a= Sum(f, (x,1,k)).doit()
    print(k,"차 급수",N(a))

