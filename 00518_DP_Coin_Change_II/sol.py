class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        ### Solution1: DP
        ### Time Complexity: O(M*N)
        ### Space Complexity: O(M*N)
        coins.sort()
        DP = [[0] * (amount+1) for _ in range(len(coins) + 1)]
        for r in range(len(coins)):
            DP[r][-1] = 1
        for i in range(len(coins)-1, -1, -1):
            for j in range(amount-1, -1, -1):
                coin = coins[i]
                DP[i][j] = (
                    0 if (j + coin) >= amount+1 else DP[i][j + coin]
                    + DP[i+1][j]
                )
        return DP[0][0]


        ### Solution2: memory efficient
        ### Time Complexity: O(M*N)
        ### Space Complexity: O(N)
        # coins.sort()
        # prev_dp = [0] * (amount+1)
        # prev_dp[-1] = 1
        # for i in range(len(coins)-1, -1, -1):
        #     curr_dp = [0] * (amount+1)
        #     curr_dp[-1] = 1
        #     for j in range(amount-1, -1, -1):
        #         coin = coins[i]
        #         curr_dp[j] = (
        #             0 if (j + coin) >= amount+1 else curr_dp[j + coin]
        #             + prev_dp[j]
        #         )
        #     prev_dp = curr_dp
        # return prev_dp[0]