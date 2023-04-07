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
    y_[0] = c[0]
    for i in range(1, n):
        y_[i] = c_[i] - (sum(LU[i][j] * y_[j] for j in range(i)))
    return y_


def rueckwaerts(LU_, y_):
    n = len(LU_)
    x_ = np.zeros(n)
    x_[n - 1] = y_[n - 1] / LU_[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x_[i] = (y_[i] - (sum(LU[i][j] * x_[j] for j in range(n - 1, i, -1)))) / LU_[i][i]
    return x_


if __name__ == '__main__':
    # von a1
    print("A1a für b:")
    A = np.array([
        [0, 1, 3, 1],
        [1, 1, 2, 0],
        [4, 4, 8, 2],
        [2, 6, 4, 8]])
    b = np.array([5, 1, 8, 18])
    LU, p = zerlegung(A)
    c = permutation(p, b)
    y = vorwaerts(LU, c)
    x = rueckwaerts(LU, y)
    print(f"{A=}")
    print(f"{LU=}")
    print(f"{b=}")
    print(f"{p=}")
    print(f"{c=}")
    print(f"{y=}")
    print(f"{x=}")
    print("A1b für b':")
    b_strich = np.array([5, 7, 28, 22])
    LU, p = zerlegung(A)
    c = permutation(p, b_strich)
    y = vorwaerts(LU, c)
    x = rueckwaerts(LU, y)
    print(f"{A=}")
    print(f"{LU=}")
    print(f"{b_strich=}")
    print(f"{p=}")
    print(f"{c=}")
    print(f"{y=}")
    print(f"{x=}")
    print("------------------------------------------------------------------------------------")
    # von a2.1
    A = np.array([
        [0, 0, 0, 1],
        [2, 1, 2, 0],
        [4, 4, 0, 0],
        [2, 3, 1, 0]])
    b = np.array([3, 5, 4, 5])
    # für b lösen
    print("A2 Lösen für b:")
    LU, p = zerlegung(A)
    c = permutation(p, b)
    y = vorwaerts(LU, c)
    x = rueckwaerts(LU, y)
    print(f"{A=}")
    print(f"{LU=}")
    print(f"{b=}")
    print(f"{p=}")
    print(f"{c=}")
    print(f"{y=}")
    print(f"{x=}")
    # für b' lösen
    print("A2 Lösen für b':")
    b_strich = np.array([4, 10, 12, 11])
    LU, p = zerlegung(A)
    c = permutation(p, b_strich)
    y = vorwaerts(LU, c)
    x = rueckwaerts(LU, y)
    print(f"{A=}")
    print(f"{LU=}")
    print(f"{b_strich=}")
    print(f"{p=}")
    print(f"{c=}")
    print(f"{y=}")
    print(f"{x=}")
    print("------------------------------------------------------------------------------------")
    # von a2.2
    print("Routine wird für das weitere System für n = 10, 20, 100 angewendet")
    for n in [10, 20, 100]:
        A = np.array([1 / (i+j-1) for i in range(1, n+1) for j in range(1, n+1)]).reshape(n, n)
        b = np.array([1 / (i+1) for i in range(1, n+1)])
        LU, p = zerlegung(A)
        c = permutation(p, b)
        y = vorwaerts(LU, c)
        x = rueckwaerts(LU, y)
        print(f"{n=} => {x=}")

    print("daraus kann man sich erschließen, dass für größere n eine größere Ungenauigkeit folgt.")