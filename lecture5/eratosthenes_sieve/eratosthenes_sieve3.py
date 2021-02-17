from math import sqrt


def eratosthenes_sieve(number: int):
    if type(number) not in [int]:
        raise TypeError

    if number < 0:
        raise ArithmeticError

    array = [True] * number

    for divisor in range(2, int(sqrt(number)) + 1):
        for index in range(2 * divisor, number, divisor):
            array[index] = False

    for index in range(number):
        if array[index]:
            print(index)
