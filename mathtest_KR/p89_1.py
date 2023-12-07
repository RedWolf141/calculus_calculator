from sympy import *

k = Symbol('k')
n = Symbol('n')

f = (2*n + 4*k) / (n*n + k*n + k*k)
h=0
for x in range(1,5):
   ax = Sum(f, (k,1,x))
   h += Limit(ax,n,oo, dir="+").doit()

print(h)

