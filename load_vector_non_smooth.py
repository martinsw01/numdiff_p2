import numpy as np
from quadrature import gaussian_quad


def hat_up(x, x0, x1):
    """First half of hat function, with peak at x1"""
    return (x-x0)/(x1-x0)


# Last half of hat function, with peak at x0
def hat_down(x, x0, x1):
    """Last half of hat function, with peak at x0"""
    return (x1-x)/(x1-x0)


def elemental_load_vector_non_smooth_solution(alpha, b, c):
    def create_load_vector(u, x0, x1):
        h = x1-x0
        A = alpha*(u(x1)-u(x0))/h  # Exact integral of (alpha u_x psi_x)
        return np.array([
            gaussian_quad(lambda x: b*u(x)/h+c*u(x)*hat_up(x, x0, x1), x0, x1)-A,
            gaussian_quad(lambda x: -b*u(x)/h+c*u(x)*hat_down(x, x0, x1), x0, x1)+A
        ])
    return create_load_vector
