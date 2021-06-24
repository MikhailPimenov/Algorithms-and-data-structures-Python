def heap_sort4(a: list):
    heapify(a)

    for i in range(len(a) - 1):
        a[0], a[len(a) - 1 - i] = a[len(a) - 1 - i], a[0]
        sift_down(a, len(a) - 1 - i, 0)


def child1_index(index: int) -> int:
    return 2 * index + 1


def child2_index(index: int) -> int:
    return child1_index(index) + 1


def child1_exists(length: int, index: int) -> bool:
    return child1_index(index) < length


def child2_exists(length: int, index: int) -> bool:
    return child2_index(index) < length


def sift_down(a: list, length: int, i: int):
    while child1_exists(length, i):
        old_i = i
        if child2_exists(length, i) and a[child2_index(i)] > a[child1_index(i)]:
            if a[child2_index(i)] > a[i]:
                i = child2_index(i)
        elif a[child1_index(i)] > a[i]:
            i = child1_index(i)

        if i == old_i:
            return
        a[i], a[old_i] = a[old_i], a[i]


def heapify(a: list):
    for i in reversed(range(len(a) // 2 + 1)):
        sift_down(a, len(a), i)
