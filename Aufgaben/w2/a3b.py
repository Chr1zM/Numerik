import numpy as np


def vorwaerts(L_, b_):
    n = len(L_)
    y_ = np.zeros(n)
    y_[0] = b_[0]
    for i in range(1, n):
        y_[i] = b_[i] - (sum(L_[i][j] * y_[j] for j in range(i))) / L_[i][i]
    return y_


def rueckwaerts(Lt_, y_):
    n = len(Lt_)
    x_ = np.zeros(n)
    x_[n - 1] = y_[n - 1] / Lt_[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x_[i] = (y_[i] - (sum(Lt_[i][j] * x_[j] for j in range(n - 1, i, -1)))) / Lt_[i][i]
    return x_


def cholesky(A_):
    main_diag_ = A_.diagonal().copy()
    sub_diag_ = A_.diagonal(-1).copy()
    main_diag_[0] = np.sqrt(main_diag_[0])
    for i in range(A_.shape[0] - 1):
        sub_diag_[i] /= main_diag_[i]
        main_diag_[i + 1] = np.sqrt(main_diag_[i + 1] - sub_diag_[i] ** 2)
    return main_diag_, sub_diag_


if __name__ == '__main__':
    for n in [100, 1000, 10000]:
        A = np.diag(np.full(n, 2, dtype=float), 0) + np.diag(np.full(n - 1, -1, dtype=float), 1) + np.diag(
            np.full(n - 1, -1, dtype=float), -1)

        main_diag, sub_diag = cholesky(A)
        b = np.full(n, (-1) / (n + 1) ** 2, dtype=float)
        L = np.diag(main_diag) + np.diag(sub_diag, -1)
        y = vorwaerts(L, b)  # Ly = b
        x = rueckwaerts(L.T, y)  # L^T x = y
        print(f"{n=}: {x.T=}")
