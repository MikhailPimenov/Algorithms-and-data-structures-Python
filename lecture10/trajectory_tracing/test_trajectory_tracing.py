import unittest
from .trajectory_tracing2 import trajectory_tracing as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        prices = [5, 5, 5, 5, 5, 5, 100, 5, 5, 5, 100, 5, 100, 5, 100, 5, 100, 5]

        allowed = [False, True, True,
                   False, True, True, True, True,
                   False, True, True, True, True, True, True, True, True, True]

        self.assertEqual(algorithm(prices, allowed, 18), 50)
        self.assertRaises(TypeError, algorithm, 1, 'a', 2)
        self.assertRaises(ArithmeticError, algorithm, prices, allowed + [False], 18)
        self.assertRaises(ArithmeticError, algorithm, prices, allowed, 30)


if __name__ == '__main__':
    unittest.main()
