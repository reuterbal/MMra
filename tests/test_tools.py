#!/usr/bin/python3

import unittest

import sys
import io
from contextlib import contextmanager


@contextmanager
def captured_output():
    """Redirects output, taken from: https://stackoverflow.com/a/17981937"""
    new_out, new_err = io.StringIO(), io.StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestTools(unittest.TestCase):

    def test_print_intermediates(self):
        """Tests print_intermediates()"""
        def testfun(*args):
            import tools
            if tools.is_intermediate_values:
                tools.intermediate_values = [(a, a, a, a) for a in args]
            return 42

        from tools import print_intermediates

        column_headers = ['n', 'A', 'BBB', 'CCCCCC', 'dd']
        expected_output = (" n |     A |   BBB | CCCCCC |    dd\n"
                           "---+-------+-------+--------+-------\n"
                           " 0 | 10000 | 10000 |  10000 | 10000\n"
                           " 1 |     4 |     4 |      4 |     4\n"
                           " 2 |     2 |     2 |      2 |     2\n"
                           " 3 |     1 |     1 |      1 |     1\n")

        with captured_output() as (out, err):
            ret = print_intermediates(testfun, 10000, 4, 2, 1,
                                      column_headers=column_headers)
        output = out.getvalue()

        self.assertEqual(ret, 42)
        self.assertEqual(output, expected_output)
