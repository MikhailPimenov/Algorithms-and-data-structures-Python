def longest_increasing_subsequence(a: list):
    f = increasing_subsequence(a)
    result = reveal_longest_increasing_subsequence(a, f)
    return result


def increasing_subsequence(a: list):
    f = [0] * len(a)

    for k in range(len(a)):
        maximum = 0
        for s in range(k):
            if a[k] > a[s] and f[s] > maximum:
                maximum = f[s]
        f[k] = maximum + 1
    return f


def get_start_index(f:list):
    maximum = max(*f)
    for k in range(len(f)):
        if f[k] == maximum:
            return k


def reveal_longest_increasing_subsequence(a: list, f: list):
    length = max(*f)
    result = [0] * length

    index = get_start_index(f)

    result_index = length - 1
    current_maximum = length + 1

    while index >= 0:
        if f[index] == current_maximum - 1:
            result[result_index] = a[index]
            result_index -= 1
            current_maximum -= 1
        index -= 1

    return result
