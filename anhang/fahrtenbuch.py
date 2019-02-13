#!/usr/bin/python3


class Fahrt:
    """Klasse zur Repraesentation einer einzelnen Fahrt.

    Speichert Fahrername, Start- und Endzeit sowie
    Kilometerstand vor und nach der Fahrt.
    """

    def __init__(self, name, start_zeit=0, start_km=0,
                 ende_zeit=0, ende_km=0):
        """Erzeugt eine neue Instanz mit dem angegebenen
        Fahrernamen.

        Start- und Enddaten koennen direkt angegeben werden
        oder spaeter via start() und ende() gesetzt werden.
        """
        self._name = name
        self.start(start_zeit, start_km)
        self.ende(ende_zeit, ende_km)

    def start(self, zeit, kilometerstand):
        """Speichert Abfahrtszeit und Kilometerstand bei
        Anfang der Fahrt.
        """
        self._start_zeit = zeit
        self._start_kilometer = kilometerstand

    def ende(self, zeit, kilometerstand):
        """Speichert Ankunftszeit und Kilometerstand bei
        Ende der Fahrt.
        """
        self._ende_zeit = zeit
        self._ende_kilometer = kilometerstand

    @property
    def start_zeit(self):
        return self._start_zeit

    @property
    def ende_zeit(self):
        return self._ende_zeit

    @property
    def start_kilometer(self):
        return self._start_kilometer

    @property
    def ende_kilometer(self):
        return self._ende_kilometer

    def strecke(self):
        """Berechnet die zurueckgelegte Strecke."""
        return self.ende_kilometer - self.start_kilometer

    def zeit(self):
        """Berechnet die benoetigte Zeit."""
        return self.ende_zeit - self.start_zeit

    def v_avg(self):
        """Berechnet die Durchschnittsgeschwindigkeit."""
        return self.strecke() / self.zeit()

    def __str__(self):
        """Erzeugt eine Textausgabe zu dieser Fahrt."""
        text = ('{} ist in {} h {} km gefahren '
                '(Durchschnittsgeschwindigkeit: {} km/h)')
        return text.format(self._name, self.zeit(),
                           self.strecke(), self.v_avg())


class Fahrtenbuch:
    """Klasse zum Sammeln von Fahrten."""

    def __init__(self):
        """Legt ein leeres Fahrtenbuch an."""
        self._liste = []

    def neuer_eintrag(self, *daten):
        """Legt einen neuen Eintrag im Fahrtenbuch ab.

        Es kann entweder eine Instanz der Klasse Fahrt oder
        die zum Erzeugen einer Instanz benoetigten Daten
        angegeben werden.
        """
        if len(daten) == 1 and isinstance(daten[0], Fahrt):
            self._liste.append(daten[0])
        else:
            self._liste.append(Fahrt(*daten))

    def __str__(self):
        """Erzeugt eine textuelle Ausgabe aller Eintraege
        des Fahrtenbuchs.
        """
        self._liste.sort(key=lambda f: f.start_zeit)
        return '\n'.join([str(f) for f in self._liste])
