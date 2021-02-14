def p_function(string: str):
    p_array = [0] * len(string)
    if len(string) == 1:
        return p_array

    p_array[1] = (1 if string[1] == string[0] else 0)

    for index in range(2, len(string)):
        p_index = index - 1
        while True:
            if string[index] == string[p_array[p_index]]:
                p_array[index] = p_array[p_index] + 1
                break
            else:
                p_index = p_array[p_index]
            if not p_index:
                if string[index] == string[0]:
                    p_array[index] = 1
                else:
                    p_array[index] = 0
                break
    return p_array
