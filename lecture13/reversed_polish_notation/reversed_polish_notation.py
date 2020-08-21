from lecture13 import my_stack as stack


def reversed_polish_notation(notation: list):
    stk = stack
    stk.clear()

    for symbol in notation:
        if symbol not in ['+', '-', '*', '/']:
            stk.push(symbol)
        else:
            y = stk.pop()
            x = stk.pop()
            if symbol == '+':
                result = x + y
            elif symbol == '-':
                result = x - y
            elif symbol == '*':
                result = x * y
            else:
                if y != 0:
                    result = x / y
                else:
                    result = 0
            stk.push(result)

    return stk.pop()
