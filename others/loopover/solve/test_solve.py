import copy
import unittest
from .solve import solve


def print_board(board: list):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(f'{board[i][j]:<5}', end='')
        print()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        max_row = 3
        max_column = 5
        solved_pattern = [[i * max_column + j + 1 for j in range(0, max_column)]
                          for i in range(0, max_row)]

        print_board(solved_pattern)
        solved_board = copy.deepcopy(solved_pattern)
        pattern = [[i * max_column + j + 1 for j in range(max_column - 1, -1, -1)]
                   for i in range(max_row - 1, -1, -1)]
        print_board(pattern)

        board = copy.deepcopy(pattern)

        print('solve:')
        solve(board, solved_board)
        print_board(board)

        self.assertEqual(solved_pattern, board, 'test #1')


if __name__ == '__main__':
    unittest.main()
