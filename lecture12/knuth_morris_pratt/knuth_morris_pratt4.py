from lecture12.p_function.p_function4 import p_function4 as p_function


def decorator_adapter(wrappee):
    def wrapper(s: str, ss: str):
        if type(s) == list:
            s = ''.join(s)
        if type(ss) == list:
            ss = ''.join(ss)
        return wrappee(s, ss)

    return wrapper


@decorator_adapter
def knuth_morris_pratt4(s: str, ss: str) -> int:
    if not len(ss) or not len(s) or len(s) < len(ss):
        return -1

    long_string = ss + '#' + s
    p_array = p_function(long_string)

    for i in range(2 * len(ss), len(long_string)):
        if p_array[i] == len(ss):
            return i - 2 * len(ss)

    return -1
