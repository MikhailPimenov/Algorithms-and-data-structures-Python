# lecture 11 part 3 of 3
# part 1
# chess_queen_trace
# part 2
# largest_common_subsequence
# part 3
# largest_increasing_subsequence


def length_largest_increasing_subsequence(array: list, frequency: list):
    for i in range(1, len(array) + 1):
        max_f = 0
        for j in range(1, i):
            if array[i - 1] > array[j - 1] and frequency[j] > max_f:
                max_f = frequency[j]
        frequency[i] = 1 + max_f

    print(*frequency)
    return max(*frequency)


def find_max_element_lower_than_barrier_in_range(array, barrier, begin, end):
    b_status = False
    max_element = -1

    k = begin
    while k < end:
        if array[k] < barrier:
            max_element = array[k]
            b_status = True
            break
        k += 1

    while k < end:
        if max_element < array[k] < barrier:
            max_element = array[k]
        k += 1

    result = [max_element, int(b_status)]

    return result


def set_largest_increasing_subsequence(array: list, frequency: list, sub_array: list):
    sub = len(sub_array) - 1

    max_frequency_to_consider = max(*frequency)

    end = len(array)
    begin = end
    barrier = max(*array) + 1

    k = len(array)
    while k > 0:
        if frequency[k] < max_frequency_to_consider:
            begin -= 1
        else:
            result = find_max_element_lower_than_barrier_in_range(array, barrier, begin - 2, end)
            element = result[0]
            b_found = bool(result[1])
            if b_found:
                sub_array[sub] = element
                sub -= 1
                barrier = element
                max_frequency_to_consider -= 1
            end = k
            begin = end
        k -= 1

    return sub_array


def largest_increasing_subsequence(array: list):
    """
    Returns one of largest increasing subsequences of array.
    :param array: list of elements to find largest increasing subsequence
    :return: list of elements
    """
    frequency = [0] * (len(array) + 1)

    length = length_largest_increasing_subsequence(array, frequency)

    sub_array = [0] * length
    set_largest_increasing_subsequence(array, frequency, sub_array)

    return sub_array


def test_largest_increasing_subsequence(algorithm):
    array = [0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 3, 2, 2, 2, 4, 0, 0, 0, 5, 0, 0, 0, 6, 0, 0, 0, 7, 0, 0, 0, 8, 0, 0, 0, 9,
             0, 0, 0, 10, 5, 5, 5]
    result = algorithm(array)
    print(result)
    print("test #1", "ok" if result == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] else "FAILED")

    array = [5, 4, 3, 2, 1, 2]
    result = algorithm(array)
    print(result)
    print("test #2", "ok" if result == [1, 2] else "FAILED")

    array = [0, 4, 3, 2, 1, 2]
    result = algorithm(array)
    print(result)
    print("test #3", "ok" if result == [0, 1, 2] else "FAILED")

    array = [0, 0, 0, 8, 7, 6, 0, 4, 5, 1, 7, 9]
    result = algorithm(array)
    print(result)
    print("test #4", "ok" if result == [0, 4, 5, 7, 9] else "FAILED")

    array = [1, 0, 2, 3]
    result = algorithm(array)
    print(result)
    print("test #5", "ok" if result == [0, 2, 3] else "FAILED") # [1,2,3] can be too

    array = [1, 0, 2, 3]
    result = algorithm(array)
    print(result)
    print("test #6", "ok" if result == [1, 2, 3] else "FAILED") # [0,2,3] can be too


def test_find_max_lower_than_barrier_in_range(algorithm):
    array = [0, 0, 0, 1, 0, 4, 3, 7, 4, 2, 9, 4]

    result = algorithm(array, 9, 0, len(array))
    print("test #1", "ok" if result[0] == 7 and bool(result[1]) else "FAILED")

    result = algorithm(array, 4, 2, 7)
    print("test #2", "ok" if result[0] == 3 and bool(result[1]) else "FAILED")

    result = algorithm(array, -5, 2, 7)
    print("test #3", "ok" if result[0] == -1 and not bool(result[1]) else "FAILED")


test_largest_increasing_subsequence(largest_increasing_subsequence)
# test_find_max_lower_than_barrier_in_range(find_max_value_lower_than_barrier_in_range)
