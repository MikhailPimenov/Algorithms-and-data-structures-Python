def power_fast(base: int, power: int):
    if type(base) not in [int]:
        raise TypeError
    if type(power) not in [int]:
        raise  TypeError
    if base < 0 or power < 0:
        raise ArithmeticError


    if power == 0:
        return 1

    if power % 2 == 0:
        return power_fast(base * base, power // 2)
    else:
        return power_fast(base, power - 1) * base
