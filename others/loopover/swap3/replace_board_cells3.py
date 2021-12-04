from others.loopover.point.point import Point


def replace_board_cells3(
        board: list,
        start: Point,
        finish: Point,
        buffer: Point
) -> None:
    """
    Swaps 3 elements in board. Modifies board.
    :param board: list where to swap elements.
    :param start: Point - start element. On this place there will be buffer element.
    :param finish: Point - finish element. On this place there will be start element.
    :param buffer: Point - buffer element. On this place there will be finish element.
    :return: None
    """
    (board[finish.row][finish.column],
     board[start.row][start.column],
     board[buffer.row][buffer.column]) = \
    (board[start.row][start.column],
     board[buffer.row][buffer.column],
     board[finish.row][finish.column])