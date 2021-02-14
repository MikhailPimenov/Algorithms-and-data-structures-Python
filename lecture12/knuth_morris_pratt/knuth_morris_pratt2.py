from lecture12.p_function.p_function2 import p_function


def knuth_morris_pratt(string: list, substring: list):
    if not len(string) or not len(substring):
        return -1
    super_string = substring[:]
    super_string.append('#')
    super_string += string

    p_array = p_function(super_string)

    for index in range(len(super_string)):
        if p_array[index] == len(substring):
            return index - 2 * len(substring)
    return -1
