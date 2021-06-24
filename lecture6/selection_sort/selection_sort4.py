def selection_sort4(a: list):
    for i in reversed(range(1, len(a))):
        m = 0
        for j in range(1, i + 1):
            if a[j] > a[m]:
                m = j
        a[i], a[m] = a[m], a[i]
