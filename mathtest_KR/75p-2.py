import sympy as sp
from sympy import *
x = sp.Symbol('x')

f = ( Pow(16,x) - Pow(4,x) ) / (Pow(4,x) + Pow(2,x))

k = sp.integrate(f, (x,0,1))
k = sp.simplify(k)

print(k)
