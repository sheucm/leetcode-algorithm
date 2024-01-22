import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        ### Solution1: start & end list
        ### Time Complexity: O(NLogN)
        ### Space Complexity: O(N)
        ### Mindset: Compare the min start and min end to determine the current meeting room count.
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        ans, cnt = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if starts[s] >= ends[e]:
                e += 1
                cnt -= 1
            else:
                s += 1
                cnt += 1
            ans = max(ans, cnt)
        return ans



        ### Solution2: Heap
        ### Time Complexity: O(NLogN)
        ### Space Complexity: O(N)
        ### Mindset: Check the current min end time before new meeting
        # intervals.sort(key=lambda i: i[0])
        # ans = 1
        # h = [intervals[0][1]]
        # for start, end in intervals[1:]:
        #     while h and start >= h[0]:
        #         heapq.heappop(h)
        #     heapq.heappush(h, end)
        #     ans = max(ans, len(h))
        # return ans



        ### Solution: Bruce Force
        ### Time Complexity: O(N^2)
        ### Space Complexity: O(N^2)
        # intervals.sort(key=lambda i: i[0])
        # outputs = [[intervals[0]]]
        # for start, end in intervals[1:]:
        #     is_inserted = False
        #     for output in outputs:
        #         last_end = output[-1][1]
        #         if start < last_end:  # overlap
        #             continue
        #         else:
        #             is_inserted = True
        #             output.append([start, end])
        #             break
        #     if not is_inserted:
        #         outputs.append([[start, end]])
        # return len(outputs)