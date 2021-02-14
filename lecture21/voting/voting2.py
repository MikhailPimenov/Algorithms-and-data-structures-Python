def voting(stream: list):
    data = {}

    for i in range(1,len(stream)):
        if stream[i] not in data:
            data[stream[i]] = 1
        else:
            data[stream[i]] += 1
    return data
