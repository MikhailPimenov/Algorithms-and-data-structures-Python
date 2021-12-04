def get_shift_reduced(shift: int, length: int) -> int:
    shift = shift % length
    shift = -length + shift if shift > length // 2 else shift
    return shift


def shift_forward(array: list, length: int, shift: int, buffer: tuple) -> None:
    if shift < 0:
        return

    start = shift
    finish = length

    for index in reversed(range(start, finish)):
        array[index] = array[index - shift]

    for index, value in enumerate(buffer):
        array[index] = value


def shift_backward(array: list, length: int, shift: int, buffer: tuple) -> None:
    if shift > 0:
        return

    start = 0
    finish = length + shift

    for index in range(start, finish):
        array[index] = array[index - shift]

    for index, value in enumerate(buffer):
        array[index + length + shift] = value


def shift_array(array: list, length: int, shift: int) -> None:
    shift = get_shift_reduced(shift, length)

    buffer = array[(length - shift):length] if shift > 0 else array[0:abs(shift)]

    if shift > 0:
        shift_forward(array, length, shift, buffer)
        return

    shift_backward(array, length, shift, buffer)


def shift_row(array: list, row: int, shift: int) -> None:
    shift_array(array[row], len(array[row]), shift)


def shift_column(array: list, column: int, shift: int) -> None:
    column_as_row = [array[index][column] for index in range(len(array))]
    shift_array(column_as_row, len(column_as_row), shift)

    for index in range(len(array)):
        array[index][column] = column_as_row[index]
