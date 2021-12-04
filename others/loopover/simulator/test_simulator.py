import unittest
import copy

from .simulator import simulator as algorithm
# from ..solve import solve as solving_algorithm
from others.loopover.solve.solve import solve as solving_algorithm


def print_board(board: list):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(f'{board[i][j]:<5}', end='')
        print()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pattern = [
            [3, 1, 2],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
        ]
        solved_pattern = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [10, 11, 12],
        ]
        board = copy.deepcopy(pattern)
        moves = ['L0']

        algorithm(board, tuple(moves))
        self.assertEqual(solved_pattern, board, "test #1:")

        board = copy.deepcopy(pattern)
        moves = ['R0', 'R0']

        algorithm(board, tuple(moves))
        self.assertEqual(solved_pattern, board, "test #2:")

        pattern = [
            [1, 5, 3],
            [4, 8, 6],
            [7, 11, 9],
            [10, 2, 12],
        ]
        board = copy.deepcopy(pattern)
        moves = ['D1']

        algorithm(board, tuple(moves))
        self.assertEqual(solved_pattern, board, "test #3:")

        board = copy.deepcopy(pattern)
        moves = ['U1', 'U1', 'U1']

        algorithm(board, tuple(moves))
        self.assertEqual(solved_pattern, board, "test #4:")

        pattern = [
            [4, 5, 3],
            [7, 8, 6],
            [9, 10, 11],
            [1, 2, 12],
        ]
        board = copy.deepcopy(pattern)
        moves = ['L2', 'D0', 'D1']

        algorithm(board, tuple(moves))
        self.assertEqual(solved_pattern, board, "test #5:")

        board = copy.deepcopy(pattern)
        moves = ['R2', 'R2', 'D0', 'D1']

        algorithm(board, tuple(moves))
        self.assertEqual(solved_pattern, board, "test #6:")

        board = copy.deepcopy(pattern)
        moves = ['R2', 'R2', 'U0', 'U0', 'U0', 'D1']

        algorithm(board, tuple(moves))
        self.assertEqual(solved_pattern, board, "test #7:")

        board = copy.deepcopy(pattern)
        moves = ['R2', 'R2', 'U0', 'U0', 'U0', 'U1', 'U1', 'U1']

        algorithm(board, tuple(moves))
        self.assertEqual(solved_pattern, board, "test #7:")

        pattern = [
            ['A', 'C', 'D', 'B', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
        ]
        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
        ]

        board = copy.deepcopy(pattern)
        print('before:')
        for i in range(len(board)):
            print(board[i])
        moves = solving_algorithm(board, solved_pattern)

        print('after:')
        for i in range(len(board)):
            print(board[i])
        print(moves)


if __name__ == '__main__':
    unittest.main()
