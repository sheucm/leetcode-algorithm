from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ### Solution1: Hash Map
        ### Time Complexity: O(S+T)
        ### Space Complexity: ~O(1)
        if len(s) != len(t): return False
        m = defaultdict(int)
        for c in s:
            m[c] += 1
        for c in t:
            m[c] -= 1
        for c in m:
            if m[c] != 0: return False
        return True


        ### Solution1: Use no memory to solve it
        ### Time Complexity: O(SLogS + TLogT)
        ### Space Complexity: O(1)
        # if len(s) != len(t): return False
        # s = sorted(s)
        # t = sorted(t)
        # for i in range(len(s)):
        #     if s[i] != t[i]:
        #         return False
        # return True
        