import numpy
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


def permutation(p_, b_):
    n = len(b_)
    c_ = numpy.copy(b_)
    for i in range(1, n):
        if p_[i - 1] != i:
            c_[[p_[i - 1] - 1, i - 1]] = c_[[i - 1, p_[i - 1] - 1]]

    return c_


def vorwaerts(LU, c):
    return LU, c


def rueckwaerts(LU, y):
    return LU, y


if __name__ == '__main__':
    A = np.array([
        [0, 0, 0, 1],
        [2, 1, 2, 0],
        [4, 4, 0, 0],
        [2, 3, 1, 0]])
    b = np.array([3, 5, 4, 5])
    b_strich = np.array([4, 10, 12, 11])
    print("A:")
    print(A)
    LU, p = zerlegung(A)
    print("LU:")
    print(LU)
    print("b:")
    print(b)
    print("p:")
    print(p)
    print("c:")
    c = permutation(p, b)
    print(c)
    print("")

    # von a1
    print("A1a:")
    A = np.array([
        [0, 1, 3, 1],
        [1, 1, 2, 0],
        [4, 4, 8, 2],
        [2, 6, 4, 8]])
    b = np.array([5, 1, 8, 18])
    print("A:")
    print(A)
    LU, p = zerlegung(A)
    print("LU:")
    print(LU)
    print("b:")
    print(b)
    print("p:")
    print(p)
    print("c:")
    c = permutation(p, b)
    print(c)
    print("")
