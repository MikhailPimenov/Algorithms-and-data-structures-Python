import unittest
import copy
from .swap3 import swap3 as algorithm
from .swap3 import Point


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
        result_board[0][0] = 40
        result_board[3][9] = 31
        result_board[3][0] = 1
        result_moves = ['U0', 'R3', 'D0', 'L3']

        algorithm(board, Point(3, 9), Point(0, 0), moves, search_board)
        self.assertEqual(board, result_board, 'test #1')
        self.assertEqual(moves, result_moves, 'test #1.1')
        moves.clear()

        board = copy.deepcopy(pattern)
        result_board = copy.deepcopy(pattern)
        result_board[0][9] = 31
        result_board[3][9] = 10
        result_board[3][0] = 40
        result_moves = ['U9', 'L3', 'D9', 'R3']

        algorithm(board, Point(3, 0), Point(0, 9), moves, search_board)
        self.assertEqual(board, result_board, 'test #2')
        self.assertEqual(moves, result_moves, 'test #2.1')
        moves.clear()

        board = copy.deepcopy(pattern)
        result_board = copy.deepcopy(pattern)
        result_board[0][0] = 12
        result_board[1][0] = 1
        result_board[1][1] = 11
        result_moves = ['D0', 'L1', 'U0', 'R1']

        algorithm(board, Point(1, 1), Point(0, 0), moves, search_board)
        self.assertEqual(board, result_board, 'test #3')
        self.assertEqual(moves, result_moves, 'test #3.1')
        moves.clear()

        board = copy.deepcopy(pattern)
        result_board = copy.deepcopy(pattern)
        result_board[0][1] = 11
        result_board[1][1] = 2
        result_board[1][0] = 12
        result_moves = ['D1', 'R1', 'U1', 'L1']

        algorithm(board, Point(1, 0), Point(0, 1), moves, search_board)
        self.assertEqual(board, result_board, 'test #4')
        self.assertEqual(moves, result_moves, 'test #4.1')
        moves.clear()

        board = copy.deepcopy(pattern)
        result_board = copy.deepcopy(pattern)
        result_board[0][2] = 34
        result_board[3][3] = 33
        result_board[3][2] = 3
        result_moves = ['U2', 'L3', 'D2', 'R3']

        algorithm(board, Point(3, 3), Point(0, 2), moves, search_board)
        self.assertEqual(board, result_board, 'test #5')
        self.assertEqual(moves, result_moves, 'test #5.1')
        moves.clear()

        board = copy.deepcopy(pattern)
        result_board = copy.deepcopy(pattern)
        result_board[0][4] = 14
        result_board[1][3] = 15
        result_board[1][4] = 5
        result_moves = ['D4', 'R1', 'U4', 'L1']

        algorithm(board, Point(1, 3), Point(0, 4), moves, search_board)
        self.assertEqual(board, result_board, 'test #6')
        self.assertEqual(moves, result_moves, 'test #6.1')
        moves.clear()

    def test_linear_not_near(self):
        search_board = {}
        moves = []
        max_row = 4
        max_column = 10
        pattern = [[i * max_column + j + 1 for j in range(0, max_column)]
                   for i in range(0, max_row)]
        print_board(pattern)

        board = copy.deepcopy(pattern)
        result_board = copy.deepcopy(pattern)
        result_board[3][2] = 37
        result_board[3][3] = 33
        result_board[3][6] = 34
        result_moves = ['U2', 'R2', 'D3', 'L3', 'L3', 'L3', 'U3', 'R3', 'R3', 'R3', 'L2', 'D2']

        algorithm(board, Point(3, 6), Point(3, 2), moves, search_board)

        self.assertEqual(result_board, board, 'test #1')
        self.assertEqual(result_moves, moves, 'test #1.1')
        moves.clear()

        board = copy.deepcopy(pattern)
        result_board = copy.deepcopy(pattern)
        result_board[3][0] = 40
        result_board[3][1] = 31
        result_board[3][9] = 32
        result_moves = ['U0', 'R2', 'D1', 'R3', 'R3', 'U1', 'L3', 'L3', 'L2', 'D0']

        algorithm(board, Point(3, 9), Point(3, 0), moves, search_board)

        self.assertEqual(result_board, board, 'test #2')
        self.assertEqual(result_moves, moves, 'test #2.1')
        moves.clear()

        board = copy.deepcopy(pattern)
        result_board = copy.deepcopy(pattern)
        result_board[2][5] = 28
        result_board[2][6] = 26
        result_board[2][7] = 27
        result_moves = ['U5', 'R1', 'D6', 'L2', 'U6', 'R2', 'L1', 'D5']

        algorithm(board, Point(2, 7), Point(2, 5), moves, search_board)

        self.assertEqual(result_board, board, 'test #3')
        self.assertEqual(result_moves, moves, 'test #3.1')
        moves.clear()

    def test_linear_near(self):
        search_board = {}
        moves = []
        max_row = 4
        max_column = 10
        pattern = [[i * max_column + j + 1 for j in range(0, max_column)]
                   for i in range(0, max_row)]
        print_board(pattern)

        board = copy.deepcopy(pattern)
        result_board = copy.deepcopy(pattern)
        result_board[1][4] = 16
        result_board[1][5] = 17
        result_board[1][6] = 15
        result_moves = ['U4', 'R0', 'R0', 'D6', 'R1', 'U6', 'L1', 'L0', 'L0', 'D4']

        algorithm(board, Point(1, 5), Point(1, 4), moves, search_board)

        self.assertEqual(result_board, board, 'test #1')
        self.assertEqual(result_moves, moves, 'test #1.1')
        moves.clear()

        board = copy.deepcopy(pattern)
        result_board = copy.deepcopy(pattern)
        result_board[1][8] = 20
        result_board[1][9] = 29
        result_board[2][8] = 19
        result_moves = ['U8', 'D8', 'L1', 'U8', 'R1', 'D8']

        algorithm(board, Point(1, 9), Point(1, 8), moves, search_board)

        self.assertEqual(result_board, board, 'test #2')
        self.assertEqual(result_moves, moves, 'test #2.1')
        moves.clear()


if __name__ == '__main__':
    unittest.main()
