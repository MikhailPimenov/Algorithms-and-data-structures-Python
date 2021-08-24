from others.loopover.swap3.swap3 import Point
from others.loopover.swap3.swap3 import swap3
from others.loopover.is_tail_solved.is_tail_solved import is_tail_solved
from others.loopover.move.horizontal_move.horizontal_move import horizontal_move
from others.loopover.swap2.swap2_horizontal.swap2_horizontal import swap2_horizontal
from others.loopover.swap2.swap2_vertical.swap2_vertical import swap2_vertical


def solve(board: list, solved_board: list):
    search_board = {
        board[i][j]: Point(i, j)
        for i in range(len(board))
        for j in range(len(board[i]))
    }

    moves = []
    for row in range(len(board) - 1):
        for column in range(len(board[row])):
            start = search_board[solved_board[row][column]]
            finish = Point(row, column)
            swap3(board, start, finish, moves, search_board)

    row = len(board) - 1
    for column in range(len(board[row]) - 2):
        start = search_board[solved_board[row][column]]
        finish = Point(row, column)
        swap3(board, start, finish, moves, search_board)

    if is_tail_solved(board, solved_board):
        return moves

    if len(board) % 2 and len(board[0]) % 2:
        return None

    if len(board) % 2:
        start = Point(row, len(board[row]) - 1)
        finish = Point(row - 1, len(board[row]) - 1)
        swap2_horizontal(board, start, finish, len(board[row]), moves, search_board)

        start = Point(row, len(board[row]) - 2)
        finish = Point(row - 1, len(board[row]) - 1)
        swap3(board, start, finish, moves, search_board)
        swap3(board, start, finish, moves, search_board)

        return moves

    start = Point(row, len(board[row]) - 1)
    finish = Point(row, len(board[row]) - 2)
    swap2_vertical(board, start, finish, len(board), moves, search_board)
    return moves
