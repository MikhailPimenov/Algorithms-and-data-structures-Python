def longest_common_subsequence3(array1: list, array2: list):
    length, f = get_length_of_longest_common_subsequence(array1, array2)

    array = [None] * length
    k = length
    i = len(array2)
    j = len(array1)

    while i > 0 and j > 0:
        if f[i - 1][j] == f[i][j - 1]:
            if f[i - 1][j - 1] < f[i][j]:
                array[k - 1] = array1[j - 1]
                k -= 1
            i -= 1
            j -= 1
        elif f[i - 1][j] < f[i][j - 1]:
            j -= 1
        else:
            i -= 1
    return array


def get_length_of_longest_common_subsequence(array1: list, array2: list):
    f = [[0] * (len(array1) + 1) for _ in range(len(array2) + 1)]

    for i in range(1, len(array2) + 1):
        for j in range(1, len(array1) + 1):
            if array1[j - 1] == array2[i - 1]:
                f[i][j] = f[i - 1][j - 1] + 1
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])

    return f[-1][-1], f
