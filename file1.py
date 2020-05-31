# lecture 10
# binary_search
# fibbonachi
# minimal_cost_trace


def left_boundary(array: list, key):
    """
    Returns index of last element lower than key,
    or -1 in case there are no elements in array lower than key.
    :param array: array to be searched in
    :param key: element left boundary is searched for
    :return: index or -1
    """

    left = -1
    right = len(array)

    while right - left > 1:
        middle = left + (right - left) // 2
        if array[middle] < key:
            left = middle
        else:
            right = middle

    return left


def right_boundary(array: list, key):
    """
    Returns index of first element greater than key,
    or len(array) in case there are no elements in array greater than key.
    :param array: array to be searched in
    :param key: element left boundary is searched for
    :return: index or len(array)
    """

    left = -1
    right = len(array)

    while right - left > 1:
        middle = left + (right - left) // 2
        if array[middle] <= key:
            left = middle
        else:
            right = middle

    return right


def binary_search(array: list, key):
    """
    Searches key in array.
    :param array: array to be searched in
    :param key: element to search
    :return: list with 3 elements: first 0 if key was not found,
    1 if key was found. Second is left boundary - index of last element lower than key,
    or -1 in case there were no elements in array lower than key.
    Third is right boundary - index of first element greater than key,
    or len(array) in case there were no elements in array greater than key.
    """

    left = left_boundary(array, key)
    right = right_boundary(array, key)

    if right - left > 1:
        flag = 1
    else:
        flag = 0

    result = [flag, left, right]

    return result


def fibbonachi(n: int):
    """
    Prints first n Fibbonachi numbers, not using recursion
    :param n:
    :return:
    """
    array = [0] * n
    array[0] = 0
    array[1] = 1

    for index in range(2, n):
        array[index] = array[index - 1] + array[index - 2]
        print(array[index], '\n')


def minimal_cost_trace(n, price_array: list):
    """
    Calculates minimal cost to reach point n from point 0.
    :param n: index of final point
    :param price_array: list of prices when step into each point
    :return: minimal cost
    """

    cost_array = [0] * n
    cost_array[0] = price_array[0]
    cost_array[1] = price_array[1] + cost_array[0]

    for index in range(2, n):
        cost_array[index] = price_array[index] + min(cost_array[index - 2], cost_array[index - 1])

    return cost_array[n - 1]


def test_left_boundary(algorithm):
    array = [0, 0, 0, 0, 1, 1, 2, 2, 3, 5, 5, 5, 6, 7, 8, 8, 8, 9, 9, 9]
    n = len(array)

    print("test #1:", "ok" if algorithm(array, 0) == -1 else "FAILED")
    print("test #2:", "ok" if algorithm(array, 1) == 3 else "FAILED")
    print("test #3:", "ok" if algorithm(array, 2) == 5 else "FAILED")
    print("test #4:", "ok" if algorithm(array, 4) == 8 else "FAILED")
    print("test #5:", "ok" if algorithm(array, 9) == 16 else "FAILED")
    print("test #6:", "ok" if algorithm(array, 15) == 19 else "FAILED")
    print("test #7:", "ok" if algorithm(array, -5) == -1 else "FAILED")


def test_right_boundary(algorithm):
    array = [0, 0, 0, 0, 1, 1, 2, 2, 3, 5, 5, 5, 6, 7, 8, 8, 8, 9, 9, 9]
    n = len(array)

    print("test #1:", "ok" if algorithm(array, 0) == 4 else "FAILED")
    print("test #2:", "ok" if algorithm(array, 1) == 6 else "FAILED")
    print("test #3:", "ok" if algorithm(array, 2) == 8 else "FAILED")
    print("test #4:", "ok" if algorithm(array, 4) == 9 else "FAILED")
    print("test #5:", "ok" if algorithm(array, 9) == 20 else "FAILED")
    print("test #6:", "ok" if algorithm(array, 15) == 20 else "FAILED")
    print("test #7:", "ok" if algorithm(array, -5) == 0 else "FAILED")


def test_binary_search(algorithm):
    array = [0, 0, 0, 0, 1, 1, 2, 2, 3, 5, 5, 5, 6, 7, 8, 8, 8, 9, 9, 9]

    print("test #0:", "ok" if algorithm(array, -5) == [int(False), -1, 0] else "FAILED")
    print("test #1:", "ok" if algorithm(array, 0) == [int(True), -1, 4] else "FAILED")
    print("test #2:", "ok" if algorithm(array, 1) == [int(True), 3, 6] else "FAILED")
    print("test #3:", "ok" if algorithm(array, 2) == [int(True), 5, 8] else "FAILED")
    print("test #4:", "ok" if algorithm(array, 3) == [int(True), 7, 9] else "FAILED")
    print("test #5:", "ok" if algorithm(array, 4) == [int(False), 8, 9] else "FAILED")
    print("test #6:", "ok" if algorithm(array, 5) == [int(True), 8, 12] else "FAILED")
    print("test #7:", "ok" if algorithm(array, 6) == [int(True), 11, 13] else "FAILED")
    print("test #8:", "ok" if algorithm(array, 9) == [int(True), 16, 20] else "FAILED")
    print("test #9:", "ok" if algorithm(array, 12) == [int(False), 19, 20] else "FAILED")


def test_fibbonachi(algorithm):
    algorithm(20)


def test_minimal_cost_trace(algorithms):
    price_array = [0, 1, 0, 0, 2, 0, 1, 0, 3, 0, 4, 0, 1, 0, 0, 1]

    print("test #1: ", "ok" if algorithms(len(price_array), price_array) == 1 else "FAILED")


test_left_boundary(left_boundary)
test_right_boundary(right_boundary)
test_binary_search(binary_search)
test_fibbonachi(fibbonachi)
test_minimal_cost_trace(minimal_cost_trace)
