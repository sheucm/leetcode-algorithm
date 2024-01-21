class Solution:

    def _robber1_solution(self, nums: List[int]) -> int:
        DP = [0] * (len(nums) + 2)
        DP[-1] = 0
        DP[-2] = 0
        for i in range(len(nums)-1, -1, -1):
            DP[i] = max(
                nums[i] + DP[i+2],
                DP[i+1]
            )
        return DP[0]

    def rob(self, nums: List[int]) -> int:
        return max(
            nums[0],   # Special Case for len(nums) = 1
            self._robber1_solution(nums[1:]), 
            self._robber1_solution(nums[:-1])
        )