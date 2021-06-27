def merge_sort5_adapter(wrappee):
    def wrapper(a: list, *args, **kwargs):
        return wrappee(a, len(a), *args, **kwargs)

    return wrapper


@merge_sort5_adapter
def merge_sort5(a: list, length: int) -> None:
    b = a[:]
    merge_sort_recursive(a, 0, length, b)


def merge(a: list, begin: int, end: int,
          a1: list, begin1: int, end1: int,
          a2: list, begin2: int, end2: int):
    index = begin
    index1 = begin1
    index2 = begin2

    while index1 < end1 and index2 < end2:
        if a1[index1] <= a2[index2]:
            a[index] = a1[index1]
            index1 += 1
        else:
            a[index] = a2[index2]
            index2 += 1

        index += 1

    while index1 < end1:
        a[index] = a1[index1]
        index1 += 1
        index += 1

    while index2 < end2:
        a[index] = a2[index2]
        index2 += 1
        index += 1


def copy(destination: list, begin: int, end: int, source: list) -> None:
    for i in range(begin, end):
        destination[i] = source[i]


def merge_sort_recursive(a: list, begin: int, end: int, b: list) -> None:
    length = end - begin

    if length < 2:
        return

    merge_sort_recursive(a, begin, begin + length // 2, b)
    merge_sort_recursive(a, begin + length // 2, end, b)

    merge(b, begin, end, a, begin, begin + length // 2, a, begin + length // 2, end)

    copy(a, begin, end, b)
