def generate_numbers(base: int, length: int = -1, prefix: list = None):
    if type(base) not in [int]:
        raise TypeError
    if type(length) not in [int]:
        raise TypeError

    if base > 10 or base < 1:
        raise ArithmeticError

    length = base if length == -1 else length
    prefix = prefix or []

    if length < 1:
        print(prefix)
        return

    for digit in range(base):
        prefix.append(digit)
        generate_numbers(base, length - 1, prefix)
        prefix.pop()

    pass
