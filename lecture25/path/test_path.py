import unittest
# from .path2 import path as algorithm
# from .path3 import path3 as algorithm
from .path4 import path4 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        adjacency_lists = {
            'A': {'F', 'N', 'B', 'G', 'D', 'J'},
            'B': {'A', 'H', 'P'},
            'C': {'H', 'M'},
            'D': {'A', 'J', 'G'},
            'E': {'J', 'K'},
            'F': {'A', 'F', 'I'},
            'G': {'A', 'D', 'L', 'M'},
            'H': {'B', 'C'},
            'I': {'U', 'F'},
            'J': {'E', 'F', 'D'},
            'K': {'E'},
            'L': {'G'},
            'M': {'G', 'C'},
            'N': {'A', 'O'},
            'O': {'N', 'T'},
            'P': {'B', 'V'},
            'Q': {'U', 'S'},
            'R': {'T', 'V'},
            'S': {'Q', 'T'},
            'T': {'S', 'R', 'O'},
            'U': {'I', 'Q'},
            'V': {'R', 'P'}
        }
        answer = ['G', 'D', 'J']
        result = algorithm(adjacency_lists, 'G', 'J')
        self.assertEqual(answer, result, "test #1")

        answer = ['A', 'N', 'O', 'T']
        result = algorithm(adjacency_lists, 'A', 'T')
        self.assertEqual(answer, result, "test #2")

        answer = ['G', 'A', 'B']
        result = algorithm(adjacency_lists, 'G', 'B')
        self.assertEqual(answer, result, "test #3")


if __name__ == '__main__':
    unittest.main()
