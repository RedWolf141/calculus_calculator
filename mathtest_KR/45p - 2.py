import sympy as sp


x = sp.Symbol('x')
#f(x) = x / (tanx+cotx)
f = x / (sp.tan(x) + sp.cot(x))

#f'(x)를 구함
fp = sp.diff(x)

# f (pi/4) = a를 구현함
a = f.subs(x,sp.pi/4)

newf = (f - a) / (x- sp.pi/4)
b = sp.Limit(newf,x,sp.pi/4).doit()
print(a,b, b/a)
