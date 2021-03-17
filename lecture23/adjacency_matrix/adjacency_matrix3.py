def adjacency_matrix3():
    m, n = map(int, input("Enter number of vertexes and number of edges:").split())

    vertexes = {}
    matrix = [[0] * (m + 1) for _ in range(m + 1)]

    start_index = 1
    for _ in range(n):
        v1, v2 = input("Enter the edge:").split()

        for v in v1, v2:
            if v not in vertexes:
                vertexes[v] = start_index
                start_index += 1

        index1 = vertexes[v1]
        index2 = vertexes[v2]

        matrix[index1][index2] += 1
        matrix[index2][index1] += 1

    return list(vertexes.keys()), vertexes, matrix

