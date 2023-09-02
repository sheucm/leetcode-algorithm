class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        
        n, ans = len(startTime), 0
        jobs = sorted([[endTime[i], startTime[i], profit[i]] for i in range(n)])
        dp = [0 for i in range(n)]
        dp[0] = jobs[0][2]

        for i in range(1, n):
            prev_idx = bisect.bisect_right(jobs, [jobs[i][1]+1])
            if prev_idx == 0:
                dp[i] = max(dp[i-1], jobs[i][2])
            else:
                dp[i] = max(dp[i-1], dp[prev_idx - 1] + jobs[i][2])
            ans = max(ans, dp[i])
        return ans

