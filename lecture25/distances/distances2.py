from collections import deque


def distances(graph: dict, start):
    gray_and_black = set()
    q = deque()
    d = {v: None for v in graph}

    d[start] = 0
    q.append(start)
    gray_and_black.add(start)
    while q:
        current = q.popleft()

        for n in graph[current]:
            if n not in gray_and_black:
                q.append(n)
                d[n] = d[current] + 1
                gray_and_black.add(n)

    return d
