#!/usr/bin/python3


def diff(f, x, h):
    """Wertet den (vorwaerts genommenen) Differenzenquotienten
    fuer die Funktion f an der Stelle x mit Schrittweite h aus.
    """
    return (f(x + h) - f(x)) / h


def reihe_vorw(a, n, T=float):
    """Wertet eine Reihe fuer die angegebenen Glieder aus,
    wobei die Folgenglieder durch a(k) gegeben sind und verwendet
    Summationsreihenfolge vorwaerts.
    """
    h = T(0)
    for k in range(1, n + 1):
        h += a(k)
    return h


def reihe_rueck(a, n, T=float):
    """Wertet eine Reihe fuer die angegebenen Glieder aus,
    wobei die Folgenglieder durch a(k) gegeben sind und verwendet
    Summationsreihenfolge rueckwaerts.
    """
    h = T(0)
    for k in range(n, 0, -1):
        h += a(k)
    return h


def test_eq(a, b):
    """Prueft fuer zwei Zahlen a und b, ob 3a = b gilt."""
    return 3 * a == b
