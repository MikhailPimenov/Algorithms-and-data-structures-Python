def get_length_of_longest_increasing_subsequence4(a: list, f: list) -> int:
    for i in range(len(f)):
        maximum = 0
        for j in range(i):
            if a[j] < a[i] and f[j] > maximum:
                maximum = f[j]
        f[i] = maximum + 1

    return max(*f)


def reveal_longest_increasing_subsequence4(a: list, f: list, length: int) -> list:
    start = 0
    maximum = 0
    for i in range(len(f)):
        if f[i] > maximum:
            maximum = f[i]
            start = i

    s = [None] * length
    s_index = length - 1
    s[s_index] = a[start]
    s_index -= 1

    for i in reversed(range(start + 1)):
        if f[i] == maximum - 1:
            s[s_index] = a[i]
            maximum -= 1
            s_index -= 1
        if maximum == 1:
            break

    return s


def longest_increasing_subsequence4(a: list) -> list:
    f = [None] * len(a)
    length = get_length_of_longest_increasing_subsequence4(a, f)

    s = reveal_longest_increasing_subsequence4(a, f, length)
    return s
