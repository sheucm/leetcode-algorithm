class Solution:

    def _longestCommonSubseq(self, s1: str, s2: str) -> int:
        DP = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

        for r in range(len(s1)-1, -1, -1):
            for c in range(len(s2)-1, -1, -1):
                if s1[r] == s2[c]:
                    DP[r][c] = 1 + DP[r+1][c+1]
                else:
                    DP[r][c] = max(
                        DP[r+1][c],
                        DP[r][c+1],
                    )
        return DP[0][0]

    def longestPalindromeSubseq(self, s: str) -> int:
        
        return self._longestCommonSubseq(s, s[::-1])