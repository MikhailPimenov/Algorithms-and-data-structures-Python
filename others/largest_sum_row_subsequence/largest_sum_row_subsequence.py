def _sum_of_elements(sequence: list, first_index: int, last_index):
    assert first_index >= 0
    assert last_index >= 0
    assert last_index >= first_index
    assert first_index <= len(sequence)
    assert last_index < len(sequence)

    result = 0
    for k in range(first_index, last_index):
        result += sequence[k]

    return result


def largest_sum_row_subsequence(sequence: list):
    ff = [[0] * (len(sequence) + 1) for k in range(len(sequence) + 1)]

    for i in range(1, len(sequence) + 1):
        for j in range(1, i + 1):
            if j < i:
                ff[i][j] = ff[i - 1][j]
            else:
                sums = [0] * j

                for s in range(j - 1):
                    sums[s] = ff[i][j - (s + 1)]
                    sums[s] += _sum_of_elements(sequence, j - (s + 1), j - 1)

                maximum = max(sums)

                if maximum > 0:
                    ff[i][j] = sequence[i - 1] + maximum
                else:
                    ff[i][j] = sequence[i - 1]

    return max(*ff[len(sequence)])
