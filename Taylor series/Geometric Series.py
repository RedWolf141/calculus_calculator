import math as ma


def Geo1(): # 1/(1-x) , x = 0.1
    a = 0
    for x in range(15):
        a += ma.pow(0.1,x)
        k = 1/0.9 - a
        print(x, "차 근사값 = ", a, "\n1/(1-x)과(와)의 차 =", k)

def Geo2(): # x / (1-x)^2, x= 0.1
    a = 0
    for x in range(15):
        a += x * ma.pow(0.1, x)
        k = 0.1 / ma.pow(0.9, 2)
        print(x, "차 근사값 = ", a, "\nx / (1-x)^2 과(와)의 차 =", k)
def Geo3(): # 2x^2 / (1-x)^3, x=0.1
    a = 0
    for x in range(15):
        a += x * (x-1) * ma.pow(0.1, x)
        k = 0.02 / ma.pow(0.9, 3)
        print(x, "차 근사값 = ", a, "\n2x^2 / (1-x)^3 과(와)의 차 =", k)
Geo1()
Geo2()
Geo3()