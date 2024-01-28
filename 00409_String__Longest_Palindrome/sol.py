from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        counter = Counter(s)
        pair_cnt = 0
        single_cnt = 0
        for char, cnt in counter.items():
            pair_cnt += cnt // 2
            single_cnt += cnt % 2
        return pair_cnt * 2 + (1 if single_cnt > 0 else 0)

