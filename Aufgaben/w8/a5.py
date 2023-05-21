import numpy as np
import math

epsilon = 1e-6


def newton_method(f_fun_, f_diff_fun_, x_k_):
    k_ = 0
    x_k_minus_1_ = np.full(x_k_.shape, float('inf'))

    while np.linalg.norm(x_k_ - x_k_minus_1_) > epsilon and np.linalg.norm(f_fun_(x_k_)) > epsilon:
        x_k_minus_1_ = x_k_
        x_k_ = x_k_ - np.linalg.solve(f_diff_fun_(x_k_), f_fun_(x_k_))
        k_ += 1

    return x_k_, k_


if __name__ == '__main__':
    f = lambda x: np.array([math.sin(x[0]) - x[1], math.exp(-x[1]) - x[0]])
    f_diff = lambda x: np.array([[math.cos(x[0]), -1], [-1, -math.exp(-x[1])]])
    x_k, k = newton_method(f, f_diff, np.array([1, 1]))
    print(20 * "-" + f" Newton-Verfahren für Vektoren der Dimension {x_k} " + 20 * "-")
    print(f"steps={k}")
    print(f"x_k={x_k}")
    print(f"f(x_k)={f(x_k)}")
