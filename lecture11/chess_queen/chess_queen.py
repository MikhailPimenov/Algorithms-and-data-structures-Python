def chess_queen(m: int, n: int):
    deck = [[0] * (n + 1) for j in range(m + 1)]

    for i in range(m + 1):
        deck[i][0] = 0
    for j in range(n + 1):
        deck[0][j] = 0

    deck[1][1] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i != 1 or j != 1:
                deck[i][j] = deck[i - 1][j] + deck[i][j - 1]

    return deck[m][n]
