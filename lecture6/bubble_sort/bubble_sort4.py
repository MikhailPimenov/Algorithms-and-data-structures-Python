def bubble_sort4(a: list):
    for i1 in range(len(a) - 1):
        go_on = False
        for i2 in range(len(a) - 1 - i1):
            if a[i2] > a[i2 + 1]:
                a[i2], a[i2 + 1] = a[i2 + 1], a[i2]
                go_on = True
        if not go_on:
            return
