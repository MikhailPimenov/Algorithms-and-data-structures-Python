from others.loopover.point.point import Point


def update_search_board2(board: list, search_board: dict, start: Point, finish: Point) -> None:
    """
    Updates search board, swapping start element and finish element.
    :param board: list - where elements are taken from.
    :param search_board: dictionary with all elements as keys and their coordinates as values - to be updated
    :param start: Point - its coordinates in search_board will be replaced with coordinates of finish.
    :param finish: Point - its coordinates in search_board will be replaced with coordinates of start.
    :return: None
    """
    search_board[board[start.row][start.column]] = finish
    search_board[board[finish.row][finish.column]] = start
