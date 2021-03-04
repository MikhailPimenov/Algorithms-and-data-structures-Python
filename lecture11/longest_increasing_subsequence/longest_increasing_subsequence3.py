def longest_increasing_subsequence3(array: list):
    length, f = get_length_of_longest_increasing_subsequence(array)
    subsequence = reveal_longest_increasing_subsequence(array, length, f)
    return subsequence


def get_length_of_longest_increasing_subsequence(array: list):
    f = [None] * len(array)

    for i in range(len(f)):
        max_element = 0
        for j in range(i):
            if f[j] > max_element and array[j] < array[i]:
                max_element = f[j]
        f[i] = 1 + max_element

    return max(f), f


def reveal_longest_increasing_subsequence(array: list, length: int, f: list):
    max_index = 0
    for i in range(len(f)):
        if f[i] > f[max_index]:
            max_index = i

    r = length - 1
    subsequence = [None] * length
    subsequence[r] = array[max_index]
    r -= 1

    i = max_index
    while i >= 0:
        if f[i] == f[max_index] - 1:
            max_index = i
            subsequence[r] = array[max_index]
            r -= 1
        i -= 1

    return subsequence
