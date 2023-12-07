from sympy import *

x = Symbol('x')

f = (ln(3+x) + ln(3-x)) / 2

a = integrate(f,(x,-2,2))

print(a)