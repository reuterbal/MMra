#!/usr/bin/python3

import unittest
import random

from math import sqrt


class TestKap4(unittest.TestCase):
    ggt_pairs = ((1364, 496, 124), (17, 13, 1), (1071, 1029, 21),
                 (0, 5, 5), (3, 0, 3))

    def test_ggt(self):
        """Tests ggt()."""
        from kap4 import ggt
        for (a, b, g) in self.ggt_pairs:
            self.assertEqual(ggt(a, b), g)
            self.assertEqual(ggt(b, a), g)

    def test_ggt_wechselwegnahme(self):
        """Tests ggt_wechselwegnahme()."""
        from kap4 import ggt_wechselwegnahme as ggt
        for (a, b, g) in self.ggt_pairs:
            self.assertEqual(ggt(a, b), g)
            self.assertEqual(ggt(b, a), g)

    def test_ggt_rueckwaerts(self):
        """Tests ggt_rueckwaerts()."""
        from kap4 import ggt_rueckwaerts as ggt
        for (a, b, g) in self.ggt_pairs:
            (g_, m, n) = ggt(a, b)
            self.assertEqual(g, g_)
            self.assertEqual(m * a + n * b, g)
            (g_, m, n) = ggt(b, a)
            self.assertEqual(g, g_)
            self.assertEqual(m * b + n * a, g)

    def test_ggt_vorwaerts(self):
        """Tests ggt_vorwaerts()."""
        from kap4 import ggt_vorwaerts as ggt
        for (a, b, g) in self.ggt_pairs:
            (g_, m, n) = ggt(a, b)
            self.assertEqual(g, g_)
            self.assertEqual(m * a + n * b, g)
            (g_, m, n) = ggt(b, a)
            self.assertEqual(g, g_)
            self.assertEqual(m * b + n * a, g)

    def test_regula_falsi(self):
        """Tests regula_falsi()."""
        from kap4 import regula_falsi
        A, a = sqrt(2), regula_falsi(lambda x: x * x - 2, 1, 2, 1e-13)
        self.assertAlmostEqual(a, A, delta=1e-13)
        self.assertNotEqual(a, A)
        A, a = sqrt(2), regula_falsi(lambda x: 2 - x * x, 1, 2, 1e-13)
        self.assertAlmostEqual(a, A, delta=1e-13)
        self.assertNotEqual(a, A)
        B, b = 2, regula_falsi(lambda x: x * x - 4, 1, 3, 1e-10)
        self.assertAlmostEqual(b, B, delta=1e-10)
        self.assertNotEqual(b, B)
        C, c = 3, regula_falsi(lambda x: x * x * x - 27, 2, 4, 1e-12)
        self.assertAlmostEqual(c, C, delta=1e-12)
        self.assertNotEqual(c, C)

    def test_regula_falsi_mpmath(self):
        """Tests regula_falsi() with arbitrary precision."""
        from kap4 import regula_falsi
        from mpmath import mp

        mp.dps = 32
        A = mp.mpf('1.4142135623730950490071645462558243')
        a = regula_falsi(lambda x: x * x - 2, mp.mpf(1), mp.mpf(2),
                         mp.mpf(1.e-18))
        self.assertEqual(a, A)

    def test_zifferndarstellung(self):
        """Tests zifferndarstellung()."""
        from kap4 import zifferndarstellung
        from fractions import Fraction

        Q, l = zifferndarstellung(Fraction(147181, 999000), 10)
        self.assertEqual(Q, [1, 4, 7, 3, 2, 8])
        self.assertEqual(l, 3)

        Q, l = zifferndarstellung(Fraction(1, 5), 2)
        self.assertEqual(Q, [0, 0, 1, 1])
        self.assertEqual(l, 0)

        Q, l = zifferndarstellung(Fraction(1, 17), 10)
        self.assertEqual(Q, [0, 5, 8, 8, 2, 3, 5, 2, 9, 4, 1, 1, 7, 6, 4, 7])
        self.assertEqual(l, 0)

    def test_dezimaldarstellung(self):
        """Tests dezimaldarstellung()."""
        from kap4 import dezimaldarstellung
        from fractions import Fraction
        Q = dezimaldarstellung(Fraction(1, 5))
        self.assertEqual(Q, [2])
        Q = dezimaldarstellung(Fraction(1, 16))
        self.assertEqual(Q, [0, 6, 2, 5])

    def test_summendarstellung(self):
        """Tests summendarstellung()."""
        from kap4 import summendarstellung
        from fractions import Fraction

        for _ in range(10):
            ab = (random.randrange(1, 20), random.randrange(21, 100))
            q = Fraction(*ab)
            S = summendarstellung(q)

            self.assertEqual(q, sum(S))

            for s in S:
                self.assertEqual(s.numerator, 1)

    def test_bruchdarstellung(self):
        """Tests bruchdarstellung()."""
        from kap4 import bruchdarstellung, zifferndarstellung
        from fractions import Fraction

        for _ in range(10):
            ab = (random.randrange(-100, 100), random.randrange(1, 100))
            q = Fraction(*ab)
            self.assertEqual(bruchdarstellung(*zifferndarstellung(q)), q)

    def test_RationaleZahl(self):
        """Tests datatype RationaleZahl."""
        from kap4 import RationaleZahl
        from fractions import Fraction, gcd

        def frac2Rat(q):
            return RationaleZahl(q.numerator, q.denominator)

        for _ in range(10):
            ab1 = (random.randrange(-20, 20), random.randrange(1, 20))
            ab2 = (random.randrange(-20, 20), random.randrange(1, 20))
            d1 = gcd(*ab1)
            AB1 = (ab1[0] // d1, ab1[1] // d1)
            f1, f2 = Fraction(*ab1), Fraction(*ab2)
            q1, q2 = RationaleZahl(*ab1), RationaleZahl(*ab2)

            self.assertEqual(q1.m, AB1[0])
            self.assertEqual(q1.n, AB1[1])
            self.assertEqual(str(q1), '{}/{}'.format(*AB1))
            self.assertEqual(repr(q1), 'RationaleZahl({}, {})'.format(*AB1))

            self.assertEqual(abs(q1), RationaleZahl(abs(ab1[0]), ab1[1]))
            self.assertEqual(abs(q2), RationaleZahl(abs(ab2[0]), ab2[1]))

            self.assertEqual(q1, RationaleZahl(*ab1))
            self.assertEqual(q1, RationaleZahl(*AB1))
            self.assertNotEqual(q1, RationaleZahl(ab1[0] - 1, ab1[1]))

            self.assertEqual(q1 <= q2, f1 <= f2)
            self.assertEqual(q2 <= q1, f2 <= f1)

            self.assertEqual(+q1, q1)
            self.assertEqual(+q2, q2)
            self.assertEqual(-q1, RationaleZahl(-ab1[0], ab1[1]))
            self.assertEqual(-q2, RationaleZahl(-ab2[0], ab2[1]))

            self.assertEqual(q1 + q2, frac2Rat(f1 + f2))
            self.assertEqual(q2 + q1, frac2Rat(f1 + f2))
            self.assertEqual(q1 - q2, frac2Rat(f1 - f2))
            self.assertEqual(q2 - q1, frac2Rat(f2 - f1))

            self.assertEqual(q1 * q2, frac2Rat(f1 * f2))
            self.assertEqual(q2 * q1, frac2Rat(f1 * f2))

            q3 = q1 / q2
            f3 = f1 / f2
            self.assertEqual(q3.m, f3.numerator)
            self.assertEqual(q3.n, f3.denominator)

            self.assertEqual(4 + q1, frac2Rat(4 + f1))
            self.assertEqual(q1 + 4, frac2Rat(f1 + 4))
            self.assertEqual(2 - q1, frac2Rat(2 - f1))
            self.assertEqual(q1 - 2, frac2Rat(f1 - 2))
            self.assertEqual(4 * q1, frac2Rat(4 * f1))
            self.assertEqual(q1 * 4, frac2Rat(f1 * 4))

            q3, q4 = 3 / q2, q2 / 3
            f3, f4 = 3 / f2, f2 / 3
            self.assertEqual(q3.m, f3.numerator)
            self.assertEqual(q3.n, f3.denominator)
            self.assertEqual(q4.m, f4.numerator)
            self.assertEqual(q4.n, f4.denominator)
