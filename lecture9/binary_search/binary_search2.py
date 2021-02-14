def binary_search(array: list, element):
    left = left_boundary(array, element)
    right = right_boundary(array, element)

    found = right - left > 1

    return found, left, right


def left_boundary(array: list, element):
    left = -1
    right = len(array)

    while right - left > 1:
        middle = (right + left) // 2
        if array[middle] >= element:
            right = middle
        else:
            left = middle

    return left


def right_boundary(array: list, element):
    left = -1
    right = len(array)

    while right - left > 1:
        middle = (right + left) // 2
        if array[middle] <= element:
            left = middle
        else:
            right = middle

    return right
