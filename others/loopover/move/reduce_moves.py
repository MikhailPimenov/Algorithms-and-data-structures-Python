class Stack:
    """
    Classic implementation of stack.
    """
    def __init__(self):
        self.stack = []

    def push_back(self, element):
        self.stack.append(element)

    def pop_back(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def __bool__(self):
        return not not len(self.stack)


def opposite(move: str) -> str:
    """
    Returns opposite step. For example for 'D0' opposite step is 'U0',
    for 'R7' opposite step is 'L7', for 'U4' opposite step is 'D4' and so on.
    :param move: str - move to find opposite step (move) for.
    :return: str - opposite step.
    """
    if move[0] == 'U':
        return f'D{move[1:]}'
    if move[0] == 'D':
        return f'U{move[1:]}'
    if move[0] == 'L':
        return f'R{move[1:]}'
    if move[0] == 'R':
        return f'L{move[1:]}'


def reduce_moves(moves: list) -> list:
    """
    Returns list of moves without opposite steps which cancel each other.
    New list if fully equivalent but can be shorter.
    :param moves: list to find equivalent perhaps shorter moves for.
    :return: list - equivalent but shorter list of moves.
    """
    stack = Stack()

    for move in moves:
        if stack and stack.top() == opposite(move):
            stack.pop_back()
            continue
        stack.push_back(move)

    return stack.stack



