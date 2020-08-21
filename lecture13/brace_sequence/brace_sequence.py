from lecture13 import my_stack as stack


def brace_sequence(sequence: str):
    stk = stack
    stk.clear()

    b1o = '('
    b1c = ')'
    b2o = '['
    b2c = ']'

    for brace in sequence:
        if brace not in [b1o, b1c, b2o, b2c]:
            continue
        if brace in [b1o, b2o]:
            stk.push(brace)
        else:
            if stk.empty():
                return False
            else:
                if brace == b1c:
                    if stk.top() == b1o:
                        stk.pop()
                    else:
                        return False
                else: # brace == b2c
                    if stk.top() == b2o:
                        stk.pop()
                    else:
                        return False

    return stk.empty()
