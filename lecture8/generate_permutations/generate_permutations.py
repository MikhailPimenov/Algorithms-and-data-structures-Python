def generate_permutations(elements:list, max_length:int=-1, permutation:list=[], used:list=[]):
    if type(elements) not in [list]:
        raise TypeError
    if type(max_length) not in [int]:
        raise TypeError
    if type(permutation) not in [list]:
        raise TypeError

    permutation = permutation or []
    used = used or []

    if max_length < 1:
        print(permutation)
        return

    for index in range(len(elements)):
        if index not in used:
            used.append(index)
            permutation.append(elements[index])
            generate_permutations(elements, max_length - 1, permutation, used)
            permutation.pop()
            used.pop()
        else:
            generate_permutations(elements, max_length - 1, permutation, used)


