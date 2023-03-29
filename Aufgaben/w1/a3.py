import math


def rechteckSum(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + i * h) for i in range(n))


# komische Werte bei Trapezregel..
def trapezregel(f, a, b, n):
    h = (b - a) / n
    return (h / 2) * (f(a) + 2 * sum(f(a + i * h) + f(b) for i in range(n)))


f1 = lambda x: 1 / (x ** 2)
f2 = lambda x: math.log2(x)

f1resExact = 9.9
f2resExact = 0.38629

print("Exakte Werte:")
print("f1: " + str(f1resExact))
print("f2: " + str(f2resExact) + "\n")

for n in [100, 200, 500, 1000, 10000, 100000]:
    print("n = " + str(n))

    print("f1: rechteck=" + str(rechteckSum(f1, 1 / 10, 10, n)))
    print("f1: trapez=" + str(trapezregel(f1, 1 / 10, 10, n)))
    print("---------------------------------")

for n in [1, 5, 10, 20, 50, 100, 200, 500, 1000, 10000, 100000]:
    print("n = " + str(n))
    print("f2: rechteck=" + str(rechteckSum(f2, 1, 2, n)))
    print("f2: trapez=" + str(trapezregel(f2, 1, 2, n)))
    print("---------------------------------")
