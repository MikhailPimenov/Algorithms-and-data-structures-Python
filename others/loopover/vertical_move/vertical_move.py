from others.loopover.base_move.base_move import base_move


def vertical_move(moves: list, start_row: int, finish_row: int, length: int, current_column: int):
    base_move(
        to_beginning='U',
        to_end='D',
        moves=moves,
        start=start_row,
        finish=finish_row,
        length=length,
        current_other=current_column,
    )
