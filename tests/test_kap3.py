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

# Initialize with current system time
random.seed()


def binom(n, k):
    from math import factorial as fac
    return fac(n) // fac(k) // fac(n - k) if k <= n else 1


class TestKap3(unittest.TestCase):

    def test_nchoosek(self):
        """Tests nchoosek() with 10 random numbers."""
        from kap3 import nchoosek
        for _ in range(10):
            n = random.randrange(20)
            k = random.randrange(20)
            self.assertEqual(nchoosek(n, k), binom(n, k))

    def test_pascal(self):
        """Tests pascal() up to N = 20."""
        from kap3 import pascal
        N = 20
        p = pascal(N)
        for n in range(N + 1):
            for k in range(n + 1):
                self.assertEqual(p[n][k], binom(n, k))

    def test_erat(self):
        """Tests erat() with given list of primes."""
        from kap3 import erat
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                  59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
                  127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
                  191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
                  257, 263, 269, 271]
        self.assertEqual(erat(271), primes)
        self.assertEqual(erat(270), primes[:-1])
        self.assertEqual(erat(272), primes)

    def test_probediv(self):
        """Tests probediv() with 10 random numbers."""
        from kap3 import erat, probediv
        from functools import reduce
        for _ in range(10):
            n = random.randrange(1000)
            primes = set(erat(n))
            f = probediv(n)
            self.assertTrue(set(f) <= primes)
            self.assertEqual(reduce(lambda x, y: x * y, f), n)

    def test_fermat_probediv(self):
        """Tests fermat_probediv() with 10 random numbers."""
        from kap3 import fermat_probediv, probediv
        from functools import reduce
        for _ in range(10):
            n = random.randrange(1000)
            f = fermat_probediv(n)
            self.assertEqual(f, probediv(n))
            self.assertEqual(reduce(lambda x, y: x * y, f), n)

    def test_fermat(self):
        """Tests fermat() with 10 random numbers."""
        from kap3 import fermat, probediv
        from functools import reduce
        for _ in range(10):
            n = random.randrange(1000)
            f = fermat(n)
            self.assertEqual(f, probediv(n))
            self.assertEqual(reduce(lambda x, y: x * y, f), n)
