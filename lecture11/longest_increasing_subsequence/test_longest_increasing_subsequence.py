import unittest
# from .longest_increasing_subsequence2 import longest_increasing_subsequence as algorithm
# from .longest_increasing_subsequence3 import longest_increasing_subsequence3 as algorithm
# from .longest_increasing_subsequence4 import longest_increasing_subsequence4 as algorithm
from .longest_increasing_subsequence5 import longest_increasing_subsequence5 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sequence = [1, 2, 3, 4, 5]
        subsequence = [1, 2, 3, 4, 5]
        result = algorithm(sequence)
        self.assertEqual(len(result), len(subsequence), "test #1")
        self.assertEqual(result, subsequence, "test #1.1")

        sequence = [1, 9, 2, 8, 3, 7, 4, 6, 5, 6]
        subsequence = [1, 2, 3, 4, 5, 6]
        result = algorithm(sequence)
        self.assertEqual(len(result), len(subsequence), "test #2")
        self.assertEqual(result, subsequence, "test #2.1")

        sequence = [1, 9, 2, 9, 3, 9, 4, 9]
        subsequence = [1, 2, 3, 4, 9]
        result = algorithm(sequence)
        self.assertEqual(len(result), len(subsequence), "test #3")
        self.assertEqual(result, subsequence, "test #3.1")

        sequence = [4, 3, 1, 2]
        subsequence = [1, 2]
        result = algorithm(sequence)
        self.assertEqual(len(result), len(subsequence), "test #4")
        self.assertEqual(result, subsequence, "test #4.1")

        sequence = [4, 1, 2, 0]
        subsequence = [1, 2]
        result = algorithm(sequence)
        self.assertEqual(len(result), len(subsequence), "test #5")
        self.assertEqual(result, subsequence, "test #5.1")

        sequence = [9, 8, 7, 1, 6, 2, 3]
        subsequence = [1, 2, 3]
        result = algorithm(sequence)
        self.assertEqual(len(result), len(subsequence), "test #6")
        self.assertEqual(result, subsequence, "test #6.1")

        sequence = [0, 0, 1, 0, 0, 2, 0, 0, 3, 0, 0, 4, 0, 0, 5]
        subsequence = [0, 1, 2, 3, 4, 5]
        result = algorithm(sequence)
        self.assertEqual(len(result), len(subsequence), "test #7")
        self.assertEqual(result, subsequence, "test #7.1")

        sequence = [0, 0, 1, 0, 0, 2, 0, 0, 3, 2, 2, 4, 0, 0, 5]
        subsequence = [0, 1, 2, 3, 4, 5]
        result = algorithm(sequence)
        self.assertEqual(len(result), len(subsequence), "test #8")
        self.assertEqual(result, subsequence, "test #8.1")

        sequence = [0, 0, 1, 0, 0, 2, 0, 0, 3, 2, 2, 4, 0, 0, 5]
        subsequence = [0, 1, 2, 3, 4, 5]
        result = algorithm(sequence)
        self.assertEqual(len(result), len(subsequence), "test #9")
        self.assertEqual(result, subsequence, "test #9.1")

        sequence = [4, 1, 2, 3, 0, 1]
        subsequence = [1, 2, 3]
        result = algorithm(sequence)
        self.assertEqual(len(result), len(subsequence), "test #10")
        self.assertEqual(result, subsequence, "test #10.1")

        sequence = [4, 5, 1, 2, 0, 3, 3, 3, 0, 0, 1]
        subsequence = [1, 2, 3]
        result = algorithm(sequence)
        self.assertEqual(len(result), len(subsequence), "test #11")
        self.assertEqual(result, subsequence, "test #11.1")

        sequence = [0, 0, 1, 0, 9, 2, 9, 9, 3, 2, 2, 4, 0, 0, 5]
        subsequence = [0, 1, 2, 3, 4, 5]
        result = algorithm(sequence)
        self.assertEqual(len(result), len(subsequence), "test #12")
        self.assertEqual(result, subsequence, "test #12.1")


if __name__ == '__main__':
    unittest.main()
