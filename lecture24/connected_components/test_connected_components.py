import unittest
from .connected_components import connected_components as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        adjacency_lists = {
            'A': set(),
            'B': set(),
            'C': set(),
            'D': set(), }
        answer = 4
        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #1")

        adjacency_lists = {
            'A': {'B'},
            'B': {'A'},
            'C': set(),
            'D': set(), }
        answer = 3
        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #2")

        adjacency_lists = {
            'A': {'B'},
            'B': {'A'},
            'C': {'D'},
            'D': {'C'}, }
        answer = 2
        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #3")

        adjacency_lists = {
            'A': {'B', 'C', 'D'},
            'B': {'A', 'C', 'D'},
            'C': {'D', 'A', 'B'},
            'D': {'C', 'A', 'B'}, }
        answer = 1
        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #4")


if __name__ == '__main__':
    unittest.main()
