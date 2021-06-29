def levenstein5(a: str, b: str) -> int:
    F = [[i + j if not i * j else 0 for j in range(len(b) + 1)] for i in range(len(a) + 1)]

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1])

    return F[-1][-1]
