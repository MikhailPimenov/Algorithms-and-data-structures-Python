def bubble_sort(array: list):
    for k in range(len(array)):
        for i in range(len(array) - k - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
