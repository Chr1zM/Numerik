import numpy
import matplotlib.pyplot
import math


def exp(x, n):
    return sum(math.pow(x, k) / math.factorial(k) for k in range(n + 1))


def expAlt(x, n):
    return sum(math.pow(x, n - k) / math.factorial(n - k) for k in range(n + 1))


for x in [1, 2, 5, 20]:
    res = numpy.array([exp(x, n) for n in range(1, 40)])
    resAlt = numpy.array([expAlt(x, n) for n in range(1, 40)])

    matplotlib.pyplot.plot(range(1, 40), res, label="exp", linewidth=4, color='r')
    matplotlib.pyplot.plot(range(1, 40), resAlt, label="expAlt", color='blue')
    matplotlib.pyplot.ylabel("f(x)")
    matplotlib.pyplot.xlabel("n")
    matplotlib.pyplot.legend(["exp", "expAlt"])
    matplotlib.pyplot.show()
