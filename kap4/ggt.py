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
