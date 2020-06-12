# lecture 24 part 3 of 3
# graphs
# depth_first_search
# sort (topological_sort)


def depth_first_search(vertex, adjacency_list: dict, gray_and_black: set, gray: list, black: list):
    gray_and_black.add(vertex)
    gray.append(vertex)

    for neighbour in adjacency_list[vertex]:
        if neighbour in gray:
            return False
        cycle_not_detected = True
        if neighbour not in gray_and_black:
            cycle_not_detected = depth_first_search(neighbour, adjacency_list, gray_and_black, gray, black)
        if not cycle_not_detected:
            return False

    gray.pop()
    black.append(vertex)

    return True


def sort(adjacency_list: dict):
    gray_and_black = set()
    black = []

    for vertex in adjacency_list:
        if vertex not in gray_and_black:
            gray = []
            cycle_not_detected = depth_first_search(vertex, adjacency_list, gray_and_black, gray, black)
            if not cycle_not_detected:
                return {}

    index = {}
    count = 0
    for k in range(len(adjacency_list)):
        index[count] = black.pop()
        count += 1

    return index


def test_sort(algorithm):
    print("testing sort:")

    adjacency_list = {'A': {'B'},
                      'B': {'C'},
                      'C': {'D'},
                      'D': set(), }
    index1 = {0: 'A',
              1: 'B',
              2: 'C',
              3: 'D', }
    index2 = algorithm(adjacency_list)
    print("test #1:", "ok" if index1 == index2 else "FAILED")

    adjacency_list = {'A': {'B'},
                      'B': {'C', 'E'},
                      'C': {'D'},
                      'D': set(),
                      'E': {'C', 'D'}, }
    index1 = {0: 'A',
              1: 'B',
              3: 'C',
              4: 'D',
              2: 'E'}
    index2 = algorithm(adjacency_list)
    print("test #2:", "ok" if index1 == index2 else "FAILED")

    adjacency_list = {'A': {'B'},
                      'B': {'C', 'G'},
                      'C': {'D'},
                      'D': {'K', 'H'},
                      'H': {'K'},
                      'K': {'I', 'E'},
                      'I': {'E'},
                      'E': {'J', 'F'},
                      'J': {'F'},
                      'G': {'C'},
                      'F': set(), }
    index1 = {0: 'A',
              1: 'B',
              2: 'G',
              3: 'C',
              4: 'D',
              5: 'H',
              6: 'K',
              7: 'I',
              8: 'E',
              9: 'J',
              10: 'F', }
    index2 = algorithm(adjacency_list)
    print("test #3:", "ok" if index1 == index2 else "FAILED")

    adjacency_list = {'A': {'B'},
                      'B': {'C', 'E'},
                      'C': {'D'},
                      'D': set(),
                      'E': {'C', 'A'}, }
    index1 = {}
    index2 = algorithm(adjacency_list)
    print("test #4:", "ok" if index1 == index2 else "FAILED")


test_sort(sort)
