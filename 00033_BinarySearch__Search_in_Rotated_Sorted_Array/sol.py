class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        ### Time Complexity: O(logN)
        ### SpaceTime Complexity: O(1)

        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums)-1


        left = 0
        right = len(nums) - 1

        ans = -1
        while True:
            m = (left + right) // 2
            if m == left:
                break
            if nums[m] == target:
                return m
            
            if nums[m] > nums[left]:
                if nums[left] < target < nums[m]:
                    right = m
                else:
                    left = m
            else:
                if target > nums[left] or target < nums[m]:
                    right = m
                else:
                    left = m
        
        return ans

