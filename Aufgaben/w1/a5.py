import math

import numpy
import sys
sys.setrecursionlimit(10**7)


def sqrtAbleitung(i, ai, x, x0):
    if i == 0:
        return ai
    else:
        ai = (3 / (2 * i) - 1) * (x / x0 - 1) * sqrtAbleitung(i, ai-1, x, x0)
        return sqrtAbleitung(i - 1, ai, x, x0) + ai


def anzSchritte(ai, x, x0):
    eps = 0.05
    i = 10
    while True:
        diff = math.fabs(exact - sqrtAbleitung(i, ai, x, x0))
        i = i + 1
        if diff < eps:
            break
    return i


x = 2
exact = math.sqrt(x)
res1 = sqrtAbleitung(10, 1, x, 1)
res2 = sqrtAbleitung(10, 2, x, 4)

print("Wurzelannäherung mit i=500, ai=1, x=2 und x_0=1: \n" + str(res1))
print("Wurzelannäherung mit i=500, ai=1, x=2 und x_0=4: \n" + str(res2))

#print("5a.2: mit ai=1, x=2 und x_0=1:" + str(anzSchritte(1, x, 1)) + " Schritte werden benötigt.")
print("5a.2: mit ai=1, x=2 und x_0=1:" + str(anzSchritte(1, x, 4)) + " Schritte werden benötigt.")
