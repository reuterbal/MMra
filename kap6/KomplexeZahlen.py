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


class KomplexeZahl:
    """Datentyp zur Darstellung von und dem Rechnen mit
    komplexen Zahlen.
    """

    def __init__(self, real=0, imag=0):
        """Erstellt eine komplexe Zahl mit angegebenem
        Real- und Imaginaerteil.
        """
        self.re = real
        self.im = imag

    @property
    def re(self):
        """Liefert den Realteil der komplexen Zahl."""
        return self._re

    @re.setter
    def re(self, real):
        """Aendert den Realteil der komplexen Zahl."""
        self._re = float(real)

    @property
    def im(self):
        """Liefert den Imaginaerteil der komplexen Zahl."""
        return self._im

    @im.setter
    def im(self, imag):
        """Aendert den Imaginaerteil der komplexen Zahl."""
        self._im = float(imag)

    def __str__(self):
        """Wandelt die komplexe Zahl in eine Zeichenkette"""
        return '{}{:+}i'.format(self.re, self.im)

    def __repr__(self):
        """Liefert Python-Repraesentation der kmpl. Zahl."""
        return 'KomplexeZahl({}, {})'.format(self.re, self.im)

    def __abs__(self):
        """Liefert den Betrag der komplexen Zahl."""
        return sqrt(self.re * self.re + self.im * self.im)

    def __pos__(self):
        """Operator '+z'."""
        return KomplexeZahl(self.re, self.im)

    def __neg__(self):
        """Operator '-z'."""
        return KomplexeZahl(-self.re, -self.im)

    def __eq__(self, other):
        """Prueft Gleichheit der komplexen Zahl mit einem
        anderen Objekt."""
        return (isinstance(other, KomplexeZahl) and
                other.re == self.re and other.im == self.im)

    def __add__(self, other):
        """Addiert komplexe Zahl zu einer anderen Zahl."""
        if not isinstance(other, KomplexeZahl):
            other = KomplexeZahl(other)
        return KomplexeZahl(self.re + other.re,
                            self.im + other.im)

    def __sub__(self, other):
        """Subtrahiert eine andere Zahl von kmplx. Zahl."""
        return self + (-other)

    def __mul__(self, other):
        """Multipliziert die komplexe Zahl mit einer Zahl"""
        if not isinstance(other, KomplexeZahl):
            other = KomplexeZahl(other)
        re = self.re * other.re - self.im * other.im
        im = self.re * other.im + self.im * other.re
        return KomplexeZahl(re, im)

    def __truediv__(self, other):
        """Dividiert die komplexe Zahl durch andere Zahl."""
        if not isinstance(other, KomplexeZahl):
            other = KomplexeZahl(other)
        mod2 = abs(other) * abs(other)
        re_im = (other.re / mod2, -other.im / mod2)
        return self * KomplexeZahl(*re_im)

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
        return KomplexeZahl(other) / self


def phase(z):
    """Berechnet den Winkel, den eine komplexe Zahl in der
    komplexen Zahlenebene mit der x-Achse einnimmt.

    :return: Winkel im Intervall [0, 2 * pi)
    """
    from math import atan, pi
    if not isinstance(z, (complex, KomplexeZahl)):
        raise TypeError("z ist keine komplexe Zahl")

    if z.re > 0:
        if z.im >= 0:
            return atan(z.im / z.re)
        else:
            return atan(z.im / z.re) + 2 * pi
    elif z.re < 0:
        return atan(z.im / z.re) + pi
    else:
        if z.im == 0:
            return 0
        elif z.im > 0:
            return pi / 2
        else:
            return 3 * pi / 2


def polar(z):
    """Liefert zu einer komplexen Zahl die Polardarstellung.

    :param z: Zahl des Typs complex oder KomplexeZahl.
    :return: Tupel (r, phi).
    """
    if not isinstance(z, (complex, KomplexeZahl)):
        raise TypeError("z ist keine komplexe Zahl")

    return (abs(z), phase(z))
