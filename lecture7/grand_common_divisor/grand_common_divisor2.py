def grand_common_divisor(a: int, b: int):
    if type(a) not in [int] or type(b) not in [int]:
        raise TypeError
    if a <= 0 or b <= 0:
        raise ArithmeticError

    return gcd(a, b)


def gcd(a: int, b: int):
    return a if b == 0 else gcd(b, a % b)


