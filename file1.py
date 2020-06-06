# lecture 18
# class heap
# heapify_fast
# heap_sort

from HeapSimple import HeapSimple


def heapify_fast(array: list):
    heap = HeapSimple()
    heap.values = array[:]
    heap.length = len(array)

    for i in range(len(array) // 2 - 1, -1, -1):
        heap.sift_down(i)

    for i in range(len(array)):
        array[i] = heap.values[i]


def heap_sort(array: list):
    heap = HeapSimple(array)

    for i in range(len(array)):
        array[i] = heap.extract_min()


def test_heapify_fast(algorithm):
    array = [9, 8, 7, 10, 10, 10, 6, 5, 4, 3, 2, 1, 0, 2]
    algorithm(array)
    print(*array)


def test_sort(algorithm, string: str = ""):
    print("testing:", string)

    array = [1, 3, 4, 1, 3, 2, 0, 5, 9, 10, 6, 5]
    array_sorted = [0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 9, 10]
    algorithm(array)
    print("test #1:", "ok" if array == array_sorted else "FAILED")

    array = [1, 3, 4, 6, 5]
    array_sorted = [1, 3, 4, 5, 6]
    algorithm(array)
    print("test #2:", "ok" if array == array_sorted else "FAILED")

    array = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    array_sorted = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    algorithm(array)
    print("test #3:", "ok" if array == array_sorted else "FAILED")

    array = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    array_sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    algorithm(array)
    print("test #4:", "ok" if array == array_sorted else "FAILED")


# test_heapify_fast(heapify_fast)
test_sort(heap_sort, "heap_sort")
