class Solution:

    def __init__(self):
        self.cache = {}

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

        #### Solution1: Cache
        ### Time Complexity: O(N^2)
        ### Space Complexity: O(N^2)
        # if not text1 or not text2:
        #     return 0
        # if text1 in self.cache and text2 in self.cache[text1]:
        #     return self.cache[text1][text2]
        # if text2 in self.cache and text1 in self.cache[text2]:
        #     return self.cache[text2][text1]
        # ans = 0
        # if text1[0] == text2[0]:
        #     ans = 1 + self.longestCommonSubsequence(text1[1:], text2[1:])
        # else:
        #     ans = max(
        #         self.longestCommonSubsequence(text1[1:], text2),
        #         self.longestCommonSubsequence(text1, text2[1:])
        #     )
        # self.cache[text1] = self.cache.get(text1, {})
        # self.cache[text1][text2] = ans
        # self.cache[text2] = self.cache.get(text2, {})
        # self.cache[text2][text1] = ans
        # return ans


        ### Solution2: DP
        ### Time Complexity: O(N^2)
        ### Space Complexity: O(N^2)
        DP = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    DP[i][j] = 1 + DP[i+1][j+1]
                else:
                    DP[i][j] = max(
                        DP[i+1][j],
                        DP[i][j+1]
                    )
        return DP[0][0]
                    
