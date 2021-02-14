def invert_array(x: list, length: int):
    if type(x) not in [list]:
        raise TypeError
    if type(length) not in [int]:
        raise TypeError

    for index in range(length // 2):
        x[index], x[length - index - 1] = x[length - index - 1], x[index]

    return x
