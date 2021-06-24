def get_length_of_longest_common_subsequence4(a1: tuple, a2: tuple) -> tuple:
    ff = [[i * j if i * j == 0 else None for j in range(len(a1) + 1)] for i in range(len(a2) + 1)]

    for i in range(1, len(a2) + 1):
        for j in range(1, len(a1) + 1):
            if a1[j - 1] == a2[i - 1]:
                ff[i][j] = 1 + ff[i - 1][j - 1]
            else:
                ff[i][j] = max(ff[i - 1][j], ff[i][j - 1])

    return ff, ff[-1][-1]


def get_longest_common_subsequence4(a1: tuple, a2: tuple, ff: tuple, length: int) -> list:
    i = len(a2)
    j = len(a1)
    s_index = length - 1

    s = [None] * length

    while i and j:
        if ff[i - 1][j] == ff[i][j - 1]:
            if ff[i - 1][j - 1] < ff[i][j]:
                s[s_index] = a1[j - 1]
                s_index -= 1
            i -= 1
            j -= 1
        else:
            if ff[i - 1][j] > ff[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return s


def longest_common_subsequence4(a1: tuple, a2: tuple) -> list:
    ff, length = get_length_of_longest_common_subsequence4(a1, a2)
    s = get_longest_common_subsequence4(a1, a2, ff, length)
    return s
