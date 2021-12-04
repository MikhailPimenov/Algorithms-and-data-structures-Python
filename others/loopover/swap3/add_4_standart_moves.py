from others.loopover.point.point import Point
from others.loopover.move.vertical_move.vertical_move import vertical_move
from others.loopover.move.horizontal_move.horizontal_move import horizontal_move


def add_4_standard_moves(
        board: list,
        start: Point,
        finish: Point,
        moves: list
) -> None:
    """
    Adds four steps to moves. These four steps swap three elements without
    changing any other elements on board. Does not modify board, just adds steps.
    Start and finish elements should not be on one line.
    :param board: list with elements. Does not modifies board, just takes lengths of rows and columns.
    :param start: Point - start element which is supposed to appear on the place of finish element.
    :param finish: Point - finish element which is supposed to appear on the place of buffer element.
    Buffer usually lays under finish and on the same row as start.
    :param moves: list to assign new steps to.
    :return: None
    """
    assert start.row != finish.row
    assert start.column != finish.column

    vertical_move(moves, finish.row, start.row, len(board), finish.column)
    horizontal_move(moves, start.column, finish.column, len(board[start.row]), start.row)
    vertical_move(moves, start.row, finish.row, len(board), finish.column)
    horizontal_move(moves, finish.column, start.column, len(board[start.row]), start.row)
