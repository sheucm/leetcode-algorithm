class Solution:
    def isalnum(self, c: str) -> bool:
        return (
            (ord('A') <= ord(c) <= ord('Z')) or
            (ord('a') <= ord(c) <= ord('z')) or
            (ord('0') <= ord(c) <= ord('9'))
        )
    def isPalindrome(self, s: str) -> bool:

        ### Solution1: Simplest
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        # new_s = ""
        # for c in s:
        #     if c.isalnum():
        #         new_s += c.lower()
        # return new_s == new_s[::-1]



        ### Solution2: Implement it with O(1) memory using left-right pointers.
        ### Extra: Implement isalnum() function
        ### Time Complexity: O(N)
        ### Space Complexity: O(N)
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.isalnum(s[l]):
                l += 1
            while r > l and not self.isalnum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True