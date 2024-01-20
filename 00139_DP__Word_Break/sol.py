class Solution:
    def __init__(self):
        self.cache = {}  # For solution1

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        ### Solution1: Using Cache + Recursive
        ### Time Complexity: O(n * m)
        ### Space Complexity: O(n)
        # if len(s) == 0:
        #     return True
        # if s in self.cache:
        #     return self.cache[s]
        # ans = False
        # for w in wordDict:
        #     if s.startswith(w):
        #         ans = ans or self.wordBreak(s[len(w):], wordDict)
        # self.cache[s] = ans
        # return ans


        ### Solution2: Using DP
        ### Time Complexity: O(n * m)
        ### Space Complexity: O(n)
        DP = [False] * (len(s) + 1)
        DP[-1] = True
        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i+len(w)] == w:
                    DP[i] = DP[i+len(w)]
                if DP[i]:
                    break
        return DP[0]

