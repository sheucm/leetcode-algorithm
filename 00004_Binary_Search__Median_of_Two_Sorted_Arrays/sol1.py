class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)
        mid_idx = math.floor(len(nums) / 2)
        if len(nums) % 2 == 0:
            return (nums[mid_idx] + nums[mid_idx - 1]) / 2
        else:
            return nums[mid_idx]

        
