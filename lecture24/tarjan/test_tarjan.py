import unittest
# from .tarjan2 import tarjan as algorithm
from .is_sorted_graph import is_sorted_graph
# from .tarjan3 import tarjan3 as algorithm
from .tarjan4 import tarjan4 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        adjacency_lists = {
            'A': {'B', 'C'},
            'B': {'C', 'D'},
            'C': {'D'},
            'D': {}, }
        result = algorithm(adjacency_lists)
        self.assertEqual(True, is_sorted_graph(adjacency_lists, result), "test #1")

        adjacency_lists = {
            'A': {'B', 'C', 'D'},
            'B': {'C'},
            'C': {'F'},
            'D': {'E'},
            'E': {'G'},
            'F': {'G'},
            'G': set(),
        }
        result = algorithm(adjacency_lists)
        self.assertEqual(True, is_sorted_graph(adjacency_lists, result), "test #2")

        adjacency_lists = {
            'A': {'B', 'F'},
            'B': {'C', 'E'},
            'C': {'J', 'D'},
            'D': {'I', 'L', 'M'},
            'E': {'J', 'G'},
            'F': {'H'},
            'G': {'I'},
            'H': {'O', 'G'},
            'I': {'P', 'R', 'S', 'N'},
            'J': {'K'},
            'K': {'G', 'I'},
            'L': {'N'},
            'M': {'T'},
            'N': {'T'},
            'O': {'Q', 'P'},
            'P': {'R'},
            'Q': {'V'},
            'R': {'S'},
            'S': {'T'},
            'T': set(),
            'V': {'R'},
        }
        result = algorithm(adjacency_lists)
        self.assertEqual(True, is_sorted_graph(adjacency_lists, result), "test #3")

        adjacency_lists = {
            'A': {'B', 'C'},
            'B': {'C', 'D'},
            'C': {'D'},
            'D': {'A'}, }
        result = algorithm(adjacency_lists)
        self.assertEqual(False, is_sorted_graph(adjacency_lists, result), "test #4")

        adjacency_lists = {
            'A': {'B', 'F'},
            'B': {'C', 'E'},
            'C': {'J', 'D'},
            'D': {'I', 'L', 'M'},
            'E': {'J', 'G'},
            'F': {'H'},
            'G': {'I'},
            'H': {'O', 'G'},
            'I': {'P', 'R', 'S', 'N'},
            'J': {'K'},
            'K': {'G', 'I'},
            'L': {'N'},
            'M': {'T'},
            'N': {'T'},
            'O': {'Q', 'P'},
            'P': {'R'},
            'Q': {'V'},
            'R': {'S'},
            'S': {'T'},
            'T': {'A'},
            'V': {'R'},
        }
        result = algorithm(adjacency_lists)
        self.assertEqual(False, is_sorted_graph(adjacency_lists, result), "test #5")

        adjacency_lists = {
            'A': {'B', 'D', 'C'},
            'B': {'D'},
            'C': {'D'},
            'D': set(), }
        result = algorithm(adjacency_lists)
        self.assertEqual(True, is_sorted_graph(adjacency_lists, result), "test #6")

        adjacency_lists = {
            'A': {'B'},
            'B': {'C', 'D'},
            'C': set(),
            'D': {'E', 'C'},
            'E': {'C'}, }
        result = algorithm(adjacency_lists)
        self.assertEqual(True, is_sorted_graph(adjacency_lists, result), "test #7")

        adjacency_lists = {
            'A': {'B'},
            'B': {'C', 'D'},
            'C': set(),
            'D': {'E', 'C'},
            'E': {'C', 'A'}, }
        result = algorithm(adjacency_lists)
        self.assertEqual(False, is_sorted_graph(adjacency_lists, result), "test #8")

        adjacency_lists = {
            'A': {'B', 'E', 'F', 'D'},
            'B': {'C'},
            'C': set(),
            'D': {'F', 'C'},
            'E': {'B', 'C', 'F'},
            'F': {'C'}, }
        result = algorithm(adjacency_lists)
        self.assertEqual(True, is_sorted_graph(adjacency_lists, result), "test #9")

        adjacency_lists = {
            'A': {'B'},
            'B': {'C', 'D'},
            'C': {'D', 'E'},
            'D': {'E'},
            'E': set(), }
        result = algorithm(adjacency_lists)
        self.assertEqual(True, is_sorted_graph(adjacency_lists, result), "test #10")

        adjacency_lists = {
            'A': {'B'},
            'B': {'C', 'D'},
            'C': {'D', 'E'},
            'D': {'E'},
            'E': {'C'}, }
        result = algorithm(adjacency_lists)
        self.assertEqual(False, is_sorted_graph(adjacency_lists, result), "test #11")

        adjacency_lists = {
            'A': {'B'},
            'B': {'C'},
            'C': {'A'}, }
        result = algorithm(adjacency_lists)
        self.assertEqual(False, is_sorted_graph(adjacency_lists, result), "test #12")

        adjacency_lists = {
            'A': {'B', 'C'},
            'B': {'C'},
            'C': {'D'},
            'D': {'A'}, }
        result = algorithm(adjacency_lists)
        self.assertEqual(False, is_sorted_graph(adjacency_lists, result), "test #13")

        adjacency_lists = {
            'A': {'B', 'D', 'F'},
            'B': {'C'},
            'C': {'D', 'E'},
            'D': {'E'},
            'E': {'F'},
            'F': set(), }
        result = algorithm(adjacency_lists)
        self.assertEqual(True, is_sorted_graph(adjacency_lists, result), "test #14")

        adjacency_lists = {
            'A': {'C'},
            'B': {'E'},
            'C': {'D', 'E'},
            'D': set(),
            'E': set(), }
        result = algorithm(adjacency_lists)
        self.assertEqual(True, is_sorted_graph(adjacency_lists, result), "test #15")


if __name__ == '__main__':
    unittest.main()
