import unittest
from .is_sorted_graph import is_sorted_graph as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        adjacency_lists = {
            'A': {'B', 'C'},
            'B': {'C', 'D'},
            'C': {'D'},
            'D': {},
        }
        numbers = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 3
        }
        self.assertEqual(True, algorithm(adjacency_lists, numbers), "test #1")

        numbers = {
            'A': 1,
            'B': 1,
            'C': 2,
            'D': 3
        }
        self.assertEqual(False, algorithm(adjacency_lists, numbers), "test #2")

        numbers = {
            'A': 1,
            'B': 0,
            'C': 2,
            'D': 3
        }
        self.assertEqual(False, algorithm(adjacency_lists, numbers), "test #3")

        adjacency_lists = {
            'A': {'B', 'C', 'D'},
            'B': {'C'},
            'C': {'F'},
            'D': {'E'},
            'E': {'G'},
            'F': {'G'},
            'G': set(),
        }
        numbers = {
            'A': 0,
            'B': 3,
            'C': 4,
            'D': 1,
            'E': 2,
            'F': 5,
            'G': 6
        }
        self.assertEqual(True, algorithm(adjacency_lists, numbers), "test #4")

        numbers = {
            'A': 0,
            'B': 1,
            'C': 3,
            'D': 2,
            'E': 4,
            'F': 5,
            'G': 6
        }
        self.assertEqual(True, algorithm(adjacency_lists, numbers), "test #5")

        numbers = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 4,
            'E': 5,
            'F': 3,
            'G': 6
        }
        self.assertEqual(True, algorithm(adjacency_lists, numbers), "test #6")

        numbers = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 1,
            'E': 2,
            'F': 4,
            'G': 6
        }
        self.assertEqual(False, algorithm(adjacency_lists, numbers), "test #7")

        numbers = {
            'A': 0,
            'B': 1,
            'C': 2,
            'D': 4,
            'E': 5,
            'F': 3,
            'G': 16
        }
        self.assertEqual(False, algorithm(adjacency_lists, numbers), "test #8")

        adjacency_lists = {
            'A': {'B', 'C'},
            'B': {'C', 'D'},
            'C': {'D'},
            'D': {},
        }
        numbers = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4,
        }
        self.assertEqual(True, algorithm(adjacency_lists, numbers), "test #9")

        numbers = {
            'A': 21,
            'B': 22,
            'C': 23,
            'D': 24,
        }
        self.assertEqual(False, algorithm(adjacency_lists, numbers), "test #10")


if __name__ == '__main__':
    unittest.main()
