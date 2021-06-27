import unittest
# from lecture6.bubble_sort.bubble_sort2 import bubble_sort as algorithm
# from lecture6.insertion_sort.insert_sort2 import insertion_sort as algorithm
# from lecture6.selection_sort.selection_sort2 import selection_sort as algorithm
# from lecture9.hoar_sort.hoar_sort2 import hoar_sort as algorithm
# from lecture9.merge_sort.merge_sort2 import merge_sort as algorithm
# from lecture19.heap_sort.heap_sort2 import heap_sort as algorithm
# from lecture6.bubble_sort.bubble_sort3 import bubble_sort3 as algorithm
# from lecture6.insertion_sort.insert_sort3 import insert_sort3 as algorithm
# from lecture6.selection_sort.selection_sort3 import selection_sort3 as algorithm
# from lecture19.heap_sort.heap_sort3 import heap_sort3 as algorithm
# from lecture9.merge_sort.merge_sort3 import merge_sort3 as algorithm
# from lecture9.hoar_sort.hoar_sort3 import hoar_sort3 as algorithm
# from lecture6.bubble_sort.bubble_sort4 import bubble_sort4 as algorithm
# from lecture6.insertion_sort.insert_sort4 import insert_sort4 as algorithm
# from lecture6.selection_sort.selection_sort4 import selection_sort4 as algorithm
# from lecture19.heap_sort.heap_sort4 import heap_sort4 as algorithm
# from lecture9.hoar_sort.hoar_sort4 import hoar_sort4 as algorithm
# from lecture9.merge_sort.merge_sort4 import merge_sort4 as algorithm
# from lecture6.insertion_sort.insertion_sort5 import insertion_sort5 as algorithm
# from lecture6.selection_sort.selection_sort5 import selection_sort5 as algorithm
# from lecture6.bubble_sort.bubble_sort5 import bubble_sort5 as algorithm
# from lecture19.heap_sort.heap_sort5 import heap_sort5 as algorithm
# from lecture9.merge_sort.merge_sort5 import merge_sort5 as algorithm
from lecture9.hoar_sort.hoar_sort5 import hoar_sort5 as algorithm


class MyTestCase(unittest.TestCase):
    def test_something(self):
        array = [1, 3, 2, 5, 4]
        array_sorted = [1, 2, 3, 4, 5]
        algorithm(array)
        self.assertEqual(array_sorted, array, "test #1")

        array = [5, 5, 5, 5, 5]
        array_sorted = [5, 5, 5, 5, 5]
        algorithm(array)
        self.assertEqual(array_sorted, array, "test #2")

        array = [5, 5, 4, 5, 5]
        array_sorted = [4, 5, 5, 5, 5]

        algorithm(array)
        self.assertEqual(array_sorted, array, "test #3")

        array = [5, 15, 14, 25, 15, 9, 7, 10, 10, 0, 2]
        array_sorted = [0, 2, 5, 7, 9, 10, 10, 14, 15, 15, 25]
        algorithm(array)
        self.assertEqual(array_sorted, array, "test #4")
        array = [
            1, 5, 7, 8, 9, 4, 5, 6, 1, 2, 3, 0, 2,
            4, 9, 8, 7, 1, 2, 5, 4, 7, 9, 8, 6, 5,
            4, 3, 2, 1, 0, 3, 2, 1, 4, 5, 7, 8, 9,
            8, 5, 6, 8, 7, 0, 9, 2, 1, 5, 4, 8, 9,
            6, 1, 5, 7, 8, 1, 0, 3, 1, 4, 7, 9, 8,
            6, 4, 5, 3, 1, 0, 2, 5, 7, 2, 7, 3, 9
        ]
        array_sorted = [
            0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3,
            3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6,
            7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8,
            8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9
        ]
        algorithm(array)
        self.assertEqual(array_sorted, array, "test #5")

        array = [
            4, 8, 7, 6, 0, 9, 4, 3, 8, 1, 7, 2, 0, 4, 0, 7, 0, 7, 9, 8,
            6, 8, 5, 7, 4, 6, 3, 5, 2, 4, 1, 4, 3, 1, 2, 6, 4, 7, 6, 5,
            3, 1, 6, 9, 1, 5, 2, 9, 1, 6, 1, 3, 1, 2, 8, 7, 9, 7, 8, 6,
            5, 3, 1, 2, 9, 5, 9, 7, 6, 8, 3, 1, 2, 6, 2, 9, 7, 6, 8, 3,
            1, 6, 2, 9, 7, 6, 8, 2, 4, 1, 5, 4, 4, 5, 7, 8, 8, 9, 5, 6,
            3, 1, 3, 1, 6, 4, 6, 5, 7, 9, 4, 9, 1, 3, 4, 2, 7, 9, 8, 3,
            4, 2, 1, 3, 2, 9, 5, 9, 7, 8, 4, 2, 1, 4, 7, 8, 9, 6, 5, 2,
            3, 1, 4, 7, 8, 9, 2, 1, 5, 7, 2, 5, 6, 1, 4, 5, 4, 8, 6, 0,
            8, 6, 9, 7, 8, 9, 0, 1, 2, 3, 4, 1, 1, 2, 3, 0, 7, 8, 6, 4,
            8, 5, 8, 7, 8, 9, 9, 0, 5, 1, 2, 0, 0, 4, 5, 7, 0, 3, 8, 1,
        ]
        array_sorted = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7,
            7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8,
            8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9,
            9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
        ]
        algorithm(array)
        self.assertEqual(array_sorted, array, "test #6")

        array = [
            1, 5, 7, 8, 9, 4, 5, 6, 1, 2, 3, 0, 2,
            6, 1, 5, 7, 8, 1, 0, 3, 1, 4, 7, 9, 8,
            4, 9, 8, 7, 1, 2, 5, 4, 7, 9, 8, 6, 5,
            8, 5, 6, 8, 7, 0, 9, 2, 1, 5, 4, 8, 9,
            4, 3, 2, 1, 0, 3, 2, 1, 4, 5, 7, 8, 9,
            6, 4, 5, 3, 1, 0, 2, 5, 7, 2, 7, 3, 9
        ]
        array_sorted = [
            0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3,
            3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6,
            7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8,
            8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9
        ]
        algorithm(array)
        self.assertEqual(array_sorted, array, "test #7")

        array = [
            4, 8, 7, 6, 0, 9, 4, 3, 8, 1, 7, 2, 0, 4, 0, 7, 0, 7, 9, 8,
            1, 6, 2, 9, 7, 6, 8, 2, 4, 1, 5, 4, 4, 5, 7, 8, 8, 9, 5, 6,
            3, 1, 4, 7, 8, 9, 2, 1, 5, 7, 2, 5, 6, 1, 4, 5, 4, 8, 6, 0,
            3, 1, 3, 1, 6, 4, 6, 5, 7, 9, 4, 9, 1, 3, 4, 2, 7, 9, 8, 3,
            3, 1, 6, 9, 1, 5, 2, 9, 1, 6, 1, 3, 1, 2, 8, 7, 9, 7, 8, 6,
            4, 2, 1, 3, 2, 9, 5, 9, 7, 8, 4, 2, 1, 4, 7, 8, 9, 6, 5, 2,
            5, 3, 1, 2, 9, 5, 9, 7, 6, 8, 3, 1, 2, 6, 2, 9, 7, 6, 8, 3,
            6, 8, 5, 7, 4, 6, 3, 5, 2, 4, 1, 4, 3, 1, 2, 6, 4, 7, 6, 5,
            8, 6, 9, 7, 8, 9, 0, 1, 2, 3, 4, 1, 1, 2, 3, 0, 7, 8, 6, 4,
            8, 5, 8, 7, 8, 9, 9, 0, 5, 1, 2, 0, 0, 4, 5, 7, 0, 3, 8, 1,
        ]
        array_sorted = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7,
            7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8,
            8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9,
            9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, ]
        algorithm(array)
        self.assertEqual(array_sorted, array, "test #8")

        array = [
            8, 6, 9, 7, 8, 9, 0, 1, 2, 3, 4, 1, 1, 2, 3, 0, 7, 8, 6, 4,
            8, 5, 8, 7, 8, 9, 9, 0, 5, 1, 2, 0, 0, 4, 5, 7, 0, 3, 8, 1,
            6, 8, 5, 7, 4, 6, 3, 5, 2, 4, 1, 4, 3, 1, 2, 6, 4, 7, 6, 5,
            5, 3, 1, 2, 9, 5, 9, 7, 6, 8, 3, 1, 2, 6, 2, 9, 7, 6, 8, 3,
            4, 8, 7, 6, 0, 9, 4, 3, 8, 1, 7, 2, 0, 4, 0, 7, 0, 7, 9, 8,
            4, 2, 1, 3, 2, 9, 5, 9, 7, 8, 4, 2, 1, 4, 7, 8, 9, 6, 5, 2,
            3, 1, 6, 9, 1, 5, 2, 9, 1, 6, 1, 3, 1, 2, 8, 7, 9, 7, 8, 6,
            3, 1, 4, 7, 8, 9, 2, 1, 5, 7, 2, 5, 6, 1, 4, 5, 4, 8, 6, 0,
            3, 1, 3, 1, 6, 4, 6, 5, 7, 9, 4, 9, 1, 3, 4, 2, 7, 9, 8, 3,
            1, 6, 2, 9, 7, 6, 8, 2, 4, 1, 5, 4, 4, 5, 7, 8, 8, 9, 5, 6,
        ]
        array_sorted = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7,
            7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8,
            8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9,
            9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
        ]
        algorithm(array)
        self.assertEqual(array_sorted, array, "test #9")

        array = [
            8, 6, 9, 7, 8, 9, 0, 1, 2, 3, 4, 1, 1, 2, 3, 0, 7, 8, 6, 4, 0,
            8, 5, 8, 7, 8, 9, 9, 0, 5, 1, 2, 0, 0, 4, 5, 7, 0, 3, 8, 1, 1,
            6, 8, 5, 7, 4, 6, 3, 5, 2, 4, 1, 4, 3, 1, 2, 6, 4, 7, 6, 5, 2,
            5, 3, 1, 2, 9, 5, 9, 7, 6, 8, 3, 1, 2, 6, 2, 9, 7, 6, 8, 3, 3,
            4, 8, 7, 6, 0, 9, 4, 3, 8, 1, 7, 2, 0, 4, 0, 7, 0, 7, 9, 8, 4,
            4, 2, 1, 3, 2, 9, 5, 9, 7, 8, 4, 2, 1, 4, 7, 8, 9, 6, 5, 2, 5,
            3, 1, 6, 9, 1, 5, 2, 9, 1, 6, 1, 3, 1, 2, 8, 7, 9, 7, 8, 6, 6,
            3, 1, 4, 7, 8, 9, 2, 1, 5, 7, 2, 5, 6, 1, 4, 5, 4, 8, 6, 0, 7,
            3, 1, 3, 1, 6, 4, 6, 5, 7, 9, 4, 9, 1, 3, 4, 2, 7, 9, 8, 3, 8,
            1, 6, 2, 9, 7, 6, 8, 2, 4, 1, 5, 4, 4, 5, 7, 8, 8, 9, 5, 6, 9,
        ]
        array_sorted = [
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
            2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3,
            3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4,
            4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5,
            5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6,
            6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7,
            7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8,
            8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 9,
            9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
        ]
        algorithm(array)
        self.assertEqual(array_sorted, array, "test #10")


if __name__ == '__main__':
    unittest.main()
