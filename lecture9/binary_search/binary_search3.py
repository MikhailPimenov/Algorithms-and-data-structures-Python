def left_boundary(array: list, item: int):
    left = -1
    right = len(array)

    while right - left > 1:
        middle = (right - left) // 2 + left
        if array[middle] < item:
            left = middle
        else:
            right = middle

    return left


def right_boundary(array: list, item: int):
    left = -1
    right = len(array)

    while right - left > 1:
        middle = (right - left) // 2 + left
        if array[middle] > item:
            right = middle
        else:
            left = middle

    return right


def binary_search3(array: list, item: int):
    left = left_boundary(array, item)
    right = right_boundary(array, item)

    item_is_found = True if right - left > 1 else False
    return item_is_found, left, right
