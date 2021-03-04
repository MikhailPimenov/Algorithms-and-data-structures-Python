def chess_queen3(m: int, n: int):
    f = [[1] * m for _ in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            f[i][j] = f[i][j - 1] + f[i - 1][j]
    return f[-1][-1]
