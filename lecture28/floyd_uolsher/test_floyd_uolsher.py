import unittest
from .floyd_uolsher import floyd_uolsher as algorithm
from lecture26.dijkstra.dijkstra import dijkstra


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
        answer = {}
        for vertex in adjacency_lists:
            answer[vertex] = dijkstra(adjacency_lists, vertex)

        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #1")

        adjacency_lists = {
            'A': {'B': 2, 'H': 15, 'M': 2, 'N': 6, 'O': 10},
            'B': {'A': 2, 'C': 1, 'D': 5},
            'C': {'B': 1, 'D': 3, 'F': 2, 'G': 1},
            'D': {'B': 5, 'C': 3, 'F': 4, 'E': 6, 'M': 4, 'N': 8, 'O': 12},
            'E': {'D': 6, 'F': 7, 'I': 2, 'J': 1, 'K': 3, 'L': 5},
            'F': {'C': 2, 'D': 4, 'E': 7, 'G': 1, 'H': 3},
            'G': {'C': 1, 'F': 1},
            'H': {'A': 15, 'F': 3, 'I': 12, 'J': 2, 'K': 4, 'L': 6},
            'I': {'E': 2, 'H': 12},
            'J': {'E': 1, 'H': 2},
            'K': {'E': 3, 'H': 4},
            'L': {'E': 5, 'H': 6},
            'M': {'A': 2, 'D': 4},
            'N': {'A': 6, 'D': 8},
            'O': {'A': 10, 'D': 12},
        }
        answer = {}
        for vertex in adjacency_lists:
            answer[vertex] = dijkstra(adjacency_lists, vertex)

        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #2")

        adjacency_lists = {
            'A': {'T': 18, 'B': 4, 'C': 1, 'H': 6, 'I': 7, 'N': 1},
            'B': {'A': 4, 'D': 5, 'O': 4},
            'C': {'A': 1, 'D': 5, 'H': 3, 'G': 7},
            'D': {'B': 5, 'O': 8, 'E': 4, 'F': 5, 'C':5},
            'E': {'O': 8, 'N': 8, 'M': 9, 'F': 3, 'D': 4},
            'F': {'D': 5, 'E': 3, 'M': 6, 'L': 6, 'K': 3, 'G': 2},
            'G': {'C': 7, 'F': 2, 'K': 2, 'H': 4},
            'H': {'A': 6, 'C': 3, 'G': 4, 'J': 2},
            'I': {'A': 7, 'V': 8},
            'J': {'H': 2, 'V': 3, 'S': 4},
            'K': {'G': 2, 'R': 5, 'T': 6, 'F': 3},
            'L': {'F': 6, 'M': 1, 'P': 9, 'R': 4},
            'M': {'N': 8, 'E': 9, 'F': 6, 'L': 1, 'P': 2},
            'N': {'A': 1, 'E': 8, 'M': 8},
            'O': {'B': 4, 'D': 8, 'E': 8},
            'P': {'M': 2, 'L': 9, 'Q': 3},
            'Q': {'P': 3, 'R': 4},
            'R': {'L': 4, 'Q': 4, 'T': 4, 'K': 5},
            'S': {'T': 6, 'J': 4},
            'T': {'R': 4, 'K': 6, 'S': 6, 'A': 18},
            'V': {'I': 8, 'J': 3},
        }
        answer = {}
        for vertex in adjacency_lists:
            answer[vertex] = dijkstra(adjacency_lists, vertex)

        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #3")

        adjacency_lists = {
            'A': {'B': 2, 'H': 15},
            'B': {'A': 2, 'C': 1, 'D': 5},
            'C': {'B': 1, 'D': 3, 'F': 2, 'G': 1},
            'D': {'B': 5, 'C': 3, 'F': 4, 'E': 6},
            'E': {'D': 6, 'F': 7, 'I': 2, 'J': 1, 'K': 3, 'L': 5},
            'F': {'C': 2, 'D': 4, 'E': 7, 'G': 1, 'H': 3},
            'G': {'C': 1, 'F': 1},
            'H': {'A': 15, 'F': 3, 'I': 12, 'J': 2, 'K': 4, 'L': 6},
            'I': {'E': 2, 'H': 12},
            'J': {'E': 1, 'H': 2},
            'K': {'E': 3, 'H': 4},
            'L': {'E': 5, 'H': 6},
        }
        answer = {}
        for vertex in adjacency_lists:
            answer[vertex] = dijkstra(adjacency_lists, vertex)

        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #4")


if __name__ == '__main__':
    unittest.main()
