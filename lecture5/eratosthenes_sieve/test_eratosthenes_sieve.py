import unittest
# from .eratosthenes_sieve2 import eratosthenes_sieve
from .eratosthenes_sieve5 import eratosthenes_sieve5 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        algorithm(100)
        self.assertRaises(ArithmeticError, algorithm, -5)
        self.assertRaises(TypeError, algorithm, "ABCDEF")


if __name__ == '__main__':
    unittest.main()
