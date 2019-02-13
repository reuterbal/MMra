#!/usr/bin/python3

import unittest
import random

# Initialize with current system time
random.seed()


class TestKap2(unittest.TestCase):

    def test_str(self):
        """Tests __str__() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            i = random.randrange(100)
            n = NatuerlicheZahl(i)
            self.assertEqual(str(n), str(i))

    def test_repr(self):
        """Tests __repr__() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            i = random.randrange(100)
            n = NatuerlicheZahl(i)
            self.assertEqual(repr(n), 'NatuerlicheZahl({})'.format(i))

    def test_eq(self):
        """Tests 'm == n'."""
        from kap2 import NatuerlicheZahl
        self.assertNotEqual(NatuerlicheZahl(5), 7)
        self.assertNotEqual(5, NatuerlicheZahl(7))
        self.assertEqual(NatuerlicheZahl(5), 5)
        self.assertEqual(5, NatuerlicheZahl(5))
        self.assertEqual(NatuerlicheZahl(3), NatuerlicheZahl(3))
        self.assertEqual(NatuerlicheZahl(7 / 2), NatuerlicheZahl(3))
        self.assertEqual(NatuerlicheZahl(2), NatuerlicheZahl(2.7))

    def test_next(self):
        """Tests next() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            i = random.randrange(100)
            n = NatuerlicheZahl(i)
            self.assertEqual(n.next(), NatuerlicheZahl(i + 1))

    def test_prev(self):
        """Tests prev() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            i = random.randrange(1, 100)
            n = NatuerlicheZahl(i)
            self.assertEqual(n.prev(), NatuerlicheZahl(i - 1))

    def test_add(self):
        """Tests __add__() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            a, b = random.randrange(100), random.randrange(100)
            m, n = NatuerlicheZahl(a), NatuerlicheZahl(b)
            self.assertEqual(m + n, NatuerlicheZahl(a + b))
            m += n
            self.assertEqual(m, NatuerlicheZahl(a + b))

    def test_mul(self):
        """Tests __mul__() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            a, b = random.randrange(100), random.randrange(100)
            m, n = NatuerlicheZahl(a), NatuerlicheZahl(b)
            self.assertEqual(m * n, NatuerlicheZahl(a * b))
            m *= n
            self.assertEqual(m, NatuerlicheZahl(a * b))

    def test_le(self):
        """Tests __le__() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            a, b = random.randrange(100), random.randrange(100)
            m, n = NatuerlicheZahl(a), NatuerlicheZahl(b)
            self.assertEqual(m <= n, a <= b)

    def test_sub(self):
        """Tests __sub__() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            a, b = random.randrange(100), random.randrange(100)
            m, n = NatuerlicheZahl(a), NatuerlicheZahl(b)
            if a <= b:
                self.assertEqual(n - m, NatuerlicheZahl(b - a))
            else:
                with self.assertRaises(ValueError):
                    n - m

    def test_div(self):
        """Tests divmod() and '//' with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            a, b = random.randrange(100), random.randrange(1, 100)
            m, n = NatuerlicheZahl(a), NatuerlicheZahl(b)
            k, l = divmod(a, b)
            self.assertEqual(divmod(m, n),
                             (NatuerlicheZahl(k), NatuerlicheZahl(l)))
            self.assertEqual(m // n, NatuerlicheZahl(a // b))
            self.assertEqual(m % n, NatuerlicheZahl(a % b))
        with self.assertRaises(ValueError):
            divmod(NatuerlicheZahl(random.randrange(100)), NatuerlicheZahl(0))

    def test_umwandlung_pq(self):
        """Tests umwandlung_pq() with given numbers and bases."""
        from kap2 import Stellenwertsystem, umwandlung_pq
        self.assertEqual(umwandlung_pq(Stellenwertsystem(2, [0, 0, 1, 1]), 10),
                         Stellenwertsystem(10, [2, 1]))
        self.assertEqual(umwandlung_pq(Stellenwertsystem(23, [18, 9, 1]), 10),
                         Stellenwertsystem(10, [4, 5, 7]))
        self.assertEqual(umwandlung_pq(Stellenwertsystem(23, [18, 9, 1]), 9),
                         Stellenwertsystem(9, [7, 2, 0, 1]))
        self.assertEqual(umwandlung_pq(Stellenwertsystem(9, [7, 2, 0, 1]), 23),
                         Stellenwertsystem(23, [18, 9, 1]))

    def test_ibn_al_banna(self):
        """Tests ibn_al_banna() with random numbers and bases."""
        from kap2 import Stellenwertsystem, ibn_al_banna
        p = random.randrange(1, 25)
        len_na = random.randrange(8)
        len_nb = random.randrange(8)
        na = [random.randrange(p) for _ in range(len_na)]
        nb = [random.randrange(p) for _ in range(len_nb)]

        fa = 0
        for k in range(len(na)):
            fa += na[k] * p**k

        fb = 0
        for k in range(len(nb)):
            fb += nb[k] * p**k

        nc = ibn_al_banna(Stellenwertsystem(p, na), Stellenwertsystem(p, nb))

        fc = 0
        for k in range(len(nc)):
            fc += int(nc[k]) * p**k

        self.assertEqual(fc, fa * fb)

    def test_plusrek(self):
        """Tests plusrek() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            a, b = random.randrange(100), random.randrange(100)
            m, n = NatuerlicheZahl(a), NatuerlicheZahl(b)
            self.assertEqual(m.plusrek(n), NatuerlicheZahl(a + b))

    def test_multrek(self):
        """Tests multrek() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            a, b = random.randrange(100), random.randrange(100)
            m, n = NatuerlicheZahl(a), NatuerlicheZahl(b)
            self.assertEqual(m.multrek(n), NatuerlicheZahl(a * b))

    def test_kleinergleichrek(self):
        """Tests kleinergleichrek() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            a, b = random.randrange(100), random.randrange(100)
            m, n = NatuerlicheZahl(a), NatuerlicheZahl(b)
            self.assertEqual(m.kleinergleichrek(n), a <= b)

    def test_subrek(self):
        """Tests subrek() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            a, b = random.randrange(100), random.randrange(100)
            m, n = NatuerlicheZahl(a), NatuerlicheZahl(b)
            if a <= b:
                self.assertEqual(n.subrek(m), NatuerlicheZahl(b - a))
            else:
                with self.assertRaises(ValueError):
                    n.subrek(m)

    def test_divmodrek(self):
        """Tests divmodrek() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            a, b = random.randrange(100), random.randrange(1, 100)
            m, n = NatuerlicheZahl(a), NatuerlicheZahl(b)
            k, l = divmod(a, b)
            self.assertEqual(m.divmodrek(n),
                             (NatuerlicheZahl(k), NatuerlicheZahl(l)))
        with self.assertRaises(ValueError):
            NatuerlicheZahl(random.randrange(100)).divmodrek(
                NatuerlicheZahl(0))

    def test_horner(self):
        """Tests horner() with a random polynomial."""
        from kap2 import horner, Stellenwertsystem
        p = random.randrange(1, 15)
        len_n = random.randrange(10)
        n = [random.randrange(p) for _ in range(len_n)]

        f = 0
        for k in range(len_n):
            f += n[k] * p**k

        self.assertEqual(horner(Stellenwertsystem(p, n), p), f)

    def test_umwandlung(self):
        """Tests umwandlung() with given numbers and bases."""
        from kap2 import Stellenwertsystem, NatuerlicheZahl, umwandlung
        self.assertEqual(umwandlung(12, 2), Stellenwertsystem(2, [0, 0, 1, 1]))
        self.assertEqual(umwandlung(NatuerlicheZahl(754), NatuerlicheZahl(23)),
                         Stellenwertsystem(NatuerlicheZahl(23),
                                           [NatuerlicheZahl(18),
                                            NatuerlicheZahl(9),
                                            NatuerlicheZahl(1)]))
        self.assertEqual(umwandlung(754, 9),
                         Stellenwertsystem(9, [7, 2, 0, 1]))

    def test_fast_differenz(self):
        """Tests fast_differenz() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            a, b = random.randrange(100), random.randrange(100)
            m, n = NatuerlicheZahl(a), NatuerlicheZahl(b)
            if a <= b:
                self.assertEqual(n.fast_differenz(m), NatuerlicheZahl(b - a))
            else:
                self.assertEqual(n.fast_differenz(m), None)

    def test_fast_differenzrek(self):
        """Tests fast_differenzrek() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            a, b = random.randrange(100), random.randrange(100)
            m, n = NatuerlicheZahl(a), NatuerlicheZahl(b)
            if a <= b:
                self.assertEqual(n.fast_differenzrek(m),
                                 NatuerlicheZahl(b - a))
            else:
                self.assertEqual(n.fast_differenzrek(m), None)

    def test_pow(self):
        """Tests __pow__() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            a, b = random.randrange(4), random.randrange(10)
            m, n = NatuerlicheZahl(a), NatuerlicheZahl(b)
            self.assertEqual(n**m, NatuerlicheZahl(b**a))

    def test_lt(self):
        """Tests __lt__() with 10 random numbers."""
        from kap2 import NatuerlicheZahl
        for _ in range(10):
            a, b = random.randrange(100), random.randrange(100)
            m, n = NatuerlicheZahl(a), NatuerlicheZahl(b)
            self.assertEqual(m < n, a < b)

    def test_fib(self):
        """Tests fib()."""
        from kap2 import fib
        series = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

        for n, f in enumerate(series):
            self.assertEqual(fib(n), f)

    def test_fib_rek(self):
        """Tests fib_rek()."""
        from kap2 import fib_rek
        series = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

        for n, f in enumerate(series):
            self.assertEqual(fib_rek(n), f)
