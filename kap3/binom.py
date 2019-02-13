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


def nchoosek(n, k):
    """Berechnet den Binomialkoeffizienten "n ueber k",
    definiert als n! / (k! * (n-k)!).

    :param n: Positive Ganzzahl.
    :param k: Positive Ganzzahl.
    :return: Binomialkoeffizient.
    """
    k = min(k, n - k)
    denominator = 1
    for i in range(1, k + 1):
        denominator = denominator * i
    nominator = 1
    for i in range(n - k + 1, n + 1):
        nominator = nominator * i
    return nominator // denominator


def pascal(N):
    """Berechnet alle Binomialkoeffizienten "n ueber k"
    mit 0 <= n <= N, 0 <= k <= n und gibt diese als
    Liste von Listen zurueck, wobei Eintrag [n][k]
    dem Binomialkoeffizienten "n ueber k" entspricht.

    :param N: Maximalwert fuer n (und k), positive Ganzzahl.
    :return: Liste von Listen mit Binomialkoeffizienten.
    """
    dreieck = [[1]]
    for n in range(1, N + 1):
        zeile = (n + 1) * [1]
        for k in range(1, n):
            zeile[k] = (dreieck[n - 1])[k - 1] + (dreieck[n - 1])[k]
        dreieck = dreieck + [zeile]
    return dreieck
