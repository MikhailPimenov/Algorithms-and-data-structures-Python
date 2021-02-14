def generate_permutations(array: list, length: int):
    if type(array) != list:
        raise TypeError
    if type(length) != int:
        raise TypeError

    permutation = []
    used = set()
    for variable_length in range(1, length + 1):
        generate_permutations_with_constant_length(array, variable_length, permutation, used)
        permutation.clear()
        used.clear()


def generate_permutations_with_constant_length(array: list, length: int, permutation: list, used:set):
    if length < 1:
        print(permutation)
        return

    for index in range(len(array)):
        if (array[index], index) not in used:
            permutation.append(array[index])
            used.add((array[index], index))
            generate_permutations_with_constant_length(array, length - 1, permutation, used)
            permutation.pop()
            used.remove((array[index], index))
