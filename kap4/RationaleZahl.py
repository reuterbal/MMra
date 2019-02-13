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

from .ggt import ggt


class RationaleZahl:
    """Datentyp zur Darstellung von und dem Rechnen mit
    komplexen Zahlen.
    """

    def __init__(self, m=0, n=1):
        """Erstellt eine rationale Zahl mit angegebenem
        Zaehler m und Nenner n.
        """
        s = -1 if m * n < 0 else 1
        self.m, self.n = s * abs(m), abs(n)
        self.kuerzen()

    def kuerzen(self):
        """Ermittelt den groessten gemeinsamen Teiler von
        Zaehler und Nenner und dividiert beide durch diesen.
        """
        d = ggt(abs(self.m), self.n)
        self.m, self.n = self._m // d, self.n // d

    @property
    def m(self):
        """Liefert den Zaehler der rationalen Zahl."""
        return self._m

    @m.setter
    def m(self, m):
        """Aendert den Zaehler der rationalen Zahl."""
        self._m = int(m)

    @property
    def n(self):
        """Liefert den Nenner der rationalen Zahl."""
        return self._n

    @n.setter
    def n(self, n):
        """Aendert den Nenner der rationalen Zahl."""
        if n < 0:
            raise ValueError("Nenner < 0")
        self._n = int(n)

    def __str__(self):
        """Wandelt die rationale Zahl in eine Zeichenkette"""
        return '{}/{}'.format(self.m, self.n)

    def __repr__(self):
        """Liefert Python-Repraesentation der rat. Zahl."""
        return 'RationaleZahl({}, {})'.format(self.m, self.n)

    def __abs__(self):
        """Liefert den Betrag der rationalen Zahl."""
        return RationaleZahl(abs(self.m), self.n)

    def __pos__(self):
        """Operator '+q'."""
        return RationaleZahl(self.m, self.n)

    def __neg__(self):
        """Operator '-q'."""
        return RationaleZahl(-self.m, self.n)

    def __eq__(self, other):
        """Prueft Gleichheit der rationalen Zahl mit einem
        anderen Objekt."""
        return (isinstance(other, RationaleZahl) and
                other.m == self.m and other.n == self.n)

    def __le__(self, other):
        """Prueft ob die Zahl kleiner oder gleich einer
        anderen Zahl ist."""
        if not isinstance(other, RationaleZahl):
            other = RationaleZahl(other)
        return self.m * other.n <= other.m * self.n

    def __add__(self, other):
        """Addiert rationale Zahl zu einer anderen Zahl."""
        if not isinstance(other, RationaleZahl):
            other = RationaleZahl(other)
        m = self.m * other.n + other.m * self.n
        n = self.n * other.n
        return RationaleZahl(m, n)

    def __sub__(self, other):
        """Subtrahiert eine andere Zahl von der rat. Zahl."""
        return self + (-other)

    def __mul__(self, other):
        """Multipliziert die rationale Zahl mit einer Zahl"""
        if not isinstance(other, RationaleZahl):
            other = RationaleZahl(other)
        m, n = self.m * other.m, self.n * other.n
        return RationaleZahl(m, n)

    def __truediv__(self, other):
        """Dividiert die komplexe Zahl durch andere Zahl."""
        if not isinstance(other, RationaleZahl):
            other = RationaleZahl(other)
        m, n = self.m * other.n, self.n * other.m
        return RationaleZahl(m, n)

    def __radd__(self, other):
        """Kommutation der Addition."""
        return self.__add__(other)

    def __rsub__(self, other):
        """Umgekehrte Subtraktion."""
        return (-self) + other

    def __rmul__(self, other):
        """Kommutation der Multiplikation."""
        return self * other

    def __rtruediv__(self, other):
        """Reziproke Division."""
        return RationaleZahl(other) / self
