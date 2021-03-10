def levenstein3(array1: list, array2: list):
    f = [[i + j if i * j == 0 else 0
         for j in range(len(array1) + 1)] for i in range(len(array2) + 1)]

    for i in range(1, len(array2) + 1):
        for j in range(1, len(array1) + 1):
            if array1[j - 1] == array2[i - 1]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j] = 1 + min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1])

    return f[-1][-1]
