def shift_array5(a: list, shift: int) -> list:
    if shift < 0 or shift > len(a):
        shift = (len(a) + shift) % len(a)

    buffer = [a[i] for i in range(len(a) - shift, len(a))]

    for i in reversed(range(len(a) - shift)):
        a[i + shift] = a[i]

    for i in range(shift):
        a[i] = buffer[i]

    return a
