import numpy as np


def elemental_stiffness_matrix(alpha, b, c, h):
    return np.array([[alpha/h+b/2+c*h/3, -alpha/h+b/2+c*h/6],
                     [-alpha/h-b/2+c*h/6, alpha/h-b/2+c*h/3]])


def stiffness_matrix(alpha, b, c, H, M):
    A = np.zeros((M, M))

    for k in range(0, M-1):
        Ak = elemental_stiffness_matrix(alpha, b, c, H[k])

        A[k:k+2, k:k+2] += Ak

    A[([0, -1], [0, -1])] = 1
    A[([0, -1], [1, -2])] = 0

    return A

