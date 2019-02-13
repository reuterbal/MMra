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
