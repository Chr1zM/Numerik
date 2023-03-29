import math


def pqFormel(p, q):
    d = math.sqrt(p * p + q)
    return -p - d, -p + d


def pqFormelAlt(p, q):
    x1 = -p - math.sqrt(p * p + q)
    x2 = -q / x1
    return x1, x2


q = 1
for p in [math.pow(10, 2), math.pow(10, 4), math.pow(10, 6), math.pow(10, 7), math.pow(10, 8)]:
    result = pqFormel(p, q)
    altResult = pqFormelAlt(p, q)
    print("pq: x1=" + str(result[0]) + " x2=" + str(result[1]))
    print("pqAlt: x1=" + str(altResult[0]) + " x2=" + str(altResult[1]))
    print("diff: (" + str(result[0]-altResult[0]) + ", " + str(result[1]-altResult[1]) + ")\n")
