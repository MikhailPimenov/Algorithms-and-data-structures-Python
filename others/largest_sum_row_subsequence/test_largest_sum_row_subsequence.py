import unittest
from .largest_sum_row_subsequence import largest_sum_row_subsequence as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sequence = [-5, -5, -5, 10, 10, 10, -5, -5, 9, 9, 9, 9, -5, -5, ]
        answer = 56
        result = algorithm(sequence)
        self.assertEqual(answer, result, "test #1")

        sequence = [-5, -5, -5, 10, 10, 10, -500, -500, 9, 9, 9, 9, -5, -5, ]
        answer = 36
        result = algorithm(sequence)
        self.assertEqual(answer, result, "test #2")

        sequence = [-5, -5, -5, 10, 10, 10, -500, -500, 99, -5, -5, ]
        answer = 99
        result = algorithm(sequence)
        self.assertEqual(answer, result, "test #3")

        sequence = [-5, -5, -5, 10, 10, 10, -5, -5, 99, -5, -5, ]
        answer = 119
        result = algorithm(sequence)
        self.assertEqual(answer, result, "test #4")

        sequence = [1, 10, 1, ]
        answer = 12
        result = algorithm(sequence)
        self.assertEqual(answer, result, "test #5")

        sequence = [1, 10, -1, ]
        answer = 11
        result = algorithm(sequence)
        self.assertEqual(answer, result, "test #6")

        sequence = [1, -10, 1, ]
        answer = 1
        result = algorithm(sequence)
        self.assertEqual(answer, result, "test #7")

        sequence = [1, -10, 2, ]
        answer = 2
        result = algorithm(sequence)
        self.assertEqual(answer, result, "test #8")

        sequence = [-5, -5, -5, 10, -5, 10, -5, 10, -5, 10, ]
        answer = 25
        result = algorithm(sequence)
        self.assertEqual(answer, result, "test #9")

        sequence = [-5, -5, -5, 10, -5, 10, -5, 10, -50, 10, ]
        answer = 20
        result = algorithm(sequence)
        self.assertEqual(answer, result, "test #10")

        sequence = [-5, -5, -5, 10, -50, 10, -5, 10, -50, 10, ]
        answer = 15
        result = algorithm(sequence)
        self.assertEqual(answer, result, "test #11")


if __name__ == '__main__':
    unittest.main()
