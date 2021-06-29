def longest_common_subsequence5(a: list, b: list) -> tuple:
    length, F = get_length(a, b)

    p = reveal_subsequence(a, b, F, length)

    return p


def get_length(a: list, b: list) -> tuple:
    F = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                F[i][j] = F[i - 1][j - 1] + 1
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])

    return F[-1][-1], F


def reveal_subsequence(a: list, b: list, F: list, length: int) -> tuple:
    i = len(a)
    j = len(b)

    k = length - 1
    p = [None] * length

    while i and j:
        if F[i - 1][j] == F[i][j - 1]:
            if F[i - 1][j - 1] < F[i][j]:
                p[k] = a[i - 1]
                k -= 1
            i -= 1
            j -= 1
        elif F[i - 1][j] < F[i][j - 1]:
            j -= 1
        else:
            i -= 1

    return p
