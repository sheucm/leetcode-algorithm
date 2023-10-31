class Solution:

    def longestValidParentheses(self, s: str) -> int:

        if len(s) < 2:
            return 0

        stack = [-1]
        ans = 0
        for idx, ch in enumerate(s):
            if ch == '(':
                stack.append(idx)
                continue

            stack.pop()
            if not stack:    # pop -1
                stack.append(idx)
            else:
                tmp = idx - stack[-1]
                ans = max(ans, tmp)


        return  ans   
        
