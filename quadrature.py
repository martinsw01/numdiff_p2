# Trapezoid quadratures
import numpy as np


def quadrature_phi0(f, x0, x1):
    return gaussian_quad(lambda x: f(x)*(x-x0)/(x1-x0), x0, x1)


def quadrature_phi1(f, x0, x1):
    return gaussian_quad(lambda x: f(x)*(x1-x)/(x1-x0), x0, x1)


ksi, w = np.polynomial.legendre.leggauss(2)


def gaussian_quad(f, x0, x1):
    q = 0.5*(x1-x0)*ksi+0.5*(x1+x0)
    return 0.5*(x1-x0)*np.sum(w*f(q))
