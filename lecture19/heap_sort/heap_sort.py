def _sift_down(array: list, length: int, index: int):
    while 2 * index + 1 < length:
        old_index = index
        if 2 * index + 2 < length and array[2 * index + 2] > array[2 * index + 1]:
            if array[2 * index + 2] > array[index]:
                index = 2 * index + 2
        else:
            if array[2 * index + 1] > array[index]:
                index = 2 * index + 1
        if index != old_index:
            array[index], array[old_index] = array[old_index], array[index]
        else:
            return


def _heapify(array: list):
    for k in range(len(array) // 2, -1, -1):
        _sift_down(array, len(array), k)


def _extract_top(array: list, length: int):
    result = array[0]
    array[0] = array[length - 1]
    _sift_down(array, length - 1, 0)

    return result


def heap_sort(array: list):
    _heapify(array)
    for k in range(len(array)):
        array[len(array) - 1 - k] = _extract_top(array, len(array) - k)
