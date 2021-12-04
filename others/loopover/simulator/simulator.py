from others.loopover.simulator.shift_array.shift_array import shift_row, shift_column


def simulator(board: list, moves: tuple) -> None:
    if not moves:
        return

    previous_move = moves[0]
    shift = 1
    for index in range(1, len(moves)):
        if previous_move == moves[index]:
            shift += 1
            previous_move = moves[index]
            continue

        if previous_move[0] in ('L', 'U'):
            shift *= -1

            if previous_move[0] == 'L':
                shift_row(board, int(previous_move[1]), shift)
                previous_move = moves[index]
                shift = 1
                continue

            shift_column(board, int(previous_move[1]), shift)
            previous_move = moves[index]
            shift = 1
            continue

        if previous_move[0] == 'R':
            shift_row(board, int(previous_move[1]), shift)
            previous_move = moves[index]
            shift = 1
            continue

        shift_column(board, int(previous_move[1]), shift)
        previous_move = moves[index]
        shift = 1

    if previous_move[0] in ('L', 'U'):
        shift *= -1

        if previous_move[0] == 'L':
            shift_row(board, int(previous_move[1]), shift)
            return

        shift_column(board, int(previous_move[1]), shift)
        return

    if previous_move[0] == 'R':
        shift_row(board, int(previous_move[1]), shift)
        return

    shift_column(board, int(previous_move[1]), shift)
