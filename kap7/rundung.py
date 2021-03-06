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
