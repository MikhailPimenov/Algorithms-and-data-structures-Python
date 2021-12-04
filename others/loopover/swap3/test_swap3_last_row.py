import unittest
import copy

from others.loopover.point.point import Point
from swap3_last_row import swap3_last_row as algorithm
from others.loopover.simulator.simulator import simulator as simulator_algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'w', 'y', 'X', 'v'],
        ]
        search_board = {
            symbol: Point(row_index, column_index)
            for row_index, row in enumerate(pattern)
            for column_index, symbol in enumerate(row)
        }

        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'v', 'w', 'X', 'y'],
        ]
        solved_search_board = {
            symbol: Point(row_index, column_index)
            for row_index, row in enumerate(solved_pattern)
            for column_index, symbol in enumerate(row)
        }
        board_for_moves = copy.deepcopy(pattern)
        moves = []
        start = Point(4, 4)
        finish = Point(4, 1)
        algorithm(
            board=board_for_moves,
            start=start,
            finish=finish,
            moves=moves,
            search_board=search_board,
        )
        board_for_simulator = copy.deepcopy(pattern)

        simulator_algorithm(board_for_simulator, tuple(moves))
        self.assertEqual(solved_pattern, board_for_simulator, 'test #1')
        self.assertEqual(solved_search_board, search_board, 'test #1.1')

        pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'x', 'v', 'w', 'Y'],
        ]
        search_board = {
            symbol: Point(row_index, column_index)
            for row_index, row in enumerate(pattern)
            for column_index, symbol in enumerate(row)
        }

        solved_pattern = [
            ['A', 'B', 'C', 'D', 'E'],
            ['F', 'G', 'H', 'I', 'J'],
            ['K', 'L', 'M', 'N', 'O'],
            ['P', 'Q', 'R', 'S', 'T'],
            ['U', 'v', 'w', 'x', 'Y'],
        ]
        solved_search_board = {
            symbol: Point(row_index, column_index)
            for row_index, row in enumerate(solved_pattern)
            for column_index, symbol in enumerate(row)
        }
        board_for_moves = copy.deepcopy(pattern)
        moves = []
        start = Point(4, 2)
        finish = Point(4, 1)
        algorithm(
            board=board_for_moves,
            start=start,
            finish=finish,
            moves=moves,
            search_board=search_board,
        )
        board_for_simulator = copy.deepcopy(pattern)

        simulator_algorithm(board_for_simulator, tuple(moves))
        self.assertEqual(solved_pattern, board_for_simulator, 'test #2')
        self.assertEqual(solved_search_board, search_board, 'test #2.1')


if __name__ == '__main__':
    unittest.main()
