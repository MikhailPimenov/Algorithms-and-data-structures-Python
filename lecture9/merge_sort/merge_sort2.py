def merge_sort(array: list):
    buffer_array = array[:]

    _merge_recursive(array, 0, len(array), buffer_array)


def _merge(destination: list, begin: int, end: int,
           source1: list, begin1: int, end1: int,
           source2: list, begin2: int, end2: int):
    assert end - begin == (end1 - begin1) + (end2 - begin2)

    index = begin
    index1 = begin1
    index2 = begin2

    while index1 < end1 and index2 < end2:
        if source1[index1] <= source2[index2]:
            destination[index] = source1[index1]
            index1 += 1
        else:
            destination[index] = source2[index2]
            index2 += 1
        index += 1

    while index1 < end1:
        destination[index] = source1[index1]
        index1 += 1
        index += 1

    while index2 < end2:
        destination[index] = source2[index2]
        index2 += 1
        index += 1


def _merge_recursive(array: list, begin: int, end: int, buffer_array: list):
    length = end - begin

    if length < 2:
        return

    _merge_recursive(array, begin, begin + length // 2, buffer_array)
    _merge_recursive(array, begin + length // 2, end, buffer_array)

    _merge(buffer_array, begin, end,
           array, begin, begin + length // 2,
           array, begin + length // 2, end)

    _copy(array, buffer_array, begin, end)


def _copy(destination: list, source: list, begin: int, end: int):
    for index in range(begin, end):
        destination[index] = source[index]
