def fibonacci5(n: int) -> int:
    if n == 0 or n == 1:
        return n

    return fibonacci5(n - 1) + fibonacci5(n - 2)


cache = [None] * 1000


def fibonacci5_recursive_cache(n: int) -> int:
    if cache[n] is None:
        if n == 0 or n == 1:
            cache[n] = n
        else:
            cache[n] = fibonacci5_recursive_cache(n - 1) + fibonacci5_recursive_cache(n - 2)

    return cache[n]


def fibonacci5_dynamic_programming(n: int) -> int:
    f = [None] * (n + 2)

    f[0] = 0
    f[1] = 1

    for i in range(2, n):
        f[i] = f[i - 1] + f[i - 2]

    return f[n - 1]


def fibonacci5_generator() -> int:
    preprevious = 0
    previous = 1

    while True:
        yield preprevious + previous
        preprevious, previous = previous, preprevious + previous
