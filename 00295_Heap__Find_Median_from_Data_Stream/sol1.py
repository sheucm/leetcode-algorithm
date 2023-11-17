import heapq

class MedianFinder:

    def __init__(self):
        # Space: O(N)
        self.lo_max_heap = []
        self.hi_min_heap = []


    def addNum(self, num: int) -> None:
        if not self.lo_max_heap:
            heapq.heappush(self.lo_max_heap, -num)
            return

        # Speed: O(logN)
        if -self.lo_max_heap[0] >= num:
            heapq.heappush(self.lo_max_heap, -num)
        else:
            heapq.heappush(self.hi_min_heap, num)
        
        # Speed: O(logN)
        if (
            len(self.hi_min_heap) > len(self.lo_max_heap)
        ):
            _p = heapq.heappop(self.hi_min_heap)
            heapq.heappush(self.lo_max_heap, -_p)
        elif (
            len(self.lo_max_heap) - len(self.hi_min_heap) > 1
        ):
            _p = heapq.heappop(self.lo_max_heap) * -1
            heapq.heappush(self.hi_min_heap, _p)
        
        assert len(self.lo_max_heap) >= len(self.hi_min_heap)
        


    def findMedian(self) -> float:
        # Speed: O(1)
        if (len(self.lo_max_heap) + len(self.hi_min_heap)) % 2 == 1:
            return self.lo_max_heap[0] * -1
        else:
            return (self.lo_max_heap[0] * -1 + self.hi_min_heap[0]) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
