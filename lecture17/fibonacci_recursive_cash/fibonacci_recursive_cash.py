cash = [None] * 10000


def fibonacci_recursive_cash(n: int) -> int:
    if n < 0 or n > 10000:
        raise ArithmeticError

    if cash[n] is None:
        if n < 2:
            cash[n] = n
        else:
            cash[n] = fibonacci_recursive_cash(n - 1) + fibonacci_recursive_cash(n - 2)
    return cash[n]
