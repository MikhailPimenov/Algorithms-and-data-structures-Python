def chess_queen5(m: int, n: int) -> int:
    f = [[1 if not i * j else None for j in range(n)] for i in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            f[i][j] = f[i - 1][j] + f[i][j - 1]

    return f[-1][-1]
