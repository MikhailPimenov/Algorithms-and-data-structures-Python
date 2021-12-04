def base_move(
        to_beginning: str,
        to_end: str,
        moves: list,
        start: int,
        finish: int,
        length: int,
        current_other: int
) -> None:
    """
    Adds moves for shifting row/column. No actual array shifting occurs. This function
    does not modify array, just adds moves. Calculates the number of steps in both straight
    (forward) and reversed (backward) directions and chooses one with minimal number of steps.
    :param to_beginning: str - letter to represent move to the beginning, for example 'L' for
    left-move, or 'U' for up-move.
    :param to_end: str - letter to represent move to the end, for example 'R' for right-move,
    or 'D' for down-move.
    :param moves: List of moves to assign new moves to. Difference between start
    and finish determines how many steps will be assigned.
    :param start: int - starting position. Difference between starting and finishing position
    determines how many times shifting by one will be occurred.
    :param finish: int - finishing position. Difference between starting and finishing position
    determines how many times shifting by one will be occurred.
    :param length: int - length of the array.
    :param current_other: int - row or column to shift.
    :return: None
    """

    #  no moves required:
    if finish == start:
        return

    #  number of steps:
    straight_steps = abs(finish - start)

    #  number of steps in opposite direction:
    reversed_steps = length - straight_steps

    #  choosing minimal number of steps:
    if straight_steps < reversed_steps:
        number_of_steps = straight_steps
        direction = to_end if finish - start > 0 else to_beginning
    else:
        number_of_steps = reversed_steps
        direction = to_beginning if finish - start > 0 else to_end

    #  creating steps:
    all_moves = [f'{direction}{current_other}'] * number_of_steps

    #  adding all steps to moves:
    moves.extend(all_moves)
