def hoar_sort5(a: list) -> None:
    return hoar_sort_recursive(a, 0, len(a))


def hoar_sort_recursive(a: list, begin: int, end: int) -> None:
    length = end - begin

    if length < 2:
        return

    pivot_index = begin  # got to be random
    pivot = a[pivot_index]

    lower = 0
    greater = 0
    for i in range(begin, end):
        if a[i] < pivot:
            lower += 1
        elif a[i] > pivot:
            greater += 1

    equal = length - lower - greater

    lower_index = begin
    equal_index = begin + lower
    greater_index = end - 1

    while equal_index <= greater_index:
        if a[greater_index] > pivot:
            greater_index -= 1
        elif a[greater_index] < pivot:
            a[greater_index], a[lower_index] = a[lower_index], a[greater_index]
            lower_index += 1
        else:
            a[greater_index], a[equal_index] = a[equal_index], a[greater_index]
            equal_index += 1

    hoar_sort_recursive(a, begin, begin + lower)
    hoar_sort_recursive(a, begin + lower + equal, end)
