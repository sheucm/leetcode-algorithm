class Solution:
    def __init__(self):
        self.cache = {}

    def rob(self, nums: List[int], idx = 0) -> int:

        ### Solution1: Cache
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        # _nums = nums[idx:]
        # if len(_nums) == 0:
        #     return 0
        # if len(_nums) == 1:
        #     return _nums[0]
        # if idx in self.cache:
        #     return self.cache[idx]
        # ans = max(
        #     _nums[0] + self.rob(nums, idx + 2),
        #     _nums[1] + self.rob(nums, idx + 3)
        # )
        # self.cache[idx] = ans
        # return ans



        ### Solution2: DP
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        DP = [0] * (len(nums) + 2)
        DP[-1] = 0
        DP[-2] = 0
        for i in range(len(nums) - 1, -1, -1):
            DP[i] = max(
                DP[i+2] + nums[i],
                DP[i+1]
            )
        return DP[0]

        
        