def adjacency_lists5() -> dict:
    n, m = map(int, input("Enter the number of vertexes and edges:").split())

    graph = {}

    for _ in range(m):
        v1, v2 = input("Enter the edge:").split()

        for v in v1, v2:
            if v not in graph:
                graph[v] = set()

        graph[v1].add(v2)
        graph[v2].add(v1)

    return graph
