def p_function3(array: list):
    p_array = [None] * len(array)
    p_array[0] = 0

    for i in range(1, len(array)):
        p_index = p_array[i - 1]
        while True:
            if array[i] == array[p_index]:
                p_array[i] = p_index + 1
                break
            else:
                if p_index == 0:
                    p_array[i] = 0
                    break
                p_index = p_array[p_index]

    return p_array
