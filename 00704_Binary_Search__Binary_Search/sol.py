import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        ### Solution1
        # idx = bisect.bisect_left(nums, target)
        # return idx if idx < len(nums) and nums[idx] == target else -1
        

        ### Solution2: 
        ### Time Complexity: O(logN)
        ### Space Complexity: O(1)
        if target == nums[0]: return 0
        if target == nums[-1]: return len(nums)-1
        l, r = 0, len(nums)-1
        while l < r:
            m = (l + r) // 2
            if nums[m] == target: return m
            if m == l: break
            if target > nums[m]: 
                l = m
            else:
                r = m
        return -1