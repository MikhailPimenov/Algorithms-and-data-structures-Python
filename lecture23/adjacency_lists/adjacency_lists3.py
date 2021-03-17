def adjacency_lists3():
    m, n = map(int, input("Enter the number of vertexes "
                          "and the number of edges: ").split())

    adjacency_lists = {}

    for _ in range(n):
        v1, v2 = input("Enter the edge: ").split()

        for v in v1, v2:
            if v not in adjacency_lists:
                adjacency_lists[v] = set()

        adjacency_lists[v1].add(v2)
        adjacency_lists[v2].add(v1)

    return adjacency_lists