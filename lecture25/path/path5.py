from collections import deque


def path5(G: dict, start, finish) -> tuple:
    q = deque()
    q.append(start)
    distances = {}
    distances[start] = 0
    found = False

    while q and not found:
        vertex = q.popleft()
        for neighbor in G[vertex]:
            if neighbor not in distances:
                distances[neighbor] = 1 + distances[vertex]
                if neighbor == finish:
                    found = True
                    break
                q.append(neighbor)

    if not found:
        return tuple()

    vertex = finish
    path = [None] * (distances[finish] + 1)
    path[distances[finish]] = finish
    k = distances[finish] - 1

    while vertex != start:
        for neighbor in G[vertex]:
            if neighbor in distances and distances[neighbor] == distances[vertex] - 1:
                path[k] = neighbor
                k -= 1
                vertex = neighbor
                break

    return path
