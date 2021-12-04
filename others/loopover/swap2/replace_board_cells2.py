from others.loopover.point.point import Point


def replace_board_cells2(board: list, start: Point, finish: Point) -> None:
    """
    Swaps start and finish in board.
    :param board: list - where elements replace each other.
    :param start: Point - after this function is called this element will have coordinates of finish.
    :param finish: Point - after this function is called this element will have coordinates of start.
    :return: None
    """
    temp = board[start.row][start.column]
    board[start.row][start.column] = board[finish.row][finish.column]
    board[finish.row][finish.column] = temp
