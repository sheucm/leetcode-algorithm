class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ans = []
        for idx, itv in enumerate(intervals):
            if newInterval[1] < itv[0]:  # Non-overlap case
                ans.append(newInterval)
                ans = ans + intervals[idx:]
                return ans

            elif newInterval[0] > itv[1]:   # Non-overlap case
                ans.append(itv)
            
            else:   # Overlap case
                newInterval = [
                    min(newInterval[0], itv[0]),
                    max(newInterval[1], itv[1])
                ]
        ans.append(newInterval)
        return ans