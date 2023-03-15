from scipy.integrate import quad  # Incredibly overkill?

def quadrature_phi0(f, x0, x1) -> float:
    def f_psi0(x):
        return f(x) * (x-x0)/(x1-x0)
    return quad(f_psi0, x0, x1)[0]


def quadrature_phi1(f, x0, x1) -> float:
    def f_psi1(x):
        return f(x) * (x-x1)/(x0-x1)
    return quad(f_psi1, x0, x1)[0]
