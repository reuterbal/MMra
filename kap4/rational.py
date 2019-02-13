#!/usr/bin/python3

from fractions import Fraction


def zifferndarstellung(q, p=10):
    """Wandelt eine als fractions.Fraction gegebene Zahl
    0 < q < 1 in die periodische Zifferndarstellung zu einer
    beliebigen Basis p um.

    :param q: rationale Zahl 0 < q < 1.
    :param p: Basis fuer die Zifferndarstellung.
    :return (Q, k): Tupel mit Liste Q der Ziffern und
              Laenge l des endlichen Dezimalbruchanteils.
    """
    if not isinstance(q, Fraction):
        raise TypeError

    Q, P, restbrueche = [], 1, []
    while not q * P in restbrueche:
        restbrueche += [q * P]
        P *= p
        Q += [(q.numerator * P) // q.denominator]
        q -= Fraction(Q[-1], P)
    return Q, restbrueche.index(q * P)


def dezimaldarstellung(q):
    """Wandelt eine als fractions.Fraction gegebene Zahl
    0 < q < 1 in Dezimaldarstellung um.

    Beachte: Fuer Zahlen mit periodischer Dezimaldarstellung
    terminiert dieses Verfahren nicht!

    :param q: rationale Zahl 0 < q < 1.
    :return: Liste mit Ziffern [n_1, n_2, ...].
    """
    if not isinstance(q, Fraction):
        raise TypeError

    Q, J = [], 10
    while q != 0:
        Q += [int(q * J)]
        q -= Fraction(Q[-1], J)
        J *= 10
    return Q


def summendarstellung(q):
    """Wandelt eine als fractions.Fraction gegebene Zahl
    0 < q < 1 in eine endliche Summe von Stammbruechen um.

    :param q: rationale Zahl 0 < q < 1.
    :return: Liste mit Stammbruechen [1/n_1, 1/n_2, ...].
    """
    if not isinstance(q, Fraction):
        raise TypeError

    S = []
    while q.numerator != 1:
        a = (q.numerator + q.denominator - 1) // q.numerator
        S.append(Fraction(1, a))
        q = Fraction(q.numerator * a - q.denominator,
                     q.denominator * a)
    return S + [q]


def bruchdarstellung(Q, k, p=10):
    """Wandelt eine in periodischer Zifferndarstellung zur
    Basis 10 gegebene Zahl in Bruchdarstellung um.

    :param Q: Liste mit Ziffern [n_1, n_2, ...].
    :param k: Vorperiodenlaenge.
    :param p: Basis der Zifferndarstellung (Standard: 10).
    :return: Bruchdarstellung als fractions.Fraction
    """
    # Umwandlung mittels Horner-Schema
    a = 0
    for ni in Q[:k]:
        a = a * p + ni
    t = 0
    for ni in Q[k:]:
        t = t * p + ni

    # Summe aus endlichem und periodischem Anteil
    l = len(Q) - k
    q = Fraction(a * (p**l - 1) + t, p**k * (p**l - 1))
    return q
