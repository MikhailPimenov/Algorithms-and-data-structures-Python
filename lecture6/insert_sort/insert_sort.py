def insert_sort(array: list):
    for k in range(1, len(array)):
        i = k
        for j in range(k - 1, -1, -1):
            if array[i] < array[j]:
                array[i], array[j] = array[j], array[i]
                i -= 1
