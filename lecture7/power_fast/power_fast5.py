def power_fast5(base: int, n: int) -> int:
    if not n:
        return 1

    if n == 1:
        return base

    if n < 0:
        return -1

    if not n % 2:
        return power_fast5(base, n - 1) * base

    return power_fast5(base * base, (n - 1) // 2) * base
