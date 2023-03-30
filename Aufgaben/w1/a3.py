import math
import matplotlib.pyplot
import numpy


def rechteckSum(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + i * h) for i in range(n))


def trapezregel(f, a, b, n):
    h = (b - a) / n
    return h / 2 * (f(a) + 2 * sum(f(a + i * h) for i in range(1, n)) + f(b))


def plotFunctions(f1, f2):
    res = numpy.array([rechteckSum(f1, 1 / 10, 10, n) for n in range(1, 50)])
    resAlt = numpy.array([trapezregel(f1, 1 / 10, 10, n) for n in range(1, 50)])

    matplotlib.pyplot.plot(range(1, 50), res, label="rechteckSum")
    matplotlib.pyplot.plot(range(1, 50), resAlt, label="trapezregel")
    matplotlib.pyplot.ylabel("f(x)")
    matplotlib.pyplot.xlabel("n")
    matplotlib.pyplot.legend(["rechteckSum", "trapezregel"])
    matplotlib.pyplot.show()

    res = numpy.array([rechteckSum(f2, 1, 2, n) for n in range(1, 50)])
    resAlt = numpy.array([trapezregel(f2, 1, 2, n) for n in range(1, 50)])

    matplotlib.pyplot.plot(range(1, 50), res, label="rechteckSum")
    matplotlib.pyplot.plot(range(1, 50), resAlt, label="trapezregel")
    matplotlib.pyplot.ylabel("f(x)")
    matplotlib.pyplot.xlabel("n")
    matplotlib.pyplot.legend(["rechteckSum", "trapezregel"])
    matplotlib.pyplot.show()


f1 = lambda x: 1 / (x ** 2)
f2 = lambda x: math.log(x)

f1resExact = 9.9
f2resExact = 0.38629

print("Exakte Werte:")
print("f1: " + str(f1resExact))
print("f2: " + str(f2resExact) + "\n")

for n in [10, 50, 100, 500]:
    print("n = " + str(n))

    print("f1: rechteck=" + str(rechteckSum(f1, 1 / 10, 10, n)))
    print("f1: trapez=" + str(trapezregel(f1, 1 / 10, 10, n)))
    print("---------------------------------")

print("\n")

for n in [10, 50, 100, 500]:
    print("n = " + str(n))
    print("f2: rechteck=" + str(rechteckSum(f2, 1, 2, n)))
    print("f2: trapez=" + str(trapezregel(f2, 1, 2, n)))
    print("---------------------------------")

plotFunctions(f1, f2)
