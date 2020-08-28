def hoar_sort(array: list):
    _hoar_sort_recursive(array, 0, len(array))


def _hoar_sort_recursive(array: list, first_index: int, last_index: int):
    if last_index - first_index < 2:
        return

    barrier_index = first_index  # got to be random
    barrier_element = array[barrier_index]

    lower = 0
    greater = 0
    for i in range(first_index, last_index):
        if array[i] < barrier_element:
            lower += 1
        elif array[i] > barrier_element:
            greater += 1

    equal = last_index - first_index - lower - greater

    lower_index = first_index
    equal_index = first_index + lower
    greater_index = last_index - 1

    while greater_index >= equal_index:
        if array[greater_index] > barrier_element:
            greater_index -= 1
        elif array[greater_index] < barrier_element:
            array[greater_index], array[lower_index] = array[lower_index], array[greater_index]
            lower_index += 1
        else:  # array[greater_index] == barrier_element
            array[greater_index], array[equal_index] = array[equal_index], array[greater_index]
            equal_index += 1

    _hoar_sort_recursive(array, first_index, last_index - equal - greater)
    _hoar_sort_recursive(array, first_index + lower + equal, last_index)
