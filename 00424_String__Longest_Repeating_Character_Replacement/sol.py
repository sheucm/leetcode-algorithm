from collections import defaultdict
class Solution:
    def characterReplacement(self, S: str, K: int) -> int:
        
        ### Time Complexity: O(N)
        ### Space Complexity: O(1)
        count = defaultdict(int)
        ans = 0
        l = 0
        for r in range(len(S)):
            count[S[r]] += 1
            while (r - l + 1) - max(count.values()) > K:
                count[S[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans



