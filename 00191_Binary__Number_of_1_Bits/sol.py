class Solution:
    def hammingWeight(self, n: int) -> int:
        
        ### Solution1: Transfer to String
        # s = bin(n)[2:]
        # cnt = 0
        # for ch in s:
        #     if ch == '1':
        #         cnt += 1
        # return cnt


        ### Solution2: Bit
        cnt = 0
        for _ in range(32):
            cnt += n & 1
            n >>= 1
        return cnt
