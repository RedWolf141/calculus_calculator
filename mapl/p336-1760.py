from sympy import *

x = Symbol('x')
sum = 0
new_sum = 0
for k in range(1,101):
    f = pow(tan(x), k)
    a = integrate(f , (x,0,pi/4))
    a.evalf()
    sum += a

for k in range(2,52):
    new_sum += 1/k

print(sum-new_sum)