def hoar_sort3(array: list):
    hoar_sort_recursive(array, 0, len(array))


def hoar_sort_recursive(array: list, begin: int, end: int):
    length = end - begin

    if length < 2:
        return

    pivot_index = begin  # must be random
    pivot = array[pivot_index]

    lower = 0
    greater = 0
    for index in range(begin, end):
        if array[index] < pivot:
            lower += 1
        elif array[index] > pivot:
            greater += 1
    equal = length - lower - greater

    lower_index = begin
    greater_index = end - 1
    equal_index = begin + lower

    while equal_index <= greater_index:
        if array[greater_index] > pivot:
            greater_index -= 1
        elif array[greater_index] < pivot:
            array[greater_index], array[lower_index] = array[lower_index], array[greater_index]
            lower_index += 1
        else:
            array[greater_index], array[equal_index] = array[equal_index], array[greater_index]
            equal_index += 1

    hoar_sort_recursive(array, begin, begin + lower)
    hoar_sort_recursive(array, begin + lower + equal, end)
