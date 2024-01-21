class Solution:
    def __init__(self):
        self.cache = {}

    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        ### Solution1 : cache
        ### Time Complexity: O(len(target) * N)
        ### Space Complexity: O(len(target))
        # if target == 0:
        #     return 1
        # if target in self.cache:
        #     return self.cache[target]
        # total_cnt = 0
        # for num in nums:
        #     if num <= target:
        #         total_cnt += self.combinationSum4(nums, target - num)
        # self.cache[target] = total_cnt
        # return total_cnt


        
        ### Solution2: DP
        ### Time Complexity: O(len(target) * N)
        ### Space Complexity: O(len(target))
        DP = [0] * (target+1)
        DP[0] = 1
        for t in range(1, target+1):
            for n in nums:
                if n > t:
                    continue
                DP[t] += DP[t - n]
        return DP[target]


