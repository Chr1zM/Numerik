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


if __name__ == '__main__':
    A = np.array([
        [0, 0, 0, 1],
        [2, 1, 2, 0],
        [4, 4, 0, 0],
        [2, 3, 1, 0]
    ], dtype=np.float64)

    LU, p = zerlegung(A, True)

    print(f"{LU=}")
    print(f"{p=}")

    b1 = np.array([3, 5, 4, 5])
    c1 = permutation(p, b1)
    y1 = vorwaerts(LU, c1)
    x1 = rueckwaerts(LU, y1)

    print(f"{b1=}")
    print(f"{c1=}")
    print(f"{y1=}")
    print(f"{x1=}")

    b2 = np.array([4, 10, 12, 11])
    c2 = permutation(p, b2)
    y2 = vorwaerts(LU, c2)
    x2 = rueckwaerts(LU, y2)

    print(f"{b2=}")
    print(f"{c2=}")
    print(f"{y2=}")
    print(f"{x2=}")

    beta = 10

    for n in [10, 20, 100]:
        A = np.eye(n, n) + np.diag(np.full((n - 1,), -beta, dtype=np.float64), -1)
        A[0, -1] = beta
        A[-1, -1] = 0

        b = np.full((n,), 1 - beta, dtype=np.float64)
        b[0] = 1 + beta
        b[-1] = -beta

        for pivot in [True, False]:
            LU, p = zerlegung(A, pivot)
            b_perm = permutation(p, b)
            y = vorwaerts(LU, b_perm)
            x = rueckwaerts(LU, y)
            print(f"{n=}, {pivot=}, {x=}")
    print("Daraus kann man erkennen, dass das Ergebnis mit Spaltenpivot genauer ist.")