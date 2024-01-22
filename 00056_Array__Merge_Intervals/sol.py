class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ### Time Complexity: O(N)
        ### Space Compplexity: O(N)
        intervals = sorted(intervals, key=lambda i: i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = output[-1][1]
            if start <= last_end: # merge case
                output[-1][1] = max(end, last_end)
            else:
                output.append([start, end])
        return output

        