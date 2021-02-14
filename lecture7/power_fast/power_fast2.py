def power_fast(base: int, n: int):
    if type(base) != int:
        raise TypeError
    if type(n) != int:
        raise TypeError
    if base < 0:
        raise ArithmeticError
    if n < 0:
        raise ArithmeticError

    if n == 0:
        return 1
    if n % 2 != 0:
        return base * power_fast(base * base, (n - 1) // 2)
    return base * power_fast(base, n - 1)

