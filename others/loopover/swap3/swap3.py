from others.loopover.move.horizontal_move.horizontal_move import horizontal_move
from others.loopover.move.vertical_move.vertical_move import vertical_move
from others.loopover.point.point import Point

from .add_4_standart_moves import add_4_standard_moves
from .update_search_board3 import update_search_board3
from .replace_board_cells3 import replace_board_cells3


def swap3(
        board: list,
        start: Point,
        finish: Point,
        moves: list,
        search_board: dict
) -> None:
    """
    Swaps 3 elements. Modifies board, modifies search_board. Assigns steps to moves.
    Selects the third element - buffer element. After this function is called start
    element would be on the place of finish element. Finish element would be on the place
    of buffer element. Buffer element would be on the place of start element.
    The buffer (the third element to be swapped) has row of start element and
    has column of finish element in case start and finish elements have both different rows
    and columns. If start and finish have the same row the buffer element will have finish
    column and start/finish row + 1 (it will be below the finish element). If start and
    finish have the same column the buffer element hill have start row and start/finish
    column - 1 (it will be adjacent to the left side of start element). This function
    should not be called when start is above finish.
    :param board: list where to swap elements.
    :param start: Point - this element will be on the position of finish.
    :param finish: Point - this element will be on the position of buffer.
    :param moves: list of steps to assign new steps to.
    :param search_board: dictionary with all elements as keys and their coordinates as values.
    :return: None
    """
    if start == finish:
        return

    #  for the last two elements of the board this function is not suitable:
    if start.row == finish.row and \
            start.row == len(board) - 1 and \
            finish.column == len(board[start.row]) - 2:
        assert False

    assert start.row >= finish.row

    if start.row == finish.row:
        row = start.row
        vertical_move(
            moves=moves,
            start_row=row,
            finish_row=row - 1,
            length=len(board),
            current_column=finish.column,
        )

        start_for_moves = start
        finish_for_moves = Point(
            (row - 1 + len(board)) % len(board),
            finish.column
        )

        add_4_standard_moves(
            board=board,
            start=start_for_moves,
            finish=finish_for_moves,
            moves=moves,
        )

        vertical_move(
            moves=moves,
            start_row=row,
            finish_row=row + 1,
            length=len(board),
            current_column=finish.column,
        )

        start_to_replace = start
        finish_to_replace = finish
        buffer_to_replace = Point(
            (row + 1 + len(board)) % len(board),
            finish.column
        )

        start_symbol = board[start_to_replace.row][start_to_replace.column]
        finish_symbol = board[finish_to_replace.row][finish_to_replace.column]
        buffer_symbol = board[buffer_to_replace.row][buffer_to_replace.column]
        update_search_board3(
            start=start_symbol,
            finish=finish_symbol,
            buffer=buffer_symbol,
            search_board=search_board,
        )

        replace_board_cells3(
            board=board,
            start=start_to_replace,
            finish=finish_to_replace,
            buffer=buffer_to_replace,
        )

        return

    if start.column == finish.column:
        column = start.column
        horizontal_move(
            moves=moves,
            start_column=column - 1,
            finish_column=column,
            length=len(board[start.row]),
            current_row=start.row,
        )

        start_for_moves = Point(
            start.row,
            (column + 1) % len(board[start.row]),
        )
        finish_for_moves = finish

        add_4_standard_moves(
            board=board,
            start=start_for_moves,
            finish=finish_for_moves,
            moves=moves,
        )

        horizontal_move(
            moves=moves,
            start_column=column + 1,
            finish_column=column,
            length=len(board[start.row]),
            current_row=start.row,
        )

        start_to_replace = start
        finish_to_replace = finish
        buffer_to_replace = Point(
            start.row,
            (column - 1 + len(board[start.row])) % len(board[start.row]),
        )

        start_symbol = board[start_to_replace.row][start_to_replace.column]
        finish_symbol = board[finish_to_replace.row][finish_to_replace.column]
        buffer_symbol = board[buffer_to_replace.row][buffer_to_replace.column]

        update_search_board3(
            start=start_symbol,
            finish=finish_symbol,
            buffer=buffer_symbol,
            search_board=search_board,
        )

        replace_board_cells3(
            board=board,
            start=start_to_replace,
            finish=finish_to_replace,
            buffer=buffer_to_replace,
        )

        return

    buffer = Point(
        start.row if start.row > finish.row else finish.row,
        finish.column if start.row > finish.row else start.column,
    )

    add_4_standard_moves(board, start, finish, moves)

    start_symbol = board[start.row][start.column]
    finish_symbol = board[finish.row][finish.column]
    buffer_symbol = board[buffer.row][buffer.column]

    update_search_board3(
        start=start_symbol,
        finish=finish_symbol,
        buffer=buffer_symbol,
        search_board=search_board,
    )

    replace_board_cells3(
        board=board,
        start=start,
        finish=finish,
        buffer=buffer,
    )
