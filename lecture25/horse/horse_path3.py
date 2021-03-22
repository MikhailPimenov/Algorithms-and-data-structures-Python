from collections import deque


def add_vertex(graph: dict, letters: str, numbers: str, letter_index: int, number_index: int):
    graph[letters[letter_index] + numbers[number_index]] = set()


def add_edge(graph: dict, letters: str, numbers: str, letter_index1: int, number_index1: int,
             letter_index2: int, number_index2: int):
    graph[letters[letter_index1] + numbers[number_index1]].add(
        letters[letter_index2] + numbers[number_index2]
    )
    graph[letters[letter_index2] + numbers[number_index2]].add(
        letters[letter_index1] + numbers[number_index1]
    )


def create_graph():
    letters = "abcdefgh"
    numbers = "12345678"

    g = dict()
    for l in range(len(letters)):
        for n in range(len(numbers)):
            add_vertex(g, letters, numbers, l, n)

    for l in range(len(letters)):
        for n in range(len(numbers)):
            if l + 2 < len(letters) and n + 1 < len(numbers):
                add_edge(g, letters, numbers, l + 2, n + 1, l, n)
            if l + 1 < len(letters) and n + 2 < len(numbers):
                add_edge(g, letters, numbers, l + 1, n + 2, l, n)
            if l - 2 >= 0 and n - 1 >= 0:
                add_edge(g, letters, numbers, l - 2, n - 1, l, n)
            if l - 1 >= 0 and n - 2 >= 0:
                add_edge(g, letters, numbers, l - 1, n - 2, l, n)
            if l + 2 < len(letters) and n - 1 >= 0:
                add_edge(g, letters, numbers, l + 2, n - 1, l, n)
            if l + 1 < len(letters) and n - 2 >= 0:
                add_edge(g, letters, numbers, l + 1, n - 2, l, n)
            if l - 2 >= 0 and n + 1 < len(numbers):
                add_edge(g, letters, numbers, l - 2, n + 1, l, n)
            if l - 1 >= 0 and n + 2 < len(numbers):
                add_edge(g, letters, numbers, l - 1, n + 2, l, n)
    return g


def horse_path3(start, finish):
    g = create_graph()

    q = deque()
    q.append(start)
    distances = dict()
    distances[start] = 0
    stop_flag = False

    while q and not stop_flag:
        vertex = q.popleft()

        for neighbor in g[vertex]:
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                q.append(neighbor)
                if neighbor == finish:
                    stop_flag = True

    if not stop_flag:
        return []

    path = [None] * (distances[finish] + 1)
    path[distances[finish]] = finish
    index = distances[finish] - 1

    vertex = finish
    while vertex != start:
        for neighbor in g[vertex]:
            if neighbor in distances and distances[neighbor] == distances[vertex] - 1:
                path[index] = neighbor
                index -= 1
                vertex = neighbor
                break

    return path
