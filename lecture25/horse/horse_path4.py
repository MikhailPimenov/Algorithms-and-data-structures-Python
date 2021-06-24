from collections import deque


def set_vertex(i: int, j: int):
    letters = "abcdefgh"
    numbers = "12345678"
    return letters[i] + numbers[j]


def add_vertex(g: dict, i: int, j: int):
    v = set_vertex(i, j)
    g[v] = set()


def add_edge(g: dict, i1: int, j1: int, i2: int, j2: int):
    v1 = set_vertex(i1, j1)
    v2 = set_vertex(i2, j2)

    g[v1].add(v2)
    g[v2].add(v1)


def create_graph() -> dict:
    g = dict()
    for i in range(8):
        for j in range(8):
            add_vertex(g, i, j)

    for i in range(8):
        for j in range(8):
            if i + 2 < 8 and j + 1 < 8:
                add_edge(g, i, j, i + 2, j + 1)
            if i + 1 < 8 and j + 2 < 8:
                add_edge(g, i, j, i + 1, j + 2)
            if i - 2 >= 0 and j - 1 >= 0:
                add_edge(g, i, j, i - 2, j - 1)
            if i - 1 >= 0 and j - 2 >= 0:
                add_edge(g, i, j, i - 1, j - 2)
            if i + 2 < 8 and j - 1 >= 0:
                add_edge(g, i, j, i + 2, j - 1)
            if i + 1 < 8 and j - 2 >= 0:
                add_edge(g, i, j, i + 1, j - 2)
            if i - 2 >= 0 and j + 1 < 8:
                add_edge(g, i, j, i - 2, j + 1)
            if i - 1 >= 0 and j + 2 < 8:
                add_edge(g, i, j, i - 1, j + 2)
    return g


def horse_path4(start: str, finish: str) -> list:
    g = create_graph()

    q = deque()
    q.append(start)

    d = dict()
    d[start] = 0
    finish_is_found = False
    while q and not finish_is_found:
        vertex = q.popleft()
        for neighbor in g[vertex]:
            if neighbor not in d:
                d[neighbor] = d[vertex] + 1
                q.append(neighbor)
                if neighbor == finish:
                    finish_is_found = True
                    break

    if not finish_is_found:
        return []

    path = [None] * (d[finish] + 1)
    i = d[finish]
    path[i] = finish
    i -= 1
    vertex = finish
    while vertex != start:
        for neighbor in g[vertex]:
            if neighbor in d and d[neighbor] == d[vertex] - 1:
                path[i] = neighbor
                i -= 1
                vertex = neighbor
                break

    return path


