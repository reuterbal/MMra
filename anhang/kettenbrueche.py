#!/usr/bin/python3


def kettenbruch_ausw(a):
    """Auswertung eines Kettenbruchs, der als Folge
    (a_0, a_1, ..., a_n) mit a_n >= 2 gegeben ist.

    :param a: Folgenglieder [a_0, a_1, ..., a_n].
    :return: Ausgewertete Zahl.
    """
    x = a[-1]
    for a_k in reversed(a[:-1]):
        x = a_k + 1 / x
    return x


def kettenbruch_ausw_rekursiv(a):
    """Rekursive Auswertung eines Kettenbruchs, der
    als Folge (a_0, a_1, ..., a_n) mit a_n >=2 gegeben ist.

    :param a: Folgenglieder [a_0, a_1, ..., a_n].
    :return: Ausgewertete Zahl.
    """
    if len(a) == 1:
        return a[0]
    else:
        return a[0] + 1 / kettenbruch_ausw_rekursiv(a[1:])


def kettenbruch_ausw_rational(a):
    """Auswertung eines Kettenbruchs, der als Folge
    (a_0, a_1, ..., a_n) mit a_n >= 2 gegeben ist und
    Darstellung als rationale Zahl.

    :param a: Folgenglieder [a_0, a_1, ..., a_n].
    :return: Tupel (p, q) der rationalen Zahl p/q.
    """
    p, q = a[-1], 1
    for a_k in reversed(a[:-1]):
        p, q = q + a_k * p, p
    return p, q


def kettenbruch(x):
    """Sucht nach der Kettenbruchdarstellung einer Zahl x.

    Das Verfahren terminiert nur fuer rationale Zahlen x.

    :param x: Darzustellende Zahl x > 0.
    :return: Liste [a_0, a_1, ..., a_n] mit Folgengliedern.
    """
    a, y = [int(x)], x - int(x)
    while y != 0:
        a += [int(1 / y)]
        y = 1 / y - a[-1]
    return a
