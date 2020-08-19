def longest_increasing_subsequence(sequence: list):
    f = [0] * (len(sequence) + 1)

    length = calculate_length(sequence, f)
    result = subsequence(sequence, f, length)
    return result


def calculate_length(sequence: list, f: list):
    for k in range(1, len(sequence) + 1):
        maximum = 0
        maximum_index = 0
        for i in range(1, k):
            if f[i] > maximum and sequence[i - 1] < sequence[k - 1]:
                maximum = f[i]
                maximum_index = i
        f[k] = f[maximum_index] + 1
    return max(*f)


def subsequence(sequence: list, f: list, length: int):
    result = [0] * length

    current_maximum = max(*f)
    current_maximum_index = 0
    for k in range(len(sequence) + 1):
        if f[k] == current_maximum:
            current_maximum_index = k
            break

    sub_index = length - 1
    result[sub_index] = sequence[current_maximum_index - 1]
    sub_index -= 1

    index = current_maximum_index
    while index > 0:
        if f[index] == f[current_maximum_index] - 1:
            result[sub_index] = sequence[index - 1]
            sub_index -= 1
            current_maximum_index = index
        index -= 1

    return result
