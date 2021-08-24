from others.loopover.move.horizontal_move.horizontal_move import horizontal_move
from others.loopover.move.vertical_move.vertical_move import vertical_move
from others.loopover.point.point import Point


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

    if start.row == finish.row and \
            start.row == len(board) - 1 and \
            finish.column == len(board[start.row]) - 2:
        assert False

    buffer = Point(start.row, finish.column if start.row > finish.row else start.column)

    if start.row == finish.row:
        if start.column - finish.column >= 2:
            vertical_move(
                moves,
                start.row,
                start.row - 1,
                len(board),
                finish.column
            )
            horizontal_move(
                moves,
                finish.column,
                finish.column + 1,
                len(board[start.row - 1]),
                start.row - 1
            )
            new_buffer = Point(finish.row, finish.column + 1)
            new_finish = Point(finish.row - 1, finish.column + 1)
            update_search_board(board, start, finish, new_buffer, search_board)
            replace_board_cells(board, start, finish, new_buffer)
            add_4_standard_moves(board, start, new_finish, moves)
            horizontal_move(
                moves,
                finish.column + 1,
                finish.column,
                len(board[start.row - 1]),
                start.row - 1
            )
            vertical_move(
                moves,
                start.row - 1,
                start.row,
                len(board),
                finish.column
            )
            return

        # start.row != 0  !!! or use (start.row % length) instead of (start.row)
        if start.column < len(board[start.row]) - 1:
            vertical_move(
                moves,
                start.row,
                start.row - 1,
                len(board),
                finish.column
            )
            horizontal_move(
                moves,
                finish.column,
                finish.column + 2,
                len(board[start.row - 1]),
                start.row - 1
            )
            new_finish = Point(finish.row - 1, finish.column + 2)
            new_buffer = Point(start.row, start.column + 1)
            update_search_board(board, start, finish, new_buffer, search_board)  # check if it is correct
            replace_board_cells(board, start, finish, new_buffer)
            add_4_standard_moves(board, start, new_finish, moves)
            horizontal_move(
                moves,
                finish.column + 2,
                finish.column,
                len(board[start.row - 1]),
                start.row - 1
            )
            vertical_move(
                moves,
                start.row - 1,
                start.row,
                len(board),
                finish.column
            )
            return

        assert start.row < len(board) - 1
        vertical_move(moves, start.row, start.row - 1, len(board), finish.column)

        new_buffer = Point(finish.row + 1, finish.column)
        new_finish = Point(finish.row - 1, finish.column)
        update_search_board(board, start, finish, new_buffer, search_board)
        replace_board_cells(board, start, finish, new_buffer)
        add_4_standard_moves(board, start, new_finish, moves)

        vertical_move(moves, start.row - 1, start.row, len(board), finish.column)

        return

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

    update_search_board(board, start, finish, buffer, search_board)
    replace_board_cells(board, start, finish, buffer)
    add_4_standard_moves(board, start, finish, moves)
