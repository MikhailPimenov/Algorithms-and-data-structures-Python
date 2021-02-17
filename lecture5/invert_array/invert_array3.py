def invert_array(array: list, length: int):
    if type(array) not in [list]:
        raise TypeError
    if type(length) not in [int]:
        raise TypeError

    for index in range(length // 2):
        array[index], array[length - index - 1] = array[length - index - 1], array[index]
    return array
