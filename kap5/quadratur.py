#!/usr/bin/python3

# This file belongs to the collection of Python codes from the book
#
#   "Mit Mathe richtig anfangen - Eine Einfuehrung mit integrierter Anwendung
#    der Programmiersprache Python"
#
# by Peter Knabner, Balthasar Reuter, and Raphael Schulz.
# Published by Springer-Spektrum, 2019.
#
# If you want to use this code please include a reference to this publication.
#
# Copyright (C) 2019 Peter Knabner, Balthasar Reuter, Raphael Schulz.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


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
