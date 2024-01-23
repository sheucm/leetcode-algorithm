class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        ### Solution1: Space efficient
        ### Time Complexity: O(N)
        ### Space Complexity: O(1)
        intervals.sort()
        end = intervals[0][1]
        ans = 0
        for itv in intervals[1:]:
            if itv[0] >= end:
                end = itv[1]
            else:
                ans += 1
                end = min(end, itv[1])
        return ans
        



        ### Solution2: Will record the answer list
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        # intervals.sort()
        # output = [intervals[0]]
        # remove_cnt = 0
        # for start, end in intervals[1:]:
        #     last_end = output[-1][1]
        #     if start < last_end: # overlap
        #         remove_cnt += 1
        #         if end < last_end:
        #             output[-1] = [start, end]
        #     else:
        #         output.append([start, end])
        # return remove_cnt