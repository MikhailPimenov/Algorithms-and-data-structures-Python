import unittest
# from .distances2 import distances as algorithm
# from .distances3 import distances3 as algorithm
# from .distances4 import distances4 as algorithm
from .distances5 import distances5 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        adjacency_lists = {
            'A': {'B', 'C', 'D', 'E', 'F'},
            'B': {'A', 'G', 'H'},
            'C': {'A', 'I', 'J'},
            'D': {'A', 'K'},
            'E': {'A', 'L', 'M'},
            'F': {'F', 'O', 'N'},
            'G': {'B', 'P', 'Q'},
            'H': {'B', 'R', 'S'},
            'I': {'C', 'T', 'V'},
            'J': {'C', 'U', 'W'},
            'K': {'D', 'X', 'Y'},
            'L': {'E', 'Z'},
            'M': {'E'},
            'N': {'F'},
            'O': {'F'},
            'P': {'G'},
            'Q': {'G'},
            'R': {'H'},
            'S': {'H'},
            'T': {'I'},
            'V': {'I'},
            'U': {'J'},
            'W': {'J'},
            'X': {'K'},
            'Y': {'K'},
            'Z': {'L'}, }
        answer = {
            'A': 0,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1,
            'F': 1,
            'G': 2,
            'H': 2,
            'I': 2,
            'J': 2,
            'K': 2,
            'L': 2,
            'M': 2,
            'N': 2,
            'O': 2,
            'P': 3,
            'Q': 3,
            'R': 3,
            'S': 3,
            'T': 3,
            'V': 3,
            'U': 3,
            'W': 3,
            'X': 3,
            'Y': 3,
            'Z': 3, }
        result = algorithm(adjacency_lists, 'A')
        self.assertEqual(answer, result, "test #1")

        answer = {
            'A': 3,
            'B': 2,
            'C': 4,
            'D': 4,
            'E': 4,
            'F': 4,
            'G': 3,
            'H': 1,
            'I': 5,
            'J': 5,
            'K': 5,
            'L': 5,
            'M': 5,
            'N': 5,
            'O': 5,
            'P': 4,
            'Q': 4,
            'R': 0,
            'S': 2,
            'T': 6,
            'V': 6,
            'U': 6,
            'W': 6,
            'X': 6,
            'Y': 6,
            'Z': 6, }
        result = algorithm(adjacency_lists, 'R')
        self.assertEqual(answer, result, "test #2")

        answer = {
            'A': 1,
            'B': 2,
            'C': 2,
            'D': 2,
            'E': 0,
            'F': 2,
            'G': 3,
            'H': 3,
            'I': 3,
            'J': 3,
            'K': 3,
            'L': 1,
            'M': 1,
            'N': 3,
            'O': 3,
            'P': 4,
            'Q': 4,
            'R': 4,
            'S': 4,
            'T': 4,
            'V': 4,
            'U': 4,
            'W': 4,
            'X': 4,
            'Y': 4,
            'Z': 2,
        }
        result = algorithm(adjacency_lists, 'E')
        self.assertEqual(answer, result, "test #3")

        answer = {
            'A': 2,
            'B': 3,
            'C': 1,
            'D': 3,
            'E': 3,
            'F': 3,
            'G': 4,
            'H': 4,
            'I': 2,
            'J': 0,
            'K': 4,
            'L': 4,
            'M': 4,
            'N': 4,
            'O': 4,
            'P': 5,
            'Q': 5,
            'R': 5,
            'S': 5,
            'T': 3,
            'V': 3,
            'U': 1,
            'W': 1,
            'X': 5,
            'Y': 5,
            'Z': 5,
        }
        result = algorithm(adjacency_lists, 'J')
        self.assertEqual(answer, result, "test #4")

        if __name__ == '__main__':
            unittest.main()
