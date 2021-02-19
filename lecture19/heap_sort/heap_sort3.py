def heap_sort3(array: list):
    heapify(array)
    for index in range(len(array) - 1):
        array[0], array[len(array) - 1 - index] = array[len(array) - 1 - index], array[0]
        sift_down(array, 0, len(array) - 1 - index)


def heapify(array: list):
    for index in reversed(range(len(array) // 2)):
        sift_down(array, index, len(array))


def child1_index(index: int):
    return 2 * index + 1


def child2_index(index: int):
    return child1_index(index) + 1


def child1_exists(index: int, length: int):
    return child1_index(index) < length


def child2_exists(index: int, length: int):
    return child2_index(index) < length


def sift_down(array: list, index: int, length: int):
    while child1_exists(index, length):
        old_index = index

        if child2_exists(index, length) and (array[child2_index(index)] > array[child1_index(index)]):
            if array[child2_index(index)] > array[index]:
                index = child2_index(index)
        elif array[child1_index(index)] > array[index]:
            index = child1_index(index)

        if index != old_index:
            array[index], array[old_index] = array[old_index], array[index]
        else:
            break
