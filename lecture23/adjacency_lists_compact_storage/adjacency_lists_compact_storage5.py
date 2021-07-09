def adjacency_lists_compact_storage5(vertexes: list, lists: list) -> tuple:
    start_index = 0
    compact_lists = []
    indexes = [0]

    for adjacency_list in lists:
        for neighbor in adjacency_list:
            compact_lists.append(neighbor)
            start_index += 1

        indexes.append(start_index)

    return vertexes, indexes, compact_lists
