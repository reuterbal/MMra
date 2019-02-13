#!/usr/bin/python3

from math import sqrt


def madhava(n):
    """Approximation von pi / sqrt(12) ueber die
    Reihendarstellung von Madhava.

    Die Partialsummen ergeben sich als
    s_0 = 1,
    s_{n+1} = s_n + (-1)^(n+1) / (3^(n+1) * (2n + 3)).

    :param n: Auswertungslaenge der Reihe.
    :return: n-te Partialsumme der Reihe.
    """
    import tools
    if tools.is_intermediate_values:
        tools.intermediate_values = [(1, sqrt(12))]

    sign, pow3 = 1, 1.
    s = 1
    for k in range(n):
        sign, pow3 = -sign, 3. * pow3
        s += sign / (pow3 * (2 * k + 3))
        if tools.is_intermediate_values:
            tools.intermediate_values.append((s, s * sqrt(12)))
    return s


def atan_taylor(x, n):
    """Approximation von atan(x) unter Verwendung einer
    Taylorentwicklung um x=0.

    :param n: Anzahl Reihenglieder.
    :return: Approximation fuer atan(x).
    """
    sign, pow2k1 = 1, x
    arctan = 0
    for k in range(n):
        arctan += sign * pow2k1 / (2 * k + 1)
        sign, pow2k1 = -sign, pow2k1 * x * x
    return arctan


def machin(n):
    """Approximation von pi / 4 ueber die Approximations-
    form von John Machin unter Verwendung der
    Taylorapproximation des arctan um x = 0.

    :param n: Anzahl Reihenglieder fuer arctan.
    :return: Approximation fuer pi / 4.
    """
    return (4 * atan_taylor(1 / 5, n) -
            atan_taylor(1 / 239, n))


def compute_pk(x, y, s):
    """Berechnet den Naeherungswert p_k fuer Pi aus den
    Iterierten x_k, y_k, s_k des Brent-Salamin-Verfahrens.
    """
    return (x + y) * (x + y) / (2 * s)


def brent_salamin(n, fn_sqrt=sqrt):
    """Berechnet eine Naeherung fuer Pi mittels des
    Brent-Salamin-Verfahrens.

    :param n: Anzahl Iterationen.
    :param fn_sqrt: Zur Wurzel-Approximation zu verwendende
                    Funktion (optional).
    :return: Approximation von Pi.
    """
    import tools
    if tools.is_intermediate_values:
        tools.intermediate_values = [(1, 1 / fn_sqrt(2), 0.5,
                                      compute_pk(1, 1 / fn_sqrt(2), 0.5))]

    x, y, s = 1, 1 / fn_sqrt(2), 0.5
    for k in range(n):
        x, x_old, y = (x + y) / 2, x, fn_sqrt(x * y)
        s -= 2**(k + 1) * (x - x_old) * (x - x_old)
        if tools.is_intermediate_values:
            tools.intermediate_values.append((x, y, s, compute_pk(x, y, s)))
    return compute_pk(x, y, s)


def next_ramanujan(k, fak_k, fak_4k, pow_4k):
    """Hilfsfunktion, die das naechste Glied der
    Ramanujan-Reihe berechnet.

    :param k: Index des Glieds.
    :param fak_k: Wert fuer k!.
    :param fak_4k: Wert fuer (4k)!.
    :param pow_4k: Wert fuer 396^(4k).
    :return: Naechstes Summenglied.
    """
    fak_k_2 = fak_k * fak_k
    return (fak_4k * (1103 + 26390 * k) /
            (fak_k_2 * fak_k_2 * pow_4k))


def ramanujan(n, T=float, fn_sqrt=sqrt):
    """Berechnet eine Naherung fuer 1/Pi mittels der
    Reihendarstellung von Ramanujan.

    :param n: Anzahl Reihenglieder.
    :param T: Datentyp fuer Zahlendarstellung (optional).
    :param fn_sqrt: Funktion zur Wurzelberechnung (optional).
    :return: Approximation fuer 1/Pi.
    """
    coef = 2 * fn_sqrt(2) / 9801
    pow_396_4 = T(396 * 396 * 396 * 396)
    fak_k, fak_4k, pow_4k = T(1), T(1), T(1)
    s = next_ramanujan(0, fak_k, fak_4k, pow_4k)

    import tools
    if tools.is_intermediate_values:
        tools.intermediate_values = [(coef * s, 1 / (coef * s))]

    for k in range(1, n + 1):
        fak_k, pow_4k = fak_k * k, pow_4k * pow_396_4
        fak_4k *= (4 * k * (4 * k - 1) * (4 * k - 2) *
                   (4 * k - 3))
        s += next_ramanujan(k, fak_k, fak_4k, pow_4k)
        if tools.is_intermediate_values:
            tools.intermediate_values.append((coef * s, 1 / (coef * s)))
    return coef * s
