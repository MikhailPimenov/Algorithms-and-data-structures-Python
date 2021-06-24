import unittest
# from .discrete_bag2 import discrete_bag as algorithm
# from .discrete_bag3 import discrete_bag3 as algorithm
from .discrete_bag4 import discrete_bag4 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        items = [(1, 20), (2, 30), (3, 30), (4, 40), (5, 50)]
        mass = 10
        answer = 120
        result = algorithm(items, mass)
        self.assertEqual(answer, result, "test #1")

        items = [(2, 30), (2, 30), (4, 30), (4, 40), (5, 50)]
        mass = 10
        answer = 110
        result = algorithm(items, mass)
        self.assertEqual(answer, result, "test #2")

        items = [(2, 30), (2, 30), (2, 30), (3, 30), (4, 40), (5, 50)]
        mass = 10
        answer = 130
        result = algorithm(items, mass)
        self.assertEqual(answer, result, "test #3")


if __name__ == '__main__': \
        unittest.main()
