def find(container: list, element) -> int:
    for i in range(len(container)):
        if container[i] == element:
            return i
    return -1


def list_to_dict_replacer(wrappee):
    def wrapper(*args, **kwargs):
        vertexes, indexes, matrix = wrappee(*args, **kwargs)

        indexes = {vertexes[i]: indexes[i] for i in range(len(vertexes))}

        return vertexes, indexes, matrix

    return wrapper


@list_to_dict_replacer
def adjacency_matrix4() -> tuple:
    n, k = map(int, input("Enter the number of vertexes and edges:").split())

    vertexes = []
    indexes = []
    matrix = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(k):
        v1, v2 = input("Enter the edge:").split()

        i1 = find(vertexes, v1)
        if i1 == -1:
            vertexes.append(v1)
            indexes.append(len(vertexes))
            i1 = indexes[len(vertexes) - 1]
        else:
            i1 = indexes[i1]

        i2 = find(vertexes, v2)
        if i2 == -1:
            vertexes.append(v2)
            indexes.append(len(vertexes))
            i2 = indexes[len(vertexes) - 1]
        else:
            i2 = indexes[i2]

        matrix[i1][i2] += 1
        matrix[i2][i1] += 1

    return vertexes, indexes, matrix
