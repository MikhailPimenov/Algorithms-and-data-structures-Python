from ..swap2 import swap2
from others.loopover.point.point import Point


def swap2_vertical(
        board: list,
        start: Point,
        finish: Point,
        length: int,
        moves: list,
        search_board: dict,
) -> None:
    """
    Swaps two horizontally adjacent elements. Assigns steps to moves.
    Modifies board and search_board. This function can be called
    if vertical length of the board is even. All this function is doing
    is calling base swap2 function with letters to_beginning = 'L' and to_end = 'R'.
    It is called vertical because main direction of steps is from up to down.
    :param board: list whose elements should be swapped.
    :param start: Point - element to be swapped with finish. After this function is called
    start element will have coordinates of finish element.
    :param finish: Point - element to be swapped with start. After this function is called
    finish element will have coordinates of start element.
    :param length: int - vertical length of the board. Must be even, otherwise it is
    impossible to do such swap.
    :param moves: list to assign new steps to.
    :param search_board: dictionary with all elements as keys and their coordinates as values.
    :return: None
    """
    assert start.row == finish.row
    assert not length % 2

    swap2(
        board=board,
        start=start,
        finish=finish,
        to_beginning='L',
        to_end='R',
        length=length,
        moves=moves,
        search_board=search_board,
    )
