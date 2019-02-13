#!/usr/bin/python3


def russ_mult(a, b):
    """Berechnet das Produkt zweier natuerlicher Zahlen
    unter Verwendung der Verdopplungs-Halbierungs-Methode
    (russische Bauernmultiplikation).

    Als einzige Operationen werden Halbieren (mit Abrunden)
    sowie Verdoppeln genutzt.
    :param a, b: Faktoren des Produktes a * b.
    :return: Produkt a * b.
    """
    m = 0
    while a != 0:
        k, l = divmod(a, 2)
        if l == 1:
            m += b
        a, b = k, 2 * b
    return m


def russ_mult_rek(a, b):
    """Berechnet das Produkt zweier natuerlicher Zahlen
    unter Verwendung der Verdopplungs-Halbierungs-Methode
    (russische Bauernmultiplikation) in einer rekursiven
    Variante.

    Als einzige Operationen werden Halbieren (mit Abrunden)
    sowie Verdoppeln genutzt.
    :param a, b: Faktoren des Produktes a * b.
    :return: Produkt a * b.
    """
    if a == 1:
        return b
    else:
        k, l = divmod(a, 2)
        m = 2 * russ_mult_rek(k, b)
        if l == 1:
            m += b
        return m
