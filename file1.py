# lecture 12 part 1 of 2
# part 1
# levenshtein
# part 2
# pi_function
# find_substring_kmp

def levenshtein(string1: str, string2: str):
    """
    Finds minimal distance between string1 and string2
    :param string1: first str of symbols
    :param string2: second str of symbols
    :return:
    """

    frequency = [[0] * (len(string2) + 1) for k in range(len(string1) + 1)]

    for i in range(len(string1) + 1):
        frequency[i][0] = i

    for j in range(len(string2) + 1):
        frequency[0][j] = j

    for i in range(1, len(string1) + 1):
        for j in range(1, len(string2) + 1):
            if string1[i - 1] == string2[j - 1]:
                frequency[i][j] = frequency[i - 1][j - 1]
            else:
                frequency[i][j] = 1 + min(frequency[i - 1][j], frequency[i][j - 1], frequency[i - 1][j - 1])

    return frequency[len(string1)][len(string2)]


def test_levenshtein(algorithm):
    string1 = "garden is empty"
    string2 = "father"

    print("test #1:", "ok" if algorithm(string1, string2) == 13 else "FAILED")

    string1 = "pig is big"
    string2 = "big"
    print("test #2:", "ok" if algorithm(string1, string2) == 7 else "FAILED")

    string1, string2 = string2, string1
    print("test #3:", "ok" if algorithm(string1, string2) == 7 else "FAILED")

    string1 = "field"
    string2 = "cold"
    print("test #4:", "ok" if algorithm(string1, string2) == 3 else "FAILED")

    string1 = "bottom"
    string2 = "getters"
    print("test #5:", "ok" if algorithm(string1, string2) == 5 else "FAILED")

    string1 = "golden"
    string2 = "cold"
    print("test #6:", "ok" if algorithm(string1, string2) == 3 else "FAILED")


test_levenshtein(levenshtein)
