from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        N = len(nums)

        
        ### Solution1: DP
        ### Time Complexity: O(N^2)
        DP = [1] * N ## Represent the max_length from 0 ~ i index.
        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]:
                    DP[i] = max(DP[i], DP[j] + 1)
        return max(DP)

        
        ### Solution2: Bisect Search
        ### Time Complexity: O(N)
        # li = []
        # for n in nums:
        #     i = bisect_left(li, n)
        #     if i == len(li):
        #         li.append(n)
        #     else:
        #         li[i] = n
        # return len(li)
        

            