import unittest
from .fibonacci_recursive_cash import fibonacci_recursive_cash as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for k in range(1,15):
            print(algorithm(k))


if __name__ == '__main__':
    unittest.main()
