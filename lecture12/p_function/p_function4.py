def p_function4(a: str) -> list:
    p_array = [None] * len(a)
    p_array[0] = 0

    for i in range(1, len(a)):
        p_index = p_array[i - 1]

        while True:
            if a[i] == a[p_index]:
                p_array[i] = p_index + 1
                break
            if not p_index:
                p_array[i] = 0
                break
            p_index = p_array[p_index - 1]

    return p_array
