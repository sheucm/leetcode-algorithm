import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        _min_heap = []
        _max_heap = []
        
        for li_no, li in enumerate(nums):
            heapq.heappush(_min_heap, (li[0], li_no, 0))  # val, li_no, li_idx
            heapq.heappush(_max_heap, (-li[0], li_no, 0))  # val, li_no, li_idx
            
        
        ans = [_min_heap[0][0], -_max_heap[0][0]]

        while _min_heap:
            val, li_no, li_idx = heapq.heappop(_min_heap)

            if li_idx + 1 >= len(nums[li_no]):
                break
            
            li_idx += 1
            val = nums[li_no][li_idx]
            heapq.heappush(_min_heap, (val, li_no, li_idx))  # val, li_no, li_idx
            heapq.heappush(_max_heap, (-val, li_no, li_idx))  # val, li_no, li_idx

            _tmp = [_min_heap[0][0], -_max_heap[0][0]]
            assert -_max_heap[0][0] >= _min_heap[0][0]

            if (_tmp[1] - _tmp[0]) < (ans[1] - ans[0]):
                ans = _tmp
        return ans


