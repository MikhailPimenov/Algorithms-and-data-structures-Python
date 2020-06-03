# lecture 12 part 2 of 2
# part 1
# levenshtein
# part 2
# pi_function
# find_substring_kmp


def pi_function(string: str):
    """
    Returns array of pi-function values for each symbol of string
    :param string:
    :return:
    """
    frequency = [0] * len(string)
    frequency[0] = 0

    for index in range(1, len(string)):
        p_index = frequency[index - 1]

        while True:
            if string[index] == string[p_index]:
                if p_index > 0:
                    frequency[index] = 1 + frequency[index - 1]
                else:  # p_index == 0:
                    frequency[index] = 1
                break
            else:
                if p_index > 0:
                    p_index = frequency[p_index]
                else:  # p_index == 0:
                    frequency[index] = 0
                    break

    return frequency


def find_substring_kmp(string: str, substring: str):
    """
    Returns index of first appearance substring in string
    :param string: str to search in
    :param substring: str to search for
    :return: index in string
    """
    sum_string = substring + "#" + string;
    pi_array = pi_function(sum_string)

    result = -1
    for k in range(len(pi_array)):
        if pi_array[k] == len(substring):
            result = k - len(substring) - len(substring)
            break

    return result


def test_pi_function(algorithm):
    print("testing pi_function:")

    string = "abababa"
    result = [0, 0, 1, 2, 3, 4, 5]
    print("test #1:", "ok" if algorithm(string) == result else "FAILED")

    string = "akeakea"
    result = [0, 0, 0, 1, 2, 3, 4]
    print("test #2:", "ok" if algorithm(string) == result else "FAILED")

    string = "alalcda"
    result = [0, 0, 1, 2, 0, 0, 1]
    print("test #3:", "ok" if algorithm(string) == result else "FAILED")

    string = "acdabcdabacd"
    result = [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 2, 3]
    print("test #4:", "ok" if algorithm(string) == result else "FAILED")


def test_find_substring_kmp(algorithm):
    print("testing find_substring:")

    string = "father"
    sub_string = "garden"
    print("test #1:", "ok" if algorithm(string, sub_string) == -1 else "FAILED")

    string = "pigisbig"
    sub_string = "big"
    print("test #2:", "ok" if algorithm(string, sub_string) == 5 else "FAILED")

    string = "dog"
    sub_string = "horse"
    print("test #3:", "ok" if algorithm(string, sub_string) == -1 else "FAILED")

    string = ""
    sub_string = ""
    print("test #4:", "ok" if algorithm(string, sub_string) == 0 else "FAILED")

    string = "suddenly"
    sub_string = "suddenly"
    print("test #5:", "ok" if algorithm(string, sub_string) == 0 else "FAILED")

    string = "suddenly suddenly"
    sub_string = "sud"
    print("test #6:", "ok" if algorithm(string, sub_string) == 0 else "FAILED")

    string = "suddenly and suddenly they got crazy and crazy"
    sub_string = "raz"
    print("test #7:", "ok" if algorithm(string, sub_string) == 32 else "FAILED")

    string = "that terrible weather is annoying me"
    sub_string = "noy"
    print("test #8:", "ok" if algorithm(string, sub_string) == 27 else "FAILED")

    string = "big"
    sub_string = "pig is big"
    print("test #9:", "ok" if algorithm(string, sub_string) == -1 else "FAILED")


test_pi_function(pi_function)
test_find_substring_kmp(find_substring_kmp)
