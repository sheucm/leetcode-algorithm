import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        ### Time Complexity: O(logN)
        heapq.heappush(self.small, -num)
        
        while self.small and self.large and self.small[0] * -1 > self.large[0]:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)

        while len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, val)
        
        while len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)


    def findMedian(self) -> float:
        ### Time Complexity: O(1)
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()