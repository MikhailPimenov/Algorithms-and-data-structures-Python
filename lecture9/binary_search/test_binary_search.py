import unittest
from .binary_search2 import binary_search as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [1, 1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 6, 6, 7, 7, 7, 7, 7, 8, 9]

        element = 0
        result = algorithm(array, element)
        self.assertEqual(result, (False, -1, 0))

        element = 12
        result = algorithm(array, element)
        self.assertEqual(result, (False, 19, 20))

        element = 1
        result = algorithm(array, element)
        self.assertEqual(result, (True, -1, 5))

        element = 2
        result = algorithm(array, element)
        self.assertEqual(result, (True, 4, 7))

        element = 3
        result = algorithm(array, element)
        self.assertEqual(result, (True, 6, 8))

        element = 5
        result = algorithm(array, element)
        self.assertEqual(result, (False, 10, 11))

        element = 7
        result = algorithm(array, element)
        self.assertEqual(result, (True, 12, 18))

        element = 8
        result = algorithm(array, element)
        self.assertEqual(result, (True, 17, 19))



if __name__ == '__main__':
    unittest.main()
