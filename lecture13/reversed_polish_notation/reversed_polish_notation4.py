def reversed_polish_notation4(ss: list) -> int:
    stack = []

    for s in ss:
        if s in ('+', '-', '*', '/'):
            second = stack.pop()
            first = stack.pop()

            if s == '+':
                result = first + second
            elif s == '-':
                result = first - second
            elif s == '*':
                result = first * second
            else:
                if second:
                    result = first // second
                else:
                    raise ZeroDivisionError
            stack.append(result)
            continue
        stack.append(s)

    return stack[-1]
