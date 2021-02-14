def chess_queen(m: int, n: int):
    s = [[0] * (m + 1) for k in range(n + 1)]

    s[1][1] = 1

    for k in range(1, n + 1):
        for t in range(1, m + 1):
            if not (k == 1 and t == 1):
                s[k][t] = s[k - 1][t] + s[k][t - 1]
    return s[n][m]
