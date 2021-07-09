def brace_sequence5(ss: str) -> bool:
    b1o = '('
    b2o = '['
    b1c = ')'
    b2c = ']'

    stack = []

    for s in ss:
        if s in (b1o, b2o, b1c, b2c):
            if s in (b1c, b2c):
                if not stack:
                    return False
                if stack[-1] != b1o and s == b1c:
                    return False
                if stack[-1] != b2o and s == b2c:
                    return False
                stack.pop()
            else:
                stack.append(s)

    return len(stack) == 0
