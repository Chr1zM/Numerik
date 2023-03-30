import math


def pqFormel(p, q):
    d = math.sqrt(p * p + q)
    return max(-p - d, -p + d)


def pqFormelAlt(p, q):
    x1 = -p - math.sqrt(p * p + q)
    x2 = -q / x1
    return max(x1, x2)


q = 1
for p in [math.pow(10, 2), math.pow(10, 4), math.pow(10, 6), math.pow(10, 7), math.pow(10, 8)]:
    result = pqFormel(p, q)
    altResult = pqFormelAlt(p, q)
    print("pq: x=" + str(result))
    print("pqAlt: x=" + str(altResult))
    print("diff: " + str(abs(result-altResult)) + "\n")
