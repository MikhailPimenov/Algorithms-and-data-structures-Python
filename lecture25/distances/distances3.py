from collections import deque

def distances3(graph:dict, start_vertex):
    q = deque()
    q.append(start_vertex)
    distances = dict()
    distances[start_vertex] = 0

    while q:
        vertex = q.popleft()

        for neighbor in graph[vertex]:
            if neighbor not in distances:
                distances[neighbor] = distances[vertex] + 1
                q.append(neighbor)

    return distances