import unittest
# from .reversed_polish_notation2 import reversed_polish_notation as algorithm
from .reversed_polish_notation3 import reversed_polish_notation3 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        notation = [5, 7, '+']
        self.assertEqual(12, algorithm(notation), "test #1")

        notation = [5, 7, '-']
        self.assertEqual(-2, algorithm(notation), "test #2")

        notation = [5, 7, '*']
        self.assertEqual(35, algorithm(notation), "test #3")

        notation = [5, 7, '+', 4, '*']
        self.assertEqual(48, algorithm(notation), "test #4")

        notation = [4, 5, '+', 3, '*', 5, 9, '+', 2, '/', '-', 9, 2, '*', '-']
        self.assertEqual(2, algorithm(notation), "test #5")


if __name__ == '__main__':
    unittest.main()
