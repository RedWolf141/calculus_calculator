import sympy as sp

x= sp.Symbol("x")
y = sp.Symbol("y")

def fx():
    f = sp.Pow(2, sp.ln(x)) + x
    fp = sp.diff(f)
    a = 1 / fp.subs(1)
    print(a)

##def inverse_fx():
##    f = sp.Pow(2, sp.ln(x) + x)
##    y = f(x)
##    inf = f^(-1)(y)
##    a = 1 / inf.subs(2)
 ##   print(a)


inverse_fx()