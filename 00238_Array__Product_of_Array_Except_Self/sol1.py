class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        sol = [1] * len(nums)
        pre = 1

        for i in range(len(nums)):
            sol[i] *= pre
            pre *= nums[i]
        
        post = 1
        for i in range(len(nums)-1, -1, -1):
            sol[i] *= post
            post *= nums[i]
                
        return sol