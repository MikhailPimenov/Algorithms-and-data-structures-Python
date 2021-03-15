def election3(votes: tuple):
    if type(votes[0]) == int:
        number = votes[0]

    results = {}
    for i in range(1, number + 1):
        if votes[i] not in results:
            results[votes[i]] = 1
        else:
            results[votes[i]] += 1

    return results