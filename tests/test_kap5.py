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

import unittest

from math import sqrt, pi, sin


class TestTools(unittest.TestCase):

    def test_heron(self):
        """Tests heron()"""
        from kap5 import heron

        a = sqrt(2)
        self.assertAlmostEqual(heron(2), a, delta=1.e-12)
        self.assertAlmostEqual(heron(2, iters=10), a, delta=1.e-15)
        self.assertAlmostEqual(heron(2, iters=10, x0=100), a, delta=1e-12)

    def test_heron_mpmath(self):
        """"Tests heron() with arbitrary precision"""
        from kap5 import heron
        from mpmath import mp

        mp.dps = 128
        mp.pretty = False
        A = mp.mpf(('1.4142135623730950488016887242096980785696718753769480731'
                    '766797379907324784621070388503875343276416016397857783845'
                    '578298249912463702'))
        a = heron(mp.mpf(2), 7, mp.mpf(1.))
        self.assertEqual(a, A)

    def test_fixpunkt_iter(self):
        """Tests fixpunkt_iter()"""
        from kap5 import fixpunkt_iter

        self.assertAlmostEqual(fixpunkt_iter(2, 0.1, iters=20, x0=1.),
                               1.4086498221483836, delta=1.e-15)
        self.assertAlmostEqual(fixpunkt_iter(2, 0.25, iters=20, x0=1.),
                               1.4142130679985319, delta=1.e-15)
        self.assertAlmostEqual(fixpunkt_iter(2, 0.4, iters=20, x0=1.),
                               1.4142135623730883, delta=1.e-15)

    def test_fixpunkt_res(self):
        """Tests fixpunkt_res()"""
        from kap5 import fixpunkt_res

        self.assertAlmostEqual(fixpunkt_res(2, 0.5),
                               1.414213562373095, delta=1.e-15)
        self.assertAlmostEqual(fixpunkt_res(2, 0.25),
                               1.4142135623733307, delta=1.e-15)

    def test_fixpunkt_aposteriori(self):
        """Tests fixpunkt_aposteriori()"""
        from kap5 import fixpunkt_aposteriori

        self.assertAlmostEqual(fixpunkt_aposteriori(2, 0.5, 1.141),
                               1.414213562373095, delta=1.e-15)
        self.assertAlmostEqual(fixpunkt_aposteriori(2, 0.25, 1.141),
                               1.4142135623726237, delta=1.e-15)

    def test_fixpunkt(self):
        """Tests fixpunkt()"""
        from kap5 import fixpunkt

        self.assertEqual(fixpunkt(lambda x: x, 1), 1)
        self.assertEqual(fixpunkt(lambda x: x, 0), 0)
        self.assertEqual(fixpunkt(lambda x: 2 * x, 1), 2**20)
        self.assertEqual(fixpunkt(lambda x: 2 * x, 0), 0)
        self.assertEqual(fixpunkt(lambda x: x / 2, 1), 2**(-20))

    def test_bisektion(self):
        """Tests bisektion()"""
        from kap5 import bisektion

        self.assertAlmostEqual(bisektion(lambda x: x * x - 2, 1, 2),
                               1.4142135623731065, delta=1.e-15)

    def test_newton(self):
        """Tests newton()"""
        from kap5 import newton

        self.assertAlmostEqual(newton(lambda x: x * x - 2, lambda x: 2 * x, 1),
                               sqrt(2), delta=1.e-18)
        self.assertAlmostEqual(newton(lambda x: x * x - 7, lambda x: 2 * x, 1.,
                                      eps=1.e-10),
                               sqrt(7), delta=1.e-12)

    def test_heron_abbruchkriterium(self):
        """Tests heron_abbruchkriterium()"""
        from kap5 import heron_abbruchkriterium as heron

        a = sqrt(2)
        self.assertAlmostEqual(heron(2, 1), a, delta=1.e-12)
        self.assertAlmostEqual(heron(2, 1, eps=1.e-15), a, delta=1.e-15)
        self.assertAlmostEqual(heron(2, 100), a, delta=1e-12)

    def test_heron_fehlerschaetzer(self):
        """Tests heron_fehlerschaetzer()"""
        from kap5 import heron_fehlerschaetzer as heron

        a = sqrt(2)
        self.assertAlmostEqual(heron(2, 1, 1.141), a, delta=1.e-12)
        self.assertAlmostEqual(heron(2, 1, 1.141, eps=1.e-15), a, delta=1.e-15)
        self.assertAlmostEqual(heron(2, 100, 1.141), a, delta=1e-12)

    def test_heron_kombiniert(self):
        """Tests heron_kombiniert()"""
        from kap5 import heron_kombiniert as heron

        a = sqrt(2)
        self.assertAlmostEqual(heron(2, 1, 1.141), a, delta=1.e-12)
        self.assertAlmostEqual(heron(2, 1, 1.141, eps=1.e-15), a, delta=1.e-15)
        self.assertAlmostEqual(heron(2, 100, 1.141), a, delta=1e-12)

    def test_shifting_root(self):
        """Tests shifting_root()"""
        from kap5 import shifting_root

        self.assertEqual(shifting_root(2538413.6976, 2, 10),
                         sqrt(2538413.6976))
        self.assertEqual(shifting_root(2916, 2), 54)
        self.assertAlmostEqual(shifting_root(3, 2), sqrt(3), delta=1.e-10)
        self.assertAlmostEqual(shifting_root(5, 3), pow(5, 1 / 3), delta=1e-10)

    def test_trapez(self):
        """Tests trapez()."""
        from kap5 import trapez

        # Beispiele aus Buch
        I = trapez(lambda x: sqrt(1 - x * x), 0, 1, 10)
        self.assertAlmostEqual(I, pi / 4, delta=9.e-6)
        I = trapez(lambda x: 1 / (1 + x * x), 0, 1, 10)
        self.assertAlmostEqual(I, pi / 4, delta=4.e-8)

    def test_romberg(self):
        """Tests romberg()."""
        from kap5 import trapez, romberg

        # Beispiele aus Buch
        s = [trapez(lambda x: 1 / (1 + x * x), 0, 1, i) for i in range(1, 11)]
        self.assertAlmostEqual(romberg(s), pi / 4, delta=4.e-16)

    def test_trapez_allg(self):
        """Tests trapez_allg()."""
        from kap5 import trapez_allg
        n = 1024

        # Aequidistant
        x = [i / n for i in range(n + 1)]

        I = trapez_allg(lambda x: sqrt(1 - x * x), x)
        self.assertAlmostEqual(I, pi / 4, delta=9.e-6)

        I = trapez_allg(lambda x: 1 / (1 + x * x), x)
        self.assertAlmostEqual(I, pi / 4, delta=4.e-8)

        # Gehaeuft
        x = [sin(0.5 * i * pi / n) for i in range(n + 1)]
        I = trapez_allg(lambda x: sqrt(1 - x * x), x)
        self.assertAlmostEqual(I, pi / 4, delta=5.e-7)

    def test_archimedes1(self):
        """Tests archimedes1()."""
        from kap5 import archimedes1

        u, U = archimedes1(10)
        self.assertAlmostEqual(u / 2, pi, delta=2.e-7)
        self.assertNotAlmostEqual(u / 2, pi, delta=1.e-7)
        self.assertAlmostEqual(U / 2, pi, delta=3.e-7)
        self.assertNotAlmostEqual(U / 2, pi, delta=2.e-7)

        u, U = archimedes1(20)
        self.assertAlmostEqual(u / 2, pi, delta=2.e-13)
        self.assertNotAlmostEqual(u / 2, pi, delta=1.e-13)
        self.assertAlmostEqual(U / 2, pi, delta=1.e-12)
        self.assertNotAlmostEqual(U / 2, pi, delta=1.e-13)

    def test_archimedes2(self):
        """Tests archimedes2()."""
        from kap5 import archimedes2

        u, U = archimedes2(13)
        self.assertAlmostEqual(u / 2, pi, delta=1.e-8)
        self.assertNotAlmostEqual(u / 2, pi, delta=1.e-9)
        self.assertAlmostEqual(U / 2, pi, delta=2.e-9)
        self.assertNotAlmostEqual(U / 2, pi, delta=1.e-9)

        u, U = archimedes2(20)
        self.assertAlmostEqual(u / 2, pi, delta=1.e-4)
        self.assertNotAlmostEqual(u / 2, pi, delta=1.e-5)
        self.assertAlmostEqual(U / 2, pi, delta=1.e-4)
        self.assertNotAlmostEqual(U / 2, pi, delta=1.e-5)

    def test_archimedes3(self):
        """Tests archimedes3()."""
        from kap5 import archimedes3

        u, U = archimedes3(10)
        self.assertAlmostEqual(u / 2, pi, delta=2.e-7)
        self.assertNotAlmostEqual(u / 2, pi, delta=1.e-7)
        self.assertAlmostEqual(U / 2, pi, delta=3.e-7)
        self.assertNotAlmostEqual(U / 2, pi, delta=2.e-7)

        u, U = archimedes3(20)
        self.assertAlmostEqual(u / 2, pi, delta=1.e-12)
        self.assertNotAlmostEqual(u / 2, pi, delta=1.e-13)
        self.assertAlmostEqual(U / 2, pi, delta=1.e-12)
        self.assertNotAlmostEqual(U / 2, pi, delta=1.e-13)

    def test_madhava(self):
        """Tests madhava()."""
        from kap5 import madhava

        s = madhava(10)
        self.assertAlmostEqual(s * sqrt(12), pi, delta=1.e-6)
        self.assertNotAlmostEqual(s * sqrt(12), pi, delta=1.e-7)

        s = madhava(20)
        self.assertAlmostEqual(s * sqrt(12), pi, delta=1.e-11)
        self.assertNotAlmostEqual(s * sqrt(12), pi, delta=1.e-12)

    def test_machin(self):
        """Tests machin()."""
        from kap5 import machin

        self.assertAlmostEqual(machin(4) * 4, pi, delta=9.e-7)
        self.assertNotAlmostEqual(machin(4) * 4, pi, delta=8.e-7)

        self.assertAlmostEqual(machin(10) * 4, pi, delta=1.e-15)
        self.assertNotAlmostEqual(machin(10) * 4, pi, delta=1.e-16)

    def test_brent_salamin(self):
        """Tests brent_salamin()."""
        from kap5 import brent_salamin

        self.assertAlmostEqual(brent_salamin(2), pi, delta=1.e-8)
        self.assertNotAlmostEqual(brent_salamin(2), pi, delta=1.e-9)

    def test_brent_salamin_mpmath(self):
        """Tests brent_salamin()."""
        from kap5 import brent_salamin
        from mpmath import mp

        mp.dps = 128

        self.assertAlmostEqual(brent_salamin(5, mp.sqrt), mp.pi,
                               delta=mp.mpf('1.e-83'))
        self.assertNotAlmostEqual(brent_salamin(5, mp.sqrt), mp.pi,
                                  delta=mp.mpf('1.e-84'))

    def test_ramanujan(self):
        """Tests ramanujan()."""
        from kap5 import ramanujan

        self.assertAlmostEqual(1 / ramanujan(1), pi, delta=5.e-16)
        self.assertNotAlmostEqual(1 / ramanujan(1), pi, delta=1.e-16)

    def test_ramanujan_mpmath(self):
        """Tests ramanujan()."""
        from kap5 import ramanujan
        from mpmath import mp

        mp.dps = 128

        self.assertAlmostEqual(1 / ramanujan(10, mp.mpf, mp.sqrt), mp.pi,
                               delta=mp.mpf('5.e-88'))
        self.assertNotAlmostEqual(1 / ramanujan(10, mp.mpf, mp.sqrt), mp.pi,
                                  delta=mp.mpf('4.e-88'))
