import unittest
# from .fibonacci_recursive_cash import fibonacci_recursive_cash as algorithm
from .fibonacci_recursive_cache3 import fibonacci_recursive_cache3 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        for k in range(1, 60):
            print(k, algorithm(k))


if __name__ == '__main__':
    unittest.main()
