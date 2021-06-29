from lecture12.p_function.p_function5 import p_function5 as p_function


def knuth_morris_pratt5_adapter(wrappee):
    def wrapper(string: list, substring: list, *args, **kwargs):
        return wrappee("".join(string), "".join(substring), *args, **kwargs)

    return wrapper


@knuth_morris_pratt5_adapter
def knuth_morris_pratt5(s: str, ss: str) -> int:
    if not s and not ss:
        return -1

    ls = ss + '#' + s
    p = p_function(ls)

    for i in range(2 * len(ss), len(ls)):
        if p[i] == len(ss):
            return i - 2 * len(ss)

    return -1
