def selection_sort(array: list):
    for i in range(len(array) - 1):
        min_index = i
        for s_i in range(i, len(array)):
            if array[s_i] < array[min_index]:
                min_index = s_i
        array[min_index], array[i] = array[i], array[min_index]



