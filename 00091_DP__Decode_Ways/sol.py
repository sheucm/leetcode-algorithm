class Solution:
    def __init__(self):
        self.cache = {}
    def numDecodings(self, s: str) -> int:

        ### Solution1: Cache
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        # if len(s) == 0:
        #     return 1
        # if s[0] == '0':
        #     return 0
        # if len(s) == 1:
        #     return 1
        # if s in self.cache:
        #     return self.cache[s]
        # ans = (
        #     self.numDecodings(s[1:])
        #     + (self.numDecodings(s[2:]) if int(s[:2]) <= 26 else 0)
        # )
        # self.cache[s] = ans
        # return ans



        ### Solution2: DP
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        if s[0] == '0':
            return 0
        DP = [0] * (len(s) + 1)
        DP[-1] = 1
        DP[-2] = 1 if s[-1] != '0' else 0
        for i in range(len(s)-2, -1, -1):
            if s[i] == '0':
                DP[i] = 0
            else:
                DP[i] = (
                    DP[i+1] + 
                    (DP[i+2] if int(s[i:i+2]) <= 26 else 0)
                )
        return DP[0]
