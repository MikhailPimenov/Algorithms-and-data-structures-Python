def levenstein(string1: list, string2: list):
    f = [[((i + j) if i * j == 0 else 0) for i in range(len(string2) + 1)] for j in range(len(string1) + 1)]

    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i - 1] == string2[j - 1]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j] = 1 + min(f[i - 1][j - 1], f[i][j - 1], f[i - 1][j])

    return f[len(string1)][len(string2)]
