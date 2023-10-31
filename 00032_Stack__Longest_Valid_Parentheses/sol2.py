class Solution:

    def longestValidParentheses(self, s: str) -> int:

        if len(s) < 2:
            return 0

        stack = []
        flag = [0] * len(s)

        for idx, ch in enumerate(s):
            if len(stack) == 0:
                stack.append((idx, ch))
                continue
            if stack[-1][1] == '(' and ch == ')':
                flag[stack[-1][0]] = 1
                flag[idx] = 1
                stack = stack[:-1]
            else:
                stack.append((idx, ch))

        cnt = 0
        ans = 0
        for i in flag:
            if i == 1:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
        ans = max(ans, cnt)
        
        return  ans   
        
