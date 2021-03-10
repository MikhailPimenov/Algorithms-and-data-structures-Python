import unittest
# from .p_function2 import p_function as algorithm
from .p_function3 import p_function3 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        string = ['a', 'b', 'a', 'b', 'a', 'b', 'a']
        p_array = [0, 0, 1, 2, 3, 4, 5]
        result = algorithm(string)
        self.assertEqual(p_array, result, "test #1")

        string = ['a', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b', 'a', 'c', 'd']
        p_array = [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 2, 3]
        result = algorithm(string)
        self.assertEqual(p_array, result, "test #2")

        string = ['a', 'l', 'a', 'l', 'c', 'd', 'a']
        p_array = [0, 0, 1, 2, 0, 0, 1]
        result = algorithm(string)
        self.assertEqual(p_array, result, "test #3")

        string = ['a', 'k', 'e', 'a', 'k', 'e', 'a']
        p_array = [0, 0, 0, 1, 2, 3, 4]
        result = algorithm(string)
        self.assertEqual(p_array, result, "test #4")

        string = ['a', 'a']
        p_array = [0, 1]
        result = algorithm(string)
        self.assertEqual(p_array, result, "test #5")

        string = ['a', 'b', 'a']
        p_array = [0, 0, 1]
        result = algorithm(string)
        self.assertEqual(p_array, result, "test #6")

        string = "pig is big#pig pig pig is very big pig pig is big"
        p_array = [
            0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 2, 3,
            4, 1, 2, 3, 4, 1, 2,
            3, 4, 5, 6, 7, 0, 0,
            0, 0, 0, 0, 0, 0, 0,
            1, 2, 3, 4, 1, 2, 3,
            4, 5, 6, 7, 8, 9, 10
        ]
        result = algorithm(string)
        self.assertEqual(p_array, result, "test #7")


if __name__ == '__main__':
    unittest.main()
