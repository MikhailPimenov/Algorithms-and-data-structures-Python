from others.loopover.point.point import Point
from .update_search_board2 import update_search_board2
from .replace_board_cells2 import replace_board_cells2


def swap2(
        board: list,
        start: Point,
        finish: Point,
        to_beginning: str,
        to_end: str,
        length: int,
        moves: list,
        search_board: dict,
) -> None:
    """
    Swaps two elements and adds moves with actual modification of board and search_board.
    :param board: list - board where to swap two elements.
    :param start: Point - the first element to be swapped. start becomes finish.
    :param finish: Point - the second element to be swapped. finish becomes start.
    :param to_beginning: str - letter to represent move to the beginning, for example 'L' for
    left-move, or 'U' for up-move.
    :param to_end: str - letter to represent move to the end, for example 'R' for right-move,
    or 'D' for down-move.
    :param length: int - length of the array (length of the row or column).
    :param moves: List of moves to assign new moves to. length fully determines how many
    steps will be assigned.
    :param search_board: dictionary with all elements as keys and their coordinates as values.
    :return: None
    """

    #  choosing the direction of move:
    if to_beginning == 'L':
        base_direction = 'D'
        position_along = start.column
        position_perpendicular = start.row
    else:
        base_direction = 'R'
        position_along = start.row
        position_perpendicular = start.column

    #  move consists of one step in base direction and one step in perpendicular
    #  direction (to_beginning or to_end), the next move consists of one step in
    #  that same base direction and one step in perpendicular direction but opposite
    #  to perpendicular direction of the previous move (to_end or to_beginning). These moves
    #  repeat until steps in base direction come along entire length.
    #  base_direction can be from up to down and from left to right. In these cases
    #  to_beginning/to_end would be left/right and up/down.
    #  Example for 6x10: D0-L5-D0-R5-D0-L5-D0-R5-D0-L5-D0-R5-D0 if base direction is
    #  from up to down. In that case elements board[5][0] and board[5][1] would be swapped
    #  Example for 6x10: R5-D9-R5-U9-R5-D9-R5-U9-R5-D9-R5-U9-R5-D9-R5-U9-R5-D9-R5-U9-R5 if
    #  base direction is from left to right. In that case elements board[5][9] and board[4][9]
    #  would be swapped.
    for i in range(length):
        #  step in base direction:
        moves.append(f'{base_direction}{position_along}')
        #  step in perpendicular direction. This step alternates:
        moves.append(f'{to_beginning if i % 2 else to_end}{position_perpendicular}')

    #  the last step in base direction:
    moves.append(f'{base_direction}{position_along}')

    #  updating seach_board and replacing elements on board:
    update_search_board2(board, search_board, start, finish)
    replace_board_cells2(board, start, finish)
