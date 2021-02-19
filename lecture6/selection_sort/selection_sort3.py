def selection_sort3(array: list):
    for i1 in range(len(array)):
        index_of_max = 0
        for i2 in range(1, len(array) - i1):
            if array[i2] > array[index_of_max]:
                index_of_max = i2
        array[len(array) - 1 - i1], array[index_of_max] \
            = array[index_of_max], array[len(array) - 1 - i1]
