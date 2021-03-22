import unittest
# from .kosaraju2 import kosaraju as algorithm
from .kosaraju3 import kosaraju3 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        adjacency_lists = {
            'A': {'B'},
            'B': {'C'},
            'C': {'D'},
            'D': {'A'}, }
        answer = 1
        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #1")

        adjacency_lists = {
            'A': {'B'},
            'B': {'C'},
            'C': {'D', 'E'},
            'D': set(),
            'E': {'A', 'D'}, }
        answer = 2
        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #2")

        adjacency_lists = {
            'A': {'B'},
            'B': {'C', 'D'},
            'C': {'A'},
            'D': {'E'},
            'E': {'F'},
            'F': {'D'},
            'G': {'F', 'H'},
            'H': {'I'},
            'I': {'J'},
            'J': {'G'},
            'K': {'J'}, }
        answer = 4
        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #3")


if __name__ == '__main__':
    unittest.main()
