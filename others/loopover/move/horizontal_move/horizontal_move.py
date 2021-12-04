from others.loopover.move.move import base_move


def horizontal_move(
        moves: list,
        start_column: int,
        finish_column: int,
        length: int,
        current_row: int
) -> None:
    """
    Adds moves for shifting row. Shifting value is determined by difference between
    start_column and finish_column. It calls base_move with specified parameters for
    horizontal move: with letter 'L' (left) for direction to the beginning and with
    the letter 'R' (right) for the direction to the end. No actual shift of the array
    of elements occurs, this function just adds moves and does not modify the array
    of elements.
    :param moves: List of moves to assign new moves to. Difference between start_column
    and finish_column determines how many steps will be assigned.
    :param start_column: int - starting position. After this function is called element with
    column=start_column and row=current_row will be on the position where column=finish_column
    and row=current_row. Calling this function with (start_column + k) and (finish_column + k),
    where k is integer, will lead to the same result.
    :param finish_column: int - finishing position. After this function is called element with
    column=start_column and row=current_row will be on this position where column=finish_column
    and row=current_row. Calling this function with (start_column + k) and (finish_column + k),
    where k is integer, will lead to the same result.
    :param length: int - the length of the row. Defines number after which column number
    is again zero.
    :param current_row: int - row where shifting is occurred.
    :return: None
    """
    base_move(
        to_beginning='L',
        to_end='R',
        moves=moves,
        start=start_column,
        finish=finish_column,
        length=length,
        current_other=current_row,
    )
