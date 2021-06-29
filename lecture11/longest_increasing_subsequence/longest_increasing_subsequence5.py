def longest_increasing_subsequence5(a: list) -> tuple:
    length, F = get_length(a)
    p = reveal_subsequence(a, length, F)
    return p


def reveal_subsequence(a: list, length: int, F: list) -> tuple:
    i = 0
    for j in range(len(F)):
        if F[j] == length:
            i = j
            break

    p = [None] * length
    p[length - 1] = a[i]
    i -= 1
    k = length - 2
    maximum = length

    while maximum > 1:
        if F[i] == maximum - 1:
            p[k] = a[i]
            k -= 1
            maximum -= 1
        i -= 1

    return p


def get_length(a: list) -> tuple:
    F = [None] * len(a)

    for i in range(len(a)):
        maximum = 0
        for j in range(i):
            if F[j] > maximum and a[i] > a[j]:
                maximum = F[j]
        F[i] = maximum + 1

    return max(F), F
