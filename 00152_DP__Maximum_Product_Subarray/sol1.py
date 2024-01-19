class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_ary = [0] * len(nums)
        min_ary = [0] * len(nums)

        for idx, n in enumerate(nums):
            if idx == 0:
                max_ary[idx] = n
                min_ary[idx] = n
            else:
                max_ary[idx] = max(
                    n, 
                    max_ary[idx-1] * n,
                    min_ary[idx-1] * n
                )
                min_ary[idx] = min(
                    n, 
                    max_ary[idx-1] * n,
                    min_ary[idx-1] * n
                )

        return max(max_ary)