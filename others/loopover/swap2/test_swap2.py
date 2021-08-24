import unittest

import copy

from .swap2 import swap2 as algorithm
from ..point.point import Point


def print_board(board: list):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(f'{board[i][j]:<5}', end='')
        print()


class MyTestCase(unittest.TestCase):
    def test_something(self):
        search_board = {}
        moves = []
        max_row = 4
        max_column = 10
        pattern = [[i * max_column + j + 1 for j in range(0, max_column)]
                   for i in range(0, max_row)]
        print_board(pattern)

        board = copy.deepcopy(pattern)
        result_board = copy.deepcopy(pattern)
        result_board[3][8] = 40
        result_board[3][9] = 39
        result_moves = ['D9', 'R3', 'D9', 'L3', 'D9', 'R3', 'D9', 'L3', 'D9']

        algorithm(board, Point(3, 9), Point(3, 8), 'L', 'R', 4, moves, search_board)
        self.assertEqual(result_board, board, 'test #1')
        self.assertEqual(result_moves, moves, 'test #1.1')
        moves.clear()

        board = copy.deepcopy(pattern)
        result_board = copy.deepcopy(pattern)
        result_board[3][9] = 30
        result_board[2][9] = 40
        result_moves = [
            'R3', 'D9', 'R3', 'U9',
            'R3', 'D9', 'R3', 'U9',
            'R3', 'D9', 'R3', 'U9',
            'R3', 'D9', 'R3', 'U9',
            'R3', 'D9', 'R3', 'U9',
            'R3',
        ]

        algorithm(board, Point(3, 9), Point(2, 9), 'U', 'D', 10, moves, search_board)
        self.assertEqual(result_board, board, 'test #2')
        self.assertEqual(result_moves, moves, 'test #2.1')
        moves.clear()


if __name__ == '__main__':
    unittest.main()
