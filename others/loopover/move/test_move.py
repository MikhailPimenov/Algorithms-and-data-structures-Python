import unittest
from .move import base_move as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        moves = []

        algorithm(
            to_beginning='L',
            to_end='R',
            moves=moves,
            start=3,
            finish=3,
            length=6,
            current_other=0
        )
        result = []
        self.assertEqual(moves, result, "test #1")
        result.clear()
        moves.clear()

        algorithm(
            to_beginning='L',
            to_end='R',
            moves=moves,
            start=3,
            finish=5,
            length=6,
            current_other=0
        )
        result = ['R0', 'R0']
        self.assertEqual(moves, result, "test #2")
        result.clear()
        moves.clear()

        algorithm(
            to_beginning='L',
            to_end='R',
            moves=moves,
            start=5,
            finish=3,
            length=6,
            current_other=0
        )
        result = ['L0', 'L0']
        self.assertEqual(moves, result, "test #3")
        result.clear()
        moves.clear()

        algorithm(
            to_beginning='L',
            to_end='R',
            moves=moves,
            start=5,
            finish=3,
            length=6,
            current_other=13
        )
        result = ['L13', 'L13']
        self.assertEqual(moves, result, "test #4")
        result.clear()
        moves.clear()

        algorithm(
            to_beginning='L',
            to_end='R',
            moves=moves,
            start=2,
            finish=14,
            length=15,
            current_other=0
        )
        result = ['L0', 'L0', 'L0']
        self.assertEqual(moves, result, "test #5")
        result.clear()
        moves.clear()

        algorithm(
            to_beginning='L',
            to_end='R',
            moves=moves,
            start=2,
            finish=14,
            length=150,
            current_other=0
        )
        result = ['R0', 'R0', 'R0', 'R0', 'R0', 'R0', 'R0', 'R0', 'R0', 'R0', 'R0', 'R0', ]
        self.assertEqual(moves, result, "test #6")
        result.clear()
        moves.clear()

        algorithm(
            to_beginning='L',
            to_end='R',
            moves=moves,
            start=14,
            finish=1,
            length=150,
            current_other=0
        )
        result = ['L0', 'L0', 'L0', 'L0', 'L0', 'L0', 'L0', 'L0', 'L0', 'L0', 'L0', 'L0', 'L0']
        self.assertEqual(moves, result, "test #7")
        result.clear()
        moves.clear()

        algorithm(
            to_beginning='L',
            to_end='R',
            moves=moves,
            start=14,
            finish=1,
            length=15,
            current_other=0
        )
        result = ['R0', 'R0']

        self.assertEqual(moves, result, "test #8")
        result.clear()
        moves.clear()

        algorithm(
            to_beginning='L',
            to_end='R',
            moves=moves,
            start=11,
            finish=11,
            length=15,
            current_other=0
        )
        result = []

        self.assertEqual(moves, result, "test #9")
        result.clear()
        moves.clear()

        algorithm(
            to_beginning='U',
            to_end='D',
            moves=moves,
            start=11,
            finish=11,
            length=15,
            current_other=0
        )
        result = []

        self.assertEqual(moves, result, "test #10")
        result.clear()
        moves.clear()

        algorithm(
            to_beginning='U',
            to_end='D',
            moves=moves,
            start=14,
            finish=1,
            length=15,
            current_other=0
        )
        result = ['D0', 'D0']

        self.assertEqual(moves, result, "test #11")
        result.clear()
        moves.clear()

        algorithm(
            to_beginning='U',
            to_end='D',
            moves=moves,
            start=2,
            finish=14,
            length=150,
            current_other=0
        )
        result = ['D0', 'D0', 'D0', 'D0', 'D0', 'D0', 'D0', 'D0', 'D0', 'D0', 'D0', 'D0', ]
        self.assertEqual(moves, result, "test #12")
        result.clear()
        moves.clear()

        algorithm(
            to_beginning='U',
            to_end='D',
            moves=moves,
            start=14,
            finish=1,
            length=150,
            current_other=0
        )
        result = ['U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0', 'U0']
        self.assertEqual(moves, result, "test #13")
        result.clear()
        moves.clear()


if __name__ == '__main__':
    unittest.main()
