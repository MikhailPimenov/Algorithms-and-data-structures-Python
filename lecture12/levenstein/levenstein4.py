def levenstein4(s1: str, s2: str) -> int:
    ff = [[i + j if i * j == 0 else 0 for j in range(len(s1) + 1)] for i in range(len(s2) + 1)]

    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s1[j - 1] == s2[i - 1]:
                ff[i][j] = ff[i - 1][j - 1]
            else:
                ff[i][j] = 1 + min(ff[i - 1][j - 1], ff[i - 1][j], ff[i][j - 1])

    return ff[-1][-1]
