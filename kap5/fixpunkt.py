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

from math import sqrt


def heron(a, iters=7, x0=1.):
    """Wendet das Heron-Verfahren zum Bestimmen der
    Quadratwurzel von a an.

    Die zugehoerige Iterationsvorschrift lautet
    x_{n+1} = 0.5 * (x_n + a / x_n)
    und bricht ab, sobald die angegebene Zahl an
    Iterationen erreicht ist.

    :param a: Argument der Quadratwurzel.
    :param iters: Anzahl Iterationen.
    :param x0: Startwert fuer x.
    """
    import tools
    if tools.is_intermediate_values:
        tools.intermediate_values = [(x0, )]

    x = x0
    for _ in range(iters):
        x = 0.5 * (x + a / x)
        if tools.is_intermediate_values:
            tools.intermediate_values.append((x, ))
    return x


def fixpunkt_iter(a, alpha, iters=20, x0=1.):
    """Wendet eine generalisierte Version des Heron-Verfahrens
    zum Bestimmen der Quadratwurzel von a an.

    Die zugehoerige Iterationsvorschrift lautet
    x_{n+1} = alpha * x_n + (1 - alpha) * a / x_n
    und bricht ab, sobald die angegebene Zahl an Iterationen
    erreicht ist.

    :param a: Argument der Quadratwurzel.
    :param alpha: Gewichtungsfaktor.
    :param iters: Anzahl Iterationen.
    :param x0: Startwert fuer x.
    """
    import tools
    if tools.is_intermediate_values:
        tools.intermediate_values = [(x0, )]

    x = x0
    for _ in range(iters):
        x = alpha * x + (1. - alpha) * a / x
        if tools.is_intermediate_values:
            tools.intermediate_values.append((x, ))
    return x


def err(x, a):
    """Hilfsfunktion, die den tatsaechlichen Fehler
    |x - sqrt(a)| berechnet.
    """
    return abs(x - sqrt(a))


def res(x, a):
    """Hilfsfunktion, die das Residuum |x*x-a| berechnet."""
    return abs(x * x - a)


def fixpunkt_res(a, alpha, eps=1.e-12, x0=1.):
    """Wendet eine generalisierte Version des Heron-
    Verfahrens zum Bestimmen der Quadratwurzel von a an.

    Die zugehoerige Iterationsvorschrift lautet
    x_{n+1} = alpha * x_n + (1 - alpha) * a / x_n
    und bricht ab, sobald fuer das Residuum gilt
    |(x_n)^2 - a| < eps.

    :param a: Argument der Quadratwurzel.
    :param alpha: Gewichtungsfaktor.
    :param eps: Abbruchschranke fuer Residuumskriterium.
    :param x0: Startwert fuer x.
    """
    import tools
    if tools.is_intermediate_values:
        tools.intermediate_values = [(x0, err(x0, a), res(x0, a))]

    x = x0
    while res(x, a) >= eps:
        x = alpha * x + (1. - alpha) * a / x
        if tools.is_intermediate_values:
            tools.intermediate_values.append((x, err(x, a), res(x, a)))
    return x


def aposteriori(x, a, b):
    """Hilfsfunktion, die den a-posteriori Fehlerschaetzer
    |x^2 - a| / (x + b) auswertet.
    """
    return abs(x * x - a) / (x + b)


def fixpunkt_aposteriori(a, alpha, b, eps=1.e-12, x0=1.):
    """Wendet eine generalisierte Version des Heron-
    Verfahrens zum Bestimmen der Quadratwurzel von a an.

    Die zugehoerige Iterationsvorschrift lautet
    x_{n+1} = alpha * x_n + (1 - alpha) * a / x_n
    und bricht ab, wenn fuer den a-posteriori Fehler-
    schaetzer gilt: |(x_n)^2 - a| / (x_n + b) < eps.

    :param a: Argument der Quadratwurzel.
    :param alpha: Gewichtungsfaktor.
    :param b: Untere Schranke fuer sqrt(a).
    :param eps: Abbruchschranke fuer Fehlerkriterium.
    :param x0: Startwert fuer x.
    """
    import tools
    if tools.is_intermediate_values:
        tools.intermediate_values = [(x0, err(x0, a), aposteriori(x0, a, b))]

    x = x0
    while aposteriori(x, a, b) >= eps:
        x = alpha * x + (1. - alpha) * a / x
        if tools.is_intermediate_values:
            tools.intermediate_values.append((x, err(x, a),
                                              aposteriori(x, a, b)))
    return x


def bisektion(f, x, y, eps=1.e-13):
    """Wendet das Bisektionsverfahren an, um eine Nullstelle
    der Funktion f zu finden.

    Die Iteration bricht ab, sobald |f(z)| < eps.

    :param f: Funktion, deren Nullstelle gesucht ist.
    :param x: Linksseitiger Startwert.
    :param y: Rechtsseitiger Startwert.
    :param eps: Abbruchschranke (optional).
    :return: Auswertestelle x, an der |f(x)| < eps gilt.
    """
    z = (x + y) / 2

    import tools
    if tools.is_intermediate_values:
        tools.intermediate_values = [(x, y, z, err(z, 2))]

    while abs(f(z)) >= eps:
        if f(x) * f(z) > 0:
            x, z = z, (z + y) / 2
        else:
            y, z = z, (x + z) / 2
        if tools.is_intermediate_values:
            tools.intermediate_values.append((x, y, z, err(z, 2)))
    return z


def newton(f, df, x0, eps=1.e-13):
    """Eine Implementierung des Newton-Verfahrens.

    Die Iteration bricht ab, sobald |f(x)| < eps.

    :param f: Funktion, deren Nullstelle gesucht ist.
    :param df: Ableitung der Funktion.
    :param x0: Startwert.
    :param eps: Abbruchschranke (optional).
    :return: Auswertestelle x, an der |f(x)| < eps gilt.
    """
    import tools
    if tools.is_intermediate_values:
        tools.intermediate_values = [(x0, abs(f(x0)))]

    x = x0
    while abs(f(x)) >= eps:
        x -= f(x) / df(x)
        if tools.is_intermediate_values:
            tools.intermediate_values.append((x, abs(f(x))))
    return x


def heron_abbruchkriterium(a, x0, eps=1.e-13):
    """Wendet das Heron-Verfahren zum Bestimmen der
    Quadratwurzel von a an.

    Die Iteration bricht ab, sobald die Aenderung der
    Approximation nicht mehr als eps betraegt.

    :param a: Argument der Quadratwurzel.
    :param x0: Startwert fuer x.
    :param eps: Schranke fuer das Abbruchkriterium.
    """
    x, x_old = x0, x0 + 2 * eps
    while abs(x - x_old) >= eps:
        x, x_old = 0.5 * (x + a / x), x
    return x


def fehlerschaetzer(a, x, b):
    """A posteriori Fehlerschaetzer fuer das Heron-Verfahren
    """
    return x * abs(x - a / x) / (x + b)


def heron_fehlerschaetzer(a, x0, b, eps=1.e-13):
    """Wendet das Heron-Verfahren zum Bestimmen der
    Quadratwurzel von a an.

    Die Iteration bricht ab, sobald der a posteriori
    Fehlerschaetzer die Schranke eps unterschritten hat.

    :param a: Argument der Quadratwurzel.
    :param x0: Startwert fuer x.
    :param b: Bekannte untere Schranke fuer Wurzel(a).
    :param eps: Schranke fuer das Abbruchkriterium.
    """
    x = x0
    while fehlerschaetzer(a, x, b) >= eps:
        x = 0.5 * (x + a / x)
    return x


def heron_kombiniert(a, x0, b, eps=1.e-13):
    """Wendet das Heron-Verfahren zum Bestimmen der
    Quadratwurzel von a an.

    Die Iteration bricht ab, sobald der a posteriori
    Fehlerschaetzer die Schranke eps unterschritten hat
    und die Aenderung der Approximation nicht mehr als
    eps betraegt.

    :param a: Argument der Quadratwurzel.
    :param x0: Startwert fuer x.
    :param b: Bekannte untere Schranke fuer Wurzel(a).
    :param eps: Schranke fuer das Abbruchkriterium.
    """
    x, x_old = x0, x0 + 2 * eps
    while (fehlerschaetzer(a, x, b) >= eps and
           abs(x - x_old) >= eps):
        x, x_old = 0.5 * (x + a / x), x
    return x


def fixpunkt(h, x0, iters=20):
    """Fuehrt eine Fixpunktiteration fuer eine gegebene
    Fixpunktgleichung h durch.

    Die Iteration bricht nach der angegebenen Anzahl von
    Schritten ab.

    :param h: Fixpunktgleichung.
    :param x0: Startwert.
    :param iters: Anzahl Iterationen.
    """
    x = x0
    for _ in range(iters):
        x = h(x)
    return x


def shifting_root(a, n, p=2, eps=1.e-10):
    """Berechnet die n-te Wurzel der Zahl a unter Verwendung
    des Verfahrens zum schriftlichen Wurzelziehen.

    1. Teile die Zahl in Gruppen mit n Stellen.
    2. Wiederhole bis gewuenschte Genauigkeit erreicht:
       a. Ermittle naechsten Block alpha
       b. Suche groesstes beta, deren Quadrat <= Block
       c. Aktualisiere Ergebnis y und Rest r

    :param a: Argument der Wurzel.
    :param n: Grad der Wurzel.
    :param p: Zur Berechnung zu verwendende Basis.
    :param eps: Abbruchkriterium fuer Residuum.
    """
    # Ermittle die Anzahl Gruppen mit n Stellen der Zahl a
    k = 0
    while a > p**(k * n):
        k += n

    # Initialisiere Rest, verbleibenden Anteil und Ergebnis
    # und arbeite stellenweise ab, bis Residuum klein genug
    r, x, y = 0, a, 0
    while a - y**n * p**(k * n) >= eps:
        k -= 1                            # Ergebnis-Stelle
        alpha, x = divmod(x, p**(k * n))  # Ermittle Gruppe
        for beta in range(p):        # Ermittle Quadratzahl
            tmp = (p * y + (beta + 1))**n - p**n * y**n
            if tmp > p**n * r + alpha:
                break
        y, r = (p * y + beta,
                p**n * r + alpha -
                ((p * y + beta)**n - p**n * y**n))
    return y * p**k
