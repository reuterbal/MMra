#!/usr/bin/python3


def nchoosek(n, k):
    """Berechnet den Binomialkoeffizienten "n ueber k",
    definiert als n! / (k! * (n-k)!).

    :param n: Positive Ganzzahl.
    :param k: Positive Ganzzahl.
    :return: Binomialkoeffizient.
    """
    k = min(k, n - k)
    denominator = 1
    for i in range(1, k + 1):
        denominator = denominator * i
    nominator = 1
    for i in range(n - k + 1, n + 1):
        nominator = nominator * i
    return nominator // denominator


def pascal(N):
    """Berechnet alle Binomialkoeffizienten "n ueber k"
    mit 0 <= n <= N, 0 <= k <= n und gibt diese als
    Liste von Listen zurueck, wobei Eintrag [n][k]
    dem Binomialkoeffizienten "n ueber k" entspricht.

    :param N: Maximalwert fuer n (und k), positive Ganzzahl.
    :return: Liste von Listen mit Binomialkoeffizienten.
    """
    dreieck = [[1]]
    for n in range(1, N + 1):
        zeile = (n + 1) * [1]
        for k in range(1, n):
            zeile[k] = (dreieck[n - 1])[k - 1] + (dreieck[n - 1])[k]
        dreieck = dreieck + [zeile]
    return dreieck
