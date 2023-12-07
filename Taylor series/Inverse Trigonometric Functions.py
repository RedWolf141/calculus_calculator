import math as ma

k = 0
def arcsinx():  # arcsinx, x=1 deg
    a = 0
    try:
        for x in range(15):
            a += ma.factorial(2*x) * ma.pow(ma.pi/180, 2*x+1)/ (ma.pow(4, x) * ma.pow(ma.factorial(x), (2*x)) * ma.pow((ma.pi / 180), 2*x+1))
            k = a - ma.asin(ma.pi/180)
            print(x, "차 근사값 = ", a, "\narcsin 1(deg)과(와)의 차 =", k)
    except:
        print("버퍼 연산자오류")

def arccosx():  # cosx, x=1 deg
    a = 0
    for x in range(5):
        a += ma.pi/2 -  ma.factorial(2*x) * ma.pow(ma.pi/180, 2*x+1) / (ma.pow(4, x) * ma.pow(ma.factorial(x) , (2*x + 1)) * ma.pow((ma.pi / 180), 2*x+1))
        k = a - ma.acos(ma.pi/180)
        print(x, "차 근사값 = ", ma.pi/2 - a, "\ncos 1(deg)과(와)의 차 =", k)


arcsinx()
arccosx()