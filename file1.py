# lecture 11 part 1 of 3
# part 1
# chess_queen_trace
# part 2
# largest_common_subsequence
# part 3
# largest_increasing_subsequence


def chess_queen_trace(m: int, n: int):
    """
    Counts ways to get from square 1,1 to square m,n
    :param m: number of squares on horizontal way
    :param n: number of squares on vertical way
    :return:
    """
    array = [[0] * (m + 1) for k in range(n + 1)]

    array[1][0] = 1  # in order array[1][1] = 1 set array[1][0] = 1 or set array[0][1] = 1

    for j in range(1, m + 1):
        for i in range(1, n + 1):
            array[i][j] = array[i - 1][j] + array[i][j - 1]

    return array[n][m]


def test_chess_queen_trace(algorithm):
    print("test #1:", "ok" if algorithm(2, 4) == 4 else "FAILED")
    print("test #2:", "ok" if algorithm(4, 2) == 4 else "FAILED")
    print("test #3:", "ok" if algorithm(6, 6) == 252 else "FAILED")
    print("test #4:", "ok" if algorithm(7, 7) == 924 else "FAILED")
    print("test #5:", "ok" if algorithm(8, 8) == 3432 else "FAILED")


test_chess_queen_trace(chess_queen_trace)
