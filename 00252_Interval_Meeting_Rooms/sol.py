class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        if len(intervals) == 0:
            return True
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]
        for start, end in intervals[1:]:
            last_end = output[-1][1]
            if start < last_end:  # Overlap
                return False
            else:
                output.append([start, end])
        return True