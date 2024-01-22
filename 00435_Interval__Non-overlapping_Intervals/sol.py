class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]
        remove_cnt = 0
        for start, end in intervals[1:]:
            last_end = output[-1][1]
            if start < last_end: # overlap
                remove_cnt += 1
                if end < last_end:
                    output[-1] = [start, end]
            else:
                output.append([start, end])
        return remove_cnt