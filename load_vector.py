import numpy as np

from quadrature import quadrature_phi0, quadrature_phi1


def elemental_load_vector(f, x0, x1):
    return np.array([
        quadrature_phi0(f, x0, x1),
        quadrature_phi1(f, x0, x1)
    ])


def load_vector(f, X, M, elemental_load_vector=elemental_load_vector, g0=0, g1=0):
    """
    :param f: Source
    :param X: Grid points from 0 to 1 of size M
    :param elemental_load_vector: creates the elemental load vector for each element
    :param g0: boundary at x=0
    :param g1: boundary at x=1
    """

    F = np.zeros(M)
    for i in range(M-1):
        F[i:i+2] += elemental_load_vector(f, X[i], X[i+1])

    F[2] += g0/(X[1]-X[0])
    F[-2] += g1/(X[-1]-X[-2])

    return F[1:-1]
