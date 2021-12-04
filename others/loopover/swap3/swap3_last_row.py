from others.loopover.point.point import Point
from others.loopover.move.horizontal_move.horizontal_move import horizontal_move
from others.loopover.move.vertical_move.vertical_move import vertical_move

from .add_4_standart_moves import add_4_standard_moves
from .update_search_board3 import update_search_board3
from .replace_board_cells3 import replace_board_cells3


def swap3_last_row(
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
    of buffer element. The only difference between swap3 is that buffer is on the same row.
    If start and finish are adjacent buffer will be from the right side of start.
    If start and finish have a gap between them buffer will be on the right side of finish,
    between finish and start. Do not call this function when finish is on the right side of
    start. This function is suitable for the very last row of the board, when all previous rows
    are solved and should not be modified.
    :param board: list where to swap elements.
    :param start: Point - this element will be on the position of finish.
    :param finish: Point - this element will be on the position of buffer.
    :param moves: list of steps to assign new steps to.
    :param search_board: dictionary with all elements as keys and their coordinates as values.
    :return: None
    """
    assert start.row == len(board) - 1
    assert finish.row == len(board) - 1
    assert start.row == finish.row
    assert finish.column < len(board[start.row]) - 1
    assert start.column > finish.column

    row = start.row

    #  when start and finish are adjacent to each other:
    if start.column - finish.column == 1:
        vertical_move(
            moves=moves,
            start_row=row,
            finish_row=row - 1,
            length=len(board),
            current_column=finish.column,
        )
        horizontal_move(
            moves=moves,
            start_column=finish.column,
            finish_column=(finish.column + 1) % len(board[row - 1]),
            length=len(board[row - 1]),
            current_row=row - 1,
        )

        start_for_moves = Point(
            row,
            (start.column + 1) % len(board[row])
        )
        finish_for_moves = Point(
            row - 1,
            (finish.column + 1) % len(board[row]),
        )

        add_4_standard_moves(
            board=board,
            start=start_for_moves,
            finish=finish_for_moves,
            moves=moves,
        )
        add_4_standard_moves(
            board=board,
            start=start_for_moves,
            finish=finish_for_moves,
            moves=moves,
        )

        horizontal_move(
            moves=moves,
            start_column=(finish.column + 1) % len(board[row - 1]),
            finish_column=finish.column,
            length=len(board[row - 1]),
            current_row=row - 1,
        )
        vertical_move(
            moves=moves,
            start_row=row - 1,
            finish_row=row,
            length=len(board),
            current_column=finish.column,
        )

        start_to_replace = start
        finish_to_replace = finish
        buffer_to_replace = Point(
            row,
            (start.column + 1) % len(board[row]),
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

    #  when there is a gap between start and finish:
    vertical_move(
        moves=moves,
        start_row=row,
        finish_row=row - 1,
        length=len(board),
        current_column=finish.column,
    )
    horizontal_move(
        moves=moves,
        start_column=finish.column,
        finish_column=(finish.column + 1) % len(board[row - 1]),
        length=len(board[row - 1]),
        current_row=row - 1,
    )

    start_for_moves = start
    finish_for_moves = Point(
        row - 1,
        (finish.column + 1) % len(board[row]),
    )

    add_4_standard_moves(
        board=board,
        start=start_for_moves,
        finish=finish_for_moves,
        moves=moves,
    )

    horizontal_move(
        moves=moves,
        start_column=(finish.column + 1) % len(board[row - 1]),
        finish_column=finish.column,
        length=len(board[row - 1]),
        current_row=row - 1,
    )
    vertical_move(
        moves=moves,
        start_row=row - 1,
        finish_row=row,
        length=len(board),
        current_column=finish.column,
    )

    start_to_replace = start
    finish_to_replace = finish
    buffer_to_replace = Point(
        row,
        (finish.column + 1) % len(board[row]),
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
