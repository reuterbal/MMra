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

import math


def erat(N):
    """Ermittelt alle Primzahlen kleiner oder gleich N
    mittels des Sieb des Erathostenes.

    :param N: Obere Schranke fuer Primzahlen.
    :return: Sortierte Liste aller Primzahlen <= N.
    """
    is_prime = (N + 1) * [True]
    for i in range(2, math.ceil(math.sqrt(N)) + 1):
        if is_prime[i]:
            for j in range(i * i, N + 1, i):
                is_prime[j] = False
    return [i for i in range(2, N + 1) if is_prime[i]]


def probediv(n):
    """Ermittelt die Primfaktorzerlegung einer Zahl n
    mittels Probedivision.

    :param n: Zahl, deren Primfaktorzerlegung gesucht ist.
    :return: Sortierte Liste (ggf. mit Mehrfacheintraegen)
             aller Primfaktoren.
    """
    primes = erat(math.ceil(math.sqrt(n)))
    factors = []
    for p in primes:
        while n % p == 0:
            factors.append(p)
            n = n // p
    if n > 1:
        factors.append(n)
    return sorted(factors)


def fermat_probediv(n):
    """Ermittelt die Primfaktorzerlegung einer Zahl n
    mittels Fermats Faktorisierungsmethode und Probedivision
    fuer die beiden Faktoren.

    :param n: Zahl, deren Primfaktorzerlegung gesucht ist.
    :return: Sortierte Liste (ggf. mit Mehrfacheintraegen)
             aller Primfaktoren.
    """
    if n % 2 == 0:
        return [2] + fermat_probediv(n // 2)
    x = math.ceil(math.sqrt(n))
    r = x * x - n
    y = math.floor(math.sqrt(r))
    while y * y != r:
        r, x = r + 2 * x + 1, x + 1
        y = math.floor(math.sqrt(r))
    a, b = x + y, x - y
    return sorted(probediv(a) + probediv(b))


def fermat(n):
    """Ermittelt die Primfaktorzerlegung einer Zahl n
    mittels rekursiver Anwendung von Fermats
    Faktorisierungsmethode.

    :param n: Zahl, deren Primfaktorzerlegung gesucht ist.
    :return: Sortierte Liste (ggf. mit Mehrfacheintraegen)
             aller Primfaktoren.
    """
    if n % 2 == 0:
        return [2] + fermat_probediv(n // 2)
    x = math.ceil(math.sqrt(n))
    r = x * x - n
    y = math.floor(math.sqrt(r))
    while y * y != r:
        r, x = r + 2 * x + 1, x + 1
        y = math.floor(math.sqrt(r))
    a, b = x + y, x - y
    if b == 1:
        return [a]
    else:
        return sorted(fermat(a) + fermat(b))
