def insert_sort4(a: list):
    for i in range(1, len(a)):
        for j in reversed(range(i)):
            if a[j] > a[i]:
                a[j], a[i] = a[i], a[j]
                i = j
