from sympy import *

n = Symbol('n')
k = Symbol('k')

f = Sum(1/(1 + 2*k), (k,1,n))
a = Limit(f,n,oo,dir="+")

print(a.doit())

