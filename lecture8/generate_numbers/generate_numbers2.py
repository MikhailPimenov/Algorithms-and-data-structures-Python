def generate_numbers(base: int, length: int, prefix: list = []):
    if type(base) != int:
        raise TypeError
    if type(length) != int:
        raise TypeError
    if base < 0 or base > 16:
        raise ArithmeticError
    if length < 0:
        raise ArithmeticError

    if prefix is None:
        prefix = []

    if length < 1:
        print(prefix)
        return

    for digit in range(base):
        prefix.append(digit)
        generate_numbers(base, length - 1, prefix)
        prefix.pop()
