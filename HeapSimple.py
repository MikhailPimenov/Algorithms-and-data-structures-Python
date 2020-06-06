# lecture 19 module
# class heap
# heap_sort


class HeapSimple:
    def __init__(self, array: list = None):
        self.values = array[:]
        self.length = len(array)

        for i in range(len(array) // 2 - 1, -1, -1):
            self.sift_down(i)

    def sift_up(self, i):
        while i > 0 and self.values[i] < self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]
            i = (i - 1) // 2

    def sift_down(self, i):
        while 2 * i + 1 < self.length:
            j = i
            if 2 * i + 2 < self.length and self.values[2 * i + 2] < self.values[2 * i + 1]:
                if self.values[i] > self.values[2 * i + 2]:
                    j = 2 * i + 2
            else:
                if self.values[i] > self.values[2 * i + 1]:
                    j = 2 * i + 1
            if j == i:
                return
            else:
                self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j

    def insert(self, element):
        self.values.append(element)
        self.length += 1
        self.sift_up(self.length - 1)

    def extract_min(self):
        assert self.length > 0, "Tried to extract from empty heap"

        result_to_return = self.values[0]

        new_first = self.values.pop()
        self.length -= 1
        if self.length > 0:
            self.values[0] = new_first
            self.sift_down(0)

        return result_to_return

