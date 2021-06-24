def hoar_sort4(a: list):
    hoar_sort_recursive4(a, 0, len(a))


def hoar_sort_recursive4(a: list, begin: int, end: int):
    length = end - begin
    if length < 1:
        return

    pivot_index = begin
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
    greater_index = end - 1
    equal_index = lower_index + lower

    while greater_index >= equal_index:
        if a[greater_index] < pivot:
            a[greater_index], a[lower_index] = a[lower_index], a[greater_index]
            lower_index += 1
        elif a[greater_index] == pivot:
            a[greater_index], a[equal_index] = a[equal_index], a[greater_index]
            equal_index += 1
        else:
            greater_index -= 1

    hoar_sort_recursive4(a, begin, begin + lower)
    hoar_sort_recursive4(a, begin + lower + equal, end)
