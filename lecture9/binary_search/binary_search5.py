def binary_search5(a: list, item: int) -> tuple:
    left = left_boundary(a, item)
    right = right_boundary(a, item)

    return (right - left) > 1, left, right


def left_boundary(a: list, item: int) -> int:
    left = -1
    right = len(a)

    while left < right - 1:
        middle = (left + right) // 2

        if a[middle] < item:
            left = middle
        else:
            right = middle

    return left


def right_boundary(a: list, item: int) -> int:
    left = -1
    right = len(a)

    while left < right - 1:
        middle = (left + right) // 2

        if a[middle] > item:
            right = middle
        else:
            left = middle

    return right
