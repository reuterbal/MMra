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


def fib(n):
    """Ermittelt das n-te Folgenglied der Fibonacci-Folge,
    die definiert ist als a_{n+1} = a_n + a_{n-1} mit
    a_0 = 0, a_1 = 1.

    :param n: Index des Folgenglieds, n >= 0.
    :return: n-tes Folgenglied.
    """
    if n < 1:
        return 0
    else:
        b, a = 0, 1
        for _ in range(n - 1):
            b, a = a, a + b
        return a


def fib_rek(n):
    """Ermittelt das n-te Folgenglied der Fibonacci-Folge,
    die definiert ist als a_{n+1} = a_n + a_{n-1} mit
    a_0 = 0, a_1 = 1.

    Rekursive Implementierung.

    :param n: Index des Folgenglieds, n >= 0.
    :return: n-tes Folgenglied.
    """
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rek(n - 1) + fib_rek(n - 2)
