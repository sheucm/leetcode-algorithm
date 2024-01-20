from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
            if m[n] >= 2:
                return True
        return False
