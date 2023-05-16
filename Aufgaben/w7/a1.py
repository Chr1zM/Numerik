from Blatt07_lib import *


def cg(a_, b_, x_0):
    res_ = []
    x_ = x_0
    p = r_0 = r = b_ - a_.dot(x_0)
    res_.append(np.linalg.norm(r) / np.linalg.norm(r_0))
    while np.linalg.norm(r) / np.linalg.norm(r_0) > 1e-6:
        alpha = r.dot(r) / p.dot(a_.dot(p))
        r_ = r - alpha * a_.dot(p)
        beta = r_.dot(r_) / r.dot(r)
        r = r_
        p = r_ + beta * p
        x_ += alpha * p
        res_.append(np.linalg.norm(r) / np.linalg.norm(r_0))
    return x_, res_


if __name__ == '__main__':
    for m in (50, 100, 200):
        a, b = system(m)
        x, res = cg(a, b, b)
        plt.semilogy(range(len(res)), res, label=f'm={m}')

    plt.xlabel('Iterations')
    plt.ylabel('$||r_k||_2 / ||r_0||_2$')
    plt.legend()
    plt.tight_layout()
    plt.show()
