from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        
        ### Time Complexity: O(N^2)
        ### Space Complexity: O(N)
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    ans.add((nums[i] , nums[left] , nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        ans = [[x[0],x[1],x[2]] for x in ans]
        return ans