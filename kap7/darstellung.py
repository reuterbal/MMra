#!/usr/bin/python3


def eps(T=float):
    """Funktion zur experimentellen Bestimmung des
    Zahlabstandes eps.

    :param T: Datentyp, fuer den eps bestimmt werden soll.
    """
    x = T(1)
    while T(1) + x / T(2) > T(1):
        x /= T(2)
    return x
