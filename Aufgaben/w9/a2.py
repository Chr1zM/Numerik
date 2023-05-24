# a)
import matplotlib.pyplot as plt
import numpy as np
import math


def dividierte_differenzen(xs, ys):
    xs, ys = np.asarray(xs), np.asarray(ys)
    assert xs.shape == ys.shape
    dd = np.zeros((xs.shape[0], xs.shape[0]))
    dd[:, 0] = ys
    for i in range(1, xs.shape[0]):
        dd[i:, i] = (dd[i:, i - 1] - dd[i - 1:-1, i - 1]) / (xs[i:] - xs[:-i])
    return np.diag(dd)


def horner_dd(dd, xs, x, i):
    dd, xs = np.asarray(dd), np.asarray(xs)
    q = np.full((xs.shape[0],), np.nan)
    q[0] = dd[-1]
    for i in range(xs.shape[0] - 2, -1, -1):
        q[-i - 1] = dd[i] + (x - xs[i]) * q[-i - 2]
    return q[-1]


# b)

def f(x):
    return 1 / (1 + x ** 2)


if __name__ == '__main__':
    # Aufgabe a)
    print("Aufgabe 2a:")
    xs, ys = [0, 1, 3], [3, 2, 6]
    dd = dividierte_differenzen(xs, ys)
    print(f"dd={dd}")
    q = horner_dd(dd, xs, 2, dd.shape[0] - 1)
    print(f"q={q}")

    # Aufgabe b)
    RES = 1000

    fig, axs = plt.subplots(1, 3, figsize=(21, 7))
    axs = axs.flatten()
    for i, M in enumerate((7, 9, 11)):
        xs = np.linspace(-5, 5, M)
        ys = f(xs)
        dd = dividierte_differenzen(xs, ys)
        xs_plot = np.linspace(-5, 5, RES)
        ys_plot_f = f(xs_plot)
        ys_plot_ipol = np.zeros((RES,))
        for j in range(RES):
            ys_plot_ipol[j] = horner_dd(dd, xs, xs_plot[j], dd.shape[0] - 1)
        axs[i].plot(xs_plot, ys_plot_f, label=f'$f(x)$')
        axs[i].plot(xs_plot, ys_plot_ipol, label=f'$interpolation$')
        axs[i].set_title(f'M={M}')
        axs[i].legend()
    fig.tight_layout()
    fig.show()

    # Aufgabe c)
    fig, axs = plt.subplots(1, 3, figsize=(21, 7))
    axs = axs.flatten()
    for i, M in enumerate((7, 9, 11)):
        xs = np.array([-5 * math.cos(math.pi * (2 * i + 1) / (2 * M)) for i in range(M)])
        ys = f(xs)
        dd = dividierte_differenzen(xs, ys)
        xs_plot = np.linspace(-5, 5, RES)
        ys_plot_f = f(xs_plot)
        ys_plot_ipol = np.zeros((RES,))
        for j in range(RES):
            ys_plot_ipol[j] = horner_dd(dd, xs, xs_plot[j], dd.shape[0] - 1)
        axs[i].plot(xs_plot, ys_plot_f, label=f'$f(x)$')
        axs[i].plot(xs_plot, ys_plot_ipol, label=f'$interpolation$')
        axs[i].set_title(f'M={M}')
        axs[i].legend()
    fig.tight_layout()
    fig.show()
