class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
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
                    
