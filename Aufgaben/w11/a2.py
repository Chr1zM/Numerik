import math
import numpy as np
from scipy.integrate import quad


def trapez(f_, a_, b_, n_trapez_):
    h = (b_ - a_) / n_trapez_
    s = 0.5 * (f_(a_) + f_(b_))
    for i in range(1, n_trapez_):
        s += f_(a_ + i * h)
    return s * h


def extrapolation(f_, a_, b_, sizes_):
    steps = sizes_.shape[0]
    ls = 1 / sizes_
    ls = np.asarray(ls)
    ts = np.array([trapez(f_, a_, b_, i) for i in sizes_])
    ps = np.zeros((steps, steps))
    ps[:, 0] = ts
    for i in range(1, steps):
        for j in range(1, i + 1):
            ps[i, j] = ps[i, j - 1] + (ps[i, j - 1] - ps[i - 1, j - 1]) / ((ls[i - j] / ls[i]) ** 2 - 1)
    return ps[steps - 1, steps - 1]


def romberg(f_, a_, b_, q_):
    return extrapolation(f_, a_, b_, np.array([2 ** i for i in range(q_ + 1)], dtype=int))


def bulirsch(f_, a_, b_, q_):
    ls = [1]
    if q_ > 1:
        ls.append(2)
    if q_ > 2:
        ls.append(3)
    if q_ > 3:
        for i in range(3, q_):
            ls.append(ls[i - 2] * 2)
    ls = np.array(ls)
    return extrapolation(f_, a_, b_, ls)


f = lambda x: math.sin(math.pi * x ** 2)

if __name__ == '__main__':
    exact_val = quad(f, -1, 1)[0]

    for order in (2, 4, 6, 8, 10, 12, 14, 16):
        q = order // 2
        print(f"Ordnung: {order}")
        print(f"romberg: {romberg(f, -1, 1, q)} error: {abs(exact_val - romberg(f, -1, 1, q))}")
        print(f"bulirsch: {bulirsch(f, -1, 1, q)} error: {abs(exact_val - bulirsch(f, -1, 1, q))}")
