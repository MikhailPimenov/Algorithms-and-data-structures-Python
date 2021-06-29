def p_function5_adapter(wrappee):
    def wrapper(*args, **kwargs):
        return list(wrappee(*args, **kwargs))

    return wrapper


@p_function5_adapter
def p_function5(s: str) -> tuple:
    F = [None] * len(s)
    F[0] = 0

    for i in range(1, len(s)):
        p = F[i - 1]

        while True:
            if s[i] == s[p]:
                F[i] = p + 1
                break
            if not p:
                F[i] = 0
                break
            p = F[p - 1]

    return tuple(F)
