from functools import cache

class Solution:
    def __init__(self):
        self.cache = {}

    # @cache   ### Use this decorator to replace implementing cache by ourselves for solution1.
    def uniquePaths(self, m: int, n: int) -> int:
        

        ### Solution 1: Cache
        ### Time Complexity: O(m * n)
        ### Space Complexity: O(m * n)
        # if m == 1 or n == 1:
        #     return 1
        # if f'{m}_{n}' in self.cache:
        #     return self.cache[f'{m}_{n}']
        # ans = self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)
        # self.cache[f'{m}_{n}'] = ans
        # return ans


        ### Solution 2: DP
        ### Time Complexity: O(m * n)
        ### Space Complexity: O(m * n)
        DP = [[0] * (n+1) for _ in range(m+1)]
        DP[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == (m-1) and j == (n-1):
                    continue
                DP[i][j] = DP[i+1][j] + DP[i][j+1]
        return DP[0][0]