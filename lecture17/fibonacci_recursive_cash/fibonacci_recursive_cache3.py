cache = [None] * 1000


def fibonacci_recursive_cache3(number: int):
    if type(number) != int:
        raise TypeError
    if number < 0:
        raise ArithmeticError

    if cache[number] is None:
        if number < 2:
            cache[number] = number
        else:
            cache[number] = fibonacci_recursive_cache3(number - 1) + fibonacci_recursive_cache3(number - 2)
    return cache[number]
