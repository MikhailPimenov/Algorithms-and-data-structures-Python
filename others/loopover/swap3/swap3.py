from collections import namedtuple
from others.loopover.horizontal_move.horizontal_move import horizontal_move
from others.loopover.vertical_move.vertical_move import vertical_move

Point = namedtuple('Point', 'row column')


def update_search_board(board: list, start: Point, finish: Point, buffer: Point, search_board: dict):
    search_board[board[finish.row][finish.column]] = Point(buffer.row, buffer.column)
    search_board[board[start.row][start.column]] = Point(finish.row, finish.column)
    search_board[board[buffer.row][buffer.column]] = Point(start.row, start.column)


def replace_board_cells(board: list, start: Point, finish: Point, buffer: Point):
    temp = board[finish.row][finish.column]
    board[finish.row][finish.column] = board[start.row][start.column]
    board[start.row][start.column] = board[buffer.row][buffer.column]
    board[buffer.row][buffer.column] = temp


def add_4_standard_moves(board: list, start: Point, finish: Point, moves: list):
    vertical_move(moves, finish.row, start.row, len(board), finish.column)
    horizontal_move(moves, start.column, finish.column, len(board[start.row]), start.row)
    vertical_move(moves, start.row, finish.row, len(board), finish.column)
    horizontal_move(moves, finish.column, start.column, len(board[start.row]), start.row)


def swap3(board: list, start: Point, finish: Point, moves: list, search_board: dict):
    if start == finish:
        return
    assert start.row != finish.row

    buffer = Point(start.row, finish.column if start.row > finish.row else start.column)

    if start.column == finish.column:
        if start.column == len(board[finish.row]) - 1:
            horizontal_move(
                moves,
                start.column,
                start.column - 1,
                len(board[finish.row]),
                finish.row,
            )
            buffer = Point(buffer.row, buffer.column - 1)
            update_search_board(board, start, finish, buffer, search_board)
            replace_board_cells(board, start, finish, buffer)
            add_4_standard_moves(board, start, finish, moves)
            horizontal_move(
                moves,
                start.column - 1,
                start.column,
                len(board[finish.row]),
                finish.row,
            )
            return

        horizontal_move(
            moves,
            start.column,
            start.column + 1,
            len(board[finish.row]),
            finish.row,
        )
        buffer = Point(buffer.row, buffer.column + 1)
        update_search_board(board, start, finish, buffer, search_board)
        replace_board_cells(board, start, finish, buffer)
        add_4_standard_moves(board, start, finish, moves)
        horizontal_move(
            moves,
            start.column + 1,
            start.column,
            len(board[finish.row]),
            finish.row,
        )
        return

    # if start.row == finish.row:

    update_search_board(board, start, finish, buffer, search_board)
    replace_board_cells(board, start, finish, buffer)
    add_4_standard_moves(board, start, finish, moves)
