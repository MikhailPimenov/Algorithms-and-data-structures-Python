def base_move(to_beginning: str, to_end: str, moves: list, start: int, finish: int, length: int, current_other: int):
    if finish == start:
        return

    if finish - start > 0:
        if finish - start < start + length - finish:
            direction = to_end
            number_of_steps = finish - start
        else:
            direction = to_beginning
            number_of_steps = start + length - finish
    else:
        if start - finish < length - start + finish:
            direction = to_beginning
            number_of_steps = start - finish
        else:
            direction = to_end
            number_of_steps = length - start + finish

    all_moves = [f'{direction}{current_other}'] * number_of_steps
    moves.extend(all_moves)
