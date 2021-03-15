from ..my_stack3 import My_stack3


def brace_sequence3(array: list):
    b1o = '('
    b1c = ')'
    b2o = '['
    b2c = ']'

    stack = My_stack3()

    for symbol in array:
        if symbol in (b1o, b1c, b2o, b2c):
            if symbol in (b1c, b2c):
                if symbol == b1c:
                    if stack.top() != b1o:
                        return False
                    else:
                        stack.pop_back()
                else:
                    if stack.top() != b2o:
                        return False
                    else:
                        stack.pop_back()
            else:
                stack.push_back(symbol)
    return stack.is_empty()
