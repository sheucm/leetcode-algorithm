class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ### Solution1: Brute Force
        ### Time Complexity: O(N^2)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if target == nums[i] + nums[j]:
        #             return [i, j]


        ### Solution2: Hash Map
        ### Time Complexity: O(N)
        m = {}
        for i, n in enumerate(nums):
            m[n] = i
        for i, n in enumerate(nums):
            rest = target - n
            if rest in m and m[rest] != i:
                return [i, m[rest]]
        return []