from others.loopover.swap3.swap3 import Point
from others.loopover.swap3.swap3 import swap3


def solve(board: list, solved_board: list):
    search_board = {
        board[i][j]: Point(i, j)
        for i in range(len(board))
        for j in range(len(board[i]))
    }

    search_solved_board = {
        Point(i, j): solved_board[i][j]
        for i in range(len(solved_board))
        for j in range(len(solved_board[i]))
    }

    already_solved = set()

    moves = []
    for row in range(len(board) - 1):
        for column in range(len(board[row])):
            start_symbol = solved_board[row][column]
            finish_symbol = board[row][column]

            start = search_board[solved_board[row][column]]
            finish = Point(row, column)
            swap3(board, start, finish, moves, search_board)

    row = len(board) - 1
    for column in range(len(board[row]) - 2):
        start = search_board[solved_board[row][column]]
        finish = Point(row, column)
        swap3(board, start, finish, moves, search_board)

    if tail_is_solved(board, solved_board):
        return moves

    if len(board) % 2 and len(board[0]) % 2:
        return None

    if len(board) % 2:
        swap2_horizontal(board, moves)
        start = Point(row, len(board[row]) - 2)
        finish = Point(row - 1, len(board[row]) - 1)
        swap3(board, start, finish, moves, search_board)
        return moves

    swap2_vertical(board, moves)
    return moves
