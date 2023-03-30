import math


def a_k(k, x, x0):
    if k == 0:
        return math.sqrt(x0)
    return (3 / (2 * k) - 1) * (x / x0 - 1) * a_k(k - 1, x, x0)


def y_k(k, x, x0):
    if k == 0:
        return math.sqrt(x0)
    return y_k(k - 1, x, x0) + a_k(k, x, x0)


def anzSchritte(x, x0):
    eps = 0.005
    i = 0
    while True:
        diff = math.fabs(exact - y_k(i, x, x0))
        i += 1
        if diff < eps:
            break
    return i


x = 2
exact = math.sqrt(x)
res1 = y_k(100, x, 1)
res2 = y_k(100, x, 4)

print("exact=" + str(exact))
print("Wurzelannäherung mit i=500, ai=1, x=2 und x_0=1: " + str(res1))
print("Wurzelannäherung mit i=500, ai=1, x=2 und x_0=4: " + str(res2))

print("5a.2: mit ai=1, x=2 und x_0=1: " + str(anzSchritte(x, 1)) + " Schritte werden benötigt.")
print("5a.2: mit ai=1, x=2 und x_0=1: " + str(anzSchritte(x, 4)) + " Schritte werden benötigt.")
