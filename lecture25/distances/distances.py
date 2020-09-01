from collections import deque


def distances(adjacency_lists: dict, vertex) -> dict:
    result = {v: None for v in adjacency_lists}
    result[vertex] = 0

    queue = deque()
    queue.append(vertex)

    while len(queue) > 0:
        current_vertex = queue.popleft()

        for neighbor in adjacency_lists[current_vertex]:
            if result[neighbor] is None:
                result[neighbor] = result[current_vertex] + 1
                queue.append(neighbor)

    return result