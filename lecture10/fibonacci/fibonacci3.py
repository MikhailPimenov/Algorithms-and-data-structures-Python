def fibonacci3(n: int):
    return 1 if n < 2 else fibonacci3(n - 1) + fibonacci3(n - 2)


cache = [None] * 100


def fibonacci_cached3(n: int):
    if n > 100:
        return -1

    if cache[n] is None:
        if n < 2:
            cache[n] = 1
        else:
            cache[n] = fibonacci_cached3(n - 1) + fibonacci_cached3(n - 2)
    return cache[n]


def fibonacci_fast3(n: int):
    array = [1] * (n + 1)

    for k in range(2, n + 1):
        array[k] = array[k - 1] + array[k - 2]

    return array[n]


def fibonacci_generator3():
    preprevious = 0
    previous = 1

    while True:
        current = preprevious + previous
        yield current
        preprevious = previous
        previous = current


