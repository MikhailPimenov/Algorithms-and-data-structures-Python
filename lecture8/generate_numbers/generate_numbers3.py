def generate_numbers3(base: int, length: int):
    if type(base) not in [int]:
        raise TypeError
    if type(length) not in [int]:
        raise TypeError

    if length < 0:
        raise ArithmeticError
    if base > 16 or base < 0:
        raise ArithmeticError
    
    prefix = []
    generate_numbers_recursive3(prefix, base, length)


def generate_numbers_recursive3(prefix: list, base: int, length: int):
    if length < 1:
        print(prefix)
        return

    for digit in range(base):
        prefix.append(digit)
        generate_numbers_recursive3(prefix, base, length - 1)
        prefix.pop()
