import sympy as sp

x = sp.Symbol('x')

a = sp.limit((sp.Pow(sp.tan(x),2) + sp.tan(4*x*x)) / sp.ln(1+2*x*x),x,0)

