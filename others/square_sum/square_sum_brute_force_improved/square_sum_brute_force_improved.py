import math
import time
from math import sqrt, floor
from functools import cache


@cache
def is_perfect_square(a: int, b: int) -> bool:
    return not (a + b) ** 0.5 % 1


@cache
def get_neighbor_lists(n: int) -> dict:
    lists = {i: set() for i in range(1, n + 1)}
    max_square = 2 * n - 1

    squares = {i * i for i in range(floor(sqrt(max_square)) + 1)}

    for number in lists:
        for square in squares:
            if square > number and square - number < n + 1 and square - number != number:
                lists[number].add(square - number)

    return lists


def permutation_generator(neighbors: dict, prefix: list, deep: int, used: set) -> list:
    if not deep:
        yield prefix
        return

    previous_number = prefix[-1]
    for neighbor in neighbors[previous_number]:
        # print(prefix[-1])
        if neighbor not in used:
            prefix.append(neighbor)
            # print(prefix)
            used.add(neighbor)
            yield from permutation_generator(neighbors, prefix, deep - 1, used)
            used.remove(neighbor)
            prefix.pop()


def square_sums_row(n: int):
    numbers = [i for i in range(1, n + 1)]
    start = time.time()
    neighbors = get_neighbor_lists(n)
    end = time.time()
    # print("neighbors calculated:", end - start)
    prefix = []
    used = set()

    for first_number in range(1, (n + 1)):
        # print('first number:', first_number)
        prefix.append(first_number)
        used.add(first_number)
        for permutation in permutation_generator(neighbors, prefix, n - 1, used):
            return permutation
        used.remove(first_number)
        prefix.pop()
    return False


global_start = time.time()
for n in range(1, 60):
    start = time.time()
    print(n, square_sums_row(n))  # 47 for debugging
    end = time.time()
    print(end - start)

global_end = time.time()
print(global_end - global_start)
# print(get_neighbor_lists(21))
