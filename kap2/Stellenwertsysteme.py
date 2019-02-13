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

from .NatuerlicheZahlen import NatuerlicheZahl, Zaehlen


class Stellenwertsystem:
    """Datentyp zum Darstellen einer Ganzzahl zu einer
    beliebigen Basis p.
    Der Datentyp kann mit beliebigen Ganzzahl-Datentypen
    verwendet werden, z.B. NatuerlicheZahl oder dem
    eingebauten int. Die einzelnen Stellen/Koeffizienten
    werden in einer Liste aufsteigend abgelegt.
    """

    def __init__(self, p, coef=[]):
        """Erzeugt eine neue Instanz einer Zahl zur Basis p.

        Der Datentyp des Parameters p legt den Datentyp
        fest, der fuer die Koeffizienten verwendet wird.
        Diese werden dazu ggf. in diesen Datentyp gewandelt.

        :param p: Basis des Stellenwertsystems.
        :param coef: (optionale) Stellen der Zahl.
        """
        self._type = type(p)
        self._p = p
        self.coef = coef

    @property
    def type(self):
        """Liefert den zum Darstellen von Basis und
        Koeffizienten verwendeten Datentyp.
        """
        return self._type

    @property
    def p(self):
        """Liefert die Basis des Stellenwertsystems."""
        return self._p

    @property
    def coef(self):
        """Liefert die Koeffizienten des Stellenwertsystems
        als aufsteigende Liste.
        Beispiel: Die Zahl '12' zur Basis 10 besitzt die
        Koeffizienten '[2, 1]'.
        """
        return self._coef

    @coef.setter
    def coef(self, coef):
        """Setzt die Koeffizienten des Stellenwertsystems.

        :param coef: Aufsteigende Liste mit Koeffizienten.
                     Diese werden ggf. in den Datentyp
                     des Stellenwertsystems umgewandelt.
        """

        self._coef = [self.type(nk) for nk in coef]

    def __str__(self):
        """Hilfsfunktion, um die Zahl in eine String-
        Darstellung umzuwandeln. Die Basis wird durch
        einen Unterstrich getrennt angehaengt.

        :return: Ein String mit dem Zahlenwert.
        """
        return '{}_{}'.format(
            ''.join(str(n) for n in reversed(self)), self.p)

    def __repr__(self):
        """Hilfsfunktion, die die Python-Syntax zum Erzeugen
        eines Objekts gleichen Wertes liefert.
        """
        return 'Stellenwertsystem({1}, [{0}])'.format(
            ', '.join(repr(n) for n in self), repr(self.p))

    def __eq__(self, oth):
        """Prueft Gleichheit mit einem gegebenen Objekt.

        :return: True, falls Basis und Zahlenwert ueberein
                 stimmen. Gleichheit der verwendeten
                 Datentypen wird nicht geprueft!
        """
        return (isinstance(oth, Stellenwertsystem) and
                self.p == oth.p and self.coef == oth.coef)

    def __len__(self):
        """Liefert die Anzahl Stellen/Koeffizienten."""
        return len(self.coef)

    def __getitem__(self, k):
        """Hilfsfunktion, die Zugriff auf die k-te Stelle
        mittels eckiger Klammern erlaubt.
        """
        if len(self) <= int(k):
            return self.type(0)
        else:
            return self.coef[k]

    def __setitem__(self, k, nk):
        """Hilfsfunktion, die Veraendern der k-ten Stelle
        mittels eckiger Klammern erlaubt.
        """
        if not isinstance(nk, self.type):
            nk = self.type(nk)
        if len(self) > int(k):
            self.coef[k] = nk
        else:
            self.coef += (int(k) - len(self)) * [0] + [nk]

    def __iter__(self):
        """Initialisiert den Iterator mit der Anfangs-
        position. Erlaubt das Iterieren ueber alle Stellen
        mittels Schleifen.
        """
        self.k = 0
        return self

    def __next__(self):
        """Liefert den Nachfolger der aktuellen Position,
        bis die letzte Stelle erreicht ist.
        """
        if self.k >= len(self.coef):
            raise StopIteration
        nk = self.coef[self.k]
        self.k += 1
        return nk


def horner(polynom, x=None):
    """Wertet ein Polynom an der Stelle x aus.

    :param polynom: Polynom, dessen Koeffizienten als
                    Stellen einer Instanz von
                    'Stellenwertsystem' gegeben sind.
    :param x: Auswertungsstelle, positive Ganzzahl.
    :return: Wert des Polynoms an der Stelle x.
    """
    if not isinstance(polynom, Stellenwertsystem):
        raise TypeError('Polynom nicht als Stellenwertsystem gegeben')
    if x is None:
        x = polynom.p
    f = polynom.type(0)
    for nk in reversed(polynom):
        f = f * x + nk
    return f


def umwandlung(n, p):
    """Wandelt eine in Dezimaldarstellung gegebene Ganzzahl
    n in eine Darstellung zur Basis p um.

    :param n: Umzuwandelnde Ganzzahl.
    :param p: Zielbasis.
    :return: Eine Instanz von 'Stellenwertsystem' mit der
    Zahl in Darstellung zur Basis p.
    """
    f, n = divmod(n, p)
    n = Stellenwertsystem(p, [n])
    k = 1
    while p <= f:
        f, n[k] = divmod(f, p)
        k += 1
    n[k] = f
    return n


def umwandlung_pq(polynom, q):
    """Wandelt eine als Instanz von 'Stellenwertsystem'
    gegebene Zahl in eine Darstellung zur Basis q um.
    """
    return umwandlung(horner(polynom), q)


def ibn_al_banna(a, b):
    """Multipliziert zwei Zahlen direkt in der Darstellung
    zur Basis p unter Verwendung des Multiplikationsschemas
    von Ibn Al-Banna.

    :param a, b: Instanzen von 'Stellenwertsystem' mit
                 identischer Basis p.
    :return: Instanz von Stellenwertsystem mit Darstellung
             des Produkts a * b zur Basis p.
    """
    if not (isinstance(a, Stellenwertsystem) and
            isinstance(b, Stellenwertsystem)):
        raise TypeError('a oder b nicht als Stellenwertsystem gegeben')
    if a.p != b.p:
        raise ValueError('a.p={}!=b.p={}'.format(a.p, b.p))
    # Index der hoechsten Stelle/Potenz
    n = NatuerlicheZahl(max(len(a), len(b))).prev()
    # Iterative Berechnung der Stellen k = 0,...,2n von c
    c = Stellenwertsystem(a.p)
    for k in Zaehlen(0, n * 2):
        # Multiplikation von i-ter Stelle in a mit (k-i)-ter
        # Stelle in b
        m1 = k - n if n <= k else 0
        m2 = k if k <= n else n
        for i in Zaehlen(m1, m2):
            ck = a[i] * b[k - i] + c[k]
            uebertrag, c[k] = divmod(ck, a.p)
            j = k.next()
            while uebertrag != 0:
                cj = c[j] + uebertrag
                uebertrag, c[j] = divmod(cj, a.p)
                j = j.next()
    return c
