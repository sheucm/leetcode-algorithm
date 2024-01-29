class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        
        l, r = 0, len(nums)-1
        min_val = min(nums[l], nums[r])
        while l < r:
            m = (l+r) // 2
            if m == l: break
            min_val = min(min_val, nums[m])
            if nums[m] > nums[l]:
                l = m
            else:
                r = m
        return min_val
        
        

