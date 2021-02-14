import math


def eratosthenes_sieve(n: int):
    if n < 0:
        raise ArithmeticError
    if type(n) not in [int]:
        raise TypeError

    b = [True for k in range(n + 1)]

    for step in range(2, int(math.sqrt(n + 1) + 1) ):
        for k in range(2 * step, n + 1, step):
            b[k] = False

    for number in range(n + 1):
        if b[number]:
            print(number)
