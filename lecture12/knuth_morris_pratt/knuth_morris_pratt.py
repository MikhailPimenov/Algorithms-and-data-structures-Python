from lecture12.p_function.p_function import p_function


def knuth_morris_pratt(string: list, substring: list):
    if len(string) == 0 or len(substring) == 0:
        return -1

    super_string = substring + ['#'] + string
    p_array = p_function(super_string)

    for index in range(len(super_string)):
        if len(substring) == p_array[index]:
            return index - 2 * len(substring)

    return -1
