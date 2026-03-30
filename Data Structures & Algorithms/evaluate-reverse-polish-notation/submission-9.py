class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for c in tokens:
            if c.isnumeric():
                st.append(int(c))
            elif len(c) > 1 and c[0] == '-':
                st.append(int(c))
            else:
                num2 = st.pop()
                num1 = st.pop()
                if c == "+":
                    st.append(num1 + num2)
                elif c == '-':
                    st.append(num1 - num2)
                elif c == '*':
                    st.append(num1 * num2)
                elif c == '/':
                    st.append(int(num1 / num2))
        return st.pop()
