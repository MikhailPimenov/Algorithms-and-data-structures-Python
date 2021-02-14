import unittest
from .voting2 import voting as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        stream = [10,
                  "Arkady",
                  "Arkady",
                  "Andrew",
                  "Andrew",
                  "Arkady",
                  "Anton",
                  "Arkady",
                  "Anton",
                  "Anton",
                  "Arkady"]
        answer = {"Arkady": 5,
                  "Anton": 3,
                  "Andrew": 2}
        result = algorithm(stream)
        self.assertEqual(answer, result)


if __name__ == '__main__':
    unittest.main()
