import unittest
from .adjacency_lists2 import adjacency_lists as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # 4 5
        # A B
        # B C
        # C D
        # D B
        # A D
        answer = {'A':{'B','D'},
                  'B':{'A','D','C'},
                  'C':{'B','D'},
                  'D':{'A','B','C'},}

        result = algorithm()
        self.assertEqual(answer, result, "test #1")


if __name__ == '__main__':
    unittest.main()
