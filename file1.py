# lecture 24 part 2 of 3
# graphs
# depth_first_search
# kosaraju (strongly_connected_components)


def reverse_graph(adjacency_list: dict):
    reversed_adjacency_list = {k: set() for k in adjacency_list}

    for vertex in adjacency_list:
        for neighbour in adjacency_list[vertex]:
            reversed_adjacency_list[neighbour].add(vertex)

    return reversed_adjacency_list


def depth_first_search(vertex, adjacency_list: dict, component: set, in_use: set, used: list, first_pass: bool = True):
    in_use.add(vertex)
    if not first_pass:
        component.add(vertex)

    for neighbour in adjacency_list[vertex]:
        if neighbour not in in_use:
            depth_first_search(neighbour, adjacency_list, component, in_use, used, first_pass)

    if first_pass:
        used.append(vertex)


def kosaraju(adjacency_list: dict):
    in_use = set()
    used = []

    for vertex in adjacency_list:
        if vertex not in in_use:
            depth_first_search(vertex, adjacency_list, set(), in_use, used, True)

    reversed_adjacency_list = reverse_graph(adjacency_list)

    in_use.clear()
    components = []
    for k in range(len(adjacency_list)):
        vertex = used.pop()

        if vertex not in in_use:
            component = set()
            depth_first_search(vertex, reversed_adjacency_list, component, in_use, used, False)
            components.append(component)

    return components


def test_reverse(algorithm):
    print("testing reverse_graph:")

    adjacency_list = {'A': {'B'},
                      'B': {'C', 'D'},
                      'C': {'A'},
                      'D': {'E'},
                      'E': {'F'},
                      'F': {'D'},
                      'G': {'F', 'H'},
                      'H': {'I'},
                      'I': {'M'},
                      'M': {'G'},
                      'K': {'M'}, }

    reversed_adjacency_list = {'A': {'C'},
                               'B': {'A'},
                               'C': {'B'},
                               'D': {'B', 'F'},
                               'E': {'D'},
                               'F': {'E', 'G'},
                               'G': {'M'},
                               'H': {'G'},
                               'I': {'H'},
                               'M': {'I', 'K'},
                               'K': set(), }

    result = algorithm(adjacency_list)
    print("test #1:", "ok" if result == reversed_adjacency_list else "FAILED")

    result = algorithm(reversed_adjacency_list)
    print("test #2:", "ok" if result == adjacency_list else "FAILED")


def test_kosaraju(algorithm):
    print("testing kosaraju:")

    adjacency_list = {'A': {'B'},
                      'B': {'C', 'D'},
                      'C': {'A'},
                      'D': {'E'},
                      'E': {'F'},
                      'F': {'D'},
                      'G': {'F', 'H'},
                      'H': {'I'},
                      'I': {'M'},
                      'M': {'G'},
                      'K': {'M'}, }

    components1 = [{'K'}, {'G', 'M', 'I', 'H'}, {'A', 'B', 'C'}, {'D', 'F', 'E'}]
    components2 = algorithm(adjacency_list)

    success = True
    for element in components2:
        if element not in components1:
            success = False
            break

    print("test #1:", "ok" if success else "FAILED")


test_reverse(reverse_graph)
test_kosaraju(kosaraju)
