def floyd_uolsher3(g: dict) -> dict:
    v = [None] * (len(g) + 1)

    index = 1
    for vertex in g:
        v[index] = vertex
        index += 1

    f = [{vertex: {vertex: None for vertex in g} for vertex in g} for _ in range(2)]

    index1 = 1
    for vertex1 in g:
        index2 = 1
        for vertex2 in g:
            if vertex2 in g[vertex1]:
                f[0][v[index1]][v[index2]] = g[vertex1][vertex2]
            else:
                f[0][v[index1]][v[index2]] = float("+inf")
            index2 += 1
        index1 += 1

    for i in range(1, len(g) + 1):
        f[0][v[i]][v[i]] = 0

    for k in range(1, len(g) + 1):
        for i in range(1, len(g) + 1):
            for j in range(1, len(g) + 1):
                f[k % 2][v[i]][v[j]] = min(f[(k - 1) % 2][v[i]][v[j]],
                                           f[(k - 1) % 2][v[i]][v[k]] + f[(k - 1) % 2][v[k]][v[j]])

    return f[len(g) % 2]
