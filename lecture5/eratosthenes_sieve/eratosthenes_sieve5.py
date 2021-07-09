from math import sqrt


def eratosthenes_sieve5(n: int) -> None:
    if type(n) != int:
        raise TypeError

    if n < 0:
        raise ArithmeticError

    f = [True] * n

    for divisor in range(2, int(sqrt(n) + 1)):
        for number in range(2 * divisor, n, divisor):
            if f[number]:
                f[number] = False

    for number in range(n):
        if f[number]:
            print(number)
