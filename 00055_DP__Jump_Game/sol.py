
class Solution:

    def canJump(self, nums: List[int]) -> bool:
        
        ### Solution1: DP
        ### Time Complexity: O(N * MAX_NUMBER)
        ### Space Complexity: O(N)
        # if len(nums) == 1:
        #     return True
        # DP = [False] * len(nums)
        # DP[-1] = True
        # for i in range(len(nums)-2, -1, -1):
        #     for j in range(1, nums[i]+1):
        #         idx = i + j if i + j < len(nums) else -1
        #         DP[i] = DP[i] or DP[idx]
        #         if DP[i]:
        #             break
        # return DP[0]


        ### Solution2: case algorithm
        ### Time Complexity: O(N)
        ### Space Complexity: O(1)
        max_reachable_idx = 0
        for i in range(len(nums)):
            if i > max_reachable_idx:
                return False
            max_reachable_idx = max(max_reachable_idx, i + nums[i])
            if max_reachable_idx >= len(nums) - 1:
                break
        return True
