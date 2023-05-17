import math

from Aufgaben.w8.a1 import newton


def newton_q(f, f_deriv, x, q, epsilon):
    x_prev = float('inf')
    f_x = f(x)
    i = 0
    while abs(x - x_prev) > epsilon and abs(f_x) > epsilon:
        i += 1
        x_prev = x
        f_x = f(x)
        x = x - q * f_x / f_deriv(x)
    return x, i


def newton_g(f, f_deriv, f_2deriv, x, epsilon):
    x_prev = float('inf')
    f_x = f(x)
    i = 0
    while abs(x - x_prev) > epsilon and abs(f_x) > epsilon:
        i += 1
        x_prev = x
        f_x = f(x)
        f_deriv_x = f_deriv(x)
        f_2deriv_x = f_2deriv(x)
        x = x - (f_x * f_deriv_x) / (f_deriv_x ** 2 - f_x * f_2deriv_x)
    return x, i


def f(x):
    return math.atan(x) - x


def f_deriv(x):
    return 1 / (1 + x ** 2) - 1


def f_2deriv(x):
    return -2 * x / (1 + x ** 2) ** 2


if __name__ == '__main__':
    eps = 1e-11
    x_nwtn_q, i_nwt_q = newton_q(f, f_deriv, 1, 3, epsilon=eps)  # q = 3, da 0 dreifache Nullstelle
    x_nwtn, i_nwt = newton(f, f_deriv, 1, epsilon=eps)
    x_nwtn_g, i_nwt_g = newton_g(f, f_deriv, f_2deriv, 1, epsilon=eps)

    print(f"Newton: x={x_nwtn}, f(x)={f(x_nwtn)}, iterations={i_nwt}")
    print(f"Newton_q: x={x_nwtn_q}, f(x)={f(x_nwtn_q)}, iterations={i_nwt_q}")
    print(f"Newton_g: x={x_nwtn_g}, f(x)={f(x_nwtn_g)}, iterations={i_nwt_g}")
