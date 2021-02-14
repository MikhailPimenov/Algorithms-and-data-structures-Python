from collections import deque


def horse(start, finish):
    graph = create_graph()
    path = path_from_to(graph, start, finish)
    return path


def create_graph():
    letters = "abcdefgh"
    numbers = "12345678"
    graph = dict()

    for i in range(len(letters)):
        for j in range(len(numbers)):
            graph[letters[i] + numbers[j]] = set()

    for i in range(len(letters)):
        for j in range(len(numbers)):
            if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
                add_edge(graph, letters[i] + numbers[j], letters[i + 2] + numbers[j + 1])
                add_edge(graph, letters[i + 2] + numbers[j + 1], letters[i] + numbers[j])
            if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
                add_edge(graph, letters[i] + numbers[j], letters[i + 1] + numbers[j + 2])
                add_edge(graph, letters[i + 1] + numbers[j + 2], letters[i] + numbers[j])
            if 0 <= i - 2 < 8 and 0 <= j - 1 < 8:
                add_edge(graph, letters[i] + numbers[j], letters[i - 2] + numbers[j - 1])
                add_edge(graph, letters[i - 2] + numbers[j - 1], letters[i] + numbers[j])
            if 0 <= i - 1 < 8 and 0 <= j - 2 < 8:
                add_edge(graph, letters[i] + numbers[j], letters[i - 1] + numbers[j - 2])
                add_edge(graph, letters[i - 1] + numbers[j - 2], letters[i] + numbers[j])
            if 0 <= i + 2 < 8 and 0 <= j - 1 < 8:
                add_edge(graph, letters[i] + numbers[j], letters[i + 2] + numbers[j - 1])
                add_edge(graph, letters[i + 2] + numbers[j - 1], letters[i] + numbers[j])
            if 0 <= i + 1 < 8 and 0 <= j - 2 < 8:
                add_edge(graph, letters[i] + numbers[j], letters[i + 1] + numbers[j - 2])
                add_edge(graph, letters[i + 1] + numbers[j - 2], letters[i] + numbers[j])
            if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
                add_edge(graph, letters[i] + numbers[j], letters[i - 2] + numbers[j + 1])
                add_edge(graph, letters[i - 2] + numbers[j + 1], letters[i] + numbers[j])
            if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
                add_edge(graph, letters[i] + numbers[j], letters[i - 1] + numbers[j + 2])
                add_edge(graph, letters[i - 1] + numbers[j + 2], letters[i] + numbers[j])

    return graph


def add_edge(graph: dict, vertex1, vertex2):
    graph[vertex1].add(vertex2)


def path_from_to(graph: dict, start, finish):
    distances = dict()
    gray_and_black = set()
    queue = deque()

    distances[start] = 0
    gray_and_black.add(start)
    queue.append(start)

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

    path = [finish]
    current = finish

    while current != start:
        for neighbor in graph[current]:
            if neighbor in gray_and_black:
                if distances[neighbor] == distances[current] - 1:
                    path.append(neighbor)
                    current = neighbor
                    break
    path.reverse()

    return path
