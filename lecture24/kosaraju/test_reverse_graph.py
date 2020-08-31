import unittest
from lecture24.kosaraju.reverse_graph import reverse_graph as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        adjacency_lists = {
            'A': {'B'},
            'B': {'C'},
            'C': {'D'},
            'D': {'A'}, }
        answer = {
            'A': {'D'},
            'B': {'A'},
            'C': {'B'},
            'D': {'C'}, }
        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #1")

        adjacency_lists = {
            'A': {'B'},
            'B': {'C'},
            'C': {'D', 'E'},
            'D': set(),
            'E': {'A', 'D'}, }
        answer = {
            'A': {'E'},
            'B': {'A'},
            'C': {'B'},
            'D': {'C', 'E'},
            'E': {'C'}, }
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
        answer = {
            'A': {'C'},
            'B': {'A'},
            'C': {'B'},
            'D': {'B', 'F'},
            'E': {'D'},
            'F': {'E', 'G'},
            'G': {'J'},
            'H': {'G'},
            'I': {'H'},
            'J': {'I', 'K'},
            'K': set(), }
        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #3")


if __name__ == '__main__':
    unittest.main()
