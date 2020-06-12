# lecture 24 part 1 of 3
# graphs
# depth_first_search
# count


def depth_first_search(vertex, adjacency_list: dict, in_use: set):
    in_use.add(vertex)

    for neighbour in adjacency_list[vertex]:
        if neighbour not in in_use:
            depth_first_search(neighbour, adjacency_list, in_use)


def count(adjacency_list: dict) -> int:
    in_use = set()

    counter = 0
    for vertex in adjacency_list:
        if vertex not in in_use:
            counter += 1
            depth_first_search(vertex, adjacency_list, in_use)

    return counter


def test_depth_first_search(algorithm):
    adjacency_list = {'A': set(),
                      'B': set(),
                      'C': set(),
                      'D': set(),
                      'E': set(),
                      'F': set(),
                      'G': set(),
                      'H': set(),
                      'I': set(), }
    counter = algorithm(adjacency_list)
    print("test #0:", "ok" if counter == 9 else "FAILED")

    adjacency_list = {'A': {'B', 'D'},
                      'B': {'A', 'D', 'C'},
                      'C': {'B', 'D'},
                      'D': {'A', 'B', 'C'},
                      'E': {'F', 'G'},
                      'F': {'E', 'G'},
                      'G': {'F'}}
    counter = algorithm(adjacency_list)
    print("test #1:", "ok" if counter == 2 else "FAILED")

    adjacency_list = {'A': {'B', 'D'},
                      'B': {'A', 'D', 'C'},
                      'C': {'B', 'D'},
                      'D': {'A', 'B', 'C'},
                      'E': {'F', 'G'},
                      'F': {'E', 'G'},
                      'G': {'F'},
                      'H': {'I'},
                      'I': {'H'}}
    counter = algorithm(adjacency_list)
    print("test #2:", "ok" if counter == 3 else "FAILED")

    adjacency_list = {'A': {'B', 'D'},
                      'B': {'A', 'D', 'C'},
                      'C': {'B', 'D'},
                      'D': {'A', 'B', 'C'},
                      'E': {'F', 'G'},
                      'F': {'E', 'G'},
                      'G': {'F'},
                      'H': {'I'},
                      'I': {'H'},
                      'P': {'Q'},
                      'Q': {'P'},
                      'X': set(),
                      'Y': set(),
                      'Z': set()}
    counter = algorithm(adjacency_list)
    print("test #3:", "ok" if counter == 7 else "FAILED")


test_depth_first_search(count)
