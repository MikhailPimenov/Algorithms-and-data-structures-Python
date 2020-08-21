_stack = []

def push(element):
    _stack.append(element)


def pop():
    return _stack.pop()


def top():
    return _stack[-1]


def empty():
    return len(_stack) == 0


def clear():
    _stack.clear()