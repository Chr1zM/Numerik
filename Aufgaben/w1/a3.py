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
    resf1 = numpy.array([rechteckSum(f1, 1 / 10, 10, n) for n in range(1, 100)])
    resAltf1 = numpy.array([trapezregel(f1, 1 / 10, 10, n) for n in range(1, 100)])

    matplotlib.pyplot.plot(range(1, 100), resf1, label="rechteckSum")
    matplotlib.pyplot.plot(range(1, 100), resAltf1, label="trapezregel")
    matplotlib.pyplot.ylabel("f(x)")
    matplotlib.pyplot.xlabel("n")
    matplotlib.pyplot.legend(["rechteckSum", "trapezregel"])
    matplotlib.pyplot.show()

    resf2 = numpy.array([rechteckSum(f2, 1, 2, n) for n in range(1, 100)])
    resAltf2 = numpy.array([trapezregel(f2, 1, 2, n) for n in range(1, 100)])

    matplotlib.pyplot.plot(range(1, 100), resf2, label="rechteckSum")
    matplotlib.pyplot.plot(range(1, 100), resAltf2, label="trapezregel")
    matplotlib.pyplot.ylabel("f(x)")
    matplotlib.pyplot.xlabel("n")
    matplotlib.pyplot.legend(["rechteckSum", "trapezregel"])
    matplotlib.pyplot.show()


f1 = lambda x: 1 / (x ** 2)
f2 = lambda x: numpy.log(x)

f1resExact = 9.9
f2resExact = 0.38629

print("Exakte Werte:")
print("f1: " + str(f1resExact))
print("f2: " + str(f2resExact) + "\n")


def printResult(f, a, b, exact):
    for n in [10, 50, 100, 500, 1000]:
        res1 = rechteckSum(f, a, b, n)
        res2 = trapezregel(f, a, b, n)
        print("n = " + str(n))
        print("rechteck=" + str(res1))
        print("diff: " + str(math.fabs(res1 - exact)))
        print("trapez=" + str(res2))
        print("diff: " + str(math.fabs(res2 - exact)))
        print("---------------------------------")
    print("\n")


print("f1: 1 / x^2")
printResult(f1, 1 / 10, 10, f1resExact)
print("f2: Log(x)")
printResult(f2, 1, 2, f2resExact)
plotFunctions(f1, f2)
