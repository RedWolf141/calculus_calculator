import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

def f(x):
    return np.exp(x)*np.sin(x)

x = sp.Symbol('x')
fx = sp.exp(x)*sp.sin(x)
true_integral = sp.N(sp.integrate(fx,(x,0,sp.pi)))
print("True value:", sp.N(sp.integrate(fx,(x,0,sp.pi))))

a = 0
b = np.pi
n = 16

n_list = np.zeros((5,1))
error_list = np.zeros((5,1))

for k in range(5):
    x = np.linspace(a,b,n+1)
    h = x[1] - x[0]
    sum = f(x[0])
    for i in range(np.size(x)-1):
        if i%2 == 0:
            sum = sum+4*f(x[i])
        else:
            sum = sum+2*f(x[i])
    sum = sum + f(x[n])
    sum = sum*h/3
    error = abs(true_integral-sum)
    n_list[k]=n
    error_list[k] = error
    print("simpson with n=",n,":",sum,"error:",error)

    n = n*2

plt.plot(np.log2(n_list),np.log2(error_list),'o-')
plt.xlabel(r'$log_2(n)$')
plt.ylabel(r'$log_2(error)$')
plt.show()

