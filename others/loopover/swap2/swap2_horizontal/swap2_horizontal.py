from ..swap2 import swap2
from others.loopover.point.point import Point


def swap2_horizontal(
        board: list,
        start: Point,
        finish: Point,
        length: int,
        moves: list,
        search_board: dict,
) -> None:
    """
    Swaps two vertically adjacent elements. Assigns steps to moves.
    Modifies board and search_board. This function can be called
    if horizontal length of the board is even. All this function is doing
    is calling base swap2 function with letters to_beginning = 'U' and to_end = 'D'.
    It is called horizontal because main direction of steps is from left to right.
    :param board: list whose elements should be swapped.
    :param start: Point - element to be swapped with finish. After this function is called
    start element will have coordinates of finish element.
    :param finish: Point - element to be swapped with start. After this function is called
    finish element will have coordinates of start element.
    :param length: int - horizontal length of the board. Must be even, otherwise it is
    impossible to do such swap.
    :param moves: list to assign new steps to.
    :param search_board: dictionary with all elements as keys and their coordinates as values.
    :return: None
    """
    assert start.column == finish.column
    assert not length % 2

    swap2(
        board=board,
        start=start,
        finish=finish,
        to_beginning='U',
        to_end='D',
        length=length,
        moves=moves,
        search_board=search_board,
    )
