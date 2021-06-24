class My_stack():
    def __init__(self):
        self.stack = []

    def empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def clear(self):
        self.stack.clear()


def brace_sequence4(string: str) -> bool:
    b1o = '('
    b2o = '['
    b1c = ')'
    b2c = ']'

    stack = My_stack()
    for s in string:
        if s in (b1o, b2o, b1c, b2c):
            if s in (b1c, b2c):
                if stack.empty():
                    return False
                if s == b1c and stack.pop() != b1o:
                    return False
                if s == b2c and stack.pop() != b2o:
                    return False
                continue
            stack.push(s)

    return stack.empty()
