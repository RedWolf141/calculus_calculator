import math as ma
import matplotlib.pyplot as plt
a=0
x=[]
for x in range(15):
    a += ma.pow(2, x) / ma.factorial(x)
    x.append(a)
    k = ma.exp(2) - a
    print(x, "차 근사값 = ",a, "\ne^2과의 차 =",k)

print(x)
# e^x