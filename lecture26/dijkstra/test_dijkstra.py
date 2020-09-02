import unittest
from .dijkstra import dijkstra as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        adjacency_lists = {
            'A': {'B': 2, 'H': 15},
            'B': {'A': 2, 'C': 1, 'D': 5},
            'C': {'B': 1, 'D': 3, 'F': 2, 'G': 1},
            'D': {'B': 5, 'C': 3, 'F': 4, 'E': 6},
            'E': {'D': 6, 'F': 7, 'I': 2},
            'F': {'C': 2, 'D': 4, 'E': 7, 'G': 1, 'H': 3},
            'G': {'C': 1, 'F': 1},
            'H': {'A': 15, 'F': 3, 'I': 12},
            'I': {'E': 2, 'H': 12},
        }
        start = 'A'
        answer = {'A': 0,
                  'B': 2,
                  'C': 3,
                  'D': 6,
                  'E': 12,
                  'F': 5,
                  'G': 4,
                  'H': 8,
                  'I': 14}
        result = algorithm(adjacency_lists, start)
        self.assertEqual(answer, result, "test #1")

        adjacency_lists = {
            'A': {'B': 2, 'H': 15},
            'B': {'A': 2, 'C': 1, 'D': 5},
            'C': {'B': 1, 'D': 3, 'F': 2, 'G': 1},
            'D': {'B': 5, 'C': 3, 'F': 4, 'E': 6},
            'E': {'D': 6, 'F': 7, 'I': 2},
            'F': {'C': 2, 'D': 4, 'E': 7, 'G': 1, 'H': 3},
            'G': {'C': 1, 'F': 1},
            'H': {'A': 15, 'F': 3, 'I': 12},
            'I': {'E': 2, 'H': 12},
            'J': {'K': 2},
            'K': {'J': 2},
        }
        start = 'A'
        answer = {'A': 0,
                  'B': 2,
                  'C': 3,
                  'D': 6,
                  'E': 12,
                  'F': 5,
                  'G': 4,
                  'H': 8,
                  'I': 14,
                  'J':None,
                  'K':None}
        result = algorithm(adjacency_lists, start)
        self.assertEqual(answer, result, "test #2")

        adjacency_lists = {
            'A': {'B': 2, 'H': 15},
            'B': {'A': 2, 'C': 1, 'D': 5},
            'C': {'B': 1, 'D': 3, 'F': 2, 'G': 1},
            'D': {'B': 5, 'C': 3, 'F': 4, 'E': 6},
            'E': {'D': 6, 'F': 7, 'I': 2},
            'F': {'C': 2, 'D': 4, 'E': 7, 'G': 1, 'H': 3},
            'G': {'C': 1, 'F': 1},
            'H': {'A': 15, 'F': 3, 'I': 12},
            'I': {'E': 2, 'H': 12},
        }
        start = 'E'
        answer = {'A': 12,
                  'B': 10,
                  'C': 9,
                  'D': 6,
                  'E': 0,
                  'F': 7,
                  'G': 8,
                  'H': 10,
                  'I': 2}
        result = algorithm(adjacency_lists, start)
        self.assertEqual(answer, result, "test #3")

        adjacency_lists = {
            'A': {'B': 2, 'H': 15},
            'B': {'A': 2, 'C': 1, 'D': 5},
            'C': {'B': 1, 'D': 3, 'F': 2, 'G': 1},
            'D': {'B': 5, 'C': 3, 'F': 4, 'E': 6},
            'E': {'D': 6, 'F': 7, 'I': 2},
            'F': {'C': 2, 'D': 4, 'E': 7, 'G': 1, 'H': 3},
            'G': {'C': 1, 'F': 1},
            'H': {'A': 15, 'F': 3, 'I': 12},
            'I': {'E': 2, 'H': 12},
        }
        start = 'C'
        answer = {'A': 3,
                  'B': 1,
                  'C': 0,
                  'D': 3,
                  'E': 9,
                  'F': 2,
                  'G': 1,
                  'H': 5,
                  'I': 11}
        result = algorithm(adjacency_lists, start)
        self.assertEqual(answer, result, "test #4")


if __name__ == '__main__':
    unittest.main()
