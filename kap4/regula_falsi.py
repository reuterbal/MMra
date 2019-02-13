#!/usr/bin/python3


def regula_falsi(f, x0, y0, eps=1.e-13):
    """Wendet die Regula falsi zum Bestimmen einer
    Nullstelle von f an.

    Die zugehoerige Iterationsvorschrift lautet
    z = x - f(x) * (x - y) / (f(x) - f(y))
    wobei z in der naechsten Iteration y ersetzt, falls
    f(z) * f(y) < 0, und sonst x ersetzt.

    Die Iteration bricht ab, sobald |f(x)| <= eps oder
    |f(y)| <= eps.

    :param f: Funktion f.
    :param x0: Startwert fuer x.
    :param y0: Startwert fuer y.
    :param eps: Gewuenschter Zielfehler (optional).
    """
    import tools
    if tools.is_intermediate_values:
        tools.intermediate_values = []

    x, y = x0, y0
    while abs(f(x)) > eps and abs(f(y)) > eps:
        if tools.is_intermediate_values:
            tools.intermediate_values.append((x, y))

        z = x - f(x) * (x - y) / (f(x) - f(y))
        if f(z) * f(y) < 0:
            y = z
        else:
            x = z

    if tools.is_intermediate_values:
        tools.intermediate_values.append((x, y))

    return x if abs(f(x)) < abs(f(y)) else y
