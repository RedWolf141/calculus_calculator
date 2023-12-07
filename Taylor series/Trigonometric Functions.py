import math as ma


def sinx(): # sinx, x=1 deg
    a = 0
    for x in range(15):
        a += ma.pow(-1, x) / ma.factorial(2*x+1) * ma.pow((ma.pi / 180), 2*x+1)
        k =a - ma.sin(ma.pi/180)
        print(x, "차 근사값 = ", a, "\nsin 1(deg)과(와)의 차 =", k)

def cosx(): # cosx, x=1 deg
    a = 0
    for x in range(15):
        a += ma.pow(-1, x) / ma.factorial(2*x) * ma.pow((ma.pi / 180), 2*x)
        k = a - ma.cos(ma.pi/180)
        print(x, "차 근사값 = ", a, "\ncos 1(deg)과(와)의 차 =", k)

def tanx(): # 2x^2 / (1-x)^3, x=0.1
    a = 0
    for x in range(15):
        a += x * (x-1) * ma.pow(0.1, x)
        k = 0.02 / ma.pow(0.9, 3)
        print(x, "차 근사값 = ", a, "\n2x^2 / (1-x)^3 과(와)의 차 =", k)
sinx()
cosx()