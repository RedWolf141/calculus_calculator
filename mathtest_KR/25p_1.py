import math
import matplotlib.pyplot as plt
a = 0
t =[]

for x in range(1,15):
    a += 1/((x) * (x+1))
    a += 1 / ((x+1) * (x+2))
    # an = 1/ x * (x+1) + 1/(x+1) * (x+2)를 구현
    t.append(a)

plt.plot(t)
plt.title(" 25p 1")
# 급수 t를 그래프로 표현
plt.show()
# 그래프 띄우기