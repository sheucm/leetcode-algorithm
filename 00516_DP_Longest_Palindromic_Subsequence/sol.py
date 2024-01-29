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

    def helper(self, s, start, end, cache):
        if start > end:
            return 0
        if (start, end) in cache:
            return cache[(start, end)]
        res = 0
        if s[start] == s[end]:
            length = 2 if start != end else 1
            res = length + self.helper(s, start+1, end-1, cache)
        else:
            res = max(
                self.helper(s, start+1, end, cache),
                self.helper(s, start, end-1, cache)
            )
        cache[(start, end)] = res
        return res
    def longestPalindromeSubseq(self, s: str) -> int:
        
        ### Solution1:
        return self.helper(s, 0, len(s)-1, {})
        
        ### Solution2: Use LCS Alg.
        # return self._longestCommonSubseq(s, s[::-1])