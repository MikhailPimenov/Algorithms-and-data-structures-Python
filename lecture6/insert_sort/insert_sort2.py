def insert_sort(array: list):
    for i2 in range(1, len(array)):
        for i1 in range(i2 - 1, -1, -1):
            if array[i1] > array[i2]:
                array[i1], array[i2] = array[i2], array[i1]
                i2 = i1
            else:
                break
