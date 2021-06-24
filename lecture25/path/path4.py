from collections import deque


def path4(g: dict, start, finish) -> list:
    q = deque()
    q.append(start)
    d = dict()
    d[start] = 0
    vertex = start

    while q:
        vertex = q.popleft()
        for neighbor in g[vertex]:
            if neighbor not in d:
                d[neighbor] = 1 + d[vertex]
                q.append(neighbor)
                if neighbor == finish:
                    vertex = finish
                    q.clear()
                    break

    if vertex != finish:
        return []

    p = [None] * (d[finish] + 1)
    i = d[finish]
    p[i] = finish
    i -= 1
    vertex = finish

    while vertex != start:
        for neighbor in g[vertex]:
            if neighbor in d and d[neighbor] == d[vertex] - 1:
                p[i] = neighbor
                i -= 1
                vertex = neighbor
                break

    return p
