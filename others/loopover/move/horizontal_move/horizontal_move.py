from collections import namedtuple

from others.loopover.move.move import base_move

Point = namedtuple('Point', 'row column')


def horizontal_move(moves: list, start_column: int, finish_column: int, length: int, current_row: int):
    base_move(
        to_beginning='L',
        to_end='R',
        moves=moves,
        start=start_column,
        finish=finish_column,
        length=length,
        current_other=current_row,
    )
