from ..swap2 import swap2
from others.loopover.point.point import Point


def swap2_vertical(
        board: list,
        start: Point,
        finish: Point,
        length: int,
        moves: list,
        search_board: dict,
):
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
