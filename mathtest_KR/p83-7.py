from  sympy import *

x = Symbol('x')

f = (x+2) * cos(2*x)

a = integrate(f,(x,pi/2,pi))

print(a.simplify())

