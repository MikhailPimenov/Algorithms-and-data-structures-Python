def grand_common_divisor(a: int, b: int):
    if type(a) not in [int]:
        raise TypeError
    if type(b) not in [int]:
        raise TypeError

    if a <= 0 or b <= 0:
        raise ArithmeticError

    if a % b == 0:
        return b

    return grand_common_divisor(b, a % b)
