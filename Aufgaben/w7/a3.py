import math

import numpy as np
import scipy.sparse
import scipy.sparse.linalg


def sign(x):
    return -1 if x < 0 else 1


def square_sum_of_subdiagonal(a):
    a_ = abs(a.copy())
    np.fill_diagonal(a_, 0)
    return np.sum(a_ ** 2)


def largest_not_diagonal(a, n):
    a_ = abs(a.copy())
    np.fill_diagonal(a_, 0)
    mx = np.argmax(a_)
    i = mx // n
    j = mx % n
    return i, j


def jacobi_ew(a, sorted=True):
    n = a.shape[0]
    assert (a.shape == (n, n))
    Q = np.eye(n, n)
    i = 0
    while (square_sum_of_subdiagonal(a) > 1e-3):
        i += 1
        if i % 100 == 0:
            print(square_sum_of_subdiagonal(a))
        i, j = largest_not_diagonal(a, n)
        q = scipy.sparse.eye(n, format='lil')
        alpha = (a[j, j] - a[i, i]) / (2 * a[i, j])
        c = math.sqrt(0.5 + 0.5 * math.sqrt((alpha ** 2) / (1 + alpha ** 2)))
        s = sign(alpha) / (2 * c * math.sqrt(1 + alpha ** 2))
        q[j, j] = q[i, i] = c
        q[i, j] = s
        q[j, i] = -s
        a = q.T @ a @ q
        # Q = q @ Q
    ew = np.diag(a)
    if sorted:
        ind = np.argsort(ew)
        ew = ew[ind]
        Q = Q[:, ind]
    return ew, Q
