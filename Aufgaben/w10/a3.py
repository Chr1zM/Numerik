import matplotlib.pyplot as plt
import numpy as np


def get_tsvd_index(s, alpha):
    return np.argmax(s[0] / s[1:] > 1 / alpha)


if __name__ == '__main__':
    gamma = 0.05
    n = 100
    c = 1 / (gamma * np.sqrt(2 * np.pi))

    A = c / n * np.exp(-((np.arange(n)[:, None] - np.arange(n)) / (np.sqrt(2) * n * gamma)) ** 2)

    x = np.zeros(n)
    x[45:56] = 1
    x[60:66] = 1 / 2

    b = A @ x
    b_ = b + np.random.randn(n) / 1e-6

    u, s, vt = np.linalg.svd(A)
    ind = get_tsvd_index(s, 1e-2)
    sigma_ = 1 / s
    sigma_[ind:] = 0
    x_ = vt.T @ np.diag(sigma_) @ u.T @ b

    fig, axs = plt.subplots(3, 3, figsize=(16, 16))

    for i, alpha in enumerate(10 ** (-k) for k in range(9)):
        ind = get_tsvd_index(s, alpha)
        sigma_[:ind] = 1 / s[:ind]
        sigma_[ind:] = 0
        x_ = vt.T @ np.diag(sigma_) @ u.T @ b
        axs.flatten()[i].plot(x_)
        axs.flatten()[i].set_title(f'$\\alpha$={alpha}')

    plt.show()
