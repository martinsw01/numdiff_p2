import numpy as np

from quadrature import quadrature_phi0, quadrature_phi1


def elemental_load_vector(f, x0, x1):
    return np.array([
        quadrature_phi0(f, x0, x1),
        quadrature_phi1(f, x0, x1)
    ])


def load_vector(f, X, M):
    """
    :param f: Source
    :param X: Grid points from 0 to 1 of size M
    """

    F = np.zeros_like(X)
    for i in range(1, M-1):
        F[i:i+2] += elemental_load_vector(f, X[i], X[i+1])

    return F

