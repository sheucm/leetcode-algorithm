class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        head, tail = 0, 0
        s = set()
        ans = 0
        while tail != len(string):
            while string[tail] in s:
                s.remove(string[head])
                head += 1
            s.add(string[tail])
            ans = max(ans, len(s))
            tail += 1
        return ans

