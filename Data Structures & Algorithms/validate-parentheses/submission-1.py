class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                st.append(c)
            elif st:
                if c == ')':
                    if st[-1] == '(':
                        st.pop()
                    else:
                        return False
                if c == ']':
                    if st[-1] == '[':
                        st.pop()
                    else:
                        return False
                if c == '}':
                    if st[-1] == '{':
                        st.pop()
                    else:
                        return False
            else:
                return False
        return False if st else True
                           
