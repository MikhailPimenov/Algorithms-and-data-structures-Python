from lecture13 import my_stack as stack


def brace_sequence(s: str):
    st = stack
    st.clear()

    b1o = '('
    b2o = '['
    b1c = ')'
    b2c = ']'

    for i in range(len(s)):
        if s[i] not in {b1o, b1c, b2o, b2c}:
            continue
        if s[i] in {b1c, b2c}:
            if st.empty():
                return False
            top = st.pop()
            if top == b1o and s[i] == b2c:
                return False
            elif top == b2o and s[i] == b1c:
                return False
        else:
            st.push(s[i])

    return st.empty()
