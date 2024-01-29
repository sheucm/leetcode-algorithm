from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ### Time Complexity: O(N)
        ### Time Complexity: O(N)
        counter = Counter(magazine)
        for ch in ransomNote:
            if ch in counter and counter[ch] > 0:
                counter[ch] -= 1
            else:
                return False
        return True