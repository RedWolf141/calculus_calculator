from sympy import *

x = Symbol('x')
t = Symbol('t')
h = Symbol('h')

g = (t+1) * exp(t)

f = integrate(g, (t, 2*x, 3*x))

a = Limit(f / (2*x) , x, 0).doit()

print(a)
