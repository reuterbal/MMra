#!/usr/bin/python3


def fib(n):
    """Ermittelt das n-te Folgenglied der Fibonacci-Folge,
    die definiert ist als a_{n+1} = a_n + a_{n-1} mit
    a_0 = 0, a_1 = 1.

    :param n: Index des Folgenglieds, n >= 0.
    :return: n-tes Folgenglied.
    """
    if n < 1:
        return 0
    else:
        b, a = 0, 1
        for _ in range(n - 1):
            b, a = a, a + b
        return a


def fib_rek(n):
    """Ermittelt das n-te Folgenglied der Fibonacci-Folge,
    die definiert ist als a_{n+1} = a_n + a_{n-1} mit
    a_0 = 0, a_1 = 1.

    Rekursive Implementierung.

    :param n: Index des Folgenglieds, n >= 0.
    :return: n-tes Folgenglied.
    """
    if n < 1:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rek(n - 1) + fib_rek(n - 2)
