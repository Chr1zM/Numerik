import numpy as np


def zerlegung(A):
    matrix_ = np.array(A)
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


def permutation(p, b):
    return p, b


def vorwaerts(LU, c):
    return LU, c


def rueckwaerts(LU, y):
    return LU, y


if __name__ == '__main__':
    # A = np.array([
    # [0, 0, 0, 1],
    # [2, 1, 2, 0],
    # [4, 4, 0, 0],
    # [2, 3, 1, 0]])
    A = np.array([
        [0, 0, 3, 1],
        [2, 1, 2, 0],
        [8, 8, 0, 0],
        [4, 6, 2, 4]])
    print("A:")
    print(A)
    LU, p = zerlegung(A)
    print("LU:")
    print(LU)
    print(p)
    # matrix 2
    B = np.array([
        [1, 3, 0, 1],
        [0, 1, 1, 2],
        [2, 1, -3, 0],
        [1, 7, 4, 1]])
    # b = [3, 5, 4, 5]
    print("-------")
    print("B:")
    print(B)
    LU2, p = zerlegung(A)
    print("LU:")
    print(LU2)
    print(LU2[[0, 1]])
    print(LU2[[1, 0]])
    print(p)
