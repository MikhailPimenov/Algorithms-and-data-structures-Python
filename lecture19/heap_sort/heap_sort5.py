def heap_sort5_adapter(wrappee):
    def wrapper(a: list, *args, **kwargs):
        return wrappee(a, len(a), *args, **kwargs)

    return wrapper


@heap_sort5_adapter
def heap_sort5(a: list, length: int) -> None:
    heapify(a, length)

    for i in range(length - 1):
        a[0], a[length - 1 - i] = a[length - 1 - i], a[0]
        sift_down(a, length - 1 - i, 0)


def child1_index(i: int) -> int:
    return 2 * i + 1


def child2_index(i: int) -> int:
    return 2 * i + 2


def child1_exists(length: int, i: int) -> bool:
    return child1_index(i) < length


def child2_exists(length: int, i: int) -> bool:
    return child2_index(i) < length


def sift_down(a: list, length: int, i) -> None:
    while child1_exists(length, i):
        old = i

        if child2_exists(length, i) and a[child2_index(i)] > a[child1_index(i)]:
            if a[child2_index(i)] > a[i]:
                i = child2_index(i)
        elif a[child1_index(i)] > a[i]:
            i = child1_index(i)

        if i != old:
            a[old], a[i] = a[i], a[old]
        else:
            return


def heapify(a: list, length: int) -> None:
    for i in reversed(range(length // 2)):
        sift_down(a, length, i)
