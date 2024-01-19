class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        ans = min(nums[0], nums[-1])

        start = 0
        end = len(nums) - 1

        while nums[start] > nums[end]:

            mid = (start + end) // 2
            if mid == start:
                break
            ans = min(ans, nums[mid])
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
            
        return ans
        

