import unittest
from .generate_permutations import generate_permutations as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertRaises(TypeError, algorithm, 'a', "asd")
        self.assertRaises(TypeError, algorithm, [1, 2, 3], 'a')
        self.assertRaises(TypeError, algorithm, "asd", 10)
        print("====================")
        elements = [1, 2, 3]
        print("test #1:")
        algorithm(elements, 2)
        print("test #2:")
        elements = [1, 1, 2, 3]
        algorithm(elements, 2)
        print("====================")


if __name__ == '__main__':
    unittest.main()
