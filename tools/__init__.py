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

# A bool-variable that indicates whether intermediate values
# should be stored.
# This is used, e.g., to examine convergence behaviour afterwards.
# Intermediate values should be stored in the global variable
# 'intermediate_values' as a list of tuples.
is_intermediate_values = False

# Global list of tuples. Used in conjunction with 'is_intermediate_values'.
intermediate_values = []


def print_intermediates(f, *args, column_headers=None, tostr=str):
    """Helper function that calls the given function with the
    specified parameters and prints intermediate values.

    The output is displayed using print(). Optionally, you
    can provide column headers that are printed before the
    actual output. Note that the first column is always
    a counter starting from 0.

    The function of which the convergence is to be displayed
    must check if the global variable 'is_intermediate_values'
    is True and write intermediate values as a list of tuples
    to a global variable 'intermediate values'.

    :param f: The function to be called
    :param args: An arbitrary number of arguments that should be
        passed to the function f.
    :param column_headers: An optional list of strings that are
        used as column headers.
    :param tostr: An optional function that is used to convert
        numbers to their string representation.
    """
    global is_intermediate_values
    is_intermediate_values, iiv_old = True, is_intermediate_values

    try:
        ret = f(*args)
    finally:
        is_intermediate_values = iiv_old

    print_list = [(tostr(l[0]),) + tuple(tostr(a) for a in l[1])
                  for l in enumerate(intermediate_values)]
    max_lengths = list(map(lambda l: max(l, key=len), zip(*print_list)))

    if column_headers is not None:
        max_lengths = list(map(lambda l: max(l, key=len),
                               zip(max_lengths, column_headers)))

    max_lengths = [len(a) for a in max_lengths]
    format_list = ['{{:>{0}}}'.format(l) for l in max_lengths]
    format_string = ' ' + ' | '.join(format_list)

    if column_headers is not None:
        print(format_string.format(*column_headers))
        print('+'.join([(l + 2) * '-' for l in max_lengths]))

    for a in print_list:
        print(format_string.format(*a))

    return ret
