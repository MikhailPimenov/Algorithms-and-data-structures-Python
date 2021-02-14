from collections import deque


def path(graph:dict, start, finish):
    gray_and_black = set()
    queue = deque()
    distances = dict()

    gray_and_black.add(start)
    queue.append(start)
    distances[start] = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in gray_and_black:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
                gray_and_black.add(neighbor)
                if neighbor == finish:
                    queue.clear()
                    break

    path_to = [finish]
    current = finish
    while current != start:
        for neighbor in graph[current]:
            if neighbor in gray_and_black:
                if distances[neighbor] == distances[current] - 1:
                    path_to.append(neighbor)
                    current = neighbor
                    break

    path_to.reverse()

    return path_to
