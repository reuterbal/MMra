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
import random
import math

# Initialize with current system time
random.seed()


class TestKap6(unittest.TestCase):

    def test_KomplexeZahl(self):
        """Tests datatype KomplexeZahl."""
        from kap6 import KomplexeZahl

        def c2C(z):
            return KomplexeZahl(z.real, z.imag)

        for _ in range(10):
            ab1 = (random.uniform(-10, 10), random.uniform(-10, 10))
            ab2 = (random.uniform(-10, 10), random.uniform(-10, 10))
            z1, z2 = complex(*ab1), complex(*ab2)
            c1, c2 = KomplexeZahl(*ab1), KomplexeZahl(*ab2)

            self.assertEqual(c1.re, ab1[0])
            self.assertEqual(c1.im, ab1[1])
            self.assertEqual(str(c1), '{}{:+}i'.format(*ab1))
            self.assertEqual(repr(c1), 'KomplexeZahl({}, {})'.format(*ab1))

            self.assertEqual(abs(c1),
                             math.sqrt(ab1[0] * ab1[0] + ab1[1] * ab1[1]))
            self.assertEqual(abs(c2),
                             math.sqrt(ab2[0] * ab2[0] + ab2[1] * ab2[1]))

            self.assertEqual(c1, KomplexeZahl(*ab1))
            self.assertNotEqual(c1, KomplexeZahl(ab1[0] + 1, ab1[1] - 1))

            self.assertEqual(+c1, c1)
            self.assertEqual(+c2, c2)
            self.assertEqual(-c1, KomplexeZahl(-ab1[0], -ab1[1]))
            self.assertEqual(-c2, KomplexeZahl(-ab2[0], -ab2[1]))

            self.assertEqual(c1 + c2, c2C(z1 + z2))
            self.assertEqual(c2 + c1, c2C(z1 + z2))
            self.assertEqual(c1 - c2, c2C(z1 - z2))
            self.assertEqual(c2 - c1, c2C(z2 - z1))

            self.assertEqual(c1 * c2, c2C(z1 * z2))
            self.assertEqual(c2 * c1, c2C(z1 * z2))

            c3, c4 = c1 / c2, c2 / c1
            z3, z4 = z1 / z2, z2 / z1
            self.assertAlmostEqual(c3.re, z3.real, delta=1e-12)
            self.assertAlmostEqual(c3.im, z3.imag, delta=1e-12)
            self.assertAlmostEqual(c4.re, z4.real, delta=1e-12)
            self.assertAlmostEqual(c4.im, z4.imag, delta=1e-12)

            self.assertEqual(4 + c1, c2C(4 + z1))
            self.assertEqual(c1 + 4, c2C(z1 + 4))
            self.assertEqual(2 - c1, c2C(2 - z1))
            self.assertEqual(c1 - 2, c2C(z1 - 2))
            self.assertEqual(4 * c1, c2C(4 * z1))
            self.assertEqual(c1 * 4, c2C(z1 * 4))

            c3, c4 = 3 / c2, c2 / 3
            z3, z4 = 3 / z2, z2 / 3
            self.assertAlmostEqual(c3.re, z3.real, delta=1e-12)
            self.assertAlmostEqual(c3.im, z3.imag, delta=1e-12)
            self.assertAlmostEqual(c4.re, z4.real, delta=1e-12)
            self.assertAlmostEqual(c4.im, z4.imag, delta=1e-12)

    def test_polar(self):
        """Tests polar()."""
        from kap6 import KomplexeZahl, polar
        import cmath
        from math import pi

        for _ in range(10):
            ab = (random.uniform(-10, 10), random.uniform(-10, 10))
            z, c = complex(*ab), KomplexeZahl(*ab)

            def shift2int(rp):
                if rp[1] < 0:
                    return (rp[0], rp[1] + 2 * pi)
                else:
                    return rp

            p1, p2 = polar(c), shift2int(cmath.polar(z))
            self.assertAlmostEqual(p1[0], p2[0], delta=1e-12)
            self.assertAlmostEqual(p1[1], p2[1], delta=1e-12)
