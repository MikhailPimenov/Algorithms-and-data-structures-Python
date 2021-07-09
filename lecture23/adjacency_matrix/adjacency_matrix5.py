def adjacency_matrix5_adapter(wrappee):
    def wrapper(*args, **kwargs):
        vertexes, indexes, matrix = wrappee(*args, **kwargs)

        indexes = {vertexes[i]: indexes[i] for i in range(len(vertexes))}

        return vertexes, indexes, matrix

    return wrapper


@adjacency_matrix5_adapter
def adjacency_matrix5() -> tuple:
    n, m = map(int, input("Enter the number of vertexes and edges:").split())

    matrix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    indexes = [0] * n
    vertexes = [None] * n

    v_index = 0
    for _ in range(m):
        v1, v2 = input("Enter the edge:").split()

        v1_index_in_vertexes = find(vertexes, v1)
        if v1_index_in_vertexes == -1:
            vertexes[v_index] = v1
            indexes[v_index] = v_index + 1
            v1_index_in_vertexes = v_index
            v_index += 1

        v2_index_in_vertexes = find(vertexes, v2)
        if v2_index_in_vertexes == -1:
            vertexes[v_index] = v2
            indexes[v_index] = v_index + 1
            v2_index_in_vertexes = v_index
            v_index += 1

        v1_index = indexes[v1_index_in_vertexes]
        v2_index = indexes[v2_index_in_vertexes]

        matrix[v1_index][v2_index] += 1
        matrix[v2_index][v1_index] += 1

    return vertexes, indexes, matrix


def find(source: list, item) -> int:
    for i in range(len(source)):
        if source[i] == item:
            return i
    return -1
