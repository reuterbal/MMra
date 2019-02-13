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


def archimedes1(iters, fn_sqrt=sqrt):
    """Implementierung der 1. Var. des Archimedes-Verfahrens

    Berechnet untere und obere Schranken des Umfangs aus
    U_{n+1} = 2 u_n U_n / (u_n + U_n), U_0 = 4 sqrt(3),
    u_{n+1} = sqrt(U_{n+1} u_n), u_0 = 6.

    :param iters: Anzahl Iterationen.
    :param fn_sqrt: Funktion, die zur Wurzelberechnung
                    verwendet werden soll (optional).
    :return: Tupel (u, U) mit unterer/oberer Schranke fuer
             den Umfang des Einheitskreises.
    """
    import tools
    if tools.is_intermediate_values:
        tools.intermediate_values = [(3, 2 * fn_sqrt(3))]

    u, U = 6, 4 * fn_sqrt(3)
    for _ in range(iters):
        U = 2 * u * U / (u + U)
        u = fn_sqrt(U * u)
        if tools.is_intermediate_values:
            tools.intermediate_values.append((u / 2, U / 2))
    return u, U


def compute_N(n):
    """Hilfsfunktion zum Berechnen der Anzahl der Eckpunkte
    eines Polygons, das aus n-facher Halbierung der Seiten
    eines 6-Ecks entstand.
    """
    return 6 * 2**n


def compute_t(s, fn_sqrt=sqrt):
    """Hilfsfunktion die t_n aus gegebenem s_n berechnet."""
    return 2 * s / fn_sqrt(4 - s * s)


def archimedes2(iters, fn_sqrt=sqrt):
    """Implementierung der 2. Var. des Archimedes-Verfahrens

    Berechnet untere und obere Schranke des Umfangs als
    u = N(n) * s_n, U = N(n) * t_n mittels der Folge
    s_{n+1} = sqrt(2 - sqrt(4 - s_n * s_n)), s_0 = 1
    sowie t_n = 2 s_n / sqrt(4 - s_n * s_n).

    :param iters: Anzahl Iterationen.
    :param fn_sqrt: Funktion, die zur Wurzelberechnung
                    verwendet werden soll (optional).
    :return: Tupel (u, U) mit unterer/oberer Schranke fuer
             den Umfang des Einheitskreises.
    """
    import tools
    if tools.is_intermediate_values:
        N = compute_N(0)
        tools.intermediate_values = [(N, N * compute_t(1, fn_sqrt))]

    s = 1
    for n in range(iters):
        s = fn_sqrt(2 - fn_sqrt(4 - s * s))
        if tools.is_intermediate_values:
            N = compute_N(n + 1)
            tools.intermediate_values.append((N * s / 2,
                                              N * compute_t(s, fn_sqrt) / 2))
    N = compute_N(iters)
    u, U = N * s, N * compute_t(s, fn_sqrt)
    return u, U


def archimedes3(iters, fn_sqrt=sqrt):
    """Implementierung der 3. Var. des Archimedes-Verfahrens

    Berechnet untere und obere Schranke des Umfangs als
    u = N(n) * s_n, U = N(n) * t_n mittels der Folge
    s_{n+1} = s_n / sqrt(2 + sqrt(4 - s_n * s_n)), s_0 = 1
    sowie t_n = 2 s_n / sqrt(4 - s_n * s_n).

    :param iters: Anzahl Iterationen.
    :param fn_sqrt: Funktion, die zur Wurzelberechnung
                    verwendet werden soll (optional).
    :return: Tupel (u, U) mit unterer/oberer Schranke fuer
             den Umfang des Einheitskreises.
    """
    import tools
    if tools.is_intermediate_values:
        N = compute_N(0)
        tools.intermediate_values = [(N, N * compute_t(1, fn_sqrt))]

    s = 1
    for n in range(iters):
        s = s / fn_sqrt(2 + fn_sqrt(4 - s * s))
        if tools.is_intermediate_values:
            N = compute_N(n + 1)
            tools.intermediate_values.append((N * s / 2,
                                              N * compute_t(s, fn_sqrt) / 2))
    N = compute_N(iters)
    u, U = N * s, N * compute_t(s, fn_sqrt)
    return u, U
