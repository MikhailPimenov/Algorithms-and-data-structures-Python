def reversed_polish_notation5(sequence: tuple) -> int:
    stack = []

    for s in sequence:
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
                if second == 0:
                    raise ZeroDivisionError
                result = first // second

            stack.append(result)
        else:
            stack.append(s)

    return stack.pop()
