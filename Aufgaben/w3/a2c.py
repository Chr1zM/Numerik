import numpy as np


def zerlegung(a_):
    matrix_ = np.array(a_)
    n = len(matrix_)
    p_ = []

    for i in range(n - 1):
        if matrix_[i][i] != 0:
            p_.append(i + 1)
        else:
            for j in range(i + 1, n):
                if matrix_[j][i] != 0:  # nächste nicht null zeile finden und tauschen
                    matrix_[[i, j]] = matrix_[[j, i]]
                    p_.append(j + 1)
                    break

        for j in range(i + 1, n):
            factor = matrix_[j][i] / matrix_[i][i]
            matrix_[j][i] = factor
            for k in range(i + 1, n):
                matrix_[j][k] -= factor * matrix_[i][k]
    return matrix_, p_


def permutation(p_, b_):
    n = len(b_)
    c_ = np.copy(b_)
    for i in range(1, n):
        if p_[i - 1] != i:
            c_[[p_[i - 1] - 1, i - 1]] = c_[[i - 1, p_[i - 1] - 1]]
    return c_


def vorwaerts(LU_, c_):
    n = len(LU_)
    y_ = np.zeros(n)
    y_[0] = c_[0]
    for i in range(1, n):
        y_[i] = c_[i] - (sum(LU_[i][j] * y_[j] for j in range(i)))
    return y_


def rueckwaerts(LU_, y_):
    n = len(LU_)
    x_ = np.zeros(n)
    x_[n - 1] = y_[n - 1] / LU_[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x_[i] = (y_[i] - (sum(LU_[i][j] * x_[j] for j in range(n - 1, i, -1)))) / LU_[i][i]
    return x_


def sherman_morrison(A_, b_, u_, v_):
    # LU zerlegung
    LU, p = zerlegung(A_)
    u_perm = permutation(p, u_)
    y = vorwaerts(LU, u_perm)
    z = rueckwaerts(LU, y)

    if (1 + v_.T @ z) == 0:
        raise ArithmeticError('1 + v^T z = 0')
    alpha = 1 / (1 + v_.T @ z)
    b_perm = permutation(p, b_)
    y_hat = vorwaerts(LU, b_perm)
    z_hat = rueckwaerts(LU, y_hat)
    x_hat = z_hat - alpha * (v_.T @ z_hat) * z
    return x_hat


if __name__ == '__main__':
    A = np.array([
        [0, 0, 0, 1],
        [2, 1, 2, 0],
        [4, 4, 0, 0],
        [2, 3, 1, 0]
    ])
    b = np.array([3, 5, 4, 5])
    v = np.array([0, 0, 0, 1])
    u = np.array([0, 1, 2, 3])
    print(sherman_morrison(A, b, v, u))
