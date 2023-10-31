class Solution:

    def longestValidParentheses(self, s: str) -> int:

        if len(s) < 2:
            return 0

        flag = [0] * len(s)

        last_l = 0
        l = 0
        r = 1
        while (
            l >= 0 and r < len(s) and l < r
        ):
            if s[l] == ')':
                l = r
                r += 1
                continue
            elif s[r] == '(':
                l = r
                r += 1
                continue
            
            # l = ( \ r = )
            flag[l] = 1
            flag[r] = 1

            r += 1
            while True:
                l -= 1  
                if l < 0 or flag[l] == 0:
                    break          
            
            if l < 0:
                l = r
                r += 1
        print(flag)

        ans = 0
        cnt = 0
        for i in range(len(flag)):
            if flag[i] == 1:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
        ans = max(ans, cnt)
        return  ans   
        
