from collections import deque


def distances5(G: dict, start) -> dict:
    q = deque()
    q.append(start)
    result = dict()
    result[start] = 0

    while q:
        vertex = q.popleft()

        for neighbor in G[vertex]:
            if neighbor not in result:
                result[neighbor] = 1 + result[vertex]
                q.append(neighbor)

    return result
