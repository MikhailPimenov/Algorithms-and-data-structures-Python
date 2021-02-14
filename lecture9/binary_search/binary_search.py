def left_boundary(elements: list, element):
    left = -1
    right = len(elements)

    while right - left > 1:
        middle = left + (right - left) // 2
        if elements[middle] >= element:
            right = middle
        else:
            left = middle

    return left


def right_boundary(elements: list, element):
    left = -1
    right = len(elements)

    while right - left > 1:
        middle = left + (right - left) // 2
        if elements[middle] <= element:
            left = middle
        else:
            right = middle

    return right


def binary_search(elements: list, element):
    left = left_boundary(elements, element)
    right = right_boundary(elements, element)

    result = ((right - left) > 1)

    return (result, left, right)