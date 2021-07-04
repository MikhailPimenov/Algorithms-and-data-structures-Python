from collections import deque


def chess_knight_path5(start, finish) -> tuple:
    G = create_graph()
    q = deque()
    d = {}
    q.append(start)
    d[start] = 0
    found = False

    while q and not found:
        vertex = q.popleft()
        for n in G[vertex]:
            if n not in d:
                d[n] = d[vertex] + 1
                if n == finish:
                    found = True
                    break
                q.append(n)

    if not found:
        return tuple()

    path = [None] * (d[finish] + 1)
    path[len(path) - 1] = finish
    k = len(path) - 2
    vertex = finish

    while vertex != start:
        for n in G[vertex]:
            if n in d and d[n] == d[vertex] - 1:
                path[k] = n
                k -= 1

                if n == start:
                    return path

                vertex = n
                break


def add_edge(G: dict, i1: int, j1: int, i2: int, j2: int):
    letters = "abcdefgh"
    numbers = "12345678"
    G[letters[i1] + numbers[j1]].add(letters[i2] + numbers[j2])


def add_vertex(G: dict, i: int, j: int):
    letters = "abcdefgh"
    numbers = "12345678"

    if letters[i] + numbers[j] not in G:
        G[letters[i] + numbers[j]] = set()


def create_graph() -> dict:
    G = {}

    for i in range(8):
        for j in range(8):
            add_vertex(G, i, j)

    for i in range(8):
        for j in range(8):
            if i + 2 < 8 and j + 1 < 8:
                add_edge(G, i + 2, j + 1, i, j)
                add_edge(G, i, j, i + 2, j + 1)

            if i + 1 < 8 and j + 2 < 8:
                add_edge(G, i + 1, j + 2, i, j)
                add_edge(G, i, j, i + 1, j + 2)

            if i - 2 >= 0 and j - 1 >= 0:
                add_edge(G, i - 2, j - 1, i, j)
                add_edge(G, i, j, i - 2, j - 1)

            if i - 1 >= 0 and j - 2 >= 0:
                add_edge(G, i - 1, j - 2, i, j)
                add_edge(G, i, j, i - 1, j - 2)

            if i + 2 < 8 and j - 1 >= 0:
                add_edge(G, i + 2, j - 1, i, j)
                add_edge(G, i, j, i + 2, j - 1)

            if i + 1 < 8 and j - 2 >= 0:
                add_edge(G, i + 1, j - 2, i, j)
                add_edge(G, i, j, i + 1, j - 2)

            if i - 2 >= 0 and j + 1 < 8:
                add_edge(G, i - 2, j + 1, i, j)
                add_edge(G, i, j, i - 2, j + 1)

            if i - 1 >= 0 and j + 2 < 8:
                add_edge(G, i - 1, j + 2, i, j)
                add_edge(G, i, j, i - 1, j + 2)

    return G
