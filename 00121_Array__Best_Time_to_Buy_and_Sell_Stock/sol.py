class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ### Solution: Greedy: front -> end
        ### Time Complexity: O(N)
        ### Space Complexity: O(1)
        # ans = 0
        # min_p = float('inf')        
        # for p in prices:
        #     ans = max(ans, p - min_p)
        #     min_p = min(min_p, p)
        # return ans

        ### Solution2: Greedy: End -> Front
        ### Time Complexity: O(N)
        ### Space Complexity: O(1)
        max_price = prices[-1]
        max_profit = 0
        for i in range(len(prices)-2, -1, -1):
            if prices[i] > max_price:
                max_price = prices[i]
            else:
                profit = max_price - prices[i]
                max_profit = max(max_profit, profit)
        return max_profit
            


