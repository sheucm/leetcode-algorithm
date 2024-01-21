class Solution:
    def __init__(self):
        self.cache = {}
    def climbStairs(self, n: int) -> int:


        ### Solution1: cache
        ### Time Complexity: O(N)
        ### Space Compexity: O(N)
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # if n in self.cache:
        #     return self.cache[n]
        # ans = self.climbStairs(n-1) + self.climbStairs(n-2)
        # self.cache[n] = ans
        # return ans


        
        ### Solution2: DP
        ### Time Complexity: O(N)
        ### Space Compexity: O(N)
        DP = [1] * (n+2)
        DP[-1] = 0
        for i in range(n-1, -1, -1):
            DP[i] = DP[i+1] + DP[i+2]
        return DP[0]
