#!/usr/bin/python3

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
