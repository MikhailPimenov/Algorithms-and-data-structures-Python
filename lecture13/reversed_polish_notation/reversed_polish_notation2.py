from lecture13 import my_stack as stack


def reversed_polish_notation(s:str):
    st = stack
    st.clear()

    for i in range(len(s)):
        if s[i] not in {"+","-","*","/"}:
            st.push(s[i])
        else:
            if not st.empty():
                second = st.pop()
            else:
                raise SyntaxError
            if not st.empty():
                first = st.pop()
            else:
                raise SyntaxError

            if s[i] == "+":
                result = first + second
            elif s[i] == "-":
                result = first - second
            elif s[i] == "*":
                result = first * second
            else: #s[i] == "/"
                if second:
                    result = first / second
                else:
                    raise ZeroDivisionError
            st.push(result)

    if not st.empty():
        return st.pop()
    else:
        raise SyntaxError
