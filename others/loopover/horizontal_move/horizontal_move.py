from collections import namedtuple

from others.loopover.base_move.base_move import base_move

Point = namedtuple('Point', 'row column')


# def triangle_move_horizontal(board: list, center: Point, moves: list, horizontal_steps: int = 1, vertical_steps: int = 1):
#     buffer = board[center.row + vertical_steps][center.column + horizontal_steps]
#
#     board[center.row + vertical_steps][center.column + horizontal_steps] = \
#         board[center.row][center.column]
#
#     board[center.row][center.column] = \
#         board[center.row][center.column + horizontal_steps]
#
#     board[center.row][center.column + horizontal_steps] = buffer
#
#     moves.append(f'D{center.column + horizontal_steps}') # vertical_steps times
#     moves.append(f'L{center.row}')


def horizontal_move(moves: list, start_column: int, finish_column: int, length: int, current_row: int):
    base_move(
        to_beginning='L',
        to_end='R',
        moves=moves,
        start=start_column,
        finish=finish_column,
        length=length,
        current_other=current_row,
    )


def move(board: list, start: Point, finish: Point, buffer: Point, moves: list):
    assert start.row != buffer.row or finish.row != buffer.row
    assert start.column != buffer.column or finish.column != buffer.column
    # start 0 3
    # finish 0 0
    # buffer 4 3

    if buffer.row > finish.row:
        first_direction = "D"
        steps = buffer.row - finish
        for _ in range(steps):
            moves.append(f'{first_direction}{finish.column}')


# def left_up(board: list, center: Point, moves: list, left_steps: int = 1, up_steps: int = 1 ):
#     buffer = board[center.row - up_steps][center.column - 1]
#     board[center.row - 1][center.column - 1] = board[center.row][center.column]
#     board[center.row][center.column] = board[center.row][center.column - 1]
#     board[center.row][center.column - 1] = buffer
#
#     moves.append(f'D{center.column - 1}')
#     moves.append(f'L{center.row}')
#     moves.append(f'U{center.column - 1}')
#     moves.append(f'R{center.row}')
#
#
# def up_left(board: list, center: Point, moves: list):
#     pass


max_row = 6
max_column = 6
board = [[0] * max_column for _ in range(max_row)]

number = 1
for i in range(len(board)):
    for j in range(len(board[i])):
        board[i][j] = number
        number += 1


def print_board(board: list):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(f'{board[i][j]:<5}', end='')
        print()
    print()


# print_board(board)
moves = []
# board[0][4] = 99
# print_board(board)
