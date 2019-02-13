#!/usr/bin/python3


def ggt(a, b):
    """Sucht den groessten gemeinsamen Teiler zweier
    Zahlen mittels des Euklid'schen Algorithmus.

    :param a: Ganzzahl.
    :param b: Ganzzahl.
    :return: Groesster Gemeinsamer Teiler von a und b.
    """
    n, m, l = a, b, b
    while l != 0:
        k, l = divmod(n, m)
        n, m = m, l
    return n


def ggt_wechselwegnahme(a, b):
    """Sucht den groesten gemeinsamen Teiler zweier
    Zahlen mittels Wechselwegnahme.

    :param a: Positive Ganzzahl.
    :param b: Positive Ganzzahl.
    :return: Groesster Gemeinsamer Teiler von a und b.
    """
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def ggt_rueckwaerts(a, b):
    """Sucht den groesten gemeinsamen Teiler zweier
    Zahlen sowie die entsprechenden Faktoren auf Basis
    des Euklid'schen Algorithmus durch Rueckwaertsaufbauen,
    sodass m * a + n * b = ggt(a, b)

    :param a: Positive Ganzzahl.
    :param b: Positive Ganzzahl.
    :return: Tuple (ggt, m, n).
    """
    r = []
    while b != 0:
        r = r + [a // b]
        a, b = b, a - r[-1] * b
    m, n = 1, 0
    for q in reversed(r):
        m, n = n, m - q * n
    return (a, m, n)


def ggt_vorwaerts(a, b):
    """Sucht den groesten gemeinsamen Teiler zweier
    Zahlen sowie die entsprechenden Faktoren auf Basis
    des Euklid'schen Algorithmus durch Vorwaertsaufbauen,
    sodass m * a + n * b = ggt(a, b)

    :param a: Positive Ganzzahl.
    :param b: Positive Ganzzahl.
    :return: Tuple (ggt, m, n).
    """
    new_m, m = (0, 1)
    new_n, n = (1, 0)
    while b != 0:
        r = a // b
        a, b = b, a - r * b
        new_m, m = m - r * new_m, new_m
        new_n, n = n - r * new_n, new_n
    return (a, m, n)
