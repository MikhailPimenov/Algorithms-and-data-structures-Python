# lecture 11 part 2 of 3
# part 1
# chess_queen_trace
# part 2
# largest_common_subsequence
# part 3
# largest_increasing_subsequence


def length_of_largest_common_subsequence(array1: list, array2: list, frequency: list):
    for i in range(1, len(array1) + 1):
        for j in range(1, len(array2) + 1):
            if array1[i - 1] == array2[j - 1]:
                frequency[i][j] = 1 + frequency[i - 1][j - 1]
            else:
                frequency[i][j] = max(frequency[i - 1][j], frequency[i][j - 1])

    return frequency[len(array1)][len(array2)]


def get_largest_common_subsequence(array1: list, array2: list, frequency: list, sub_array: list):
    i = len(array1)
    j = len(array2)
    sub = len(sub_array) - 1

    while i > 0 and j > 0:
        if frequency[i - 1][j] == frequency[i][j - 1]:
            if frequency[i - 1][j - 1] < frequency[i][j]:
                sub_array[sub] = array1[i - 1]
                sub -= 1
            i -= 1
            j -= 1
        elif frequency[i - 1][j] > frequency[i][j - 1]:
            i -= 1
        else:  # frequency[i-1][j] < frequency[i][j-1]
            j -= 1

    return sub_array


def largest_common_subsequence(array1: list, array2: list):
    """
    Returnes largest common subsequence of array1, array2
    :param array1: list of elements
    :param array2: list of elements
    :return:
    """
    frequency = [[0] * (len(array2) + 1) for k in range(len(array1) + 1)]

    length = length_of_largest_common_subsequence(array1, array2, frequency)

    sub_array = [0] * length

    get_largest_common_subsequence(array1, array2, frequency, sub_array)

    return sub_array


def test_largest_common_subsequence(algorithm):
    array1 = [5, 4, 3, 2, 1]
    array2 = [5, 3, 0, 1]

    print("test #1:", "ok" if algorithm(array1, array2) == [5, 3, 1] else "FAILED")

    array1 = [5, 7, 2, 8, 4, 5]
    array2 = [8, 5, 2, 5, 8, 4, 3, 8, 0, 6, 3, 2, 5, 7]

    print("test #2:", "ok" if algorithm(array1, array2) == [5, 2, 8, 4, 5] else "FAILED")
    print("test #3:", "ok" if algorithm(array1, array2) == 5 else "FAILED")


test_largest_common_subsequence(largest_common_subsequence)
