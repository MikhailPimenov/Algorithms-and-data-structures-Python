import unittest
# from .grand_common_divisor2 import grand_common_divisor
from .grand_common_divisor5 import grand_common_divisor5 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(algorithm(25, 5), 5)
        self.assertEqual(algorithm(5, 25), 5)
        self.assertEqual(algorithm(6, 8), 2)
        self.assertEqual(algorithm(8, 6), 2)
        self.assertEqual(algorithm(25, 35), 5)
        self.assertEqual(algorithm(35, 25), 5)
        self.assertEqual(algorithm(35, 35), 35)
        self.assertEqual(algorithm(18, 12), 6)
        self.assertEqual(algorithm(12, 18), 6)
        self.assertRaises(ArithmeticError, algorithm, -10, 5)
        self.assertRaises(ArithmeticError, algorithm, 10, -5)
        self.assertRaises(ArithmeticError, algorithm, -10, -5)
        self.assertRaises(TypeError, algorithm, 0.9, 1)
        self.assertRaises(TypeError, algorithm, 9, 0.1)
        self.assertRaises(TypeError, algorithm, 0.9, 0.1)
        self.assertRaises(TypeError, algorithm, 9, "asd")
        self.assertRaises(TypeError, algorithm, "asd", 5)
        self.assertRaises(TypeError, algorithm, "asd", 'a')
        self.assertRaises(TypeError, algorithm, 'a', 'a')


if __name__ == '__main__':
    unittest.main()
