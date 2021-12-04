from others.loopover.move.move import base_move


def vertical_move(
        moves: list,
        start_row: int,
        finish_row: int,
        length: int,
        current_column: int
) -> None:
    """
    Adds moves for shifting column. Shifting value is determined by difference between
    start_row and finish_row. It calls base_move with specified parameters for vertical
    move: with letter 'U' (up) for direction to the beginning and with the letter 'D'
    (down) for the direction to the end. No actual shift of the array of elements occurs,
    this function just adds moves and does not modify the array of elements.
    :param moves: List of moves to assign new moves to. Difference between start_row
    and finish_row determines how many steps will be assigned.
    :param start_row: int - starting position. After this function is called element with
    row=start_row and column=current_column will be on the position where row=finish_row
    and column=current_column. Calling this function with (start_row + k) and (finish_row + k),
    where k is integer, will lead to the same result.
    :param finish_row: int - finishing position. After this function is called element with
    row=start_row and column=current_column will be on this position where row=finish_row
    and column=current_column. Calling this function with (start_row + k) and (finish_row + k),
    where k is integer, will lead to the same result.
    :param length: int - the length of the column. It is the number of the rows. Defines number
    after which row number is zero again.
    :param current_column: int - column where shifting is occurred.
    :return: None
    """
    base_move(
        to_beginning='U',
        to_end='D',
        moves=moves,
        start=start_row,
        finish=finish_row,
        length=length,
        current_other=current_column,
    )
