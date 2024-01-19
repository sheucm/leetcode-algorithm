class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums)
        for idx, n in enumerate(nums):
            if idx == 0:
                dp[idx] = n
            else:    
                dp[idx] = max(n, dp[idx-1] + n)
        
        return max(dp)
        

