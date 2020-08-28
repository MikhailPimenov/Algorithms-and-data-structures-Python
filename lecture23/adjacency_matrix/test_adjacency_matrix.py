import unittest
from .adjacency_matrix import adjacency_matrix as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # 4 5
        # A B
        # B C
        # C D
        # D B
        # A D
        answer = ['A', 'B', 'C', 'D'], \
                 {'A': 1, 'B': 2, 'C': 3, 'D': 4}, \
                 [
                     [0, 0, 0, 0, 0],
                     [0, 0, 1, 0, 1],
                     [0, 1, 0, 1, 1],
                     [0, 0, 1, 0, 1],
                     [0, 1, 1, 1, 0],
                 ]

        result = algorithm()
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
