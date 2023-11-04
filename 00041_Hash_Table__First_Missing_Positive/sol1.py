class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            if n > 0:
                s.add(n)
        l = list(s)
        if not l:
            return 1
        l.sort()
        for idx, n in enumerate(l):
            if n != idx+1:
                return idx+1
        return len(l) + 1
