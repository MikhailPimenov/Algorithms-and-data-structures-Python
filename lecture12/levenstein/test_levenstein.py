import unittest
from .levenstein2 import levenstein as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        string1 = ['p', 'i', 'g']
        string2 = ['b', 'i', 'g']
        answer = 1
        result = algorithm(string1, string2)
        self.assertEqual(answer, result, "test #1")

        string1 = ['b', 'a', 'g']
        string2 = ['b', 'i', 'g']
        answer = 1
        result = algorithm(string1, string2)
        self.assertEqual(answer, result, "test #2")

        string1 = ['h', 'e', 'a', 'd']
        string2 = ['h', 'o', 'm', 'e']
        answer = 3
        result = algorithm(string1, string2)
        self.assertEqual(answer, result, "test #3")

        string1 = ['t', 'a', 'b', 'l', 'e']
        string2 = ['t', 'a', 'b', 'l', 'e', '1', '2', '3', '4']
        answer = 4
        result = algorithm(string1, string2)
        self.assertEqual(answer, result, "test #4")

        string1 = ['t', 'a', 'b', 'l', 'e']
        string2 = ['t', 'a', 'b', 'l', 'e']
        answer = 0
        result = algorithm(string1, string2)
        self.assertEqual(answer, result, "test #5")

        string1 = ['f', 'l', 'o', 'w', 'e', 'r']
        string2 = ['t', 'o', 'w', 'e', 'r']
        answer = 2
        result = algorithm(string1, string2)
        self.assertEqual(answer, result, "test #6")

        string1 = []
        string2 = []
        answer = 0
        result = algorithm(string1, string2)
        self.assertEqual(answer, result, "test #7")

        string1 = ['a', 'n', 's', 'w', 'e', 'r']
        string2 = ['r', 'e', 's', 'u', 'l', 't']
        answer = 5
        result = algorithm(string1, string2)
        self.assertEqual(answer, result, "test #8")

        string1 = ['p', 'i', 'g']
        string2 = ['p', 'i', 'g', ' ', 'i', 's', ' ', 'b', 'i', 'g']
        answer = 7
        result = algorithm(string1, string2)
        self.assertEqual(answer, result, "test #9")


if __name__ == '__main__':
    unittest.main()
