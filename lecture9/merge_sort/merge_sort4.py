def merge_sort4(a: list):
    b = [None] * len(a)
    begin = 0
    end = len(a)
    merge_sort_recursive(a, begin, end, b)


def merge(a: list, begin: int, end: int,
          a1: list, begin1: int, end1: int,
          a2: list, begin2: int, end2: int):
    length = end - begin
    length1 = end1 - begin1
    length2 = end2 - begin2
    assert length == length1 + length2

    i = begin
    i1 = begin1
    i2 = begin2

    while i1 < end1 and i2 < end2:
        if a1[i1] <= a2[i2]:
            a[i] = a1[i1]
            i1 += 1
        else:
            a[i] = a2[i2]
            i2 += 1
        i += 1

    while i1 < end1:
        a[i] = a1[i1]
        i1 += 1
        i += 1

    while i2 < end2:
        a[i] = a2[i2]
        i2 += 1
        i += 1


def copy(destination: list, begin: int, end: int, source: list):
    for i in range(begin, end):
        destination[i] = source[i]


def merge_sort_recursive(a: list, begin: int, end: int, b: list):
    length = end - begin
    if length < 2:
        return

    merge_sort_recursive(a, begin, begin + length // 2, b)
    merge_sort_recursive(a, begin + length // 2, end, b)

    merge(b, begin, end, a, begin, begin + length // 2, a, begin + length // 2, end)
    copy(a, begin, end, b)
