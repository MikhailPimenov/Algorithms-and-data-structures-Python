import unittest
# from .power_fast2 import power_fast as algorithm
from .power_fast5 import power_fast5 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(algorithm(2, 2), 4)
        self.assertEqual(algorithm(1, 2), 1)
        self.assertEqual(algorithm(2, 3), 8)
        self.assertEqual(algorithm(2, 4), 16)
        self.assertEqual(algorithm(2, 5), 32)
        self.assertEqual(algorithm(2, 6), 64)
        self.assertEqual(algorithm(2, 7), 128)
        self.assertEqual(algorithm(2, 8), 256)
        self.assertEqual(algorithm(2, 9), 512)
        self.assertEqual(algorithm(2, 10), 1024)
        self.assertEqual(algorithm(3, 2), 9)
        self.assertEqual(algorithm(3, 3), 27)
        self.assertEqual(algorithm(3, 4), 81)
        self.assertEqual(algorithm(0, 2), 0)
        self.assertEqual(algorithm(0, 10), 0)
        self.assertEqual(algorithm(2, 0), 1)
        self.assertEqual(algorithm(10, 0), 1)
        self.assertEqual(algorithm(10, 5), 100000)
        # self.assertRaises(ArithmeticError, algorithm, -2, 3)
        # self.assertRaises(ArithmeticError, algorithm, 2, -3)
        # self.assertRaises(ArithmeticError, algorithm, -2, -3)
        # self.assertRaises(TypeError, algorithm, 2.3, 2)
        # self.assertRaises(TypeError, algorithm, 2.3, 2.9)
        # self.assertRaises(TypeError, algorithm, "asd", 2)
        # self.assertRaises(TypeError, algorithm, 2, "asd")
        # self.assertRaises(TypeError, algorithm, "asd", "asd")
        # self.assertRaises(TypeError, algorithm, 'a', 'a')


if __name__ == '__main__':
    unittest.main()
