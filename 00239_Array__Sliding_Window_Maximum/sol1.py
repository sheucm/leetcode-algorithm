

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        l = []
        deque = [nums[0]]

        def _add(x: int):
            while len(deque) != 0 and x > deque[-1]:
                deque.pop()
            deque.append(x)


        for i in range(1, k):
            _add(nums[i])

        l.append(deque[0])

        for i in range(k, len(nums)):
            if len(deque) and nums[i - k] == deque[0]:
                deque.pop(0)

            _add(nums[i])
            l.append(deque[0])

            
        return l

