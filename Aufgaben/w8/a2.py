import math


def a_posteriori_error(x_prev, x, alpha_): return alpha_ / (1 - alpha_) * abs(x - x_prev)


def newton_apost(f, f_deriv, x, a_post, eps_):
    x_prev = float('inf')
    f_x = f(x)
    i = 0
    while a_post(x_prev, x) > eps_:
        i += 1
        x_prev = x
        f_x = f(x)
        x = x - f_x / f_deriv(x)
    return x, i


def f(x): return x + math.log(x) - 2


def f_deriv(x): return 1 + 1 / x


if __name__ == '__main__':
    alpha = 0.25
    eps = 1e-6

    x_nwtn, i_nwtn = newton_apost(f, f_deriv, 1, lambda x_prev, x: a_posteriori_error(x_prev, x, alpha), eps)
    print(f"Newton: x={x_nwtn}, f(x)={f(x_nwtn)}, iterations={i_nwtn}")
