def floyd_uolsher(graph: dict):
    d0 = {v1: {v2: graph[v1][v2]
    if v2 in graph[v1] else
    float("+inf") for v2 in graph} for v1 in graph}

    for v in d0:
        d0[v][v] = 0

    number = 0
    v = dict()
    for vertex in graph:
        v[number] = vertex
        number += 1

    d = [d0, d0]

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if i == j:
                    d[k % 2][v[i]][v[j]] = 0
                else:
                    d[k % 2][v[i]][v[j]] = min(d[(k - 1) % 2][v[i]][v[j]],
                                               d[(k - 1) % 2][v[i]][v[k]] + d[(k - 1) % 2][v[k]][v[j]])

    return d[(len(graph) - 1) % 2]
