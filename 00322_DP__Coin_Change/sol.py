from typing import List
class Solution:
    def __init__(self):
        self.cache = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins = [c for c in coins if c <= amount]


        ### Solution1: cache
        ### Time Complexity: O(amount * len(coins))
        ### Space Complexity: O(amount)
        # if amount == 0:
        #     return 0
        # if amount < 0:
        #     return float('inf')
        # if amount in self.cache:
        #     return self.cache[amount]
        # ans = float('inf')
        # for coin in coins:
        #     ret = self.coinChange(coins, amount - coin)
        #     if ret != -1:
        #         ans = min(ans, ret + 1)
        # ans = ans if ans != float('inf') else -1
        # self.cache[amount] = ans
        # return ans


        ### Solution2: DP
        ### Time Complexity: O(amount * len(coins))
        ### Space Complexity: O(amount)
        DP = [float('inf')] * (amount+1)
        DP[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    DP[i] = min(DP[i], DP[i-coin] + 1)
        ans = DP[amount] if DP[amount] != float('inf') else -1
        return ans



        
