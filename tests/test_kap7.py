#!/usr/bin/python3

import unittest


class TestKap7(unittest.TestCase):

    def test_eps(self):
        """Tests eps()."""
        from kap7 import eps
        self.assertEqual(eps(), 2.220446049250313e-16)
        # self.assertEqual(eps(), 1.1102230246251565e-16)

    def test_eps_mpmath(self):
        """Tests eps() using arbitrary precision."""
        from kap7 import eps
        from mpmath import mp

        # single
        mp.prec = 24
        self.assertEqual(eps(mp.mpf), mp.mpf('1.1920929e-7'))
        # self.assertEqual(eps(mp.mpf), mp.mpf('5.96046448e-8'))

        # double
        mp.prec = 53
        self.assertEqual(eps(mp.mpf), mp.mpf('2.2204460492503131e-16'))
        # self.assertEqual(eps(mp.mpf), mp.mpf('1.1102230246251565e-16'))

        # long double
        mp.prec = 64
        self.assertEqual(eps(mp.mpf), mp.mpf('1.08420217248550443401e-19'))
        # self.assertEqual(eps(mp.mpf), mp.mpf('5.42101086242752217004e-20'))

        mp.prec = 128
        self.assertEqual(eps(mp.mpf),
                         mp.mpf(('5.87747175411143753984368268611122'
                                 '83890933e-39')))
        # self.assertEqual(eps(mp.mpf),
        #                  mp.mpf(('2.93873587705571876992184134305561'
        #                          '41945467e-39')))

    def test_diff(self):
        """Tests diff()."""
        from kap7 import diff
        from math import sin, cos

        self.assertAlmostEqual(diff(cos, 1, 2**(-28)), -sin(1),
                               delta=2.e-9)
        self.assertAlmostEqual(diff(cos, 1, 2**(-48)), -sin(1),
                               delta=3.e-3)
        self.assertNotAlmostEqual(diff(cos, 1, 2**(-48)), -sin(1),
                                  delta=2.e-3)

    def test_test_eq(self):
        """Tests test_eq()."""
        from kap7 import test_eq

        self.assertTrue(test_eq(1, 3))
        self.assertFalse(test_eq(0.1, 0.3))
