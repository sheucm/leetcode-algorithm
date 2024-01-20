class Solution:
    def countBits(self, n: int) -> List[int]:
        
        #### Solution1: General
        # ans = []
        # for num in range(0, n+1):
        #     bianry_str = bin(num)[2:]
        #     cnt = 0
        #     for ch in bianry_str:
        #         if ch == '1':
        #             cnt += 1
        #     ans.append(cnt)
        # return ans


        ### Solution2: Bit Map
        DP = [0] * (n+1)
        for i in range(1, n+1):
            DP[i] = DP[i >> 1] + (i & 1)
        return DP

