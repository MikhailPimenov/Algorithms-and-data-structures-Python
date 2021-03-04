def longest_common_subsequence(a: list, b: list):
    f = common_subsequence(a, b)
    result = reveal_longest_common_subsequence(a, b, f)

    return result


def common_subsequence(a: list, b: list, ):
    f = [[0 for k in range(len(b) + 1)] for m in range(len(a) + 1)]

    for k in range(1, len(a) + 1):
        for m in range(1, len(b) + 1):
            if a[k - 1] == b[m - 1]:
                f[k][m] = 1 + f[k - 1][m - 1]
            else:
                f[k][m] = max(f[k - 1][m], f[k][m - 1])
    return f


def reveal_longest_common_subsequence(a: list, b: list, f: list):
    result = [0] * f[len(a)][len(b)]

    k = len(a)
    m = len(b)
    r = f[len(a)][len(b)]
    while k > 0 and m > 0:
        if f[k - 1][m] == f[k][m - 1]:
            if f[k - 1][m] < f[k][m]:
                result[r - 1] = a[k - 1]
                r -= 1
            k -= 1
            m -= 1
        elif f[k - 1][m] > f[k][m - 1]:
            k -= 1
        else:
            m -= 1

    return result
