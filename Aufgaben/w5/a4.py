import numpy as np


def householder(A: np.array):
    n = A.shape[0]
    R = np.copy(A)
    Q = np.eye(n)

    for i in range(n):
        ai = R[i:, i]
        e1 = np.array([1] + [0] * (n - i - 1))
        v = ai + np.sign(ai[0]) * np.linalg.norm(ai) * e1
        Qi = np.eye(n)
        Qi[i:, i:] -= 2 / np.linalg.norm(v) ** 2 * np.outer(v, v)
        R = Qi @ R
        Q = Qi @ Q
    return Q.T, R


def solve(Q, R, b):
    n = R.shape[0]
    x = Q.T @ b
    x[n - 1] /= R[n - 1, n - 1]
    for i in range(n - 2, -1, -1):
        x[i] -= x[i + 1:] @ R[i, i + 1:]
        x[i] /= R[i, i]
    return x


if __name__ == '__main__':
    print("")
    for n in (10, 50, 100):
        # init A, b
        A = np.zeros((n,)) + np.eye(n) + np.tril(np.full((n, n), -1), -1)
        A[:, -1] = 1
        b = np.arange(2, 3 - n, -1)
        b = np.r_[b, 2 - n]
        # Householder
        Q, R = householder(A)
        # Result
        x = solve(Q, R, b)
        print(f"{x}\n")
        print("-" * 50)

    a = np.array([
        [5, 7, -17],
        [10, -1, -19],
        [10, 20, 5]])
    q, r = householder(a)
    print(q)
    print(r)