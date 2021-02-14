def adjacency_lists_compact_storage(vs: list, ls: list):
    indexes = [0] * (len(vs) + 1)
    length = 0
    for k in range(len(ls)):
        length += len(ls[k])

    lists = [0] * length

    index = 0
    for k in range(len(ls)):
        indexes[k] = index
        for i in range(len(ls[k])):
            lists[index] = ls[k][i]
            index += 1

    indexes[len(vs)] = index

    return vs, indexes, lists