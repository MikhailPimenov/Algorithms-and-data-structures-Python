def chess_queen4(m: int, n: int) -> int:
    ff = [[1 if i * j == 0 else None for j in range(n)] for i in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            ff[i][j] = ff[i - 1][j] + ff[i][j-1]

    return ff[-1][-1]
