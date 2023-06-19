import math
import numpy as np


def f(x):
    assert x.shape == (2,)
    term1 = math.sin(x[0]) - x[1]
    term2 = math.exp(-x[1]) - x[0]
    return term1 ** 2 + term2 ** 2


def f_deriv(x):
    assert x.shape == (2,)
    x_1 = math.cos(x[0]) * 2 * (math.sin(x[0]) - x[1]) - 2 * (math.exp(-x[1]) - x[0])
    x_2 = -2 * (math.sin(x[0]) - x[1]) - 2 * math.exp(-x[1]) * (math.exp(-x[1]) - x[0])
    return np.array([x_1, x_2])


def armijo(f, f_deriv, x_start, alpha=1, rho=0.5, tau=0.5, epsilon_deriv=1e-4, max_iter=1e3):
    def lambda_func(x, p, rho, alpha):
        return f(x) + (f_deriv(x) @ p) * rho * alpha

    def phi_func(x, p, alpha):
        return f(x + alpha * p)

    x = x_start
    p = -f_deriv(x)
    i = 0
    while np.max(np.abs(p)) > epsilon_deriv and i < max_iter:
        i += 1
        alpha = 1
        while phi_func(x, p, alpha) > lambda_func(x, p, rho, alpha):
            alpha = tau * alpha
        x = x + alpha * p
        p = -f_deriv(x)
    print(f'Iterations: {i}')
    return x


if __name__ == '__main__':
    initial_points = [(5, 2), (6, 2), (-1, -1), (-2, -2)]
    for x_0 in initial_points:
        x_0 = np.array(x_0)
        x_opt = armijo(f, f_deriv, x_0)
        print(f'x_opt: {x_opt} \t')
