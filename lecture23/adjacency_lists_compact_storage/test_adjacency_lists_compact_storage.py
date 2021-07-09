import unittest
# from .adjacency_lists_compact_storage2 import adjacency_lists_compact_storage as algorithm
# from .adjacency_lists_compact_storage3 import adjacency_lists_compact_storage3 as algorithm
from .adjacency_lists_compact_storage5 import adjacency_lists_compact_storage5 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        vertexes = ['A', 'B', 'C', 'D']
        lists = [['B', 'D'], ['A', 'D', 'C'], ['B', 'D'], ['A', 'B', 'C'], ]

        answer = ['A', 'B', 'C', 'D'], \
                 [0, 2, 5, 7, 10], \
                 ['B', 'D', 'A', 'D', 'C', 'B', 'D', 'A', 'B', 'C']

        result = algorithm(vertexes, lists)
        self.assertEqual(answer, result, "test #1")


if __name__ == '__main__':
    unittest.main()
