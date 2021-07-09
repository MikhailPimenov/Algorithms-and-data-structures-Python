import unittest
from .shift_array5 import shift_array5 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(algorithm([0, 1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 0, 1, 2, 3, 4])
        self.assertEqual(algorithm([0, 1, 2, 3, 4, 5, 6, 7], 18), [6, 7, 0, 1, 2, 3, 4, 5])
        self.assertEqual(algorithm([0, 1, 2, 3, 4, 5, 6, 7], -3), [3, 4, 5, 6, 7, 0, 1, 2])
        self.assertEqual(algorithm([0, 1, 2, 3, 4, 5, 6, 7], -18), [2, 3, 4, 5, 6, 7, 0, 1])


if __name__ == '__main__':
    unittest.main()
