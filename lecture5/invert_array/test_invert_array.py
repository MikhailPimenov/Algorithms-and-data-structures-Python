import unittest
from .invert_array2 import invert_array


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(invert_array([1, 2, 3], 3), [3, 2, 1])
        self.assertEqual(invert_array([1, 2, 3, 4], 4), [4, 3, 2, 1])
        self.assertRaises(TypeError, invert_array, "asd", 3)
        self.assertRaises(TypeError, invert_array, [1, 2, 3, 4, 5], "5")


if __name__ == '__main__':
    unittest.main()
