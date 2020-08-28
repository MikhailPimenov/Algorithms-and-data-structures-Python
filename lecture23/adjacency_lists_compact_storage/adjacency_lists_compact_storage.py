def adjacency_lists_compact_storage(vertexes: list, lists: list):
    compact_lists = []
    indexes = [0] * (len(vertexes) + 1)
    for k in range(len(vertexes)):
        for i in range(len(lists[k])):
            compact_lists.append(lists[k][i])
        indexes[k + 1] = (indexes[k] + len(lists[k]))

    return vertexes, indexes, compact_lists
