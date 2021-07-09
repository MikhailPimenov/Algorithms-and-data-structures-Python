import unittest
# from .fibonacci3 import fibonacci3 as recursive_algorithm
# from .fibonacci3 import fibonacci_cached3 as cached_recursive_algorithm
# from .fibonacci3 import fibonacci_fast3 as dynamic_programming_algorithm
# from .fibonacci3 import fibonacci_generator3 as generator_algorithm

from .fibonacci5 import fibonacci5 as recursive_algorithm
from .fibonacci5 import fibonacci5_recursive_cache as cached_recursive_algorithm
from .fibonacci5 import fibonacci5_dynamic_programming as dynamic_programming_algorithm
from .fibonacci5 import fibonacci5_generator as generator_algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        algorithms = (
            recursive_algorithm,
            cached_recursive_algorithm,
            dynamic_programming_algorithm
        )

        for algorithm in algorithms:
            for k in range(20):
                print(algorithm(k))
            print()

        g = generator_algorithm()
        for k in range(20):
            print(next(g))

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
