
import heapq

class Solution:

    ## O(N * K)  --> time exceeded
    ## O(LogN * K)  --> ok

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        h = []
        for i in range(k):
            heapq.heappush(h, (-nums[i], i))
        
        ans = [-h[0][0]]

        i = k
        while i < len(nums):
            left = i - k
            assert left >= 0

            while h and h[0][1] <= left:
                heapq.heappop(h)
            
            heapq.heappush(h, (-nums[i], i))
            ans.append(-h[0][0])
            i += 1
        
        return ans

            

