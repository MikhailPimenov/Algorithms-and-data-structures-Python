from collections import deque


def inf_to_none_replacer_decorator(wrappee):
    def wrapper(*args, **kwargs):
        distances = wrappee(*args, **kwargs)
        for vertex in distances:
            if distances[vertex] == float("+inf"):
                distances[vertex] = None
        return distances

    return wrapper


@inf_to_none_replacer_decorator
def dijkstra3(graph: dict, start):
    q = deque()
    q.append(start)
    distances = {vertex: float("+inf") for vertex in graph}
    distances[start] = 0

    while q:
        vertex = q.popleft()
        for neighbor in graph[vertex]:
            if distances[vertex] + graph[vertex][neighbor] < distances[neighbor]:
                distances[neighbor] = distances[vertex] + graph[vertex][neighbor]
                q.append(neighbor)

    return distances
