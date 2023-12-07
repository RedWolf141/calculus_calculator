from sympy import *

x = Symbol('x')
y = Symbol('y')
t = Symbol('t')
dx_dt = diff(4*exp(t), t)
dy_dt = diff(2*t - exp(2*t), t)

f = Pow(Pow(dx_dt,2)+Pow(dy_dt,2),0.5)
s = integrate(f,(t,ln(2),ln(4))).doit()

print(s)