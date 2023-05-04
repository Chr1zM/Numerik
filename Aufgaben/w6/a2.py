import numpy as np


def zerlegung(a_, pivot):
    matrix_ = np.array(a_)
    n = len(matrix_)
    p_ = []

    for i in range(n - 1):
        if pivot:
            max_index = np.argmax(np.abs(matrix_[i:, i])) + i  # pivot zeile finden und tauschen
            if max_index != i:
                p_.append(max_index + 1)
                matrix_[[i, max_index]] = matrix_[[max_index, i]]
            else:
                p_.append(i + 1)
        else:
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

# Ab hier neuer Code (Nachiteration Umsetzung)
def solve_pk(LU_, p_, rk_):
    c = permutation(p_, rk_)
    y = vorwaerts(LU_, c)
    pk = rueckwaerts(LU_, y)
    return pk

def nachiteration(x_, LU_, p_, a_, b_, eps):
    m = np.copy(LU_)
    p = np.copy(p_)
    x = x_
    k = 0
    while True:
        k += 1
        rk = np.subtract(b_, a_ @ x)
        pk = solve_pk(m, p, rk)
        x += pk
        if (np.linalg.norm(pk) / np.linalg.norm(x)) < eps:
            return x


if __name__ == '__main__':
    print("a:")
    for n in (50, 70, 100):
        a = np.zeros((n,)) + np.eye(n) + np.tril(np.full((n, n), -1), -1)
        a[:, -1] = 1
        b = np.arange(2, 3 - n, -1, dtype=np.float64)
        b = np.r_[b, 2 - n]
        print(a)
        # solve
        LU, p = zerlegung(a, True)
        b_perm = permutation(p, b)
        y = vorwaerts(LU, b_perm)
        x_ = rueckwaerts(LU, y)
        x = nachiteration(x_, LU, p, a, b, 1e-10)
        print(f"mit {n} nachiterationen:")
        print(f"x={x}")

    print("b:")
    for n in (5, 10, 15):
        a = np.zeros((n, n), dtype=np.float64)
        for i in range(n):
            for j in range(n):
                a[i, j] = 0 if j > i else (1 if j == i else i + j)
        # print(a)
        b = np.array([1] + [0] * (n - 1), dtype=np.float64)
        LU, p = zerlegung(a, True)
        b_perm = permutation(p, b)
        y = vorwaerts(LU, b_perm)
        x_ = rueckwaerts(LU, y)
        x = nachiteration(x_, LU, p, a, b, 1e-10)
        print(f"mit {n} nachiterationen:")
        print(f"x={x}")
