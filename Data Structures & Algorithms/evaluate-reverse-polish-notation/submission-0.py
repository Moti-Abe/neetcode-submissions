class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        st = deque()
        for i in range(len(tokens)):
            if tokens[i] not in ["+", "-", "*", "/"]:
                st.append(int(tokens[i]))
            else:
                if len(st) >= 2:
                    x = st.pop()
                    y = st.pop()
                    if tokens[i] == "+":
                        res = y + x
                    elif tokens[i] == "-":
                        res = y - x
                    elif tokens[i] == "*":
                        res = y * x
                    else:
                        res = int(y / x)
                    st.append(res) 
        return st[0]