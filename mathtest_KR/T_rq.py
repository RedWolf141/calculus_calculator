import sympy as sp
import numpy as np
import matplotlib.pyplot as plt



x = sp.Symbol('x')
f = sp.limit(sp.ln(x) * x, x, 0, dir="+")


print(f)

