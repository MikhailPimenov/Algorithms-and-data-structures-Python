def merge_sort3(array: list):
    buf_array = array[:]
    merge_sort_recursive(array, buf_array, 0, len(array))


def merge_sort_recursive(array: list, buf_array: list, begin: int, end: int):
    length = end - begin
    if length < 2:
        return

    merge_sort_recursive(array, buf_array, begin, begin + length // 2)
    merge_sort_recursive(array, buf_array, begin + length // 2, end)

    merge(array, begin, end,
          buf_array, begin, begin + length // 2,
          buf_array, begin + length // 2, end)

    copy(buf_array, array, begin, end)


def merge(array: list, begin: int, end: int,
          array1: list, begin1: int, end1: int,
          array2: list, begin2: int, end2: int):
    assert (end - begin) == ((end1 - begin1) + (end2 - begin2))

    index = begin
    index1 = begin1
    index2 = begin2

    while index1 < end1 and index2 < end2:
        if array1[index1] <= array2[index2]:
            array[index] = array1[index1]
            index1 += 1
        else:
            array[index] = array2[index2]
            index2 += 1
        index += 1

    while index1 < end1:
        array[index] = array1[index1]
        index1 += 1
        index += 1

    while index2 < end2:
        array[index] = array2[index2]
        index2 += 1
        index += 1


def copy(destination: list, source: list, begin: int, end: int):
    for index in range(begin, end):
        destination[index] = source[index]
