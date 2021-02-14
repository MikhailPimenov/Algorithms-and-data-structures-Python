def heap_sort(array: list):
    heapify(array)
    for index in range(len(array)):
        array[0], array[len(array) - 1 - index] = array[len(array) - 1 - index], array[0]
        sift_down(array, 0, len(array) - index - 1)


def child1_i(index: int):
    return 2 * index + 1


def child1(index: int, length: int):
    return child1_i(index) < length


def child2_i(index: int):
    return 2 * index + 2


def child2(index: int, length: int):
    return child2_i(index) < length


def sift_down(array: list, index, length):
    while child1(index, length):
        old_index = index
        if child2(index, length) and array[child2_i(index)] > array[child1_i(index)]:
            if array[child2_i(index)] > array[index]:
                index = child2_i(index)
        elif array[child1_i(index)] > array[index]:
            index = child1_i(index)
        if index != old_index:
            array[index], array[old_index] = array[old_index], array[index]
        else:
            return


def heapify(array: list):
    for index in range(len(array) // 2, -1, -1):
        sift_down(array, index, len(array))
