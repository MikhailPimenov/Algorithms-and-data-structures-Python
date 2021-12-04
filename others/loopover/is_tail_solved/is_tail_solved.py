def is_tail_solved(board: list, solved_board: list) -> bool:
    """
    Returns True if two last elements of the board are correct
    according to solved_board
    :param board: list to check two last elements
    :param solved_board: list or tuple with correct elements
    :return: bool
    """
    return board[-1][-1] == solved_board[-1][-1] and \
           board[-1][-2] == solved_board[-1][-2]
