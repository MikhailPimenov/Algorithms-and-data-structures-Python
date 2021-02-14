def p_function(string: list):
    p_array = [0] * len(string)

    for index in range(1, len(string)):
        p_index = index - 1
        while True:
            if string[index] == string[p_array[p_index]]:
                p_array[index] = 1 + p_array[p_index]
                break
            if not p_index:
                break
            p_index = p_array[p_index]

    return p_array
