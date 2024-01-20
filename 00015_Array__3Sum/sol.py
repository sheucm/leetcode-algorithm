from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums = sorted(nums)
        ans = set()
        
        for i1 in range(N-2):

            i2 = i1+1
            i3 = N-1

            while i2 < i3:
                _sum = nums[i1] + nums[i2] + nums[i3]

                if _sum < 0:
                    i2 += 1
                elif _sum > 0:
                    i3 -= 1
                else:
                    ans.add((nums[i1] , nums[i2] , nums[i3]))
                    i2 += 1
                    i3 -= 1

        ans = [[x[0], x[1], x[2]] for x in ans]
        return ans