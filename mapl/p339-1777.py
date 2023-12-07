from sympy import *

x = Symbol('x')
k = input("")

k = int(k)
f = pow(x,k) * exp(x)

a = integrate(f , (x,0,1))
a.evalf()
print(a)
