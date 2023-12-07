import math as ma


def logOneminus(): # log(1-x)
    a = 0
    for x in range(1,15):
        a += -1 * (ma.pow(0.8, x) / x)
        k = ma.log10(0.2) - a
        print(x, "차 근사값 = ", a, "\nlog (1-x)과(와)의 차 =", k)
def logOnePlus(): # log(1+x)
    a = 0
    for x in range(1,15):
        a += ma.pow(-1, x+1) * ma.pow(0.1, x) / x
        k = ma.log10(1.1) - a
        print(x, "차 근사값 = ", a, "\nlog (1+x)과(와)의 차 =", k)
logOneminus()
logOnePlus()