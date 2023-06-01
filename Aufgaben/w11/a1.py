import math

import numpy as np


def trapez(f, a, b, n_trapez):
    h = (b - a) / n_trapez
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n_trapez):
        s += f(a + i * h)
    return s * h


def simpson(f, a, b, n_simpson):
    h = (b - a) / n_simpson
    s = f(a) + f(b)
    for i in range(1, n_simpson):
        s += 2 * f(a + i * h) if i % 2 == 0 else 4 * f(a + i * h)
    return (s - f(a) - f(b)) * (h / 3)


def g2(f, a, b):
    xs = np.array([-math.sqrt(3 / 5), 0, math.sqrt(3 / 5)])
    betas = np.array([5 / 9, 8 / 9, 5 / 9])
    xs_ = (b - a) / 2 * xs + (b + a) / 2
    betas_ = (b - a) / 2 * betas
    return np.sum(betas_ * f(xs_))


if __name__ == '__main__':
    exact_value = math.pi / 4
    trapez_value = trapez(lambda x: 1 / (1 + x ** 2), 0, 1, 8)
    simpson_value = simpson(lambda x: 1 / (1 + x ** 2), 0, 1, 4)
    g2_value = g2(lambda x: 1 / (1 + x ** 2), 0, 1)

    print(f"exact value: {exact_value}\n"
          f"trapez value: {trapez_value} \t\t error: {abs(exact_value - trapez_value)}\n"
          f"simpson value: {simpson_value} \t\t error: {abs(exact_value - simpson_value)}\n"
          f"g2 value: {g2_value} \t\t error: {abs(exact_value - g2_value)}")
