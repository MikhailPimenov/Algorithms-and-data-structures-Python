import unittest
# from .brace_sequence2 import brace_sequence as algorithm
# from .brace_sequence3 import brace_sequence3 as algorithm
# from .brace_sequence4 import brace_sequence4 as algorithm
from .brace_sequence5 import brace_sequence5 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sequence = "[()]"
        self.assertEqual(algorithm(sequence), True, "test #1")

        sequence = "sdfsdf(sdf)sdfsdf[sdsdf]sdf([sdf]dfsd)dsf"
        self.assertEqual(algorithm(sequence), True, "test #2")

        sequence = "[()]["
        self.assertEqual(algorithm(sequence), False, "test #3")

        sequence = "[()]]"
        self.assertEqual(algorithm(sequence), False, "test #4")

        sequence = "[(])"
        self.assertEqual(algorithm(sequence), False, "test #5")

        sequence = "["
        self.assertEqual(algorithm(sequence), False, "test #6")

        sequence = "("
        self.assertEqual(algorithm(sequence), False, "test #7")

        sequence = "]"
        self.assertEqual(algorithm(sequence), False, "test #8")

        sequence = ")"
        self.assertEqual(algorithm(sequence), False, "test #9")


if __name__ == '__main__':
    unittest.main()
