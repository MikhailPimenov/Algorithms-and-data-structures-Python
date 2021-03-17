def adjacency_lists_compact_storage3(vertexes: tuple, lists: tuple):
    length = 0
    for k in range(len(lists)):
        length += len(lists[k])
    lists_compact = [None] * length

    indexes = [None] * (len(vertexes) + 1)
    index = 0
    indexes[0] = index

    for k in range(len(lists)):
        for j in range(len(lists[k])):
            lists_compact[index] = lists[k][j]
            index += 1
        indexes[k + 1] = index

    return vertexes, indexes, lists_compact
