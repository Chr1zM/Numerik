# a)
import matplotlib.pyplot as plt
import numpy as np


def splines(xs, ys):
    xs, ys = np.asarray(xs), np.asarray(ys)
    assert xs.shape == ys.shape
    h = np.diff(xs)
    A = np.diag(2 * (h[:-1] + h[1:])) + np.diag(h[1:-1], 1) + np.diag(h[1:-1], -1)
    gamma = 6 * (ys[2:] - ys[1:-1]) / h[1:] - 6 * (ys[1:-1] - ys[:-2]) / h[:-1]
    beta = np.zeros((xs.shape[0],))
    beta[1:-1] = np.linalg.solve(A, gamma)
    beta[0] = beta[-1] = 0
    alpha = (ys[1:] - ys[:-1]) / h - h * (beta[1:] + 2 * beta[:-1]) / 6
    coeffs = np.zeros((xs.shape[0] - 1, 4))
    coeffs[:, 0] = ys[:-1]
    coeffs[:, 1] = alpha
    coeffs[:, 2] = beta[:-1] / 2
    coeffs[:, 3] = (beta[1:] - beta[:-1]) / (6 * h)
    return coeffs


def horner_spline(p, xs, x):
    # determine in which interval x lies
    if x <= xs[0]:
        return p[0, 0]
    if x >= xs[-1]:
        x = xs[-1]
    i = np.searchsorted(xs, x, side='left') - 1
    x = x - xs[i]
    p_i = np.flip(p[i])
    y = 0
    for a in p_i:
        y = a + y * x
    return y


def f(x):
    return 1 / (1 + x ** 2) + 0.5


if __name__ == '__main__':
    RES = 1000

    xs = np.array([-3, -1, 0, 1, 3])
    ys = f(xs)
    p = splines(xs, ys)
    xs_plot_real = np.linspace(-3, 3, RES)
    ys_plot_real = f(xs_plot_real)
    ys_plot_spline = np.zeros((RES,))
    for i in range(RES):
        ys_plot_spline[i] = horner_spline(p, xs, xs_plot_real[i])
    plt.plot(xs_plot_real, ys_plot_real, label=f'$f(x)$')
    plt.plot(xs_plot_real, ys_plot_spline, label=f'$interpolation$')
    plt.legend()
    plt.show()

    # b
    fig, axs = plt.subplots(1, 3, figsize=(21, 7))
    axs = axs.flatten()
    for i, M in enumerate((7, 9, 11)):
        xs = np.linspace(-5, 5, M)
        ys = f(xs)
        p = splines(xs, ys)
        xs_plot_real = np.linspace(-5, 5, RES)
        ys_plot_real = f(xs_plot_real)
        ys_plot_spline = np.zeros((RES,))
        for j in range(RES):
            ys_plot_spline[j] = horner_spline(p, xs, xs_plot_real[j])
        axs[i].plot(xs_plot_real, ys_plot_real, label=f'$f(x)$')
        axs[i].plot(xs_plot_real, ys_plot_spline, label=f'$interpolation$')
        axs[i].set_title(f'M={M}')
        axs[i].legend()
    fig.tight_layout()
    fig.show()
