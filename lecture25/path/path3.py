from collections import deque

def path3(graph:dict, start, finish):
    q = deque()
    q.append(start)
    distances = dict()
    distances[start] = 0

    stop_flag = False
    while q and not stop_flag:
        vertex = q.popleft()
        for neighbor in graph[vertex]:
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                q.append(neighbor)
                if neighbor == finish:
                    stop_flag = True
                    break

    if not stop_flag:
        return []

    path = [None] * (distances[finish] + 1)
    index = distances[finish]
    path[index] = finish
    index -= 1

    vertex = finish
    while vertex != start:
        for neighbor in graph[vertex]:
            if neighbor in distances and distances[neighbor] == distances[vertex] - 1:
                path[index] = neighbor
                index -= 1
                vertex = neighbor
                break

    return path
