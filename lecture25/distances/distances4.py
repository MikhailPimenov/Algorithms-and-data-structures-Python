from collections import deque


def distances4(g: dict, start) -> dict:
    q = deque()
    q.append(start)
    d = dict()
    d[start] = 0

    while q:
        vertex = q.popleft()
        for neighbor in g[vertex]:
            if neighbor not in d:
                d[neighbor] = 1 + d[vertex]
                q.append(neighbor)

    for vertex in g:
        if vertex not in d:
            d[vertex] = None
            
    return d
