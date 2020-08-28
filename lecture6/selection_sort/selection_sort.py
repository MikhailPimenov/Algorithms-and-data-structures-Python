def selection_sort(array: list):
    for current_index in range(len(array) - 1):
        min_index = current_index
        for search_index in range(current_index, len(array)):
            if array[search_index] < array[min_index]:
                min_index = search_index
        array[current_index], array[min_index] = array[min_index], array[current_index]
