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
