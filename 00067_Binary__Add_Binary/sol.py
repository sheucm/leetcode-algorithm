class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ### Solution1:
        # return bin(int(a, 2) + int(b, 2))[2:]
        

        ### Solution2:
        ### Time Complexity: O(N)
        ### Space Complexity: O(1)
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2))
            carry = carry // 2
        return "".join(reversed(s))

