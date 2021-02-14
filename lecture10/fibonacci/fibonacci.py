def fibonacci(n: int):
    assert n < 40
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_dynamic(n: int):
    array = [0] * (n + 1)
    array[0] = 0
    array[1] = 1

    for k in range(2, n + 1):
        array[k] = array[k - 1] + array[k - 2]

    return array[n]


cash = [None] * 10000


def fibonacci_cashed(n: int):
    assert 0 <= n < 10000
    if cash[n] is None:
        if n < 2:
            cash[n] = n
        else:
            cash[n] = fibonacci_cashed(n - 1) + fibonacci_cashed(n - 2)
    return cash[n]


def fibonacci_generator(n: int):
    preprevious = 0
    previous = 1
    for k in range(0, n + 1):
        current = preprevious + previous
        yield current
        preprevious = previous
        previous = current


# for k in fibonacci_generator(100):
#     print(k)
