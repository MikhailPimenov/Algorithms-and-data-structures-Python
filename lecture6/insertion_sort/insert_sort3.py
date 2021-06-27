def insert_sort3(array: list):
    for i1 in range(1, len(array)):
        for i2 in reversed(range(i1)):
            if array[i2] > array[i2 + 1]:
                array[i2], array[i2 + 1] = array[i2 + 1], array[i2]
            else:
                break
