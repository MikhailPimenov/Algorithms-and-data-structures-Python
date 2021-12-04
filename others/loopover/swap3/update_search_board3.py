def update_search_board3(
        start: str,
        finish: str,
        buffer: str,
        search_board: dict
) -> None:
    """
    Updates search board, swapping start element, finish element and buffer element.
    :param start: str - its coordinates in search_board will be replaced with coordinates of finish.
    :param finish: str - its coordinates in search_board will be replaced with coordinates of buffer.
    :param buffer: str - its coordinates in search_board will be replaced with coordinates of start.
    :param search_board: dictionary with all elements as keys and their coordinates as values - to be updated
    :return: None
    """
    (search_board[start],
     search_board[finish],
     search_board[buffer]) =\
    (search_board[finish],
     search_board[buffer],
     search_board[start])