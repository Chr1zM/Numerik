def get_tsvd_index(s, alpha):
    n = s.shape[0]
    assert (s.shape == (n,))
    for i in range(1, n):
        if s[0] / s[i] > 1 / alpha:
            return i


if __name__ == '__main__':
