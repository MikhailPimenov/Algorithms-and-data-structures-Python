import unittest
from .longest_common_subsequence2 import longest_common_subsequence as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sequence1 = [0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 4, 0, 0, 0, 5]
        sequence2 = [9, 9, 9, 1, 9, 9, 9, 2, 9, 9, 9, 3, 9, 9, 9, 4, 9, 9, 9, 5]
        subsequence = [1, 2, 3, 4, 5]

        result = algorithm(sequence1, sequence2)
        self.assertEqual(len(result), len(subsequence), "test #1")
        self.assertEqual(result, subsequence, "test #1.1")

        sequence1 = [0, 1, 0, 0, 2, 0, 3, 0, 4, 0, 5]
        sequence2 = [9, 1, 9, 2, 3, 4, 5, 9, 9]
        subsequence = [1, 2, 3, 4, 5]

        result = algorithm(sequence1, sequence2)
        self.assertEqual(len(result), len(subsequence), "test #2")
        self.assertEqual(result, subsequence, "test #2.1")

        sequence1 = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 0, 1, 0, 0, 2, 0, 3, 0, 4, 0, 5]
        sequence2 = [9, 1, 9, 2, 3, 4, 5, 9, 9, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31]
        subsequence = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31]

        result = algorithm(sequence1, sequence2)
        self.assertEqual(len(result), len(subsequence), "test #3")
        self.assertEqual(result, subsequence, "test #3.1")

        sequence1 = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                     30, 29, 28, 27, 26, 25, 24, 23, 22, 21]
        sequence2 = [9, 1, 9, 2, 3, 4, 5, 9, 9,
                     40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                     30, 29, 28, 27, 26, 25, 24, 23, 22, 21]
        subsequence = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                       30, 29, 28, 27, 26, 25, 24, 23, 22, 21]

        result = algorithm(sequence1, sequence2)
        self.assertEqual(len(result), len(subsequence), "test #4")
        self.assertEqual(result, subsequence, "test #4.1")

        sequence1 = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                     30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
                     0, 1, 0, 0, 2, 0, 3, 0, 4, 0, 5,
                     20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
        sequence2 = [9, 1, 9, 2, 3, 4, 5, 9, 9,
                     40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                     30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
                     20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
        subsequence = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                       30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
                       20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

        result = algorithm(sequence1, sequence2)
        self.assertEqual(len(result), len(subsequence), "test #5")
        self.assertEqual(result, subsequence, "test #5.1")

        sequence1 = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
                     0, 1, 0, 0, 2, 0, 3, 0, 4, 0, 5,
                     20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sequence2 = [9, 1, 9, 2, 3, 4, 5, 9, 9,
                     40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                     30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
                     20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
        subsequence = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                       30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
                       20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

        result = algorithm(sequence1, sequence2)
        self.assertEqual(len(result), len(subsequence), "test #6")
        self.assertEqual(result, subsequence, "test #6.1")

        sequence1 = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
                     0, 1, 0, 0, 2, 0, 3, 0, 4, 0, 5,
                     20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sequence2 = [9, 1, 9, 2, 3, 4, 5, 9, 9,
                     40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                     9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                     30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
                     9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                     20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
        subsequence = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                       30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
                       20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

        result = algorithm(sequence1, sequence2)
        self.assertEqual(len(result), len(subsequence), "test #7")
        self.assertEqual(result, subsequence, "test #7.1")

        sequence1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sequence2 = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        subsequence = []

        result = algorithm(sequence1, sequence2)
        self.assertEqual(len(result), len(subsequence), "test #8")
        self.assertEqual(result, subsequence, "test #8.1")

        sequence1 = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
                     0, 1, 0, 0, 2, 0, 3, 0, 4, 0, 5,
                     20, 19, 18, 17, 16, 15, 14, 13, 12, 11,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        sequence2 = [9, 1, 9, 2, 3, 4, 5, 9, 9,
                     40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                     9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                     30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
                     9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                     20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
        subsequence = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
                       30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
                       20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

        result = algorithm(sequence1, sequence2)
        self.assertEqual(len(result), len(subsequence), "test #9")
        self.assertEqual(result, subsequence, "test #9.1")


if __name__ == '__main__':
    unittest.main()
