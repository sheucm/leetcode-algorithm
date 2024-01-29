# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        ### Time Complexity: O(logN)
        ### Space Complexity: O(1)
        if isBadVersion(1): return 1
        if not isBadVersion(n): return 0
        l, r = 1, n
        while l < r:
            m = (l + r) // 2
            if m == l: break
            if isBadVersion(m):
                r = m
            else:
                l = m
        return r
            