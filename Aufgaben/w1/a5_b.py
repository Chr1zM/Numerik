import math


def heron(k, x, x0):
    if k == 0:
        return math.sqrt(x0)
    yk_1 = heron(k - 1, x, x0)
    return 0.5 * (yk_1 + (x / yk_1))


def anz_schritte(x, x0):
    eps = 0.005
    i = 0
    while True:
        i += 1
        diff = abs(exact - heron(i, x, x0))
        if diff < eps:
            break
    return i


x = 2
exact = math.sqrt(x)
res1 = heron(50, x, 1)
res2 = heron(50, x, 4)

print("Differenz zum exakten x_0=1: " + str(abs(res1 - exact)))
print("Differenz zum exakten Wert x_0=4: " + str(abs(res2 - exact)))

print("5a.2: mit x=2 und x_0=1: " + str(anz_schritte(x, 1)) + " Schritte werden benötigt.")
print("5a.2: mit x=2 und x_0=1: " + str(anz_schritte(x, 4)) + " Schritte werden benötigt.")
