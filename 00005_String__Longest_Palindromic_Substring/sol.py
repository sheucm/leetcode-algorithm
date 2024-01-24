class Solution:
    def longestPalindrome(self, s: str) -> str:
        ### Time Complexity: O(N^2)
        ### Space Complexity: O(1)
        res = ""
        res_len = 0
        for i in range(len(s)):

            # Check Odd Case
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > res_len:
                    res_len = (r-l+1)
                    res = s[l:r+1]
                l -= 1
                r += 1

            # Check Even Case
            l, r = i, i+1
            while l >=0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > res_len:
                    res_len = (r-l+1)
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res
        

