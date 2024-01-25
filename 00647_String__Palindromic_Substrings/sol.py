class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ### Time Complexity: O(N^2)
        ### Space Complexity: O(1)
        ans = 0
        for i in range(len(s)):
            # Odd Case
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l, r = l-1, r+1
            #Even Case
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l, r = l-1, r+1
        return ans
