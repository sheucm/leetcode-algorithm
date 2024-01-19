class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zero_idx = []
        non_zero_total = 1
        total = 1
        for idx, n in enumerate(nums):
            if n != 0:
                non_zero_total *= n
            else:
                zero_idx.append(idx)
        
        if len(zero_idx) >= 2:
            return [0] * len(nums)
        
        ans = []
        if len(zero_idx):
            for n in nums:
                if n != 0:
                    ans.append(0)
                else:
                    ans.append(non_zero_total)
        else:
            for n in nums:
                ans.append(non_zero_total // n)
                
        return ans