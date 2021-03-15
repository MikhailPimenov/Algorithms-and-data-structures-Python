from lecture13.my_stack3 import My_stack3


def reversed_polish_notation3(array: list):
    stack = My_stack3()

    for symbol in array:
        if symbol not in ('+', '-', '*', '/'):
            stack.push_back(symbol)
        else:
            result = 0
            n2 = stack.pop_back()
            n1 = stack.pop_back()

            if symbol == '+':
                result = n1 + n2
            elif symbol == '-':
                result = n1 - n2
            elif symbol == '*':
                result = n1 * n2
            else:
                if n2 != 0:
                    result = n1 // n2
                else:
                    print('divisor is zero')
            stack.push_back(result)

    return stack.top()
