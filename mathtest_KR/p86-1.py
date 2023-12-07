from sympy import *

x = Symbol('x')

f = 2 / (x*x+4*x+3)

a = integrate(f, (x,1,3)).doit()

print(a.simplify())