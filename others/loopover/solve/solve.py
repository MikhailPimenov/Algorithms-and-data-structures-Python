import copy

from others.loopover.swap3.swap3 import Point
from others.loopover.swap3.swap3 import swap3
from others.loopover.is_tail_solved.is_tail_solved import is_tail_solved
from others.loopover.swap2.swap2_horizontal.swap2_horizontal import swap2_horizontal
from others.loopover.swap2.swap2_vertical.swap2_vertical import swap2_vertical
from others.loopover.swap3.swap3_last_row import swap3_last_row
from others.loopover.move.reduce_moves import reduce_moves

from others.loopover.simulator.simulator import simulator


def solve(board: list, solved_board: list) -> list:
    board_for_simulator = copy.deepcopy(board)
    moves_pointer = 0

    #  to speed up searching elements all elements were added to hash table:
    search_board = {
        symbol: Point(row_index, column_index)
        for row_index, row in enumerate(board)
        for column_index, symbol in enumerate(row)
    }

    #  placing all elements on their places except the last line:
    #  all rows are considered in the order going straightly from up to down,
    #  and all columns are considered in the order going from left
    #  to right within current row - swapping these elements using
    #  the third buffer element which is not above current row and not from the
    #  left side - not modifying already placed elements:
    moves = []
    for row in range(len(board) - 1):
        for column in range(len(board[row])):
            #  considering current row and column - the second element (finish):
            finish = Point(row, column)

            #  looking up to this element in hash table - the first element (start):
            start = search_board[solved_board[row][column]]

            #  if position of this element differs in solved board and board, swapping elements:
            if start != finish:
                #  swapping first, second and the third element - the third element (buffer)
                #  is defined inside swap3 and is not above the current row and not from the left
                #  side of finish column - to keep all previously solved elements the same:
                swap3(board, start, finish, moves, search_board)

                simulator(board_for_simulator, tuple(moves[moves_pointer:]))
                moves_pointer = len(moves)

    #  on this stage all elements of all rows except the last one are on their final correct places

    #  for the last line swapping differs:
    #  all columns of the last row are also considered in order going from left to right
    row = len(board) - 1
    for column in range(len(board[row]) - 2):
        #  considering current place (last row and current column):
        finish = Point(row, column)

        #  looking up to this element in hash table:
        start = search_board[solved_board[row][column]]

        #  if position of this element differs in solved board and board, swapping elements:
        if start != finish:
            #  same as swap3 but for the last row - buffer element is always on the same row:
            swap3_last_row(board, start, finish, moves, search_board)

            simulator(board_for_simulator, tuple(moves[moves_pointer:]))
            moves_pointer = len(moves)

    #  on this stage all elements of all rows except the last one are on their final correct places.
    #  In the last row all elements can be either on their places, or exactly two of them from the
    #  right side are swapped. Swapping two elements without any buffer element differs from both
    #  previous swapping procedures.

    #  if two last elements are on their correct places, the task is done:
    if is_tail_solved(board, solved_board):
        #  getting rid of steps which cancel each other and returning the final answer:
        return reduce_moves(moves)

    #  if both dimensions are uneven it is impossible to swap two elements without a buffer,
    #  what means that configuration is unsolvable:
    if len(board) % 2 and len(board[0]) % 2:
        return None

    #  if vertical length is uneven:
    if len(board) % 2:
        #  the very last element and the very last element of the previous row:
        start = Point(row, len(board[row]) - 1)
        finish = Point(row - 1, len(board[row]) - 1)

        #  swapping them without a buffer:
        swap2_horizontal(board, start, finish, len(board[row]), moves, search_board)

        simulator(board_for_simulator, tuple(moves[moves_pointer:]))
        moves_pointer = len(moves)

        #  in that case element of the previous row is changed:
        start = Point(row, len(board[row]) - 2)
        finish = Point(row - 1, len(board[row]) - 1)

        swap3(board, start, finish, moves, search_board)

        simulator(board_for_simulator, tuple(moves[moves_pointer:]))
        moves_pointer = len(moves)

        swap3(board, start, finish, moves, search_board)

        simulator(board_for_simulator, tuple(moves[moves_pointer:]))
        moves_pointer = len(moves)

        #  getting rid of steps which cancel each other and returning the final answer:
        return reduce_moves(moves)

    #  if vertical length is even, swapping two last elements of the last row without buffer:
    start = Point(row, len(board[row]) - 1)
    finish = Point(row, len(board[row]) - 2)

    swap2_vertical(board, start, finish, len(board), moves, search_board)

    simulator(board_for_simulator, tuple(moves[moves_pointer:]))
    moves_pointer = len(moves)

    #  getting rid of steps which cancel each other and returning the final answer:
    return reduce_moves(moves)
