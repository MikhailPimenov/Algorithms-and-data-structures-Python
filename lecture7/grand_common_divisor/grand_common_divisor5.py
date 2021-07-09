def parameter_checker(wrappee):
    def wrapper(a: int, b: int):
        if type(a) != int or type(b) != int:
            raise TypeError
        if a < 0 or b < 0:
            raise ArithmeticError

        return wrappee(a, b)

    return wrapper


@parameter_checker
def grand_common_divisor5(a: int, b: int) -> int:
    return b if not a else grand_common_divisor5(b % a, a)
