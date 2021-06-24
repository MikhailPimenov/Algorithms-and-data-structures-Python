import unittest
# from .chess_queen2 import chess_queen as algorithm
# from .chess_queen3 import chess_queen3 as algorithm
from .chess_queen4 import chess_queen4 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(algorithm(2, 2), 2)
        m = 8
        n = 8

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                print(algorithm(i, j), end="\t\t")
            print()


if __name__ == '__main__':
    unittest.main()
