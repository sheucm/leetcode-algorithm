class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        ### Solution1:
        ### Space: O(N)
        # exist = [False] * (len(nums) + 1)
        # for n in nums:
        #     exist[n] = True
        # for n, e in enumerate(exist):
        #     if not e:
        #         return n
        # raise Exception('unexpected')



        ### Solution2:
        ### Space: O(1)
        ### transform 0 to len(nums)+1
        # N = len(nums)
        # ZERO = N+1
        # for i, n in enumerate(nums):
        #     if n == 0:
        #         nums[i] = ZERO
        #         break
        # nums.append(N + 100)  ### Add dummy number
        # for i in range(0, N):
        #     n = abs(nums[i])
        #     idx = 0 if n == ZERO else n
        #     if nums[idx] > 0:
        #         nums[idx] = -1 * nums[idx]
        # for idx, n in enumerate(nums):
        #     if n > 0:
        #         return idx
        # raise Exception('error')


        ### Solution3:
        ### Space: O(1)
        ### Basic: 
        ### total = sum([i for i in range(len(nums) + 1)])
        # total = (0 + len(nums)) * (len(nums) + 1) // 2  ## Gaussian formula
        # return total - sum(nums)



        ### Solution4: Bit solution
        ### Space: O(1)
        ### Use "XOR"
        ### XOR 2 times will back to original number
        result = 0
        for n in range(len(nums)+1):
            result ^= n
        for n in nums:
            result ^= n
        return result