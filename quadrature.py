# Trapezoid quadratures
def quadrature_phi0(f, x0, x1):
    return 0.5*f(x1) * (x1-x0)


def quadrature_phi1(f, x0, x1):
    return 0.5*f(x0) * (x1-x0)
