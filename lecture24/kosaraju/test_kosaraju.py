import unittest
# from .kosaraju2 import kosaraju as algorithm
# from .kosaraju3 import kosaraju3 as algorithm
# from .kosaraju4 import kosaraju4 as algorithm
from .kosaraju5 import kosaraju5 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        answer = set()

        adjacency_lists = {
            'A': {'B'},
            'B': {'C'},
            'C': {'D'},
            'D': {'A'}, }
        component = {'A', 'B', 'C', 'D'}
        answer.add(frozenset(component))
        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #1")
        answer.clear()

        adjacency_lists = {
            'A': {'B'},
            'B': {'C'},
            'C': {'D', 'E'},
            'D': set(),
            'E': {'A', 'D'}, }
        component = {'A', 'B', 'C', 'E'}
        answer.add(frozenset(component))
        component = {'D'}
        answer.add(frozenset(component))

        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #2")
        answer.clear()

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
        component = {'A', 'B', 'C'}
        answer.add(frozenset(component))
        component = {'D', 'E', 'F'}
        answer.add(frozenset(component))
        component = {'G', 'H', 'I', 'J'}
        answer.add(frozenset(component))
        component = {'K'}
        answer.add(frozenset(component))

        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #3")
        answer.clear()

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
            'K': {'J'},
            'L': set(),
            'M': set(),
        }
        component = {'A', 'B', 'C'}
        answer.add(frozenset(component))
        component = {'D', 'E', 'F'}
        answer.add(frozenset(component))
        component = {'G', 'H', 'I', 'J'}
        answer.add(frozenset(component))
        component = {'K'}
        answer.add(frozenset(component))
        component = {'L'}
        answer.add(frozenset(component))
        component = {'M'}
        answer.add(frozenset(component))

        result = algorithm(adjacency_lists)
        self.assertEqual(answer, result, "test #4")
        answer.clear()


if __name__ == '__main__':
    unittest.main()
