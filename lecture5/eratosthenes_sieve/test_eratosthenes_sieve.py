import unittest
from .eratosthenes_sieve2 import eratosthenes_sieve


class MyTestCase(unittest.TestCase):
    def test_something(self):
        eratosthenes_sieve(100)
        self.assertRaises(ArithmeticError, eratosthenes_sieve, -5)
        self.assertRaises(TypeError, eratosthenes_sieve, "ABCDEF")


if __name__ == '__main__':
    unittest.main()
