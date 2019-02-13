#!/usr/bin/python3

from math import sqrt, pi, atan
from functools import reduce


def mult(a, b, p=2, eps=1.e-12):
    """Multiplikation nur unter Verwendung von Addition,
    Subtraktion, Multiplikation mit (Vielfachen) der Basis
    und Stellenverschiebung (d.h. Division durch die Basis).

    :param a: Linksseitiger Faktor.
    :param b: Rechtsseitiger Faktor -1 = -p^0 < b < p^0 = 1.
    :param p: Zur Berechnung zu verwendende Basis.
    :param eps: Abbruchkriterium.
    :return: Ergebnis des Produktes a * b.
    """
    sgn = (1 if a > 0 else -1) * (1 if b > 0 else -1)
    a = abs(a)
    x, y, pp = 0, abs(b), 1
    while abs(y) > eps:
        while y - pp >= 0:
            y -= pp
            x += a * pp
        pp /= p
    return sgn * x


def div(a, b, p=2, eps=1.e-12):
    """Division nur unter Verwendung von Addition,
    Subtraktion, Multiplikation mit (Vielfachen der) Basis
    und Stellenverschiebung (d.h. Division durch die Basis).

    :param a: Divident.
    :param b: Divisor (ungleich 0).
    :param p: Zur Berechnung zu verwendende Basis.
    :param eps: Abbruchkriterium.
    :return: Ergebnis des Quotienten a / b.
    """
    x, y, z, pp = abs(a), abs(b), 0, 1
    sgn = (1 if a > 0 else -1) * (1 if b > 0 else -1)
    while abs(x) > eps:
        while x - y * pp > 0:
            x, z = x - y * pp, z + pp
        pp /= p
    return sgn * z


def get_kN(N):
    """Hilfsfunktion zum Berechnen des Wertes k_N.

    In realen Anwendungen wird dieser Wert bzw. eine Lookup-
    Table fuer verschiedene N fest eincodiert.

    :param N: Anzahl an Teilwinkeln.
    :return: Wert k_N.
    """
    k_i = [1 / sqrt(1 + 2**(-2 * j)) for j in range(N + 1)]
    return reduce(lambda a, b: a * b, k_i)


def get_angles(N):
    """Hilfsfunktion zum Berechnen der Lookup-Table fuer die
    Teilwinkel x_j.

    In realen Anwendungen wird die Tabelle fest eincodiert.

    :param N: Anzahl an Teilwinkeln.
    :return: Tabelle mit x_j fuer j = 0,...,N.
    """
    return [atan(2**(-j)) for j in range(N + 1)]


def sgn(x):
    """Hilfsfunktion zum Berechnen des Vorzeichens einer
    Zahl x."""
    return 1 if x >= 0 else -1


def sincos(x, N=24):
    """CORDIC-Algorithmus zum Berechnen von sin und cos.

    :param x: Winkel (in rad).
    :param N: Anzahl zu verwendender Teilintervalle.
    :return: Tupel mit Approximationen (sin(x), cos(x)).
    """
    if abs(x) > pi / 2:
        s, c = sincos(x - sgn(x) * pi, N)
        return -s, -c

    xj, kN = get_angles(N), get_kN(N)
    c, s, z, pp = 1., 0., x, 1
    for j in range(N):
        k = sgn(z) * pp
        c, s = c - k * s, s + k * c
        z, pp = z - sgn(z) * xj[j], pp / 2
    return kN * s, kN * c
