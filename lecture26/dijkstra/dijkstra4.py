from collections import deque


def inf_to_none_replacer(wrappee):
    def wrapper(*args, **kwargs):
        distances = wrappee(*args, **kwargs)
        for vertex in distances:
            if distances[vertex] == float('+inf'):
                distances[vertex] = None

        return distances

    return wrapper


@inf_to_none_replacer
def dijkstra4(graph: dict, start_vertex) -> dict:
    queue = deque()
    queue.append(start_vertex)

    distances = {vertex: float('+inf') for vertex in graph}
    distances[start_vertex] = 0

    while queue:
        current_vertex = queue.popleft()
        for neighbor in graph[current_vertex]:
            if distances[current_vertex] + graph[current_vertex][neighbor] < distances[neighbor]:
                distances[neighbor] = distances[current_vertex] + graph[current_vertex][neighbor]
                queue.append(neighbor)

    return distances
