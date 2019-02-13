#!/usr/bin/python3

import unittest
import random
import math

# Initialize with current system time
random.seed()


class TestAnhang(unittest.TestCase):

    def test_russ_mult_rek(self):
        """Tests russ_mult_rek()"""
        from anhang import russ_mult_rek

        for _ in range(10):
            a, b = random.randint(1, 100), random.randint(1, 100)
            self.assertEqual(russ_mult_rek(a, b), a * b)

    def test_russ_mult(self):
        """Tests russ_mult()"""
        from anhang import russ_mult

        for _ in range(10):
            a, b = random.randint(1, 100), random.randint(1, 100)
            self.assertEqual(russ_mult(a, b), a * b)

    def test_mult(self):
        """Tests mult()"""
        eps = 1e-16
        from anhang import mult
        for p in range(2, 14):
            for _ in range(10):
                a = random.uniform(-100, 100)
                b = random.uniform(-p, p)
                self.assertAlmostEqual(mult(a, b, p, eps), a * b, delta=1.e-10)

    def test_div(self):
        """Tests div()"""
        eps = 1e-16
        from anhang import div
        for p in range(2, 14):
            for _ in range(10):
                a = random.uniform(-100, 100)
                b = random.uniform(-100, 100)
                self.assertAlmostEqual(div(a, b, p, eps), a / b, delta=1.e-10)

    def test_sincos(self):
        """Tests sincos()"""
        from anhang import sincos
        for _ in range(10):
            x = random.uniform(-3 * math.pi, 3 * math.pi)
            s, c = sincos(x)
            self.assertAlmostEqual(s, math.sin(x), delta=1.e-6)
            self.assertAlmostEqual(c, math.cos(x), delta=1.e-6)

    def test_kettenbruch(self):
        """Tests kettenbruch()"""
        from anhang import kettenbruch
        a = kettenbruch(1.6)
        self.assertEqual(a, [1, 1, 1, 1, 1, 562949953421312])
        a = kettenbruch(4 + 1 / 2 + 1 / 4 + 1 / 8 + 1 / 16)
        self.assertEqual(a, [4, 1, 15, 281474976710656])
        a = kettenbruch(0.5)
        self.assertEqual(a, [0, 2])
        a = kettenbruch(17 / 33)
        self.assertEqual(a, [0, 1, 1, 16])

        from fractions import Fraction
        a = kettenbruch(Fraction('1.6'))
        self.assertEqual(a, [1, 1, 1, 2])
        a = kettenbruch(Fraction('19/33'))
        self.assertEqual(a, [0, 1, 1, 2, 1, 4])

    def test_kettenbruch_ausw(self):
        """Tests kettenbruch_ausw()"""
        from anhang import kettenbruch_ausw
        x = kettenbruch_ausw([1, 2, 3, 4, 5])
        self.assertAlmostEqual(x, 1.433121019, delta=2.e-10)
        x = kettenbruch_ausw([5, 4, 3, 2])
        self.assertAlmostEqual(x, 5.233333333, delta=4.e-10)

    def test_kettenbruch_ausw_rekursiv(self):
        """Tests kettenbruch_ausw_rekursiv()"""
        from anhang import kettenbruch_ausw_rekursiv
        x = kettenbruch_ausw_rekursiv([1, 2, 3, 4, 5])
        self.assertAlmostEqual(x, 1.433121019, delta=2.e-10)
        x = kettenbruch_ausw_rekursiv([5, 4, 3, 2])
        self.assertAlmostEqual(x, 5.233333333, delta=4.e-10)

    def test_kettenbruch_ausw_rational(self):
        """Tests kettenbruch_ausw_rational()"""
        from anhang import kettenbruch_ausw_rational
        r = kettenbruch_ausw_rational([1, 2, 3, 4, 5])
        self.assertEqual(r, (225, 157))
        r = kettenbruch_ausw_rational([5, 4, 3, 2])
        self.assertEqual(r, (157, 30))

    def test_fahrtenbuch(self):
        """Tests Fahrtenbuch() und Fahrt()"""
        from anhang import Fahrt, Fahrtenbuch

        fb = Fahrtenbuch()
        fahrt1 = Fahrt('Alice')
        fahrt1.start(0, 13157.6)
        fahrt1.ende(4 / 60, 13160.0)
        fb.neuer_eintrag(fahrt1)
        fahrt2 = Fahrt('Bob', 4 / 60, 13160.0)
        fahrt2.ende(16 / 60, 13177.4)
        fb.neuer_eintrag(fahrt2)
        fahrt3 = Fahrt('Clara', 16 / 60, 13177.4, 64 / 60, 13267.4)
        fb.neuer_eintrag(fahrt3)
        fb.neuer_eintrag('Bob', 91 / 60, 13267.4, 223 / 60, 13468.7)
        fb.neuer_eintrag('Clara', 64 / 60, 13267.4, 91 / 60, 13267.4)

        text = ('Alice ist in 0.06666666666666667 h 2.399999999999636 km '
                'gefahren (Durchschnittsgeschwindigkeit: '
                '35.99999999999454 km/h)\n'
                'Bob ist in 0.2 h 17.399999999999636 km gefahren '
                '(Durchschnittsgeschwindigkeit: 86.99999999999818 km/h)\n'
                'Clara ist in 0.8 h 90.0 km gefahren '
                '(Durchschnittsgeschwindigkeit: 112.5 km/h)\n'
                'Clara ist in 0.44999999999999996 h 0.0 km gefahren '
                '(Durchschnittsgeschwindigkeit: 0.0 km/h)\n'
                'Bob ist in 2.2 h 201.3000000000011 km gefahren '
                '(Durchschnittsgeschwindigkeit: 91.50000000000048 km/h)')
        self.assertEqual(str(fb), text)
