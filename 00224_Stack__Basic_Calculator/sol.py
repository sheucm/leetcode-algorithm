class Solution:
    def calculate(self, s: str) -> int:
        
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        st = []
        res, curr = 0, 0
        sign = 1
        for ch in s:
            if ch.isdigit():
                curr = 10 * curr + int(ch)
            elif ch in ('+', '-'):
                res += curr * sign
                curr = 0
                sign = 1 if ch == '+' else -1
            elif ch == '(':
                st.append(res)
                st.append(sign)
                res = 0
                sign = 1
            elif ch == ')':
                res += curr * sign
                res *= st.pop(-1)
                res += st.pop(-1)
                curr, sign = 0, 1
        return res + curr * sign



