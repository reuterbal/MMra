#!/usr/bin/python3


def trapez(f, a, b, n):
    """Approximiert das Integral der Funktion f im Intervall
    (a, b) unter Verwendung der Trapezregel mit der
    angegebenen Anzahl an Halbierungen der Teilintervalle.

    :param f: Integrandenfunktion f.
    :param a, b: Integrationsgrenzen.
    :param n: Anzahl Halbierungen der Teilintervalle.
    :return: Approximation des Integrals von f ueber (a, b).
    """
    h = [(b - a) / 2**k for k in range(n + 1)]
    s0 = 0.5 * (f(a) + f(b))
    s = sum(2**(k + 1) * h[k + 1] *
            sum(f(a + (2 * i + 1) * h[k + 1])
                for i in range(2**k))
            for k in range(n))
    return (s0 + s) / 2**n


def romberg(s):
    """Extrapoliert die Naeherungswerte s_k gemaess des
    Extrapolationstableaus des Romberg-Verfahrens.

    :param s: Liste s = [s_0, ..., s_m]
    :return: Verbesserte Naeherung T_m,m.
    """
    T = s
    for k in range(1, len(s)):
        T = [(4**k * a - b) / (4**k - 1)
             for a, b in zip(T[1:], T[:-1])]
    return T[0]


def trapez_allg(f, x):
    """Approximiert das Integral der Funktion f unter
    Verwendung der Trapezregel und der angegebenen (nicht
    notwendigerweise aequidistanten) Quadraturpunkte.

    :param f: Integrandenfunktion f.
    :param x: Liste der Quadaturpunkte
              [a = x_0, x_1, ... x_n = b] mit x_i > x_{i-1}.
    :return: Approximation des Integrals von f ueber (a, b).
    """
    return 0.5 * sum((r - l) * (f(l) + f(r))
                     for l, r in zip(x[:-1], x[1:]))
