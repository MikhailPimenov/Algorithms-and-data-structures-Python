from ..p_function.p_function3 import p_function3


def knuth_morris_pratt3(array: list, subarray: list):
    superarray = subarray[:]
    superarray.append('#')
    superarray = superarray[:] + array[:]

    p_array = p_function3(superarray)
    for i in range(2 * len(subarray), len(superarray)):
        if p_array[i] == len(subarray):
            return i - 2 * len(subarray)

    return -1