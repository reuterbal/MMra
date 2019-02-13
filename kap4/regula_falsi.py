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
