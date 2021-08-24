def is_tail_solved(board: list, solved_board: list):
    return board[-1][-1] == solved_board[-1][-1] and \
           board[-1][-2] == solved_board[-1][-2]
