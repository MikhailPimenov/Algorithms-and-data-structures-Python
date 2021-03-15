class My_stack3:
    def __init__(self):
        self.array = []

    def push_back(self, element):
        self.array.append(element)

    def pop_back(self):
        return self.array.pop()

    def top(self):
        if len(self.array) > 0:
            return self.array[-1]

    def is_empty(self):
        return len(self.array) == 0

    def clear(self):
        self.array.clear()