from sympy import *

n = Symbol('n')
k = Symbol('k')

f = (4*n + 2*k) / (n*n + n*k + k*k)

a = Sum(f,(k,1,n))

# Limit(a,n,oo,dir="+").doit()
Limit(a,n,5,dir="+").doit()
