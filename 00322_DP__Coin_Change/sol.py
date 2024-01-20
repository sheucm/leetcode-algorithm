from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:
            return 0
        coins = [c for c in coins if c <= amount]

        ### Solution1: DP (Bottom Up)
        DP = [float('inf')] * (amount + 1)
        DP[0] = 0
        for coin in coins:
            DP[coin] = 1
            for am in range(coin+1, amount+1):
                DP[am] = min(DP[am], 1 + DP[am - coin])
        return -1 if DP[amount] == float('inf') else DP[amount]


        ### Solution2: DP (Top Down)
        # DP = {}
        # def _func(_amount):

        #     if _amount < 0:
        #         return float('inf')
        #     if _amount == 0:
        #         return 0
        #     if _amount in DP:
        #         return DP[_amount]
            
        #     ret = float('inf')
        #     for coin in coins:
        #         ret = min(ret, _func(_amount - coin) + 1)

        #     DP[_amount] = ret
        #     return ret

        # ans = _func(amount)
        # return -1 if ans == float('inf') else ans


        
if __name__ == '__main__':
    amount = 11
    coins = [1,2,5]
    answer = 3
    ret = Solution().coinChange(coins, amount)
    print(ret)