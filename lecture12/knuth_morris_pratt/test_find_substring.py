import unittest
from .knuth_morris_pratt import knuth_morris_pratt as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        string = "This pig is very big!"
        substring = "big"

        l_string = [string[i] for i in range(len(string))]
        l_substring = [substring[i] for i in range(len(substring))]

        answer = 17
        result = algorithm(l_string, l_substring)
        self.assertEqual(answer, result, "test #1")

        string = "I forgot green bag on the sofa."
        substring = "green"

        l_string = [string[i] for i in range(len(string))]
        l_substring = [substring[i] for i in range(len(substring))]

        answer = 9
        result = algorithm(l_string, l_substring)
        self.assertEqual(answer, result, "test #2")

        string = "I used to pump my shoulders before bench press"
        substring = "press"

        l_string = [string[i] for i in range(len(string))]
        l_substring = [substring[i] for i in range(len(substring))]

        answer = 41
        result = algorithm(l_string, l_substring)
        self.assertEqual(answer, result, "test #3")

        string = "This weather gets me down."
        substring = "dog"

        l_string = [string[i] for i in range(len(string))]
        l_substring = [substring[i] for i in range(len(substring))]

        answer = -1
        result = algorithm(l_string, l_substring)
        self.assertEqual(answer, result, "test #4")

        string = "Table is black."
        substring = "Table"

        l_string = [string[i] for i in range(len(string))]
        l_substring = [substring[i] for i in range(len(substring))]

        answer = 0
        result = algorithm(l_string, l_substring)
        self.assertEqual(answer, result, "test #5")

        string = "Flower grew up on my garden."
        substring = "on"

        l_string = [string[i] for i in range(len(string))]
        l_substring = [substring[i] for i in range(len(substring))]

        answer = 15
        result = algorithm(l_string, l_substring)
        self.assertEqual(answer, result, "test #6")

        string = ""
        substring = ""

        l_string = [string[i] for i in range(len(string))]
        l_substring = [substring[i] for i in range(len(substring))]

        answer = -1
        result = algorithm(l_string, l_substring)
        self.assertEqual(answer, result, "test #7")

        string = "Notreadablestatementnotreadablestatement"
        substring = "dab"

        l_string = [string[i] for i in range(len(string))]
        l_substring = [substring[i] for i in range(len(substring))]

        answer = 6
        result = algorithm(l_string, l_substring)
        self.assertEqual(answer, result, "test #8")

        string = "pig pig pig is very big pig pig is big"
        substring = "pig is big"

        l_string = [string[i] for i in range(len(string))]
        l_substring = [substring[i] for i in range(len(substring))]

        answer = 28
        result = algorithm(l_string, l_substring)
        self.assertEqual(answer, result, "test #9")

        string = "Flower grew up on my garden."
        substring = "Flower grew up on my garden, when I was away"

        l_string = [string[i] for i in range(len(string))]
        l_substring = [substring[i] for i in range(len(substring))]

        answer = -1
        result = algorithm(l_string, l_substring)
        self.assertEqual(answer, result, "test #10")


if __name__ == '__main__':
    unittest.main()
