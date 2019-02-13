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


class NatuerlicheZahl:
    """Datentyp zum Repraesentieren einer natuerlichen
    Zahl n mit eigenen Definitionen fuer Addition,
    Subtraktion, Multiplikation, Division und Vergleich.

    Der tatsaechliche Wert der natuerlichen Zahl wird als
    int-Objekt abgespeichert.
    """

    def __init__(self, n):
        """Erzeugt eine neue Instanz einer natuerlichen
        Zahl mit Wert n."""
        self.n = n

    @property
    def n(self):
        """Liefert den Zahlenwert.

        :return: Ein int-Objekt mit dem Wert.
        """
        return self._n

    @n.setter
    def n(self, n):
        """Setzt den Zahlenwert auf n."""
        self._n = int(n)

    def __str__(self):
        """Hilfsfunktion, um die Zahl in eine String-
        Darstellung umzuwandeln.

        :return: Ein String mit dem Zahlenwert.
        """
        return "{}".format(self.n)

    def __repr__(self):
        """Hilfsfunktion, die die Python-Syntax zum Erzeugen
        eines Objekts gleichen Wertes liefert.

        :return: Ein String der Form 'NatuerlicheZahl(n)'.
        """
        return "NatuerlicheZahl({})".format(str(self))

    def __int__(self):
        """Hilfsfunktion, um die NatuerlicheZahl in den
        Standarddatentyp int umzuwandeln.

        Dies ist nuetzlich, um Objekte dieses Typs in
        Funktionen zu Verwenden, die Standard-Datentypen
        erwarten.
        """
        return self.n

    __index__ = __int__

    def next(self):
        """Nachfolgerfunktion n^+

        :return: NatuerlicheZahl mit Wert des Nachfolgers.
        """
        return NatuerlicheZahl(self.n + 1)

    def prev(self):
        """Vorgaengerfunktion n^-

        :return: NatuerlicheZahl mit Wert des Vorgaengers.
        """
        return NatuerlicheZahl(self.n - 1)

    def differenz(self, m):
        """Berechnet die Differenz mit einer Ganzzahl m.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: Differenz d = n-m oder None, falls m > n.
        """
        if not isinstance(m, NatuerlicheZahl):
            m = NatuerlicheZahl(m)

        for d in Zaehlen(0, self):
            if m + d == self:
                return d
        return None

    def __eq__(self, m):
        """Prueft Gleichheit mit m.

        :param m: NatuerlicheZahl oder andere Ganzzahl.
        :return: True, falls gleicher Wert wie m,
                 andernfalls False.
        """
        return ((isinstance(m, NatuerlicheZahl) and
                 self.n == m.n) or self.n == m)

    def __le__(self, m):
        """Prueft, ob der Wert kleiner oder gleich m
        ist, indem auf Existenz der Differenz geprueft wird.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: True, falls der Wert <= m ist, sonst False.
        """
        if not isinstance(m, NatuerlicheZahl):
            m = NatuerlicheZahl(m)

        return m.differenz(self) is not None

    def __add__(self, m):
        """Addiert eine Ganzzahl m durch wiederholtes
        Anwenden der Nachfolgerfunktion.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: Summe m + n.
        """
        if not isinstance(m, NatuerlicheZahl):
            m = NatuerlicheZahl(m)

        ret = m
        for _ in Zaehlen(1, self.n):
            ret = ret.next()
        return ret

    def __sub__(self, m):
        """Berechnet die Differenz einer Ganzzahl m,
        falls m <= n, oder loest eine Ausnahme aus.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: Differenz n - m.
        """
        if not isinstance(m, NatuerlicheZahl):
            m = NatuerlicheZahl(m)

        if m <= self:
            return self.differenz(m)
        else:
            raise ValueError("{0} < {1} in __sub__({0}, {1})".format(self, m))

    def __mul__(self, m):
        """Multipliziert die Zahl mit einer Ganzzahl m
        durch wiederholtes Addieren.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: Produkt m*n.
        """
        ret = NatuerlicheZahl(0)
        for _ in Zaehlen(1, self.n):
            ret += m
        return ret

    def __divmod__(self, m):
        """Berechnet Quotienten k und Rest l der Division
        mit einer Ganzzahl m.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: Quotient k und Rest l, sodass n = k*m + l.
        """
        if not isinstance(m, NatuerlicheZahl):
            m = NatuerlicheZahl(m)
        if m == 0:
            raise ValueError('Division durch 0')
        k, l = NatuerlicheZahl(0), self
        while m <= l:
            l -= m
            k = k.next()
        return k, l

    def __floordiv__(self, m):
        """Berechnet Quotienten k der Division mit
        einer Ganzzahl m.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: Quotient k, sodass n = k * m + l.
        """
        k, _ = divmod(self, m)
        return k

    def __mod__(self, m):
        """Berechnet Rest l der Division mit
        einer Ganzzahl m.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: Rest l, sodass n = k * m + l.
        """
        _, l = divmod(self, m)
        return l

    # Hilfsfunktionen, um bei Anwendung von Operatoren mit
    # anderem Datentyp als linker Operand die
    # implementierten Operator-Funktionen aufzurufen:

    def __radd__(self, m):
        return self.__add__(m)

    def __rmul__(self, m):
        return self.__mul__(m)

    def __rsub__(self, m):
        return NatuerlicheZahl(m) - self

    def __rdivmod__(self, m):
        return NatuerlicheZahl(m).__divmod__(self)

    def __rfloordiv__(self, m):
        return NatuerlicheZahl(m).__floordiv__(self)

    def __rmod__(self, m):
        return NatuerlicheZahl(m).__mod__(self)

    def plusrek(self, m):
        """Addiert rekursiv eine Ganzzahl m durch wieder-
        holtes Anwenden der Nachfolgerfunktion und
        Herunterzaehlen des zweiten Summanden.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: Summe m + n.
        """
        if not isinstance(m, NatuerlicheZahl):
            m = NatuerlicheZahl(m)

        if self == 0:
            return m
        else:
            return m.plusrek(self.prev()).next()

    def multrek(self, m):
        """Multipliziert die Zahl rekursiv mit einer
        Ganzzahl m durch wiederholtes Addieren des
        Multiplikators und Herunterzaehlen des
        Multiplikanden mittels Vorgaengerfunktion.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: Produkt m * n.
        """
        if not isinstance(m, NatuerlicheZahl):
            m = NatuerlicheZahl(m)

        if self == 0:
            return self
        else:
            return m.plusrek(m.multrek(self.prev()))

    def differenzrek(self, m, d=0):
        """Berechnet rekursiv die Differenz mit einer
        Ganzzahl m, indem, ausgehend von d=0 und dieses
        schrittweise erhoehend, geprueft wird, ob d der
        Differenz mit einer Ganzzahl m entspricht.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :param d: Zu pruefender Wert fuer die Differenz.
        :return: Differenz d = n-m oder None, falls m > n.
        """
        if not isinstance(m, NatuerlicheZahl):
            m = NatuerlicheZahl(m)
        if not isinstance(d, NatuerlicheZahl):
            d = NatuerlicheZahl(d)

        if m.plusrek(d) == self:
            return d
        elif d == self:
            return None
        else:
            return self.differenzrek(m, d.next())

    def kleinergleichrek(self, m):
        """Prueft, ob der Wert kleiner als der Wert von m
        ist, indem auf Existenz der Differenz mittels der
        rekursiven Implementierunggeprueft wird.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: True, falls der Wert <= m ist, sonst False.
        """
        if not isinstance(m, NatuerlicheZahl):
            m = NatuerlicheZahl(m)

        return m.differenzrek(self) is not None

    def subrek(self, m):
        """Berechnet rekursiv die Differenz einer Ganzzahl
        m, falls m <= n, oder loest eine Ausnahme aus.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: Differenz n - m.
        """
        if not isinstance(m, NatuerlicheZahl):
            m = NatuerlicheZahl(m)

        if m.kleinergleichrek(self):
            return self.differenzrek(m)
        else:
            raise ValueError("{0} < {1} in subrek({0}, {1})".format(self, m))

    def divmodrek(self, m, k=0, l=None):
        """Berechnet Quotienten k und Rest l der Division
        mit einer Ganzzahl m mittels rekursiven Abziehens
        des Nenners vom Zaehler.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: Quotient k und Rest l, sodass n = k*m+l.
        """
        if not isinstance(m, NatuerlicheZahl):
            m = NatuerlicheZahl(m)
        if not isinstance(k, NatuerlicheZahl):
            k = NatuerlicheZahl(k)
        if m == 0:
            raise ValueError('Division durch 0')
        if l is None:
            l = self
        if m.kleinergleichrek(l):
            return self.divmodrek(m, k.next(), l.subrek(m))
        else:
            return k, l

    def fast_differenz(self, m):
        """Berechnet die Differenz mit einer Ganzzahl m.

        Laufzeitoptimierte Variante von differenz():
        Summand m wird gemeinsam mit d hoch gezaehlt und
        dadurch die zusaetzliche Addition m + d in jedem
        Schritt eingespart.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: Differenz d = n-m oder None, falls m > n.
        """
        if not isinstance(m, NatuerlicheZahl):
            m = NatuerlicheZahl(m)

        for d in Zaehlen(0, self):
            if m == self:
                return d
            m = m.next()
        return None

    def fast_differenzrek(self, m, d=0):
        """Berechnet rekursiv die Differenz mit einer
        Ganzzahl m, indem, ausgehend von d=0 und dieses
        schrittweise erhoehend, geprueft wird, ob d der
        Differenz mit einer Ganzzahl m entspricht.

        Laufzeitoptimierte Variante von differenzrek():
        Summand m wird gemeinsam mit d hoch gezaehlt und
        dadurch die zusaetzliche Addition m + d in jedem
        Schritt eingespart.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :param d: Zu pruefender Wert fuer die Differenz.
        :param s: Bisherige Summe m + d.
        :return: Differenz d = n-m oder None, falls m > n.
        """
        if not isinstance(m, NatuerlicheZahl):
            m = NatuerlicheZahl(m)
        if not isinstance(d, NatuerlicheZahl):
            d = NatuerlicheZahl(d)

        if m == self:
            return d
        elif d == self:
            return None
        else:
            return self.fast_differenzrek(m.next(), d.next())

    def __lt__(self, m):
        """Prueft, ob der Wert kleiner als der Wert von m
        ist, indem auf Existenz der Differenz geprueft wird.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: True, falls der Wert <= m ist, sonst False.
        """
        if not isinstance(m, NatuerlicheZahl):
            m = NatuerlicheZahl(m)

        return m.differenz(self.next()) is not None

    def __pow__(self, m):
        """Potenziert die Zahl mit einer Ganzzahl m
        durch wiederholtes Multiplizieren.

        :param m: NatuerlicheZahl (pos. Ganzzahl oder 0).
        :return: Potenz m**n.
        """
        ret = NatuerlicheZahl(1)
        for _ in Zaehlen(1, m):
            ret *= self
        return ret


class Zaehlen:
    """Ein iterierbares Objekt zum Darstellen von
    Zaehlvorgaengen unter Verwendung von Instanzen
    von 'NatuerlicheZahl'.
    """

    def __init__(self, a, b):
        """Erzeugt ein neues iterierbares Objekt
        mit gegebenen (inklusiven) unteren bzw.
        oberen Grenzen a bzw. b.
        """
        if not isinstance(a, NatuerlicheZahl):
            a = NatuerlicheZahl(a)
        if not isinstance(b, NatuerlicheZahl):
            b = NatuerlicheZahl(b)
        self.a = a
        self.b = b

    def __iter__(self):
        """Initialisiert den Iterator mit der
        Anfangsposition.
        """
        self.n = self.a
        return self

    def __next__(self):
        """Liefert den Nachfolger der aktuellen
        Position, bis die obere Grenze erreicht ist.
        """
        if self.n == self.b.next():
            raise StopIteration
        n, self.n = self.n, self.n.next()
        return n
