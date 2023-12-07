import matplotlib.pyplot as plt
from sympy import *
k = 0
a = []
for x in range(1,30):
    k += Pow( Pow(x,1/x)-1 , x)
    a.append(k)

plt.plot(a, color="#eded33")
plt.show()


x = Symbol('x')
f = Pow ( Pow(x, 1/x)-1, x)

for k in range(1,100):
    a= Sum(f, (x,1,k)).doit()
    print(k,"차 급수",N(a))

