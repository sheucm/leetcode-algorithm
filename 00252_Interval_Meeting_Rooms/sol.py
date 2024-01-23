class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        ### Time Complexity: O(N)
        ### Space Complexity: O(1)
        if not intervals: return True
        intervals.sort()
        end = intervals[0][1]
        for itv in intervals[1:]:
            if itv[0] >= end:
                end = itv[1]
            else:
                return False
        return True