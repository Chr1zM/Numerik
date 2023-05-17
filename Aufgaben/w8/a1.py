import math
import timeit


def sekanten(f, x_prev, x_next, epsilon=1e-12):
    f_prev = f(x_prev)
    i = 0
    while abs(x_next - x_prev) > epsilon and abs(f_prev) > epsilon:
        i += 1
        f_next = f(x_next)
        x_next, x_prev = x_next - f_next * (x_next - x_prev) / (f_next - f_prev), x_next
        f_prev = f_next
    return x_next, i


def newton(f, f_deriv, x, epsilon=1e-12):
    x_prev = float('inf')
    f_x = f(x)
    i = 0
    while abs(x - x_prev) > epsilon and abs(f_x) > epsilon:
        i += 1
        x_prev = x
        f_x = f(x)
        x = x - f_x / f_deriv(x)
    return x, i


def pop(x):
    a = 9.8606
    c = -1.1085e25
    d = 0.029
    return a / (1 - c * math.exp(-d * x))


def pop_deriv(x):
    a = 9.8606
    c = -1.1085e25
    d = 0.029
    exp = math.exp(-d * x)
    return -a * c * d * exp * (1 - c * exp) ** -2


if __name__ == '__main__':
    eps = 1.1e-14
    x_sek, i_sek = sekanten(lambda x: pop(x) - 9, 1961, 2000, epsilon=eps)
    x_nwt, i_nwt = newton(lambda x: pop(x) - 9, pop_deriv, 1961, epsilon=eps)
    print(f"Sekanten: x={x_sek}, f(x)={pop(x_sek)}, iterations={i_sek} ")
    print(f"Newton: x={x_nwt}, f(x)={pop(x_nwt)}, iterations={i_nwt}")

    sekanten_time = timeit.timeit(lambda: sekanten(lambda x: pop(x) - 9, 1961, 2000, epsilon=eps), number=1)

    newton_time = timeit.timeit(lambda: newton(lambda x: pop(x) - 9, pop_deriv, 1961, epsilon=eps), number=1)

    print(f"Sekanten time: {sekanten_time} seconds")
    print(f"Newton time: {newton_time} seconds")
