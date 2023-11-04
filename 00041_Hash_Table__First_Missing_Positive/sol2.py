class Solution:

    # O(1) auxiliary space solution.
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)

        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        
        for i in range(n):

            val = abs(nums[i])

            if val > n:
                continue

            idx = val - 1

            # Mark minus as exist
            if nums[idx] > 0:
                nums[idx] = -1 * nums[idx]
        
        for i in range(n):
            is_exist = nums[i] < 0
            if not is_exist:
                return i + 1
        return n+1


