def hoar_sort(array: list, begin=-1, end=-1):
    if begin == -1:
        begin = 0
    if end == -1:
        end = len(array)

    length = end - begin

    if length < 2:
        return

    barrier_index = begin  # got to be random
    barrier = array[barrier_index]

    lower = 0
    equal = 0
    greater = 0

    for index in range(begin, end):
        if array[index] > barrier:
            greater += 1
        elif array[index] < barrier:
            lower += 1
        else:  # array[index] == barrier
            assert array[index] == barrier
            equal += 1

    lower_index = begin
    equal_index = begin + lower
    greater_index = end - 1

    while greater_index >= equal_index:
        if array[greater_index] > barrier:
            greater_index -= 1
        elif array[greater_index] < barrier:
            array[greater_index], array[lower_index] = array[lower_index], array[greater_index]
            lower_index += 1
        else:  # array[greater_index] < barrier
            assert array[greater_index] == barrier
            array[greater_index], array[equal_index] = array[equal_index], array[greater_index]
            equal_index += 1

    hoar_sort(array, begin, begin + lower)
    hoar_sort(array, begin + lower + equal, end)
