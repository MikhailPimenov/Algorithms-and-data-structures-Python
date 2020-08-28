def merge_sort(array: list):
    _merge_sort_recursive(array, len(array))


def _merge_sort_recursive(array: list, length: int):
    if length < 2:
        return

    array1 = array[:length // 2:]
    array2 = array[length // 2:length:]

    _merge_sort_recursive(array1, length // 2)
    _merge_sort_recursive(array2, length - length // 2)

    _merge(array, array1, array2)


def _merge(array: list, array1: list, array2: list):
    assert len(array) == len(array1) + len(array2)

    index = index1 = index2 = 0

    while index1 < len(array1) and index2 < len(array2):
        if array1[index1] <= array2[index2]:
            array[index] = array1[index1]
            index1 += 1
        else:
            array[index] = array2[index2]
            index2 += 1
        index += 1

    while index1 < len(array1):
        array[index] = array1[index1]
        index1 += 1
        index += 1

    while index2 < len(array2):
        array[index] = array2[index2]
        index2 += 1
        index += 1
