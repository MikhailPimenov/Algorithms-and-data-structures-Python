from datetime import datetime


def decorator_timedelta(wrappee):
    def wrapper(*args, **kwargs):
        t = datetime.now()
        result = wrappee(*args, **kwargs)
        t = datetime.now() - t
        print(t)
        return result

    return wrapper


@decorator_timedelta
def merge_sort(a: list) -> list:
    b = a[:]
    merge_recursive(a, 0, len(a), b)
    return a


def merge_recursive(a: list, start: int, end: int, b: list):
    length = end - start

    if length < 2:
        return

    merge_recursive(a, start, start + length // 2, b)
    merge_recursive(a, start + length // 2, end, b)

    merge(b, start, end,
          a, start, start + length // 2,
          a, start + length // 2, end)

    copy(a, b, start, end)


def merge(a: list, start: int, end: int,
          a1: list, start1: int, end1: int,
          a2: list, start2: int, end2: int):
    length = end - start
    length1 = end1 - start1
    length2 = end2 - start2

    assert length == length1 + length2

    index = start
    index1 = start1
    index2 = start2

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


def copy(destination: list, source: list, start: int, end: int):
    for index in range(start, end):
        destination[index] = source[index]


t = [[i for i in range(j, -1, -1)] for j in range(10000, 100000, 10000)]

# for k in range(len(t)):
#     merge_sort(t[k])
