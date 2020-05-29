# lecture 9
# merge_sort
# hoar_sort


def is_sorted(array: list, ascending: bool = True):
    sign = 2 * int(ascending) - 1

    for index in range(len(array) - 1):
        if sign * array[index + 1] < sign * array[index]:
            return False

    return True


def merge(array1: list, array2: list, array: list):  # for merge_sort(...)
    index1 = index2 = index = 0

    while index1 < len(array1) and index2 < len(array2):
        if array1[index1] <= array2[index2]:
            array[index] = array1[index1]
            index1 += 1
            index += 1
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


def merge_sort(array: list):
    """
    Sorts array using merging algorithm
    :param array: array to be sorted
    :return:
    """
    if len(array) <= 1:
        return

    middle = len(array) // 2
    left = [array[i] for i in range(middle)]
    right = [array[i] for i in range(middle, len(array))]

    merge_sort(left)
    merge_sort(right)

    merge(left, right, array)


def hoar_sort(array: list):
    """
    Sorts array using method of Hoar
    :param array: array to be sorted
    :return:
    """
    if len(array) <= 1:
        return

    barrier = array[0]  # random element of array must be here
    right = []
    middle = []
    left = []

    for index in range(len(array)):
        if array[index] < barrier:
            right.append(array[index])
        elif array[index] == barrier:
            middle.append(array[index])
        else:  # array[index] > barrier
            left.append(array[index])

    hoar_sort(right)
    hoar_sort(left)

    for index in range(len(right)):
        array[index] = right[index]
    for index in range(len(middle)):
        array[len(right) + index] = middle[index]
    for index in range(len(left)):
        array[len(right) + len(middle) + index] = left[index]


def test_is_sorted(function):
    print("test#1:", " ok" if function([0, 1, 2, 3, 4, 7]) else " FAILED")
    print("test#2:", " ok" if not function([0, 10, 2, 3, 4, 7]) else " FAILED")
    print("test#3:", " ok" if function([0, 1, 1, 1, 2, 3, 4, 7]) else " FAILED")
    print("test#4:", " ok" if not function([10, 9, 5, 4, 4, 10], False) else " FAILED")
    print("test#5:", " ok" if function([10, 9, 9, 5, 4, 4, 0], False) else " FAILED")
    print("test#6:", " ok" if function([5, 5, 5, 5, 5, 5, 5]) else " FAILED")
    print("test#7:", " ok" if function([7, 7, 7, 7, 7, 7, 7, 7, 7], False) else " FAILED")


def test_sort(algorithm):
    array = [1, 2, 0, 0, 0, 8, 7, 4, 3, 2, 1, 4, 6, 9, 8, 9]
    algorithm(array)
    print("test#1: ", "ok" if is_sorted(array) else "FAILED")

    array = [2, 3, 4, 5, 6, 7, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]
    algorithm(array)
    print("test#2: ", "ok" if is_sorted(array) else "FAILED")

    array = [2, 3, 4, 5, 6, 7]
    algorithm(array)
    print("test#3: ", "ok" if is_sorted(array) else "FAILED")

    array = [2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]
    algorithm(array)
    print("test#4: ", "ok" if is_sorted(array) else "FAILED")

    array = [2, 2, 2, 2, 2, 2, 2]
    algorithm(array)
    print("test#5: ", "ok" if is_sorted(array) else "FAILED")


test_is_sorted(is_sorted)
test_sort(merge_sort)
test_sort(hoar_sort)
