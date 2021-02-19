def bubble_sort3(array: list):
    for index1 in range(len(array) - 1):
        go_on = False
        for index2 in range(len(array) - 1 - index1):
            if array[index2] > array[index2 + 1]:
                go_on = True
                array[index2], array[index2 + 1] = array[index2 + 1], array[index2]
        if not go_on:
            break
