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
