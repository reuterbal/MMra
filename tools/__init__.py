#!/usr/bin/python3

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
