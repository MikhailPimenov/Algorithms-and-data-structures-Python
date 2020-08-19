def longest_common_subsequence(sequence1: list, sequence2: list):
    f = [([0] * (len(sequence2) + 1)) for k in range(len(sequence1) + 1)]
    length = calculate_length(sequence1, sequence2, f)
    result = subsequence(sequence1, sequence2, f, length)
    return result


def calculate_length(sequence1: list, sequence2: list, f: list):
    for i in range(1, len(sequence1) + 1):
        for j in range(1, len(sequence2) + 1):
            if sequence1[i - 1] == sequence2[j - 1]:
                f[i][j] = f[i - 1][j - 1] + 1
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])

    return f[-1][-1]


def subsequence(sequence1: list, sequence2: list, f: list, length: int):
    result = [0] * length

    i = len(sequence1)
    j = len(sequence2)
    k = length - 1
    while i > 0 and j > 0:
        if f[i - 1][j] == f[i][j - 1]:
            if f[i - 1][j - 1] < f[i][j]:
                result[k] = sequence1[i - 1]
                k -= 1
            i -= 1
            j -= 1
        else:
            if f[i - 1][j] > f[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return result
