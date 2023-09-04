class Solution:

    def _bubble_sort(self, array):
        idx = 0
        while idx < len(array):
            curr = idx + 1
            while curr < len(array):
                if array[curr] < array[idx]:
                    tmp  = array[idx]
                    array[idx] = array[curr]
                    array[curr] = tmp
                curr += 1
            idx += 1
        return array

    def _quick_sort(self, array):
        if len(array) <= 1:
            return array
        elif len(array) == 2:
            return array if array[0] <= array[1] else array[::-1]
        
        mid = math.floor(len(array) / 2)
        pivot = array[mid]

        left, right = [], []
        for idx, v in enumerate(array):
            if idx == mid:
                continue
            if v < pivot:
                left.append(v)
            else:
                right.append(v)

        return self._quick_sort(left) + [pivot] + self._quick_sort(right)

    def _merge_sort(self, array):
        if len(array) <= 1:
            return array
        elif len(array) == 2:
            return array if array[0] <= array[1] else [array[1], array[0]]
        
        mid = math.ceil(len(array) / 2)
        left = self._merge_sort(array[:mid])
        right = self._merge_sort(array[mid:])
        merged_li = []

        l, r = 0, 0
        while True:
            if r == len(right):
                merged_li += left[l:]
                break
            if l == len(left):
                merged_li += right[r:]
                break

            if left[l] <= right[r]:
                merged_li.append(left[l])
                l += 1
            else:
                merged_li.append(right[r])
                r += 1
        return merged_li
    

    def _sort(self, array):
        return self._bubble_sort(array)
        # return self._quick_sort(array)
        # return self._merge_sort(array)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self._sort(nums1 + nums2)
        mid_idx = math.floor(len(nums) / 2)
        if len(nums) % 2 == 0:
            return (nums[mid_idx] + nums[mid_idx - 1]) / 2
        else:
			return nums[mid_idx]
