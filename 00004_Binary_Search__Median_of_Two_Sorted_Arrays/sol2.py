class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        idx1 = 0
        idx2 = 0

        array = []
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] <= nums2[idx2]:
                array.append(nums1[idx1])
                idx1 += 1
            else:
                array.append(nums2[idx2])
                idx2 += 1
        
        if idx1 != len(nums1):
            array += nums1[idx1:]
        elif idx2 != len(nums2):
            array += nums2[idx2:]
        
        mid = math.floor(len(array) / 2)
        if len(array) % 2 == 0:
            return (array[mid] + array[mid - 1]) / 2
        else:
            return array[mid]
        
