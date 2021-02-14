def adjacency_matrix():
    n, m = map(int, input().split())

    index_l = 0
    index = 1
    vertex_list = [0] * n
    vertex_indexes = {}
    matrix = [[0] * (n + 1) for k in range(n + 1)]

    for k in range(m):
        v1, v2 = input().split()

        for v in v1, v2:
            if v not in vertex_list:
                vertex_list[index_l] = v
                index_l += 1
            if v not in vertex_indexes:
                vertex_indexes[v] = index
                index += 1
        v1_i = vertex_indexes[v1]
        v2_i = vertex_indexes[v2]

        matrix[v1_i][v2_i] += 1
        matrix[v2_i][v1_i] += 1

    return vertex_list, vertex_indexes, matrix
