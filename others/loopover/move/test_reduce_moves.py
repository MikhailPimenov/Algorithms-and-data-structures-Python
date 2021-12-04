import unittest
from .reduce_moves import reduce_moves as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        moves = []
        reduced_moves = []
        moves = algorithm(moves)
        self.assertEqual(reduced_moves, moves, 'test #1')

        moves = ['D0', 'D1', 'D2', 'D3', 'U3', 'U2', 'U1', 'U0']
        reduced_moves = []
        moves = algorithm(moves)
        self.assertEqual(reduced_moves, moves, 'test #2')

        moves = ['D0', 'D1', 'U1', 'R0', 'L1', 'R0', 'L0', 'R1']
        reduced_moves = ['D0', 'R0']
        moves = algorithm(moves)
        self.assertEqual(reduced_moves, moves, 'test #3')

        moves = ['D0', 'L1', 'R3', 'L0', 'R1']
        reduced_moves = ['D0', 'L1', 'R3', 'L0', 'R1']
        moves = algorithm(moves)
        self.assertEqual(reduced_moves, moves, 'test #4')

        moves = ['D0', 'L1', 'R3', 'R3', 'L3', 'R1']
        reduced_moves = ['D0', 'L1', 'R3', 'R1']
        moves = algorithm(moves)
        self.assertEqual(reduced_moves, moves, 'test #5')

        moves = ['D0', 'L1', 'R3', 'R3', 'L3', 'L3', 'R1', 'U0', 'R12']
        reduced_moves = ['R12']
        moves = algorithm(moves)
        self.assertEqual(reduced_moves, moves, 'test #6')

        moves = [
            'L0',
            'R11', 'R12', 'R123', 'R123', 'R123', 'U1234', 'U1234',
            'D1234', 'D1234', 'L123', 'L123', 'L123', 'L12', 'L11',
        ]
        reduced_moves = ['L0']
        moves = algorithm(moves)
        self.assertEqual(reduced_moves, moves, 'test #7')


if __name__ == '__main__':
    unittest.main()
