def voting(stream: list):
    n = stream[0]

    db = {}
    for i in range(1, n + 1):
        if stream[i] not in db:
            db[stream[i]] = 1
        else:
            db[stream[i]] += 1

    return db
